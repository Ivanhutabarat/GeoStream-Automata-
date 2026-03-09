import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from colorama import Fore

# Setup tema grafik agar terlihat modern (TITANCORE Style)
plt.style.use('dark_background')
sns.set_context("talk")

class VisualizerEngine:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def plot_gravity_anomaly(self, stations, anomalies, filename="gravity_profile.png"):
        """Membuat profil anomali gravitasi sepanjang lintasan"""
        plt.figure(figsize=(10, 6))
        plt.plot(stations, anomalies, marker='o', linestyle='-', color='#00FF00', label='Bouguer Anomaly')
        plt.fill_between(stations, anomalies, color='#00FF00', alpha=0.1)
        
        plt.title("Gravity Anomaly Profile", fontsize=16, color='white')
        plt.xlabel("Station Number", fontsize=12)
        plt.ylabel("Anomaly (mGal)", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        
        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()
        print(Fore.GREEN + f"[+] Gravity Plot saved to: {path}")

    def plot_resistivity_curve(self, ab_2, rho_a, filename="ves_curve.png"):
        """Membuat kurva Vertical Electrical Sounding (VES) log-log"""
        plt.figure(figsize=(8, 8))
        plt.loglog(ab_2, rho_a, marker='s', linestyle='-', color='#FFD700', label='Apparent Resistivity')
        
        plt.title("VES Apparent Resistivity Curve", fontsize=16, color='white')
        plt.xlabel("AB/2 (m)", fontsize=12)
        plt.ylabel("Rho_a (Ohm.m)", fontsize=12)
        plt.grid(True, which="both", ls="-", alpha=0.3)
        plt.legend()
        
        path = os.path.join(self.output_dir, filename)
        plt.savefig(path, dpi=300)
        plt.close()
        print(Fore.GREEN + f"[+] Resistivity Curve saved to: {path}")

if __name__ == "__main__":
    # Test Visualizer dengan data dummy
    viz = VisualizerEngine()
    
    # Dummy Gravity Data
    stations = range(1, 11)
    anoms = [12.5, 13.2, 14.8, 15.1, 14.2, 13.5, 12.1, 11.5, 10.8, 10.2]
    viz.plot_gravity_anomaly(list(stations), anoms)
    
    # Dummy Resistivity Data (Schlumberger)
    ab2 = [1.5, 2.5, 4, 6, 10, 15, 25, 40, 65, 100]
    rho = [150, 145, 130, 110, 85, 60, 45, 55, 90, 120]
    viz.plot_resistivity_curve(ab2, rho)
