
class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, oceny, kody_przedmiotow):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny if oceny is not None else []
        self.kody_przedmiotow = kody_przedmiotow if kody_przedmiotow is not None else []

    def opis(self):
        return f"Student: {self.imie} {self.nazwisko}, Numer indeksu: {self.numer_indeksu}"

    def srednia_ocen(self):
        if len(self.oceny) == 0:
            return 0
        return sum(self.oceny) / len(self.oceny)

# Tworzenie instancji klasy
student1 = Student("Jan", "Kowalski", "123456")
print(student1.opis())

#Kolekcja studentów:
#Napisz klasę Grupa, która będzie przechowywać listę studentów.
#Dodaj metodę dodaj_studenta, która będzie dodawać nowego studenta do grupy.
#Dodaj metodę studenci_z_numerem_indeksu, która będzie zwracać listę wszystkich studentów z podanym numerem indeksu.


class Przedmiot:
    def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
        self.nazwa = nazwa
        self.kod_przedmiotu = kod_przedmiotu
        self.prowadzacy = prowadzacy
        self.ects = ects

    def opis(self):
        return  f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzacy}, ECTS: {self.ects}"

class Grupa:
    def __init__(self):
        self.students = []

    def dodaj_studenta(self, student):
        self.students.append(student)

    def studenci_z_numerem_indeksu(self, numer_indeksu):
        return [student for student in self.studenci if student.numer_indeksu == numer_indeksu]

    def srednia_ocen_wszystkich_studentow(self):
        wszystkie_oceny = []

        for student in self.studenci:
            wszystkie_oceny.extend(student.oceny)

        if len(wszystkie_oceny) == 0:
            return 0

        return sum(wszystkie_oceny) / len(wszystkie_oceny)

    def eksport_do_csv(self, nazwa_pliku):
        with open(nazwa_pliku, mode="w", newline="", encoding="utf-8") as plik:
            writer = csv.writer(plik)

            writer.writerow(["imie", "nazwisko", "numer_indeksu"])

            for student in self.studenci:
                writer.writerow([student.imie, student.nazwisko, student.numer_indeksu])

    def studenci_ze_srednia_wyzsza_niz(self, wartosc):
        return [student for student in self.studenci if student.srednia_ocen() > wartosc]

class PlanZajec:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def przedmioty_prowadzone_przez(self, prowadzacy):
        return [przedmiot for przedmiot in self.przedmioty if przedmiot.prowadzacy == prowadzacy]

    def suma_ects_studenta(self, student):
        suma = 0

        for przedmiot in self.przedmioty:
            if przedmiot.kod_przedmiotu in student.kody_przedmiotow:
                suma += przedmiot.ects

        return suma

