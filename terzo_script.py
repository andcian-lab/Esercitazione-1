# 3. Terzo script che ogni 30 secondi controlla se ci sono file nella cartella ./processing e li sposta nella cartella ./out

# 1. All'avvio, lo script crea automaticamente le cartelle `./processing` e `./out` se non sono già presenti.
# 2. Avvia un ciclo continuo che controlla il contenuto di `./processing`.
# 3. Se trova dei file, li sposta in `./out` usando la libreria `shutil`.
# 4. Gestisce l'interruzione manuale (`CTRL+C`) per chiudersi in modo pulito.

import os
import shutil
import time

CARTELLA_PROCESSING = "./processing"
CARTELLA_OUT = "./out"

# Definisce un limite di file per ogni ciclo
LIMITE_BATCH = 20 

def verifica_cartelle_esistenti():
    if not os.path.exists(CARTELLA_PROCESSING) or not os.path.exists(CARTELLA_OUT):
        return False
    return True

def sposta_file():
    """Controlla i file e gestisce l'eventuale coda in modo sicuro."""
    if not os.path.exists(CARTELLA_PROCESSING):
        return

    contenuto = os.listdir(CARTELLA_PROCESSING)
    
    # Prende solo i file veri e propri
    file_totali_in_coda = [
        f for f in contenuto 
        if os.path.isfile(os.path.join(CARTELLA_PROCESSING, f))
    ]
    
    numero_file = len(file_totali_in_coda)
    
    if numero_file == 0:
        print("[INFO] Nessun file trovato in ./processing.")
        return

    # Se c'è una coda accumulata, lo segnala nel log
    if numero_file > LIMITE_BATCH:
        print(f"[⚠️ CODA RILEVATA] Ci sono ben {numero_file} file in attesa!")
        # Prendiamo solo i primi 'X' file (definiti nel LIMITE_BATCH)
        file_da_spostare = file_totali_in_coda[:LIMITE_BATCH]
        print(f"[INFO] Smaltimento coda: elaboro i primi {LIMITE_BATCH} file di questo blocco.")
    else:
        # Se i file sono pochi, li prende tutti
        file_da_spostare = file_totali_in_coda

    # Spostamento controllato dei file
    for nome_file in file_da_spostare:
        percorso_origine = os.path.join(CARTELLA_PROCESSING, nome_file)
        percorso_destinazione = os.path.join(CARTELLA_OUT, nome_file)
        
        try:
            shutil.move(percorso_origine, percorso_destinazione)
            print(f"[SUCCESS] Spostato: {nome_file} -> {CARTELLA_OUT}")
        except Exception as e:
            # Se un singolo file è corrotto o bloccato, l'errore viene isolato
            # Lo script NON si blocca e passa al file successivo
            print(f"[ERRORE] Impossibile spostare {nome_file}: {e}")

def main():
    print("Avvio del terzo script (con gestione anti-blocco della coda)...")
    
    try:
        while True:
            if verifica_cartelle_esistenti():
                sposta_file()
            else:
                print("[INFO] In attesa che le cartelle vengano create...")
            
            print("Prossimo controllo tra 30 secondi. Premi CTRL+C per interrompere.\n")
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n[STOP] Script interrotto dall'utente. Chiusura in corso...")

if __name__ == "__main__":
    main()