import numpy as np
from colorama import Fore, Style

class GravityEngine:
    def __init__(self):
        # Konstanta Standar Geofisika
        self.fac_constant = 0.3086  # mGal/m
        self.bc_constant = 0.04193  # mGal.cm3/g.m

    def calculate_fac(self, elevation):
        """Koreksi Udara Bebas (Free Air Correction)"""
        return self.fac_constant * elevation

    def calculate_bc(self, elevation, density=2.67):
        """Koreksi Bouguer (Bouguer Correction)"""
        return self.bc_constant * density * elevation

    def get_complete_anomaly(self, obs_gravity, theo_gravity, fac, bc, tc=0):
        """Menghitung Anomali Bouguer Sederhana/Lengkap"""
        # Rumus: (Gobs - Gtheo) + FAC - BC + TC
        return (obs_gravity - theo_gravity) + fac - bc + tc

if __name__ == "__main__":
    print(Fore.YELLOW + "\n[*] Running Gravity Engine (v1.1)...")
    engine = GravityEngine()
    
    try:
        # Input Data Interaktif
        h = float(input(Fore.WHITE + "Enter Elevation (m): "))
        g_obs = float(input("Enter Observed Gravity (mGal): "))
        g_theo = float(input("Enter Theoretical Gravity (mGal): "))
        rho = float(input("Enter Density (default 2.67): ") or 2.67)
        
        # Hitung Koreksi menggunakan Engine
        fac = engine.calculate_fac(h)
        bc = engine.calculate_bc(h, rho)
        
        # Hitung Anomali
        sba = engine.get_complete_anomaly(g_obs, g_theo, fac, bc)
        
        print("-" * 35)
        print(f"Elevation   : {h} m")
        print(f"FAC Result  : {fac:.4f} mGal")
        print(f"BC Result   : {bc:.4f} mGal (rho={rho})")
        print("-" * 35)
        print(Fore.GREEN + f"RESULT -> SBA : {sba:.4f} mGal")
        print(Fore.YELLOW + "[+] Calculation completed.")
        
    except ValueError:
        print(Fore.RED + "[!] Error: Input harus angka!")

    input("\nPress Enter to return...")
