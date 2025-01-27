# 70 Stunden-Projekt: Aufsetzen des Whipser-Transkriptionstools von OpenAI für das Schlaflabor

27.01: 10:30 - 12:00; 12:30 - 13:15, 15:20


Ressourcen: https://openai.com/index/whisper/

Paper: https://cdn.openai.com/papers/whisper.pdf

Model Card: https://github.com/openai/whisper/blob/main/model-card.md

Whisper Code: https://github.com/openai/whisper

## Definition Ziele:

### Hauptziel:
Automatisierte Audiotranskription der Traumberichte im Schlaflabor.
&rarr; Wenn das geht, wäre es wunderbar, wenn nach der Aufnahme des Berichtes einfach nur ein Skript gestartet werden müsste, welches die Transkription anfertigt.
Es soll als Textdatei (welches Format bleibt noch offen) gespeichert werden, sodass nur noch drüber gegangen werden muss zur Kontrolle.
Es soll unter dem selben Namen wie das dazugehörige Audiofile gespeichert werden, aber in einem anderen Ordner. 
Danach kann es gegengelesen und in die Sleeplab übersicht eingefügt werden.

Das Endergebnis soll schon so aussehen, dass verschiedene Sprecherinnen erkannt werden. Pausen per se sind vielleicht auch ganz hilfreich.

### Sekundäre Ziele:
- Außerdem, wenn das auch geht, wäre es auch gut, wenn es direkt ein Skript geben würde, welches laufen gelassen werden kann, für die Übersetzung.
- Das Programm müsste auf spezifische Sprache trainiert werden
- Es wäre richtig super, wenn auch Mundart verstanden würde

## Vorgehen
### Setup
Also erstmal muss ich rausfinden, was genau hier passiert und ob ich es in VS Code starten kann. Wenn nicht, würde mich das sehr unglücklich machen, da ich mich eigentlich nicht an eine neue Umgebung gewöhnen möchte.
Erste Frage ist: es scheint, als wären die rein Englischen Modelle besser - fange ich also mit so einem an und schaue dann, dass ich später ein multilinguales Model benutze und aufsetze? Oder fange ich direkt mit einem Mehrsprachenmodell an?
&rarr; Aufgrund der höheren Präzision und der Tatsache, dass doch viele von den Berichten Englisch sind, ergäbe es Sinn, erst ein Englisches Modell zu benutzen. Im Anschluss - wenn das so einfach ist, wie ich mir das vorstelle (ist es bestimmt nicht) - könnte ich denselben Code einfach für ein Mehrsprachenmodell ummünzen? 
&rarr; Beschluss: wir fangen mit einem Englischen Modell an.
&rarr; Nevermind, es schaut so aus, als wären die großen Modelle alle multilinugal, also benutzen wir mal [turbo]. Das scheint von der Größe und Geschwindigkeit sehr sinnvoll.


Ich sollte definitiv herausfinden, auf was genau der Code basiert, um das zumindest zu beschreiben. Ich muss es nicht zwangsläufig verstehen, aber ich sollte es beschreiben können.

### Code
1. Schritt: whisper installieren  
```py
pip install git+https://github.com/openai/whisper.git
```
2. Whisper benötigt FFmpeg, um Audiodateien zu verarbeiten. Also FFmpeg installieren für den PC. Danach muss es nicht mehr manuell installiert oder abgerufen werden, da es in Whisper enthalten ist.
3. Um das Ergebnis der Transkription in Word zu speichern, muss installiert werden.
```
pip install python-docx
```
4. Schritt: Code für Transkription über Python
&rarr; Hier wird sich die Sprache nicht spezifiziert oder detektiert, da dies nicht notwendig ist. Sie wird automatische erkannt. --> Verweis auf Skript.
Spezifizieren ist also nur bei mehr als einer Sprache notwendig.
Wenn gewusst wird, dass die Sprache Englisch ist, kann dies festgelegt werden, was die Genauigkeit erhöht.

