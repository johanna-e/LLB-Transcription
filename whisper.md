# 70 Stunden-Projekt: Aufsetzen des Whisper-Transkriptionstools von OpenAI für das Schlaflabor


27.01: 10:30 - 12:00; 12:30 - 13:15, 15:20 - 17:30 // 4.25 / 70h
--> Recherche, aufsetzen der VS Code Umgebung, des Repos, der MD-Dokumentation und der Skripte. VR PC im Sleeplab vorbereiten für Whisper: Download VS Code, Python, FFmpeg (auch wenn das nicht funktioniert), klonen des Repos, um leichter arbeiten zu können, erster Trial-Run (which failed, but that was to be expected).
--> Für heute sind wir fertig. Morgen gehts dann daran rauszufinden, warum das nicht richtig funktioniert.

28.01: 13:30 - 17:00, 22:00 - 22:15 // 8.15 / 70h
--> Heute: Modelle getestet, Fehler von gestern behoben. Whisper läuft jetzt über die GPU und über das turbo Modell. 
--> Als nächstes: Listenweise Transkriptionen, spez. Z05 Transkripionen (also inkl. Konvertierung). Transkriptionen aud DE und MIX, herausfinden, wie Transkriptionen von Mundart möglich sind. Schönes Repo gestalten. Anleitung schreiben. 

29.01: 10:20 - 11:50, 12:20 - 13:00 // 10.25 / 70h
Plan für heute: Die anderen Skripte aufsetzen. Übersetzungen probieren.
Plan für "away from lab pc": diese Dokumentation aufräumen, Bild für README gestalten, Anleitung aufsetzen, Gedanken über Workflow machen 
--> Skript für die listenweise und multilinguale Transkription aufgesetzt und ausgeführt. 
--> Als nächstes: Übersetzungen gezielt einsetzen (In MIX Skripten und extra Skript für die Übersetzung von DE Berichten --> Gedanken, ob bestehender Text übersetzt werden soll, oder gesprochener); Mundart; Whisper trainieren. Komplexeres Skript für Erkennen der Sprechenden aufsetzen und auf Effizienz testen.
--> Recherchearbeit kannst du auch von daheim aus machen, Johanna. Und das hier aufräumen auch ;)
--> Irgendwann sollte ich die Ordnerspezifischen Namen in den Skripten auch anpassen. Aber das wäre ja ein iterativer Prozess und sollte in einer Anleitung festgehalten werden, damit auch Personen nach mir das hinbekommen können.

02.02: 8:00 - 10:05 // 12.30 / 70h
"Titelblattdesign" für das Readme auf GitHub. Es war vermutlich nicht notwendig, so etwas zu diesem Zeitpunkt im Prozess zu machen, aber ich konnte mich nicht davon abhalten. Es schaut jetzt schon irgendwie deutlich schöner aus. Ob dafür fraglich viel Zeit draufgegangen ist, nur damit es ästhetisch ausschaut... vielleicht.

05.02.: 11:00 - 14:00 // 14.30 / 70h
Plan für heute: Sollte ich zuerst meine Doku sortieren? Ich glaube nicht. Es fühlt sich auch nach verschwendeter oder zumindest nicht korrekt genutzter Arbeitszeit an, wenn ich an einer ordentlichen Dokumentation sitze anstatt an etwas tatächlich inhaltlichen.
Ziel ist nach wie vor:
[x] einmal alle Skripte haben --> das wäre liste/einzeln, DE/EN/MIX und Übersetzung (ich glaube das sollte automatisch auswählen ob von DE zu EN oder andersrum, aber wenn es spezifiziert genauer ist, machen wir auch das.)

10.01: 15:30 - 16:00 // 15.00 / 70h
--> Leider einfach nur kleine Bugfixes im Labor.

13.03: 15:00 - 18:00 // 18.00 / 70h
Plan für heute: Tutorial schreiben, sodass mehrere Personen den Schmarrn bedienen können.
--> Tutorial wurde geschrieben. Die Bilder spezifisch für den Lab-PC fehlen noch, genauso wie einige Details (diese sind aber festgehalten innerhalb des Tutorials).

14.02: 11:30 - 15:30 // 22.00 / 70h
--> Whisper auf Büro PC einrichten. Geht leider nicht.
Deswegen: Tutorial fertig und Modelle (turbo vs. large) testen.

