# Koordinatensystem
Mein Koordinatensystem in Python

## Funktionen

### Zoom
Es gibt die Möglichkeit, im Koordinatensystem zu zoomen.

- Arrow-Up zum Reinzoomen
- Arrow-Down zum Rauszoomen

Das Achsen-Limit sind 1 im Reinzoomen und ca. 100k im Rauszoomen.

### Punkte
Punkte einzeichnen ist auch möglich

- Left-Click zum plazieren
- Konsoleneingabe ('ap', 'addpoint', 'addp', 'apoint') mit angehängten x + y Koordinaten

z.B. 
```
ap 3 3
```
Zeichnet einen Punkt bei x=3 und y=3 ein

Punkte werden immer P1, P2, P3 usw. benannt

### Linien
Punkte lassen sich zu Linien verbinden

- Arrow-Left verbindet die letzten zwei Punkte zu einer Linie
- Konsoleneingabe ('dr', 'drawline', 'drawl', 'dline', 'line') verbindet die letzten zwei Punkte zu einer Linie
- Konsoleneingabe ('dr', 'drawline', 'drawl', 'dline', 'line') mit angehängen zwei Punkten verbindet zwei bestimmte Punkte zu Linien

z.B. 

```
dr
```
Verbindet die letzten zwei Punkte zu einer Linie

```
dr P1 P2
```
Zeichnet eine Linie von P1 zu P2 

### Dreiecke
Drei Punkte lassen sich zu einem Dreieck verbinden

- Arrow-Right verbindet die letzten drei Punkte zu einem Dreieck
- Konsoleneingabe ('triangulate', 'connect3', 'tr', 'triangle', ) verbindet die letzten drei Punkte zu einem Dreieck
- Konsoleneingabe ('triangulate', 'connect3', 'tr', 'triangle', ) mit angehängen drei  Punkten verbindet drei bestimmte Punkte zu einem Dreieck

z.B. 

```
tr
```
Verbindet die letzten drei Punkte zu einem Dreieck

```
tr P1 P2 P3
```
Zeichnet ein Dreieck zwischen P1, P2 und P3



