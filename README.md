# Dokumentacja Projektu - Symulator Skanera Laserowego
# Project Documentation - Laser Scanner Simulator

## Dane autora / Author Information
- Imię i nazwisko / Full name: Jakub Mierzejewski
- Nr albumu / Student ID: 337264
- Przedmiot / Course: Podstawy Informatyki i Programowania

## English

### Project Goal and Description
The project implements a robot laser scanner simulation for distance measurement. The program generates laser beams at various angles and detects obstacles in their paths. The system visualizes laser beam paths and saves measurement results. Using the Bresenham algorithm for line rasterization, the program accurately simulates the behavior of a real laser scanner.

### Technical Requirements

#### Input Files
1. `otoczenie.png` (environment file)
   - 320x240 pixel PNG image
   - Black pixels (RGB: 0,0,0) represent obstacles
   - White pixels represent free space
   - Defines the robot's environment

2. `parametry.txt` (parameters file)
   - Contains 3 space-separated values
   - Format: `<x> <y> <angle>`
   - x: robot's x-coordinate (0-320)
   - y: robot's y-coordinate (0-240)
   - angle: robot's orientation in degrees (0-360)

#### Output Files
1. `symulacja.png`
   - Environment visualization with laser beams
   - Red lines represent laser beams
   - Shows beam intersections with obstacles
   - Lengths limited to 60 pixels for visual prospects

2. `wyniki.txt`
   - Contains 19 lines with numeric values
   - Each line represents a laser beam length
   - Lengths measured in pixels

### Implementation Details

#### Core Components
1. **Point Class**
   - Represents 2D coordinates
   - Validates integer coordinates
   - Implements equality comparison

2. **Line Class**
   - Implements Bresenham's algorithm
   - Generates points along the line path
   - Handles various line orientations

3. **Laser Scanner Simulation**
   - Generates 19 laser beams at 10-degree intervals
   - Scanning range: base angle ± 90 degrees
   - Maximum beam length: 60 pixels
   - Detects obstacles through pixel color analysis

#### Key Algorithms
1. **Bresenham's Algorithm**
   - Used for efficient line rasterization
   - Ensures accurate pixel-by-pixel line drawing
   - Correctly handles all line orientations

2. **Obstacle Detection**
   - Checks for black pixels (RGB: 0,0,0) along beam path
   - Includes diagonal neighbor checking
   - Returns first detected obstacle point

### Dependencies
- Python 3.x
- Required libraries:
```
certifi==2024.12.14
charset-normalizer==3.4.0
idna==3.10
iniconfig==2.0.0
numpy==2.2.0
packaging==24.2
pillow==11.0.0
pluggy==1.5.0
pytest==8.3.4
requests==2.32.3
urllib3==2.2.3
```

### Installation and Setup
1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure input files are in the correct format:
   - `otoczenie.png` - PNG format, 320x240 pixels
   - `parametry.txt` - Text file with parameters in valid ranges

### Usage
1. Run the main program:
```bash
python Main.py
```

2. The program will:
   - Load the environment and parameters
   - Perform the laser scan simulation
   - Generate visualization (`symulacja.png`)
   - Save distance measurements (`wyniki.txt`)

### Testing
- Comprehensive test suite available in `Tests.py`
- Run tests using pytest:
```bash
pytest Tests.py
```

### Error Handling
The program includes robust error handling for:
- Invalid file extensions
- Missing input files
- Out-of-range parameters
- Invalid data formats
- Image dimension mismatches

### Project Structure
```
.
├── Classes.py      # Core classes (Point, Line)
├── DataLoad.py     # File loading and validation
├── Errors.py       # Custom error definitions
├── Functions.py    # Main simulation logic
├── Main.py         # Entry point
├── Tests.py        # Test suite
└── requirements.txt
```

### Limitations
- Fixed environment size of 320x240 pixels
- Maximum laser beam length: 60 pixels
- Fixed number of laser beams (19)
- Only handles black and white images
- Angles limited to 0-360 degrees

## Polski

### Cel i opis projektu
Projekt implementuje symulator skanera laserowego robota służący do pomiaru odległości. Program generuje wiązki lasera pod różnymi kątami i wykrywa przeszkody na ich drodze. System wizualizuje ścieżki wiązek laserowych oraz zapisuje wyniki pomiarów. Wykorzystując algorytm Bresenhama do rasteryzacji linii, program dokładnie symuluje zachowanie rzeczywistego skanera laserowego.

### Wymagania techniczne