18.02: 11:00 - 13:00 // 24.00 / 70h
--> Arbeit an einem anderen Transkriptionsprojekt, welches aber diverse Learnings ermöglicht hat (s.u.)

19.02: 11:15 - 11:55 //
Update, Modelle gegeneinander testen


## Ressourcen:
Website: https://openai.com/index/whisper/

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
- Außerdem, wenn das auch geht, wäre es auch gut, wenn es direkt ein Skript geben würde, welches laufen gelassen werden kann, für die Übersetzung --> machbar
- schön wäre auch, wenn es ein Skript gibt, was einfach eine Liste an Berichten durchgeht und transkribiert --> schon gemacht
- Skript läuft automatisch in einem gewissen Zeitfenster, sodass wirklich nur noch die Aufnahmen hochgeladen werden müssen --> machbar, aber dafür sollte ich mir ein paar logisitsche Gedanken gemacht haben und mal mit Daniel reden. (Erste Idee: oben in Emmas & Xinlins Büro ist ja auch ein leistungsstarker PC, wenn der das machen könnte, wäre die ganze Sache etwas überwachter? Dann müsste nur definitiv an irgendeiner Stelle stehen, wann und wie das ganze aufhört bzw. beendet werden kann.)

### Tertiäte Ziele:
&rarr; Diese Ziele sind vorerst schwieriger zu erreichen und vermutlich weniger relevant für das zentrale Ziel der Transkription der Traumberichte. Diese Ziele würde ich ggf. auch über die 70h weiterverfolgen, einfach nur weil ich dem Projekt gerne einen richtig guten Schliff geben möchte. Heißt auch, *note to self*, an diesen Zielen sollte ich mich vorerst nicht aufhängen. Ich glaube das wird das schwerste.
- Erkennung von Sprechenden --> schwierig
- Das Programm müsste auf spezifische Sprache trainiert werden --> auch bisschen schwierig
- Es wäre richtig super, wenn auch Mundart verstanden würde --> das ist bisschen schwierig, nochmal Uni Zürich konsultieren
- Akkuratere Übersetzugen über ein anderes Tool als Whisper integrieren

### Ultimatives Ziel:
Eine Desktopanwendung, die das alles kann. Aber, Schusterin, bleib bei deinen Leisten.

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


### Tageweiser Fortschritt

**Day 2:** Also, es braucht irgendwas mit [torch], damit das Whisper die GPU benutzt und ein bisschen schneller laufen kann. Das war im Urpsrungscode auch nicht drin. Das haben wir jetzt mal verbessert. Hoffnung ist, dass es jetzt also ein bisschen fixer funktioniert. Ausserdem wurde der Weg zu FFmpeg auch ins System und nicht nur dem User eingefügt, vielleicht hilft das auch. 
Wir haben ein erstes Ergebnis! Und das passt einigermaßen gut zu dem, was ich bisher übersetzt habe.

GPU funktioniert nicht, weil pyTorch mit CUDA Uterstützung auf Python 3.11 nicht funktioniert. Aber bevor Python jetzt irgendwie wild installiert wird, würde ich vorschlagen. dass erstmal die CPU benutzt wird, weil so super langsam war das gar nicht.

Aktuell: Knapp 2-3 Minuten für 5 Minuten in turbo.
Versuch mit large: 3MiB/s
--> Mal schauen, ob large akkurater ist, aber aktuell und über die CPU ist es definitiv zu langsam.

Versuch über GPU, mal schauen wie lange. Also, das [large] Modell braucht entschieden zu lange. Wir sind bei über 15 Minute. Also entweder ist das jetzt super exakt oder es wird verworfen.

Plan: [turbo] über GPU laufen lassen --> weniger als 1 Minute. Wir behalten Turbo über die GPU.


Fixes update: ich hab irgendwie mist beim updaten gemacht (i kinda knew that) und jetzt muss ich mich morgen mal hierum kümmern. Es kommen aber noch knapp 15 Minuten auf meine arbeitszeit drauf. :D

**Day 3:** Learning: Gewisse Dinge sind case sensitive. Ich habe im Skrpit zur Listentranskription wma zu WMA geändert und jetzt werden meine 51 Berichte transkribiert. Und das sogar ziemlich fix.
Reflektion: Es hieß mal, dass Repos oder sowas in OneDrive Ordnern schwierig sind. Wenn das später also alles online läuft, ist die Frage, wie lange das gut geht. Es sollte nur einfach an einer Stelle festgehalten sein, denn wenn Fehler auftreten, könnte das eine Anlaufstelle zum Troubleshooting sein.
Neue Erkenntnis: Ein fast autonomes Laufen des Skriptes sollte gehen. Genauer finde ich das noch raus, das ist aktuell ja irgendwie nicht der Plan. Oder halt für später.

