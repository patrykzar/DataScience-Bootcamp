"""#Ustandaryzuj nazwę kolumny z datasetu.
Dane:
Wymagania:
Nazwa raw: " PATIENT_age_YEARS "
Usuń białe znaki
Zamień na małe litery
Oczekiwany rezultat:
(proste)
Zastąp _ przez " "
Użyj title case
Patient Age Years"""

nazwa = " PATIENT_age_YEARS "
nazwa = " PATIENT_age_YEARS "

nazwa = nazwa.replace('_', ' ').strip().title()
print(nazwa)

""" Zadanie 5 – Parsing ścieżki pliku
Wyodrębnij informacje ze ścieżki do pliku.
Dane:
Wymagania:
(proste)
Ścieżka: "data/processed/train_fold_03_normalized.csv"
Wyodrębnij: folder, typ zbioru (train/test), numer fold, format pliku
Użyj metod split() i indeksowania
Wyświetl każdą informację osobno"""

sciezka =  "data/processed/train_fold_03_normalized.csv"
sciezka = sciezka.replace('/', '_').replace('.', '_').split('_')
print(sciezka)

"""formatuj metryki modelu.
Dane:
Wymagania:
(proste)
Accuracy: 0.9234
Precision: 0.8891
Recall: 0.9456
Wyświetl każdą metrykę w procentach z 2 miejscami po przecinku
Użyj f-strings z formatowaniem :.2%
Dodaj estetyczne wyrównanie kolumn
"""
accuracy = 0.9234
precision = 0.8891
recall = 0.9456

print(f"{'Metric':<10} {'Value':>10}")
print("-"*20)

print(f"{'Accuracy':<10} {accuracy:>10.2%}")
print(f"{'Precision':<10} {precision:>10.2%}")
print(f"{'Recall':<10} {recall:>10.2%}")

"""Znormalizuj wartość do zakresu [0, 1].
Dane:
Wartość: 75
Wymagania:
(średnie)
Minimum w kolumnie: 50
Maximum w kolumnie: 100
Wzór: normalized = (value - min) / (max - min)
Oblicz dla wartości 75, 50, 100, 62.5
Sprawdź, czy wynik mieści się w [0, 1]
Wyświetl tabelkę: wartość oryginalna | wartość znormalizowana"""

# Dane
values = [75, 50, 100, 62.5]
min_val = 50
max_val = 100

# Normalizacja
normalized_values = [(v - min_val) / (max_val - min_val) for v in values]

# Wyświetlenie tabelki
print(f"{'Original':<10} | {'Normalized':<10}")
print("-"*25)
for orig, norm in zip(values, normalized_values):
    print(f"{orig:<10} | {norm:<10.2f}")  # :.2f -> dwie cyfry po przecinku