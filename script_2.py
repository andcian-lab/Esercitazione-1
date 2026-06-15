#!/usr/bin/env python3
"""
Autore: David Zolfaroli
Data: 15/06/2026

Titolo: Script 2 - Controllo cartella ./in e spostamento file in ./processing
Descrizione:
Lo script controlla ogni 10 secondi la cartella ./in.
Se trova dei file, li sposta nella cartella ./processing.
Ogni operazione viene loggata su console.
"""

import os
import time
import shutil


# ------------------------------------------------------------
# Funzione: inizializzaCartelle
# Crea le cartelle necessarie se non esistono già.
# Parametri formali:
#   in_dir: str -> percorso cartella di input
#   proc_dir: str -> percorso cartella di processing
# Valore di ritorno:
#   None
# ------------------------------------------------------------
def inizializzaCartelle(in_dir: str, proc_dir: str) -> None:
    os.makedirs(in_dir, exist_ok=True)
    os.makedirs(proc_dir, exist_ok=True)


# ------------------------------------------------------------
# Funzione: spostaFile
# Sposta tutti i file presenti nella cartella in_dir
# nella cartella proc_dir.
# Parametri formali:
#   in_dir: str -> percorso cartella di input
#   proc_dir: str -> percorso cartella di processing
# Valore di ritorno:
#   None
# ------------------------------------------------------------
def spostaFile(in_dir: str, proc_dir: str) -> None:
    files = os.listdir(in_dir)

    if len(files) == 0:
        print("[INFO] Nessun file da spostare.")
        return

    for nome_file in files:
        sorgente = os.path.join(in_dir, nome_file)
        destinazione = os.path.join(proc_dir, nome_file)

        if os.path.isfile(sorgente):
            shutil.move(sorgente, destinazione)
            print(f"[MOVE] Spostato: {nome_file} → ./processing")


# ------------------------------------------------------------
# Programma principale
# ------------------------------------------------------------
if __name__ == "__main__":

    # Sezione inizializzazione variabili
    IN_DIR = "./in"              # Cartella di input
    PROC_DIR = "./processing"    # Cartella di processing
    INTERVALLO = 10              # Secondi tra un controllo e l'altro

    # Inizializzazione cartelle
    inizializzaCartelle(IN_DIR, PROC_DIR)

    print("[INFO] Script avviato. Controllo ogni 10 secondi.")

    # Ciclo principale
    while True:
        spostaFile(IN_DIR, PROC_DIR)
        time.sleep(INTERVALLO)