To Do: 
[x] Listwise Skript wieder verallgemeinern bzw. abändern. Die Konvertierung brauch es ja auch nicht für alle Fälle. --> Wobei sie vermutlich auchnicht schadet. Also nochmal checken, das kann eigentlich drin bleiben.
[x] Ausprobieren, wie das funktioniert, wenn die Sprache gemischt ist. 
[] Erkennen der Sprechenden wäre noch ordentlich cool. ChatGPT sagt hierzu: Sprecherkennung (rudimentär).
[x] Übersetzungen.
[] Rausfinden, wie Zürich es geschafft hat, dass Mundart gekonnt wird.
[x] Allgemein rausfinden, wie sich Whisper trainieren lässt. --> bisschen schwierig, eigentlich gar nicht.

Zur Erkennung von sprechenden sagt ChatGPT: Leider bietet Whisper keine eingebaute Funktion zur Speaker Diarization. Wenn du wirklich die Sprecher zuordnen möchtest, müsstest du eine zusätzliche Bibliothek wie pyannote.audio verwenden, die die Sprecher anhand von Audiointervallen erkennt. Hier ist eine einfache Methode zur Trennung der Sprecher in einem rudimentären Format:
Es gibt keine direkte Möglichkeit in diesem Code, zwischen den Sprechern zu unterscheiden, ohne eine separate Speaker-Diarization-Lösung zu verwenden.
Für eine echte Sprecherzuordnung müsste man nach der Transkription die Pausen und Sprecherwechsel zwischen den Sätzen auswerten und dann manuell oder automatisch Speaker 1 und Speaker 2 zuweisen. Diese Funktionalität würde jedoch zusätzliche Bibliotheken und deutlich mehr Komplexität erfordern. --> Demnach wäre das ein längerfristiges Ziel.

Weitere Überlegung: Wenn der PC das automatisch Abrufen soll, dann geht vermutlich nur 1 Skript? Über die Logisitk mache ich mir zu einem anderen Zeitpunkt nochmal Gedanken.
Interessanter Turn: Es ist anscheinend eine Übersetzung in meinem MIX-Transkript drin, die da Überhaupt nicht hinsoll. 
Noch eine Erkenntnis: Anscheinend übersetzt Whisper teilweise automatisch. Umso wichtiger, dass am Ende spezifizierte Skripte entstanden sind. 

Im MIX Skript wird aktuell das [large] Modell verwendet. Aber das braucht aktuell nicht allzu lange und da die Sprachen gemischt sind, ist alles, was akkuratere Ergebnisse verspricht, eigentlich gern gesehen. Vor allem, da das aktuell auch unter einer Minute dauert. Frage ist dann, warum das gestern so lange war. 
Es ist möglich im Code Whisper eine gezielte Aufgabe zu geben. Das sollte ich im Kopf behalten.

&rarr; Es wird nicht automatisch in "Chunks" unterteilt, dass muss Whisper auch gesagt werden. So wird sonst eine Sprache für ein Dokument erkannt und mehrsprachige Transkriptionen können trotzdem übersetzt und falsch erkannt werden. 
Whisper kann grundsätzlich mehrere Sprachen in einer Audiodatei erkennen. Allerdings wird die gesamte Datei standardmäßig einer einzigen Sprache zugeordnet.

Der gute ChatGPT:
Das bedeutet:
✅ Wenn die Datei komplett auf Deutsch oder komplett auf Englisch ist, wird die richtige Sprache erkannt.
⚠️ Wenn die Datei mehrsprachig ist, wird oft nur eine Hauptsprache erkannt, und Teile in anderen Sprachen könnten falsch transkribiert oder fehlinterpretiert werden.

Chunks werden erstmal auf 30s gesetzt. Frage ist, ob das zu lang ist? --> Ergebnis: Das mit den Chinks und den Sprachen funktioniert gut. Aber sie wären definitiv zu lang. Kürzere Chunks wären mehr Rechenarbeit, aber da das aktuell noch schnell funktioniert, denke ich, ist das ein sehr akzeptabler trade-off.

