import os
from colorama import Fore, Style, init
from core.gravity_engine import GravityEngine
from core.resistivity_engine import ResistivityEngine
from core.visualizer_engine import VisualizerEngine
from core.sync_manager import SyncManager

# Inisialisasi Warna
init(autoreset=True)

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.CYAN + Style.BRIGHT + "==========================================")
    print(Fore.WHITE + Style.BRIGHT + "       🛰️  GEOSTREAM-AUTOMATA v1.2        ")
    print(Fore.YELLOW + "    Developer: Ivan Krisopras Hutabarat   ")
    print(Fore.CYAN + Style.BRIGHT + "==========================================")

def run_system():
    # Load Engines
    grav = GravityEngine()
    res = ResistivityEngine()
    viz = VisualizerEngine()
    sync = SyncManager()
    
    # --- LIVE MEMORY STORAGE ---
    st_names, sba_data = [], []
    count = 1

    while True:
        show_banner()
        print(f"{Fore.GREEN}[1] Gravity Engine (Input St {count})")
        print(f"{Fore.GREEN}[2] Resistivity Engine (Schlumberger)")
        print(f"{Fore.GREEN}[3] Visualizer (Generate {len(sba_data)} Plots)")
        print(f"{Fore.GREEN}[4] Auto-Sync (GitHub & Cloud)")
        print(f"{Fore.RED}[0] Exit System")
        print(Fore.CYAN + "------------------------------------------")
        
        choice = input("Select Option: ")

        # --- OPTION 1: GRAVITY ---
        if choice == '1':
            try:
                print(Fore.YELLOW + f"\n[*] Data Input for Station {count}")
                h = float(input("Elevation (m): "))
                g_obs = float(input("Observed Gravity (mGal): "))
                g_theo = float(input("Theoretical Gravity (mGal): "))
                rho = float(input("Density (default 2.67): ") or 2.67)

                # Hitung SBA
                fac = grav.calculate_fac(h)
                bc = grav.calculate_bc(h, rho)
                sba = grav.get_complete_anomaly(g_obs, g_theo, fac, bc)
                
                # Simpan ke Memori
                sba_data.append(sba)
                st_names.append(count)
                count += 1
                
                print(Fore.CYAN + "-" * 35)
                print(Fore.GREEN + Style.BRIGHT + f"SUCCESS -> SBA: {sba:.4f} mGal")
                print(Fore.CYAN + "-" * 35)
            except Exception as e:
                print(Fore.RED + f"[!] Error: {e}")
            input("\nPress Enter to return...")

        # --- OPTION 2: RESISTIVITY (FIXED) ---
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
                print(f"Geometry Factor (K): {k:.2f}")
                print(Fore.GREEN + Style.BRIGHT + f"Apparent Res (Rho_a): {rho_a:.2f} Ohm.m")
                print(Fore.CYAN + "-" * 35)
            except Exception as e:
                print(Fore.RED + f"[!] Error: {e}")
            input("\nPress Enter to return...")

        # --- OPTION 3: VISUALIZER ---
        elif choice == '3':
            if not sba_data:
                print(Fore.RED + "\n[!] No data found! Please use Option [1] first.")
            else:
                print(Fore.YELLOW + f"\n[*] Processing {len(sba_data)} stations...")
                if os.path.exists("results/gravity_profile.png"):
                    os.remove("results/gravity_profile.png")
                viz.plot_gravity_anomaly(st_names, sba_data)
                print(Fore.GREEN + "[+] SUCCESS! Real-time plot saved in /results")
            input("\nPress Enter to return...")

        # --- OPTION 4: SYNC ---
        elif choice == '4':
            print(Fore.YELLOW + "\n[*] Starting Cloud Sync...")
            sync.local_backup()
            sync.push_to_git(f"Final Report: {len(sba_data)} stations")
            print(Fore.GREEN + "[+] Cloud Sync Completed!")
            input("\nPress Enter to return...")

        elif choice == '0':
            print(Fore.RED + "\nShutting down TitanCore... Goodbye, Van!")
            break
        
        else:
            print(Fore.RED + "\n[!] Invalid Option!")
            input("Press Enter...")

if __name__ == "__main__":
    run_system()
