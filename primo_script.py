import os
import time
from datetime import datetime

# Definisce la cartella di output
output_dir = './in'

# Crea la cartella se non esiste
os.makedirs(output_dir, exist_ok=True)

print(print(f"Script avviato. Scrittura di file nella cartella '{output_dir}' ogni 10 secondi."))
print("Premi CTRL+C per interrompere.")

try:
    while True:
        # Genera il timestamp per il nome del file (es: 2026-05-20_12-49-00.txt)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}.txt"
        filepath = os.path.join(output_dir, filename)

        # Scrive il file
        with open(filepath, 'w') as file:
            file.write(f"File creato il {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            
        print(f"Creato: {filename}")

        # Attende 10 secondi prima del ciclo successivo
        time.sleep(10)

except KeyboardInterrupt:
    print("\nScript terminato dall'utente.")