Aktuell versuchen wir mehrsprachige Transkription meherer Datein (N=11), Chunks = 10s, Modell = large. Dauer: ca. 7 - 8 Minuten.

**Day 4:** Aktuell prüfen glaube ich nur die Skripte für die Listen-Transkriptionen auf eine GPU. Ich finde das aber okay bzw. würde das auch nicht in den anderen Codes nicht einbauen, weil diese 1. aktuell noch mit dem [turbo] Modell arbeiten, welches weniger Leistung braucht als das [large] Modell und daher zur Not auch über die CPU laufen kann. Das heißt, zumindest dem status-quo am 5.2 nach würde ich sagen, würde sowas den Code nur unnötig unübersichtlich machen. Ich halte es aber nicht für unmöglich, dass ich meine Meinung diesbezüglich nochmal ändere.
Ich sollte ggf. schauen, dass alles, was mit MIX läuft, über [large] funktioniert? --> Ich könnte die Skripte auch dann so anpassen, dass der Durchlauf nicht stattfindet, wenn keine GPU gefunden wird. Das könnte davor schützen, dass der PC sich einer enormen Belastung der CPU unterzieht.

Um das mit den Übersetzungen zu starten, habe ich direkt mal das mit den spezifischen Skripten probiert (um das Deutsche Transkript zu haben) und das funktioniert. Das läuft soweit.
Übersetzung: Erstmal in einem eigenen Skript, nicht automatisiert in den anderen. Vielleicht ließe sich ja am Anfang etwas einbauen in die Richtung von: alle Dateien übersetzen, die neuste oder eine bestimmte. Für die Übersetzung packen wir alle Optionen (list, one, spec) in ein Skript, weil ich erstmal davon ausgehe, dass die Übersetzungen gezielt initiiert werden, während es schön wäre, wenn die Transkriptionen so autark wie möglich laufen könnten.
Also, Übersetzungen mit Whisper sind echt nicht so ganz das Wahre. Und irgendwie vielleicht auch sinnlos vor dem Hintergrund, dass am ehesten ja schon der konvertierte Bericht übersetzt werden sollte. Ich denke, es ist mäßig hilfreich, das Skript trotzdem zu haben, aber ich halte es für eine eher wenig sinnige Lösung für Übersetzungen. Das ist also etwas, was gegen Ende angegangen wird; anhand eines anderen Tools.  



### To-Do's für 5.02
[x] one_DE Skript --> + Sätze in einzelnen Zeilen in Output in DE und EN, MIX hatte das schon  
[x] list_EN Skript  
[x] spezifische Transkription  
[x] translate_to_DE  --> DE und EN unterscheiden sich im Skript nicht, tun sie wohl :'D Aber da die Übersetzung echt nur so mittelmäßig ist, würde ich an dieser Stelle mal nicht weiterarbeiten.  
[x] translate_to_EN  
[x] ggf. anfangen ein Tutorial zu schreiben. --> 13.02

**Day 7:**
Tutorial schreiben. Es ist etwas seltsam ein Tutorial zu schreiben für eine Version, die nicht die finale sein soll. Aber es muss ja auch funktionieren.
Ich sollte defininitv dran denken, dass Bilder in das Tutorial eingefügt werden, also auch Bilder, die ich nicht von daheim aus bereitstellen kann!

- Sollte ich einen zweiten Branch erstellen für die Aktivitäten im Sleeplab? Das könnte alles im Endeffekt dann deutlich weniger chaotisch machen?

**Day 8:**
Whisper auf dem Büro PC einrichten; das sollte den Workflow gewissermaßen vereinfachen. 
Überlegung: Für den Büro-PC wird dann ein Branch erstellt, auf dem nur die Transkriptionen stattfinden. Da muss ja nichts gepusht oder gepullt werden, der muss ja eigentlich nur so laufen. 
Also, plottwist, ich kann noch nicht am Büro-PC arbeiten, da ich dort in VS Code Änderungen an Nicolas Arbeit vornehmen müsste (die er nicht gespeichert hat) und ich würde ungern irgendwo reinfunken. Also marawa nüscht.
Dann bleibts beim ursprünglichen Plan, das Tutorial erstmal so fertig zu stellen. Und ggf. hier nochmal mehr Ordnung reinzubringen.

