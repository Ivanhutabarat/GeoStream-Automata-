import os
import shutil
from datetime import datetime
from colorama import Fore

class SyncManager:
    def __init__(self, data_dir="data", result_dir="results"):
        self.data_dir = data_dir
        self.result_dir = result_dir

    def local_backup(self):
        """Menyimpan hasil ke folder storage sebelum di-sync"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        backup_name = f"storage/archive_{timestamp}"
        
        if os.path.exists(self.result_dir):
            shutil.make_archive(backup_name, 'zip', self.result_dir)
            print(Fore.CYAN + f"[*] Backup created: {backup_name}.zip")

    def push_to_git(self, message="Auto-update field data"):
        """Menjalankan command git push otomatis"""
        print(Fore.YELLOW + "[*] Pushing data to GitHub...")
        os.system("git add .")
        os.system(f'git commit -m "{message}"')
        os.system("git push origin main")
        print(Fore.GREEN + "[+] GitHub Sync Complete.")

if __name__ == "__main__":
    sync = SyncManager()
    sync.local_backup()
