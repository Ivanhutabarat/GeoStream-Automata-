import os
import requests
import json
from dotenv import load_dotenv
from colorama import Fore

# Load konfigurasi dari file .env
load_dotenv()

class GeoBot:
    def __init__(self):
        self.webhook_url = os.getenv("N8N_WEBHOOK_URL")
        self.user_name = os.getenv("USER_NAME", "Ivan")

    def send_notification(self, message, data_type="General"):
        """Mengirim notifikasi ke WhatsApp melalui n8n"""
        if not self.webhook_url:
            print(Fore.RED + "[!] Error: N8N_WEBHOOK_URL tidak ditemukan di .env")
            return

        payload = {
            "user": self.user_name,
            "type": data_type,
            "message": message,
            "status": "Success"
        }

        try:
            response = requests.post(
                self.webhook_url, 
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] Notifikasi {data_type} terkirim ke WhatsApp.")
            else:
                print(Fore.YELLOW + f"[!] Gagal mengirim: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"[!] Connection Error: {e}")

if __name__ == "__main__":
    # Test Bot
    bot = GeoBot()
    bot.send_notification("Sistem GeoStream-Automata berhasil diinisialisasi!", "System-Check")
