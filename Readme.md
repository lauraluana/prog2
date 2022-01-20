# Read Me
### Ausgangslage
Als Student hat man oftmals nicht ein hohes Einkommen, ausser man ist schon Unternehmer. Vor kurzer Zeit habe ich mich mit meinen Finanzen beschäftigt und erkannt, dass ich vollkommen meinen Überblick verloren habe.
### Funktion / Projektidee
Um meine Finanzen besser zu verwalten, wäre es schön eine Applikation zu haben, wo alle Ausgaben festgehalten werden. 
## Workflow
### Dateieingabe
Jeden Tag, wo ich Ausgaben tätige, sollen die Ausgaben in die Applikation erfasst werden. Zusätzlich sollen die **Ausgaben in Kategorien** eingeteilt werden, wie zum Beispiel *(Lebensmittel, Shopping, Tabak, Tanken, etc.)*.

Nebst der **Währung** und **Betrag** der Ausgabe, soll auch das **Datum** erfasst werden, dass die Auswertung nach Datum gefiltert zu einem späteren Zeitpunkt eingebaut werden könnte. Ausserdem soll man auch Einahmen erfassen können.

![This is an image](/static/diagram1.jpg)
### Datenausgabe
Nach der Eingabe, werden die Daten an den Nutzer auf einer separaten Seite zurückgespielt. Des weiteren gibt es eine Seite namens Analyse, wo man anhand der Kategorie ein Balkendiagramm mit allen Ausgaben *(X-Achse = Datum, Y-Achse = Betrag)* erhält.

![This is an image](/static/diagram2.jpg)

Zusätzlich wird auf der Seite Summe die **Summen aller Beträge der jeweiligen Kategorie** angezeigt. Dazu wurde ein Funktion erstellt, die alle Beträge der jeweiligen Kategorie aus der Datei **ausgaben.json** liest.
## Bedienung
Zur Verwendung der Applikation muss die **main.py** Datei gestarten werden.

## Learnings
Bei der Entwicklung meiner Web-Applikation ist mir zuspät aufgefallen, dass man bei der Programmierung eines Diagramms darauf achten muss, welche Technologie man anwendet. Ich habe leider mit **matplotlib.pyplot** gearbeitet, was dazugeführt hat, dass ich das Diagramm nicht in das HTML einfügen kann. Beim Versuch den Fehler in der letzte Woche zu beheben, ging schliesslich alles schief. Nach langen Überlegen, entschied ich mich dazu, dass Diagramm mit der falschen Technologie so stehen zulassen, so dass der Rest der Applikation normal laufen kann.

## Mögliche Erweiterungen

- Mann könnte die Ausgaben auch als eine Tabelle darstellen, so dass es wie ein Bankauszug aussieht.
- Falls mehrere Personen auf das gleiche Konto Zugriff haben, könnte man im Formular so gestaltet, dass noch die Auswahl der Person möglich wäre
- Als Meisterarbeit könnte man Versuchen, alle Ausgaben als CSV-Datei von der Web-Applikation herunter zuladen
