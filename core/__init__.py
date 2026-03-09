import numpy as np
from colorama import Fore, Style

class GravityEngine:
    def __init__(self):
        # Konstanta Standar Geofisika
        self.fac_constant = 0.3086  # mGal/m
        self.bc_constant = 0.04193  # mGal.cm3/g.m

    def calculate_fac(self, elevation):
        """Koreksi Udara Bebas (Free Air Correction)"""
        # Rumus: 0.3086 * h
        return self.fac_constant * elevation

    def calculate_bc(self, elevation, density=2.67):
        """Koreksi Bouguer (Bouguer Correction)"""
        # Rumus: 0.04193 * rho * h
        return self.bc_constant * density * elevation

    def get_complete_anomaly(self, obs_gravity, fac, bc, tc=0):
        """Menghitung Anomali Bouguer Lengkap"""
        # Rumus sederhana: Gobs + FAC - BC + TC
        return obs_gravity + fac - bc + tc

if __name__ == "__main__":
    print(Fore.YELLOW + "[*] Testing Gravity Engine...")
    engine = GravityEngine()
    
    # Contoh testing data lapangan
    h = 100 # meter
    g_obs = 978000 # mGal (contoh)
    
    fac = engine.calculate_fac(h)
    bc = engine.calculate_bc(h)
    
    print(f"Elevation : {h} m")
    print(f"FAC Result: {fac:.4f} mGal")
    print(f"BC Result : {bc:.4f} mGal")
    print(Fore.GREEN + "[+] Engine functional.")
