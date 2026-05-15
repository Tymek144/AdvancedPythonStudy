class Przedmiot:
    def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
        self.nazwa = nazwa
        self.kod_przedmiotu = kod_przedmiotu
        self.prowadzący = prowadzacy
        self.ects = ects

    def opis(self):
        return f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzący}, ECTS: {self.ects}"

przyroda = Przedmiot("przyroda", "1", "A.Kowalska", 3)
print(przyroda.opis())

''' 
Kolekcja studentów:
Napisz klasę Grupa, która będzie przechowywać listę studentów.
Dodaj metodę dodaj_studenta, która będzie dodawać nowego studenta do grupy.
Dodaj metodę studenci_z_numerem_indeksu, która będzie zwracać listę wszystkich studentów z podanym numerem indeksu.
'''