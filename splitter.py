import geopandas as gpd
import json
import os
from shapely.geometry import box

# Definiert Pfade für Eingabe- und Ausgabedaten sowie Basispfad der Ausführung
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'trees-test.geojson')
SEGMENTS_DIR = os.path.join(BASE_DIR, 'segments')

# Festlegen der Anzahl von Segmenten pro Achse im Raster
GRID_SIZE = 4

def create_segments(gdf, json_map):
    """
    Erstellt segmentierte GeoJSON-Dateien basierend auf den definierten Rastersegmenten.
    
    :param gdf: GeoDataFrame der originalen GeoJSON-Daten.
    :param json_map: Liste von Dictionaries, die Rastersegmente und Dateinamen definieren.
    """
    for segment in json_map:
        # Erstellt eine Bounding Box für das aktuelle Segment
        bbox = box(segment["min_x"], segment["min_y"], segment["max_x"], segment["max_y"])
        # Selektiert Features, die sich innerhalb der Bounding Box befinden
        segment_gdf = gdf[gdf.intersects(bbox)]
        
        # Speichert das Segment als GeoJSON, wenn es Features enthält
        if not segment_gdf.empty:
            segment_path = os.path.join(SEGMENTS_DIR, segment["file_name"])
            segment_gdf.to_file(segment_path, driver="GeoJSON")

def main():
    # Lädt die ursprünglichen GeoJSON-Daten in eine GeoDataFrame
    gdf = gpd.read_file(DATA_PATH)

    # Ermittelt die äußeren Grenzen der GeoDataFrame
    minx, miny, maxx, maxy = gdf.total_bounds

    # Berechnet die Dimensionen eines einzelnen Segments
    width = (maxx - minx) / GRID_SIZE
    height = (maxy - miny) / GRID_SIZE

    # Initialisiert die Liste, die die Karte der Segmente speichert
    json_map = []

    # Generiert die Segmente basierend auf dem Raster
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect_minx = minx + x * width
            rect_miny = miny + y * height
            rect_maxx = rect_minx + width
            rect_maxy = rect_miny + height
            file_name = f'segment_{x+1}_{y+1}.geojson'
            json_map.append({
                "min_x": rect_minx,
                "max_x": rect_maxx,
                "min_y": rect_miny,
                "max_y": rect_maxy,
                "file_name": file_name
            })

    # Stellt sicher, dass das Ausgabeverzeichnis existiert
    os.makedirs(SEGMENTS_DIR, exist_ok=True)
    
    # Ruft die Funktion zum Erstellen der Segment-Dateien auf
    create_segments(gdf, json_map)

    # Speichert die Karte der Segmente als JSON
    map_path = os.path.join(SEGMENTS_DIR, 'map.json')
    with open(map_path, 'w') as f:
        json.dump(json_map, f, indent=4)

if __name__ == '__main__':
    main()
