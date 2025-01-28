'''
import whisper
from pydub import AudioSegment
from pydub.playback import split_on_silence

model = whisper.load_model("base")

# Lade Audiofile
audio = AudioSegment.from_file("audio.mp3")

# Teile Audiofile in Segmente (z. B. basierend auf Pausen)
segments = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

# Für jedes Segment die Sprache und Transkription erkennen
for i, segment in enumerate(segments):
    # Speichere das Segment temporär
    segment.export(f"segment_{i}.wav", format="wav")

    # Lade das Segment und trimme es
    audio = whisper.load_audio(f"segment_{i}.wav")
    audio = whisper.pad_or_trim(audio)

    # Erstelle Mel-Spektrogramm
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Erkenne Sprache
    _, probs = model.detect_language(mel)
    detected_lang = max(probs, key=probs.get)
    print(f"Segment {i}: Detected language: {detected_lang}")

    # Transkribiere das Segment
    result = model.transcribe(f"segment_{i}.wav")
    print(f"Segment {i}: {result['text']}")

'''