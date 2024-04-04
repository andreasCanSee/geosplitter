# GeoSplitter

## Überblick
GeoSplitter ist ein Python-Tool, um große GeoJSON-Dateien in kleinere, handhabbare Segmente aufzuteilen. Dies ist besonders nützlich, um die Ladezeiten und Effizienz bei der Arbeit mit umfangreichen geographischen Daten in Webanwendungen oder GIS-Projekten zu verbessern. Zusätzlich generiert GeoSplitter eine JSON-Karte, die jedes Segment mit einem spezifischen Koordinatenbereich verknüpft, um eine einfache Integration und Nutzung der segmentierten Daten zu ermöglichen.

## Voraussetzungen

Bevor du GeoSplitter verwendest, stelle sicher, dass Python 3.x auf deinem System installiert ist und folgende Pakete verfügbar sind:

- Geopandas: Eine Erweiterung für Pandas, um räumliche Daten einfach zu handhaben.
- Shapely: Für geometrische Operationen innerhalb der Python-Umgebung.

Diese Abhängigkeiten kannst du durch die Installation der `requirements.txt` Datei einbinden, die im Projekt enthalten ist.

## Einrichtung

1. Klone das GeoSplitter-Repository auf dein lokales System.
2. Installiere die erforderlichen Pakete mit Pip:

```bash
pip install -r requirements.txt
```

Die `requirements.txt` enthält alle notwendigen Python-Pakete, einschließlich:

- Geopandas (`geopandas==0.14.3`)
- Shapely (`shapely==2.0.3`)
- Fiona (`fiona==1.9.6`) für das Lesen und Schreiben von GeoJSON-Dateien

## Verwendung

1. **Vorbereitung der Eingabedaten:** Platziere deine GeoJSON-Datei im `data`-Unterordner. Ändere gegebenenfalls den `DATA_PATH` im Skript, um auf deine spezifische Datei zu verweisen.
2. **Konfigurieren der Segmentgröße:** Die `GRID_SIZE` Variable im Skript bestimmt, wie viele Segmente pro Dimension erstellt werden. Experimentiere mit verschiedenen Werten, um die optimale Größe für deine Anwendung zu finden.
3. **Ausführen des Skripts:** Starte das Skript, um die GeoJSON-Datei zu segmentieren und die JSON-Karte zu generieren.

Das Ergebnis sind mehrere kleinere GeoJSON-Dateien im `segments`-Ordner und eine `map.json`, die die Segmentdateien mit den Koordinatenbereichen verknüpft.

---

berprüfen der Koordinaten und der total_bounds
Das Problem könnte daran liegen, dass die total_bounds der vollständigen Datendatei nicht korrekt berechnet oder interpretiert werden. Es ist wichtig sicherzustellen, dass die Koordinaten in der vollständigen Datei im erwarteten Format und Bereich sind. Manchmal können extrem große oder kleine Werte (Ausreißer) in den Daten die Berechnung der total_bounds beeinflussen.

Lösungsansatz:
Prüfe die total_bounds der vollständigen Datendatei, um sicherzustellen, dass sie sinnvoll sind.
Untersuche die Daten auf mögliche Ausreißer, die die Berechnungen beeinflussen könnten.
2. Anpassung der GRID_SIZE
Wenn die GRID_SIZE im Verhältnis zu den total_bounds der vollständigen Datendatei zu klein ist, könnte das dazu führen, dass die Daten nicht wie erwartet aufgeteilt werden.

Lösungsansatz:
Experimentiere mit verschiedenen Werten für GRID_SIZE, um eine passendere Aufteilung zu finden. Es kann sein, dass du für die vollständige Datendatei eine größere GRID_SIZE benötigst.
3. Überprüfung der Filterlogik
Die Logik, die bestimmt, welche Datenpunkte in welches Segment gehören, könnte fehlerhaft sein oder nicht wie erwartet mit den vollständigen Daten funktionieren.

Lösungsansatz:
Stelle sicher, dass die Filterlogik korrekt implementiert ist. Insbesondere sollte die Überprüfung, ob ein Punkt innerhalb der Bounding Box eines Segments liegt, korrekt sein.
Überprüfe, ob die intersects-Methode von Geopandas wie erwartet funktioniert, indem du manuell einige Punkte testest.
4. Räumliche Indexierung
Für sehr große Datensätze kann die Verwendung eines räumlichen Index die Effizienz der Operationen verbessern.

Lösungsansatz:
Überlege, ob du einen räumlichen Index für deine GeoDataFrame vor der Filteroperation hinzufügen kannst, um die Leistung zu verbessern.
5. Debugging und Testen
Um das Problem besser zu verstehen, könnte es hilfreich sein, das Skript mit einem reduzierten Datensatz zu testen, der näher an der Größe der vollständigen Daten liegt, aber klein genug ist, um das Problem zu isolieren und zu debuggen.

Lösungsansatz:
Teile die vollständige Datendatei in kleinere Stücke und führe das Skript schrittweise aus, um zu sehen, ab welchem Punkt das Problem auftritt.