--> Ich könnte als nächstes dann mal schauen, was aktuell der Status quo ist und ob ich nicht doch auf das [large] Modell komplett umsteige. Außerdem würde ich eigentlich gerne, wenn ich schon mit [large] arbeite, eine Unterbrechung des Vorganges einbauen, wenn keine GPU gefunden wird. Oder halt, dass, wenn keine GPU gefunden wird, nicht mit [large] sondern mit [turbo] weiter transkribiert wird. Ich denke, dass könnte ganz gut in Sachen Prävention von unnötiger Rechenleistung sein.

--> Ich glaube eines meiner langfristigen Ziele könnte sein, dass das Repo deklariert und auch so zu benutzen ist, dass es keinen Anspruch erhebt darauf, in einer hohen Klasse des Programmierens unterwegs zu sein, sondern vielmehr, dass es direkt umgesetzt werden kann, auch von Personen, die keine Erfahrung haben mit Programmieren (so wie ich). Dafür bräuchte es eben ein Code Beispiel bezüglich zu: wie wird Whisper quasi installiert.

Also, das [turbo] Modell ist in folgenden Skripts:
--> schauen, wie fix die laufen, wenn sie über [large] laufen würden und ggf. demnach umschreiben
--> also, meine Erwartung, jetzt wo ich 51 Berichte laufen lasse ist, dass es die Zeit nicht wert ist? Außer natürlich, es dauert nicht so lang, wie erwartet. Dann wäre denke ich auch eine "längere" Zeit bezogen auf Richtigkeit oder so natürlich auch okay in Kauf zu nehmen. Ich kann auch mal ChatGPT fragen, ob es sinnvoll ist, eine Entscheidung in das Skript einzubauen?
--> [large] wurde ja verwendet, um eine bessere Transkription bei gemischten Audiodateien hinzubekommen. Ich denke, bei listen ergibt es ehrlich gesagt ab einer gewissen Länge nur bedingt Sinn. Ich könnte aber auch einfach einen Schritt in das Tutorial einbauen, der das erklärt. Dann läuft das ganze nicht nur nach meinem Ermessen, sondern kann auch abgewandelt werden. 
Ich sollte herausfinden, wie qualitativ unterschiedlich die sind.

- list_DE --> 51 berichte hahahahaha. Also das dauert so ungefähr eine halbe Stunde (27min). Wenn das okay ist, kann mit [large] gearbeitet werden. Vergleich turbo:; ca. 9min. Ich finde jetzt mal heraus, wie deutlich die Unterschiede sind, aber das ist zumindest von der Zeit her schon eine Hausnummer.
- list_EN
- one_DE
- one_EN
- spec_De
- spec_EN --> 18sec mit [turbo], mit [large] grob 1.16sec. Da sollte auch der Test auf Genauigkeit dann ausschlaggebend sein.

[large]
- list_MIX
- one_MIX
- spec_MIX

**To-do's für später:** Tutorial um Modell-Infos erweitern, verschiedene Versionen gegeneinander Testen.

**Day 9:**
- Mein Skript benutzt und umgeschrieben für die BA eines Kommilitonen. So habe ich herausgefunden, dass sich die command-line mit result=model.transcribe() noch erweitern und spezifizieren lässt --> interessant für lange Sätze. Ich sollte also mal mich mit temperature() und beam_size() auseinandersetzen, herausfinden, was genau das ist und, ob es noch weitere Dinge in die Richtung gibt, die interessant für mich wären
- [large] ist nicht das aktuellste größte Modell, es gibt [large-v3], das sollte ich definitiv implementieren
- das Exportieren nach Excel funktioniert auch sehr wunderbar, das wäre also auch schon möglich. 
- auch das mit den Zeitstempeln ist echt interessant; für sleeplab Zwecke ggf. weniger, aber trotzdem sehr interessant
- ich denke Sprechererkennung sollte nach wie vor möglich sein, aber das ggf. erst deutlich später, weil das schon mit einiges an Aufwand verknüpft zu sein scheint
- es ist möglich, dass Bestätigungsmails gesendet werden, sobald die Geschichte fertig ist

--> es stellt sich übrigens auch raus, dass ich verschiedene Python Versionen habe (ich glaub das war aufgrund von torch oder so). Das ist per se kein Problem, aber es ist etwas messy und ich sollte definitiv aufpassen, dass mir das am Büro-PC nicht passiert

