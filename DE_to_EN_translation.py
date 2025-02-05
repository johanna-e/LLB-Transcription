# Deutsch zu Englisch Übersetzung

import os
import whisper
import torch

# Ordnerpfade
folder_path = "Dream transcripts"

# Prüfen, ob eine GPU verfügbar ist
device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cuda":
    print(f"GPU wird verwendet: {torch.cuda.get_device_name(0)}")
else:
    print("Keine GPU verfügbar. Whisper läuft auf der CPU.")

# Whisper-Modell laden (großes Modell für bessere Übersetzungsqualität empfohlen)
model = whisper.load_model("large")

def get_latest_file(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.docx')]
    if not files:
        return None
    return max(files, key=lambda f: os.path.getmtime(os.path.join(folder, f)))

def translate_file(file_path):
    print(f"Übersetze: {file_path}")
    result = model.transcribe(file_path, task="translate", language="en")  # Übersetzung ins Englische
    
    output_file = file_path.replace(".docx", "_translation.docx")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"Übersetzung gespeichert unter: {output_file}")

def process_files(choice):
    if choice == "1":  # Alle Dateien
        files = [f for f in os.listdir(folder_path) if f.endswith('.docx')]
        for file in files:
            translate_file(os.path.join(folder_path, file))

    elif choice == "2":  # Neueste Datei
        latest_file = get_latest_file(folder_path)
        if latest_file:
            translate_file(os.path.join(folder_path, latest_file))
        else:
            print("Keine Dateien gefunden.")

    elif choice == "3":  # Bestimmte Datei
        file_name = input("Bitte den Dateinamen (mit .docx) eingeben: ")
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            translate_file(file_path)
        else:
            print("Datei nicht gefunden.")

    else:
        print("Ungültige Auswahl.")

# Benutzerabfrage
print("Möchtest du:")
print("1 - Alle Dateien im Ordner übersetzen")
print("2 - Nur die neueste Datei übersetzen")
print("3 - Eine bestimmte Datei übersetzen")

choice = input("Bitte gib 1, 2 oder 3 ein: ")
process_files(choice)