### Überlegungen
- Es gibt bereits einige Tools, die Ähnliches machen und vermutlich auch besser, als ich es kann. Allerdings müssen dafür zur Not immer irgendwelche Leute zitiert werden und wenn ich deren Arbeit übernehmen würde, dann würden meine 70h vermutlich nicht gefüllt werden. Ich möchte schon ein bisschen versuchen, das alleine hinzubekommen.
Das heißt, noScribe aus Luzern und das Zeug aus Zürich werden als Inspiration verwendet, aber nicht übernommen.
- Mehrere Skripts (DE, EN, MIX) für Sprachversionen erstellen, um Genauigkeit zu erhöhen und dann je nach Sprache auswählen? 
- Die Audiodatein werden nicht im selben Ordner wie das Skript liegen, es muss also der Pfad ordentlich angegeben werden. &rarr; in diesem Kontext wäre es hilfreich, herauszufinden, ob es möglich ist, dass das Skript immer die "neuste" Audio aufgreift
- gff. ist das mit der neusten Audio noch zu hoch gestochen resp. interessant für später. Um zu testen, ob das ganze läuft, reicht ggf. auch einfach ein "Basic Skript"

Ergebnis, wenn Whisper geladen:
Building wheels for collected packages: openai-whisper
  Building wheel for openai-whisper (pyproject.toml) ... done
  Created wheel for openai-whisper: filename=openai_whisper-20240930-py3-none-any.whl size=813013 sha256=ab76fb4f2dc1a1983aecc9b23e951cfae289d6842855553c884963ec30607dad
  Stored in directory: C:\Users\lucid\AppData\Local\Temp\pip-ephem-wheel-cache-r5vqs6b9\wheels\1f\1d\98\9583695e6695a6ac0ad42d87511097dce5ba486647dbfecb0e
Successfully built openai-whisper
Installing collected packages: mpmath, urllib3, typing-extensions, sympy, regex, numpy, networkx, more-itertools, MarkupSafe, llvmlite, idna, fsspec, filelock, colorama, charset-normalizer, certifi, tqdm, requests, numba, jinja2, torch, tiktoken, openai-whisper
  WARNING: The script isympy.exe is installed in 'C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script normalizer.exe is installed in 'C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script tqdm.exe is installed in 'C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts convert-caffe2-to-onnx.exe, convert-onnx-to-caffe2.exe, torchfrtrace.exe and torchrun.exe are installed in 'C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script whisper.exe is installed in 'C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed MarkupSafe-3.0.2 certifi-2024.12.14 charset-normalizer-3.4.1 colorama-0.4.6 filelock-3.17.0 fsspec-2024.12.0 idna-3.10 jinja2-3.1.5 llvmlite-0.44.0 more-itertools-10.6.0 mpmath-1.3.0 networkx-3.4.2 numba-0.61.0 numpy-2.1.3 openai-whisper-20240930 regex-2024.11.6 requests-2.32.3 sympy-1.13.1 tiktoken-0.8.0 torch-2.5.1 tqdm-4.67.1 typing-extensions-4.12.2 urllib3-2.3.0

[notice] A new release of pip is available: 24.0 -> 25.0
[notice] To update, run: C:\Users\lucid\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip


Output bei erstem Versuch:

C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\whisper\__init__.py:150: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  checkpoint = torch.load(fp, map_location=device)
C:\Users\lucid\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\whisper\transcribe.py:132: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
Ein Fehler ist aufgetreten: [WinError 2] The system cannot find the file specified
PS C:\Users\lucid\Desktop\Whisper> 

Output beim Versuch den Fehler zu beheben:

PS C:\Users\lucid\Desktop\Whisper> ffmpeg -version
ffmpeg : The term 'ffmpeg' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct 
and try again.
At line:1 char:1
+ ffmpeg -version
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (ffmpeg:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException