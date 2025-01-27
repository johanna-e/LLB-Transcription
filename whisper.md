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
