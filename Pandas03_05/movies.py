import pandas as pd

def Zadanie1 ():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1", skiprows=[1])
    print(df[df['Year'] == 2000])

Zadanie1()

def Zadanie2 ():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1", skiprows=[1])
    srednie_dlugosci = df.groupby('Director')['Length'].mean()
    print(srednie_dlugosci)

Zadanie2()

def Zadanie3 ():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    new_df = df['Title', 'Director', 'Popularity']
    new_df.to_csv('movies.csv', sep=';', encoding="ISO-8859-1")

def Zadanie4 ():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    filmy_z_nagrodami = df[df['Awards'] == 'Yes'].shape[0]
    wszystkie_filmy = df.shape[0]
    procent_z_nagrodami = (filmy_z_nagrodami / wszystkie_filmy) * 100
    print(f"Procent utworów z nagrodami: {procent_z_nagrodami:.2f}%")

def Zadanie5 ():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    print(df[df['Director'] == 'Kubrick'])

def Zadanie6 ():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    df['Popularity'] = pd.to_numeric(df['Popularity'], errors='coerce')
    comedy = df[df['Subject'] == 'Comedy']
    suma_komedi = comedy['Popularity'].sum()
    print(suma_komedi)