#### Pliki wejściowe
1. `otoczenie.png` (plik środowiska)
   - Obraz PNG o wymiarach 320x240 pikseli
   - Czarne piksele (RGB: 0,0,0) reprezentują przeszkody
   - Białe piksele reprezentują wolną przestrzeń
   - Definiuje środowisko pracy robota

2. `parametry.txt` (plik parametrów)
   - Zawiera 3 wartości oddzielone spacjami
   - Format: `<x> <y> <kąt>`
   - x: współrzędna x robota (0-320)
   - y: współrzędna y robota (0-240)
   - kąt: orientacja robota w stopniach (0-360)

#### Pliki wyjściowe
1. `symulacja.png`
   - Wizualizacja środowiska z wiązkami lasera
   - Czerwone linie reprezentują wiązki lasera
   - Pokazuje przecięcia wiązek z przeszkodami
   - Długości ograniczone wizualnie do 60 pikseli

2. `wyniki.txt`
   - Zawiera 19 linii z wartościami numerycznymi
   - Każda linia reprezentuje długość wiązki lasera
   - Długości mierzone w pikselach

### Szczegóły implementacji

#### Główne komponenty
1. **Klasa Point**
   - Reprezentuje współrzędne 2D
   - Waliduje współrzędne całkowite
   - Implementuje porównywanie równości

2. **Klasa Line**
   - Implementuje algorytm Bresenhama
   - Generuje punkty wzdłuż ścieżki linii
   - Obsługuje różne orientacje linii

3. **Symulacja skanera laserowego**
   - Generuje 19 wiązek lasera w odstępach 10-stopniowych
   - Zakres skanowania: kąt bazowy ± 90 stopni
   - Maksymalna długość wiązki: 60 pikseli
   - Wykrywa przeszkody poprzez analizę koloru pikseli

#### Kluczowe algorytmy
1. **Algorytm Bresenhama**
   - Używany do efektywnej rasteryzacji linii
   - Zapewnia dokładne rysowanie linii piksel po pikselu
   - Poprawnie obsługuje wszystkie orientacje linii

2. **Wykrywanie przeszkód**
   - Sprawdza czarne piksele (RGB: 0,0,0) wzdłuż ścieżki wiązki
   - Zawiera sprawdzanie sąsiadów po przekątnej
   - Zwraca pierwszy wykryty punkt przeszkody

### Zależności
- Python 3.x
- Wymagane biblioteki:
```
certifi==2024.12.14
charset-normalizer==3.4.0
idna==3.10
iniconfig==2.0.0
numpy==2.2.0
packaging==24.2
pillow==11.0.0
pluggy==1.5.0
pytest==8.3.4
requests==2.32.3
urllib3==2.2.3
```

### Instalacja i konfiguracja
1. Instalacja wymaganych zależności:
```bash
pip install -r requirements.txt
```

2. Upewnij się, że pliki wejściowe mają prawidłowy format:
   - `otoczenie.png` - format PNG, 320x240 pikseli
   - `parametry.txt` - plik tekstowy z parametrami w odpowiednim zakresie

### Użytkowanie
1. Uruchom program główny:
```bash
python Main.py
```

2. Program:
   - Wczyta środowisko i parametry
   - Przeprowadzi symulację skanowania laserowego
   - Wygeneruje wizualizację (`symulacja.png`)
   - Zapisze pomiary odległości (`wyniki.txt`)

### Testowanie
- Kompletny zestaw testów dostępny w `Tests.py`
- Uruchomienie testów przy użyciu pytest:
```bash
pytest Tests.py
```

### Obsługa błędów
Program zawiera rozbudowaną obsługę błędów dla:
- Nieprawidłowych rozszerzeń plików
- Brakujących plików wejściowych
- Parametrów poza zakresem
- Nieprawidłowych formatów danych
- Niezgodności wymiarów obrazu

### Struktura projektu
```
.
├── Classes.py      # Podstawowe klasy (Point, Line)
├── DataLoad.py     # Ładowanie i walidacja plików
├── Errors.py       # Definicje własnych wyjątków
├── Functions.py    # Główna logika symulacji
├── Main.py         # Punkt wejścia
├── Tests.py        # Zestaw testów
└── requirements.txt
```

### Ograniczenia
- Stały rozmiar środowiska 320x240 pikseli
- Maksymalna długość wiązki lasera: 60 pikseli
- Stała liczba wiązek lasera (19)
- Obsługa tylko czarno-białych obrazów
- Kąty ograniczone do zakresu 0-360 stopni
