import math # Pakai math lebih ringan daripada numpy
from colorama import Fore

class ResistivityEngine:
    def __init__(self):
        self.name = "Res-A Engine"

    def calculate_k_schlumberger(self, AB_2, MN_2):
        """
        Menghitung Faktor Geometri (K) untuk Konfigurasi Schlumberger.
        """
        L = float(AB_2) 
        l = float(MN_2)
        
        # Cek agar tidak terjadi pembagian dengan nol atau angka negatif
        if l <= 0 or L <= l:
            return 0
            
        # Rumus K Schlumberger menggunakan math.pi
        k = (math.pi * (L**2 - l**2)) / (2 * l)
        return k

    def calculate_apparent_resistivity(self, k, voltage, current):
        if current <= 0:
            return 0
        rho_a = k * (float(voltage) / float(current))
        return rho_a
