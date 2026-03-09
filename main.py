import os
import sys
import platform
from colorama import Fore, Style, init

# Inisialisasi warna untuk terminal
init(autoreset=True)

def header():
    print(Fore.CYAN + Style.BRIGHT + "==========================================")
    print(Fore.WHITE + Style.BRIGHT + "       🛰️  GEOSTREAM-AUTOMATA v1.0        ")
    print(Fore.YELLOW + "    Developer: Ivan Krisopras Hutabarat   ")
    print(Fore.CYAN + Style.BRIGHT + "==========================================")

def check_env():
    """Mendeteksi apakah berjalan di Termux atau Desktop (VS Code)"""
    if os.path.exists('/data/data/com.termux'):
        return "Termux (Mobile)"
    else:
        return f"Desktop ({platform.system()})"

def check_structure():
    """Memastikan semua folder yang ada di gambar sudah tersedia"""
    folders = ['data', 'lib', 'matlab', 'n8n', 'core', 'results', 'storage']
    print(Fore.BLUE + "\n[*] Checking System Integrity...")
    for folder in folders:
        if os.path.exists(folder):
            print(f"  [+] Folder {folder:10} : FOUND")
        else:
            print(Fore.RED + f"  [-] Folder {folder:10} : MISSING (Please run setup.sh)")

def main():
    header()
    env = check_env()
    print(f"[*] Environment : {env}")
    check_structure()
    
    print(Fore.GREEN + "\n[!] System Ready.")
    print("Welcome back, Van. What are we processing today?")
    print("------------------------------------------")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] System Halted by User.")
        sys.exit()
