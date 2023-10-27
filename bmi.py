"""
Napisz program który:

- zapyta o imie
- zapyta o wzrost
- zapyta o wage

Na podstawie wprowadzonych danych, oblicz bmi i zapisz do pliku w formacie json.
Nazwa pliku pochodzi o wprowadzonego imienia

Zeby było ciekawiej:

program stwórz jak projekt na github i prowadź prace w gałezi 'dev'
Po zakończeniu utwórz nowy Merge Request (Pull Request) aby wprowadzić  kod do gałęzi main albo master.

Merge Request (Pull Request) będzie miejscem do komentowania kodu
"""

import json

imie = input("Podaj imię: ")
wzrost = float(input("Podaj wzrost (w centymetrach): "))
wzrost = wzrost /100
waga = int(input("Podaj wagę (w kg): "))

bmi = round(waga / (wzrost * wzrost),2)

dane = {
  "imie": imie,
  "wzrost": wzrost,
  "bmi": bmi}
plik = imie+".json"
print (imie.capitalize(), "Twoje BMI to: ", bmi)

with open(plik, "w") as outfile:
    json.dump(dane, outfile)

print("Plik zapisany jako: ", plik)
