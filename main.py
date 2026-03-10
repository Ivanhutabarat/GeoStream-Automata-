import os
from colorama import Fore, Style, init
from core.gravity_engine import GravityEngine
from core.resistivity_engine import ResistivityEngine
from core.visualizer_engine import VisualizerEngine
from core.sync_manager import SyncManager

init(autoreset=True)

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.CYAN + Style.BRIGHT + "==========================================")
    print(Fore.WHITE + Style.BRIGHT + "       🛰️  GEOSTREAM-AUTOMATA v1.2        ")
    print(Fore.YELLOW + "    Developer: Ivan Krisopras Hutabarat   ")
    print(Fore.CYAN + Style.BRIGHT + "==========================================")

def run_system():
    grav, res, viz, sync = GravityEngine(), ResistivityEngine(), VisualizerEngine(), SyncManager()
    
    # --- MEMORI DATA (INI KUNCINYA) ---
    st_names, sba_data = [], []
    count = 1

    while True:
        show_banner()
        print(f"{Fore.GREEN}[1] Input Gravity Data (St {count})")
        print(f"{Fore.GREEN}[2] Resistivity Engine")
        print(f"{Fore.GREEN}[3] Visualizer (Plot {len(sba_data)} Data)")
        print(f"{Fore.GREEN}[4] Sync & Backup")
        print(f"{Fore.RED}[0] Exit")
        
        choice = input("\nSelect Option: ")

        if choice == '1':
            try:
                h = float(input("Elevation (m): "))
                g_obs = float(input("Observed (mGal): "))
                g_theo = float(input("Theoretical (mGal): "))
                rho = float(input("Density (default 2.67): ") or 2.67)

                sba = grav.get_complete_anomaly(g_obs, g_theo, grav.calculate_fac(h), grav.calculate_bc(h, rho))
                
                # SIMPAN KE MEMORI
                sba_data.append(sba)
                st_names.append(count)
                count += 1
                
                print(Fore.GREEN + f"\n[+] Saved! SBA: {sba:.4f} mGal")
            except: print(Fore.RED + "[!] Input error!")
            input("Press Enter...")

        elif choice == '3':
            if not sba_data:
                print(Fore.RED + "[!] No data to plot!")
            else:
                print(Fore.YELLOW + "[*] Plotting Real Data...")
                if os.path.exists("results/gravity_profile.png"): os.remove("results/gravity_profile.png")
                viz.plot_gravity_anomaly(st_names, sba_data)
                print(Fore.GREEN + "[+] Success! Real plot saved to /results")
            input("Press Enter...")

        elif choice == '0': break
run_system()
