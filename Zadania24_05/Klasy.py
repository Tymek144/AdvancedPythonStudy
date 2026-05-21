from statistics import mean
import csv

class Przedmiot:
    def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
        self.nazwa = nazwa
        self.kod_przedmiotu = kod_przedmiotu
        self.prowadzacy = prowadzacy
        self.ects = ects

    def opis(self):
        return f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzacy}, ECTS: {self.ects}"

class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, oceny, kody_przedmiotow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny
        self.kody_przedmiotow = kody_przedmiotow

class Grupa:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista = []

    def dodaj_studenta(self, student):
        self.lista.append(student)

    def studenci_z_numerem_indeksu(self, numerem_indeksu):
        wynik = []
        for student in self.lista:
            if student.numer_indeksu == numerem_indeksu:
                wynik.append(student)
        return wynik
    def srednia_wszystkich(self):
        wszystkie_oceny = []
        for student in self.lista:
            wszystkie_oceny.extend(student.oceny)
        if len(wszystkie_oceny) == 0:
            return 0
        return sum(wszystkie_oceny) / len(wszystkie_oceny)
    def eksport_csv(self, nazwa_pliku):
        tabela = []
        for student in self.lista:
            tabela.append([
                student.imie,
                student.nazwisko,
                student.numer_indeksu
            ])
        with open(nazwa_pliku, mode="w", newline="", encoding="utf-8") as plik:
            writer = csv.writer(plik)
            writer.writerow(["imie", "nazwisko", "numer_indeksu"])
            writer.writerows(tabela)
    def wyzsza_srednia(self, wartosc):
        studenci_srednia = []
        for student in self.lista:
            if sum(student.oceny)/len(student.oceny) > wartosc:
                studenci_srednia.append(student)

class PlanZajec:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def przedmioty_prowadzone_przez(self, prowadzacy):
        wynik = []

        for przedmiot in self.przedmioty:
            if przedmiot.prowadzacy == prowadzacy:
                wynik.append(przedmiot)

        return wynik

    def suma_ects_studenta(self, student):
        suma = 0

        for przedmiot in self.przedmioty:
            if przedmiot.kod_przedmiotu in student.kody_przedmiotow:
                suma += przedmiot.ects

        return suma


przedmiot1 = Przedmiot("Programowanie", "INF101", "dr Anna Nowak", 5)
przedmiot2 = Przedmiot("Matematyka", "MAT202", "dr Jan Kowalski", 6)
przedmiot3 = Przedmiot("Bazy danych", "INF303", "dr Anna Nowak", 4)
plan = PlanZajec()
plan.dodaj_przedmiot(przedmiot1)
plan.dodaj_przedmiot(przedmiot2)
plan.dodaj_przedmiot(przedmiot3)
student1 = Student("Jan", "Kowalski", "123456", [4, 5, 3], ["INF101", "MAT202"])
suma = plan.suma_ects_studenta(student1)
print(f"Suma ECTS studenta {student1.imie} {student1.nazwisko}: {suma}")









