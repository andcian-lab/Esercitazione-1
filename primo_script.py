import os
import time
from datetime import datetime

# 1. Configurazione della cartella di destinazione
output_dir = './in'

# Crea la cartella se non esiste ancora nel path corrente
os.makedirs(output_dir, exist_ok=True)

print(f"Script avviato. Scrittura di file nella cartella '{output_dir}' ogni 10 secondi.")
print("Premi CTRL+C per interrompere l'esecuzione.")

try:
    while True:
        # 2. Generazione del timestamp per garantire nomi di file univoci
        # Esempio di output: 2026-06-15_12-30-00.txt
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}.txt"
        filepath = os.path.join(output_dir, filename)

        # 3. Creazione del file e scrittura del contenuto (log interno)
        with open(filepath, 'w') as file:
            file.write(f"File creato il {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            
        # Log dell'operazione stampato direttamente in console
        print(f"Creato con successo: {filename}")

        # 4. Pausa di 10 secondi prima del ciclo successivo
        time.sleep(10)

except KeyboardInterrupt:
    # Gestisce la chiusura manuale con CTRL+C evitando di mostrare l'errore di crash in console
    print("\nScript terminato correttamente dall'utente.")
