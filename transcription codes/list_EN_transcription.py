# Skript um mehrere englische Audiodateien zu transkribieren

import os
import whisper
import torch
import subprocess
from docx import Document

# Funktion zur Konvertierung von WMA in MP3
def convert_wma_to_mp3(input_path, output_path):
    subprocess.run(['ffmpeg', '-i', input_path, output_path])

# Funktion, um alle Audiodateien im Ordner zu finden
def get_audio_files(folder_path):
    # Durchsuche den Ordner nach wma-, mp3-, wav- und m4a-Dateien
    audio_files = [f for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav', '.m4a', '.WMA'))]
    return audio_files

# Prüfen, ob eine GPU verfügbar ist
device = "cuda" if torch.cuda.is_available() else "cpu"
if device == "cuda":
    print(f"GPU wird verwendet: {torch.cuda.get_device_name(0)}")
else:
    print("Keine GPU verfügbar. Whisper läuft auf der CPU.")

# Ordnerpfade
input_folder = "Traumberichte_Audio"
output_folder = "Traumberichte_Transkript"

# Versuche, alle Audiodateien im Ordner zu holen
try:
    audio_files = get_audio_files(input_folder)
    
    if audio_files:
        print(f"Gefundene Audiodateien: {audio_files}")
        
        # Lade das Whisper-Modell auf das richtige Gerät
        model = whisper.load_model("turbo", device=device)
        
        # Verarbeite jede Audiodatei im Ordner
        for audio_file in audio_files:
            print(f"Transkribiere Datei: {audio_file}")
            
            # Wenn es sich um eine WMA-Datei handelt, konvertiere sie zuerst in MP3
            if audio_file.endswith('.wma'):
                mp3_file = os.path.splitext(audio_file)[0] + '.mp3'
                input_path = os.path.join(input_folder, audio_file)
                output_path = os.path.join(input_folder, mp3_file)
                convert_wma_to_mp3(input_path, output_path)
                audio_file = mp3_file  # Jetzt die MP3-Datei verwenden
            
            # Transkribiere die Datei
            audio_path = os.path.join(input_folder, audio_file)
            result = model.transcribe(audio_path, language="en")  # Sprache: Deutsch (Schweizerdeutsch funktioniert hier mit 'de')
            
            # Erstelle ein neues Word-Dokument
            doc = Document()
            doc.add_heading(f'Transkript der Datei: {audio_file}', 0)
            
            # Füge den transkribierten Text Satz für Satz als neue Zeile hinzu
            sentences = result["text"].split(". ")  # Splitting the text by sentences
            for sentence in sentences:
                if sentence.strip():  # Nur nicht leere Sätze hinzufügen
                    doc.add_paragraph(sentence.strip())  # Füge jeden Satz in einer neuen Zeile hinzu
            
            # Sicherstellen, dass der Ausgabeordner existiert
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # Speichere die Transkription im Ordner "Traumberichte_Transkript"
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(audio_file)[0]}.docx")
            doc.save(output_file_path)
            
            print(f"Transkription erfolgreich gespeichert unter: {output_file_path}")
    
    else:
        print("Fehler: Keine Audiodateien im Ordner 'Traumberichte_Audio' gefunden.")
        
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