**Day 10**
- also, ich habe ein Skript laufen lassen, um die beiden Texte zu vergleichen (also turbo und large) und anscheinend unterscheiden sie sich stark. Heißt, ich lasse sie jetzt mal gegen meine eigene Transkription laufen und gucke, was besser ist
- [large] & JH : Distanz und Fehlerquote geringer
- [turbo] & JH : Distanz deutlich geriner, Wortfehlerquote auch.

--> also erstmal [turbo]

### Neudefinition Hauptziel
1. One Script to rule them all. 
&rarr; in dem Sinne, das ein Skript alle möglichen Transkriptionen anfertigt. Es wird gefragt, was gemacht werden soll und dann macht das Skript das automatisch. 
2. Eine Appliikation, die ein besseres GUI hat als VS Code.

### To-Do's im Prozess
[] Modellentscheidung überdenken, aktuell schein [large] auch ganz gut zu funktionieren  
[] Sprache im Code anpassen --> Kommentare, Überschrift Ausgabedatei  
[] Skripte allgemein überarbeiten und bereinigen --> durch das ständige Benutzen (ohne zu genaues Gegenchecken meinerseits) von ChatGPT sind die Skripte unfasssbar unterschiedlich. Das braucht es irgendwie nicht.  
[] Ich glaube ich sollte für das Repo auch noch ein Dokument aufsetzten, was erklärt, warum die Skripte so sind, wie sie sind? Also das, was ich hier mache, nur besser?
[] Bilder in Tutorial einfügen
[] Abchecken, ob das Tutorial auch tatsächlich den Laborbedingungen folgt. 
[] README anpassen --> Verlinkung der Skripte und Tutorial.


**Feststellung**
Erster Versuch Übersetzung gescheitert, weil Whisper nicht mit Word-Dateien arbeitet, sondern nur mit Audio, das ergibt ja Sinn. Also stellt sich jetzt die Frage: entweder also suche ich mir was, das mit Word zusammenarbeitet oder ich lasse die Audio direkt übersetzen. Frage ist, was besser - also akkurater - funktioniert. Also: da ich mein Hauptprojekt Whisper und die Transkriptionen sind, machen wir die Übersetzungen auch vorerst mit Whisper. Für höhere Genauigkeit sind andere Tools (MariamMT [Vorschlag ChatGPT, ich sollte mal PyPi checken]) besser. Das ist also ein tertiäres Ziel.

### To-Do's zum Abschluss
[] Skripte generalisieren --> aktuell stehen noch spezifische Ordnernamen drin, die werden dann irgendwann nicht mehr passen  
[] Whisper auf richtigem PC aufsetzen  
[] Definitiv mit Ralf abklären, ob das alles so in Ordnung ist. Falls mir ein Fehler passiert ist - und ich bin mir sicher, dass ChatGPT und ich sehr fehleranfällig sind - wäre es schön, wenn so wenig wie möglich dadurch in Mitleidenschaft gezogen würde (bspw. ein Befehl im Code ist falsch und der Rechner überlastet sich, ohne, dass jemand das mitbekommt)

Zwischenfrage: Aktuell wird nur immer die neuste Audio oder eben ein ganzer Ordner transkribiert. Wenn ich allerdings eine spezifische hab, müsste ich das ganze noch anpassen. Frage ist, ob ich dafür auch ein eigenes Skript brauche, oder ob ich sowas ins Tutorial (aber ansonsten "one" umbenennen in "new" [dann wird das neuste immer genommen] und das skript, wo eine gezielte verwendet wird, dann "one" nennen) --> ich habe mich für "spec" = specific entschieden, da "new" irgendwie gefühlt etwas missverständlich wäre. Weil jede zu erstellende Transkription ist ja irgendwie neu. Das wäre noch eine vernünftige Idee. Meine Sorge an der Stelle ist, dass es zu "simpel" ist und alle Leute, die so voll im Game drin sind, meine Ansätze peinlich finden, weil es sich auch einfacher lösen ließe. Aber das wäre dann eben so, würde ich sagen.

Jetzt fällt mir auch ein: Was wäre, wenn ich ein Skript hätte, was folgendes kann:
- es fragt, was gemacht werden soll (Transkription von welcher Sprache [EN, DE, MIX], one/list/new, Übersetzung)
- fragt nach input/output folder
- ggf. nach namen der Audiodate (if "one")
- ruft dann eigenständig den Code dafür ab
- läuft dann automatisch
- fragt, ob Übersetzung stattfinden soll
--> das sollte doch bestimmt irgendwie gehen?
--> definitiv gegen Ende, now focus Johanna
