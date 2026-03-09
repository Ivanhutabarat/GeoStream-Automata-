import numpy as np
from colorama import Fore

class ResistivityEngine:
    def __init__(self):
        self.name = "Res-A Engine"

    def calculate_k_schlumberger(self, AB_2, MN_2):
        """
        Menghitung Faktor Geometri (K) untuk Konfigurasi Schlumberger.
        Rumus: K = pi * ((AB/2)^2 - (MN/2)^2) / MN
        """
        # Konversi ke meter jika perlu
        L = AB_2  # Jarak arus (m)
        l = MN_2  # Jarak potensial (m)
        
        # Rumus K Schlumberger
        k = (np.pi * (L**2 - l**2)) / (2 * l)
        return k

    def calculate_apparent_resistivity(self, k, voltage, current):
        """
        Menghitung Resistivitas Semu (Rho_a).
        Rumus: Rho_a = K * (V / I)
        """
        if current == 0:
            return 0
        rho_a = k * (voltage / current)
        return rho_a

if __name__ == "__main__":
    engine = ResistivityEngine()
    print(Fore.BLUE + "[*] Testing Resistivity Engine (Schlumberger)...")
    
    # Contoh Data Lapangan
    ab_2 = 10.0  # Jarak AB/2
    mn_2 = 1.0   # Jarak MN/2
    v = 120.5    # Volt
    i = 0.5      # Ampere
    
    k = engine.calculate_k_schlumberger(ab_2, mn_2)
    rho = engine.calculate_apparent_resistivity(k, v, i)
    
    print(f"Faktor K  : {k:.2f}")
    print(f"Res. Semu : {rho:.2f} Ohm.m")
    print(Fore.GREEN + "[+] Engine ready for field data.")
