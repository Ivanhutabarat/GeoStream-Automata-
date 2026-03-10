import os
import sys
from colorama import Fore, Style, init
from core.gravity_engine import GravityEngine
from core.resistivity_engine import ResistivityEngine
from core.visualizer_engine import VisualizerEngine
from core.sync_manager import SyncManager
from whatsapp_bot_main import GeoBot

# Inisialisasi Colorama
init(autoreset=True)

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.CYAN + Style.BRIGHT + "==========================================")
    print(Fore.WHITE + Style.BRIGHT + "       🛰️  GEOSTREAM-AUTOMATA v1.2        ")
    print(Fore.YELLOW + "    Developer: Ivan Krisopras Hutabarat   ")
    print(Fore.CYAN + Style.BRIGHT + "==========================================")

def main_menu():
    show_banner()
    print(Fore.GREEN + "[1] Gravity Engine (Input Data)")
    print(Fore.GREEN + "[2] Resistivity Engine (Schlumberger)")
    print(Fore.GREEN + "[3] Visualizer (Plot Real Data)")
    print(Fore.GREEN + "[4] Auto-Sync (GitHub & WhatsApp)")
    print(Fore.RED + "[0] Exit System")
    print(Fore.CYAN + "------------------------------------------")
    return input("Select Option: ")

def run_system():
    # Load engines
    grav = GravityEngine()
    res = ResistivityEngine()
    viz = VisualizerEngine()
    sync = SyncManager()
    bot = GeoBot()

    # --- LIVE DATA STORAGE ---
    # Variabel ini untuk menyimpan data selama program jalan
    sba_list = []
    station_list = []
    station_counter = 1

    while True:
        choice = main_menu()

        if choice == '1':
            print(Fore.YELLOW + f"\n[*] Running Gravity Engine (Station {station_counter})...")
            try:
                h = float(input("Enter Elevation (m): "))
                g_obs = float(input("Enter Observed Gravity (mGal): "))
                g_theo = float(input("Enter Theoretical Gravity (mGal): "))
                rho_val = input("Enter Density (default 2.67): ")
                rho = float(rho_val) if rho_val else 2.67

                fac = grav.calculate_fac(h)
                bc = grav.calculate_bc(h, rho)
                sba = grav.get_complete_anomaly(g_obs, g_theo, fac, bc)

                # SIMPAN DATA KE LIST
                sba_list.append(sba)
                station_list.append(station_counter)
                station_counter += 1

                print(Fore.CYAN + "-" * 35)
                print(f"Result -> FAC: {fac:.4f}, BC: {bc:.4f}")
                print(Fore.GREEN + Style.BRIGHT + f"RESULT -> SBA: {sba:.4f} mGal")
                print(Fore.CYAN + "-" * 35)
                print(Fore.YELLOW + f"[!] Data saved. Total stations: {len(sba_list)}")
            except ValueError:
                print(Fore.RED + "[!] Error: Masukkan angka yang valid!")
            
            input("\nPress Enter to return...")

        elif choice == '2':
            print(Fore.YELLOW + "\n[*] Running Resistivity Engine...")
            try:
                ab2 = float(input("Enter AB/2 (m): "))
                mn2 = float(input("Enter MN/2 (m): "))
                if ab2 <= mn2:
                    print(Fore.RED + "[!] Warning: AB/2 harus lebih besar dari MN/2!")
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
            if not sba_list:
                print(Fore.RED + "\n[!] Data Kosong! Input data di menu [1] dulu.")
            else:
                print(Fore.YELLOW + f"\n[*] Generating Plots for {len(sba_list)} Stations...")
                # BERSIHKAN FILE LAMA
                if os.path.exists("results/gravity_profile.png"):
                    os.remove("results/gravity_profile.png")
                
                # PLOT DATA ASLI
                viz.plot_gravity_anomaly(station_list, sba_list)
                print(Fore.GREEN + "[+] New Plot generated using LIVE DATA!")
                print(Fore.GREEN + "[+] Path: results/gravity_profile.png")
            input("\nPress Enter to return...")

        elif choice == '4':
            print(Fore.YELLOW + "\n[*] Starting Sync Process...")
            sync.local_backup()
            bot.send_notification(f"Success! {len(sba_list)} stations processed.", "Auto-Sync")
            sync.push_to_git(f"Update: {len(sba_list)} data stations")
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
