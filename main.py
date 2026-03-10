import os
import sys
from colorama import Fore, Style, init
from core.gravity_engine import GravityEngine
from core.resistivity_engine import ResistivityEngine
from core.visualizer_engine import VisualizerEngine
from core.sync_manager import SyncManager
from whatsapp_bot_main import GeoBot

# Inisialisasi Colorama agar warna muncul di Termux
init(autoreset=True)

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.CYAN + Style.BRIGHT + "==========================================")
    print(Fore.WHITE + Style.BRIGHT + "       🛰️  GEOSTREAM-AUTOMATA v1.1        ")
    print(Fore.YELLOW + "    Developer: Ivan Krisopras Hutabarat   ")
    print(Fore.CYAN + Style.BRIGHT + "==========================================")

def main_menu():
    show_banner()
    print(Fore.GREEN + "[1] Gravity Engine (FAC & Bouguer)")
    print(Fore.GREEN + "[2] Resistivity Engine (Schlumberger)")
    print(Fore.GREEN + "[3] Visualizer (Generate Plots)")
    print(Fore.GREEN + "[4] Auto-Sync (GitHub & WhatsApp)")
    print(Fore.RED + "[0] Exit System")
    print(Fore.CYAN + "------------------------------------------")
    return input("Select Option: ")

def run_system():
    # Load semua engine dari folder core
    grav = GravityEngine()
    res = ResistivityEngine()
    viz = VisualizerEngine()
    sync = SyncManager()
    bot = GeoBot()

    while True:
        choice = main_menu()

        if choice == '1':
            print(Fore.YELLOW + "\n[*] Running Gravity Engine...")
            try:
                # Input data untuk perhitungan Geofisika
                h = float(input("Enter Elevation (m): "))
                g_obs = float(input("Enter Observed Gravity (mGal): "))
                g_theo = float(input("Enter Theoretical Gravity (mGal): "))
                rho_val = input("Enter Density (default 2.67): ")
                rho = float(rho_val) if rho_val else 2.67

                # Memanggil fungsi dari core/gravity_engine.py
                fac = grav.calculate_fac(h)
                bc = grav.calculate_bc(h, rho)
                sba = grav.get_complete_anomaly(g_obs, g_theo, fac, bc)

                print(Fore.CYAN + "-" * 35)
                print(f"Result -> FAC: {fac:.4f}, BC: {bc:.4f}")
                print(Fore.GREEN + Style.BRIGHT + f"RESULT -> SBA: {sba:.4f} mGal")
                print(Fore.CYAN + "-" * 35)
            except ValueError:
                print(Fore.RED + "[!] Error: Masukkan angka yang valid!")
            except Exception as e:
                print(Fore.RED + f"[!] Unexpected Error: {e}")
            
            input("\nPress Enter to return...")

        elif choice == '2':
            print(Fore.YELLOW + "\n[*] Running Resistivity Engine...")
            try:
                ab2 = float(input("Enter AB/2 (m): "))
                mn2 = float(input("Enter MN/2 (m): "))
                v = float(input("Voltage (V): "))
                i = float(input("Current (A): "))
                k = res.calculate_k_schlumberger(ab2, mn2)
                rho_a = res.calculate_apparent_resistivity(k, v, i)
                print(Fore.CYAN + "-" * 35)
                print(f"Result -> K: {k:.2f}")
                print(Fore.GREEN + Style.BRIGHT + f"Rho_a: {rho_a:.2f} Ohm.m")
                print(Fore.CYAN + "-" * 35)
            except ValueError:
                print(Fore.RED + "[!] Error: Masukkan angka yang valid!")
            input("\nPress Enter to return...")

        elif choice == '3':
            print(Fore.YELLOW + "\n[*] Generating Default Plots...")
            # Simulasi data dummy
            viz.plot_gravity_anomaly([1,2,3,4,5], [10,12,15,11,9])
            print(Fore.GREEN + "[+] Plots successfully saved in /results")
            input("\nPress Enter to return...")

        elif choice == '4':
            print(Fore.YELLOW + "\n[*] Starting Sync Process...")
            sync.local_backup()
            bot.send_notification("Data processing complete. Results synced to TITANCORE.", "Auto-Sync")
            sync.push_to_git("Field data update")
            print(Fore.GREEN + "[+] Sync completed!")
            input("\nPress Enter to return...")

        elif choice == '0':
            print(Fore.RED + "Shutting down GeoStream-Automata. Goodbye, Van!")
            break
        else:
            print(Fore.RED + "Invalid Option!")

if __name__ == "__main__":
    try:
        run_system()
    except Exception as e:
        print(Fore.RED + f"Critical Error: {e}")
