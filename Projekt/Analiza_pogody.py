import pandas as pd
import numpy as np
import requests
from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.dates as mdates # formatowanie osi czasowej X na wykresie
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Pobieranie współrzędnych geograficznych na podstawie nazwy miasta
def get_city(city_name): #brakuje obsługi błędów wpisania (wielkość znaków i polskie znaki bez znaczenia)
    if city_name.strip() == "":
        raise ValueError("Nie wpisano nazwy miasta.")
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": 1,
        "language": "pl",
        "format": "json"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Brak połączenia z internetem.")
    except requests.exceptions.Timeout:
        raise TimeoutError("Przekroczono czas oczekiwania na odpowiedź API.")
    except requests.exceptions.HTTPError:
        raise RuntimeError("API geokodowania zwróciło błąd HTTP.")
    except requests.exceptions.RequestException:
        raise RuntimeError("Wystąpił problem podczas pobierania danych miasta.")

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        raise ValueError("Nie znaleziono podanego miasta. Sprawdź pisownię.")
    result = data["results"][0]
    return {
        "name": result.get("name"),
        "country": result.get("country"),
        "latitude": result.get("latitude"),
        "longitude": result.get("longitude")
    }

#print(get_city("poznan"))

# Funkcja na podstawie współrzędnych geograficznych zwraca godzinową prognozę pogody na daną liczbę dni
def get_weather(latitude, longitude, forecast_days):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "forecast_days": forecast_days,
        "timezone": "auto"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Brak połączenia z internetem.")
    except requests.exceptions.Timeout:
        raise TimeoutError("Przekroczono czas oczekiwania na dane pogodowe.")
    except requests.exceptions.HTTPError:
        raise RuntimeError("API pogodowe zwróciło błąd HTTP.")
    except requests.exceptions.RequestException:
        raise RuntimeError("Wystąpił problem podczas pobierania danych pogodowych.")
    data = response.json()
    hourly = data["hourly"]
    df = pd.DataFrame({
        "czas": hourly["time"],
        "temperatura": hourly["temperature_2m"],
        "wilgotnosc": hourly["relative_humidity_2m"],
        "opady": hourly["precipitation"],
        "wiatr": hourly["wind_speed_10m"]
    }) #| Zmienne co godzinę:
    # temperatura powietrza na wysokości 2 metrów,
    # wilgotność względna powietrza na wysokości 2 metrów,
    # opady,
    # prędkość wiatru na wysokości 10 metrów.
    df["czas"] = pd.to_datetime(df["czas"])
    return df

def calculate_statistics(df):
    temperatura = df["temperatura"].to_numpy()
    opady = df["opady"].to_numpy()
    wilgotnosc = df["wilgotnosc"].to_numpy()
    wiatr = df["wiatr"].to_numpy()
    stats = {
        "Średnia temperatura [°C]": float(round(np.mean(temperatura), 2)),
        "Minimalna temperatura [°C]": float(round(np.min(temperatura), 2)),
        "Maksymalna temperatura [°C]": float(round(np.max(temperatura), 2)),
        "Rozstęp temperatury [°C]": float(round(np.max(temperatura) - np.min(temperatura), 2)),
        "Odchylenie standardowe temperatury [°C]": float(round(np.std(temperatura), 2)),
        "Suma opadów [mm]": float(round(np.sum(opady), 2)),
        "Liczba godzin z opadami": int(np.sum(opady > 0)),
        "Średnia wilgotność [%]": float(round(np.mean(wilgotnosc), 2)),
        "Maksymalna prędkość wiatru [km/h]": float(round(np.max(wiatr), 2))
    }
    return stats

def show_statistics(stats):
    for row in statystykiTabela.get_children():
        statystykiTabela.delete(row)
    for nazwa, wartosc in stats.items():
        statystykiTabela.insert("", END, values=(nazwa, wartosc))



wykres_canvas = None
def plot(df, variable):
    global wykres_canvas

    df["czas"] = pd.to_datetime(df["czas"])

    labels = {
        "temperatura": "Temperatura [°C]",
        "wilgotnosc": "Wilgotność [%]",
        "opady": "Opady [mm]",
        "wiatr": "Prędkość wiatru [km/h]"
    }

    # usunięcie poprzedniego wykresu, jeśli już był
    if wykres_canvas is not None:
        wykres_canvas.get_tk_widget().destroy()

    fig = Figure(figsize=(7.2, 3.5), dpi=100)
    ax = fig.add_subplot(111)

    if variable == "opady":
        ax.bar(
            df["czas"],
            df[variable],
            width=0.03,
            edgecolor="black"
        )
    else:
        ax.plot(
            df["czas"],
            df[variable],
            marker="o",
            markersize=3,
            linewidth=2
        )
    ax.set_title(f"Wykres: {labels[variable]}")
    ax.set_xlabel("Data i godzina")
    ax.set_ylabel(labels[variable])
    ax.grid(True, alpha=0.4)
    liczba_dni = (df["czas"].max() - df["czas"].min()).days + 1
    if liczba_dni <= 1:
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    elif liczba_dni <= 3:
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=12))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m\n%H:%M"))
    elif liczba_dni <= 7:
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
    else:
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
    ax.tick_params(axis="x", labelsize=8)
    fig.tight_layout()
    wykres_canvas = FigureCanvasTkAgg(fig, master=wykresFrame)
    wykres_canvas.draw()
    wykres_canvas.get_tk_widget().pack(fill=BOTH, expand=True)


#GUI
root = Tk()
root.title("Analiza pogody")
root.geometry("1200x750")
root.resizable(False, False)
canvas = Canvas(root, height=750, width=1200, highlightthickness=0)
canvas.pack()

#tło
background_image = PhotoImage(file="tlo.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, width=1200, height=750)

frame = Frame(root, bg="#ffffff")
frame.place(relx=0.5, rely=0.04, relwidth=0.55, relheight=0.30, anchor="n")
label_font = ("Arial", 12)
input_font = ("Arial", 12)
label_bg = "#ffffff"
label_width = 0.25
input_width = 0.50
row_height = 0.11
label_x = 0.12
input_x = 0.40

# tytuł
tytulLabel = Label(
    frame,
    text="Analiza pogody",
    font=("Arial", 18, "bold"),
    bg="#ffffff"
)
tytulLabel.place(relx=0.1, rely=0.06, relwidth=0.8, relheight=0.12)

# miasto
miastoLabel = Label(
    frame,
    text="Miasto:",
    font=label_font,
    bg=label_bg,
    anchor="e"
)
miastoLabel.place(relx=label_x, rely=0.25, relwidth=label_width, relheight=row_height)
miastoEntry = Entry(
    frame,
    font=input_font
)
miastoEntry.place(relx=input_x, rely=0.25, relwidth=input_width, relheight=row_height)
miastoEntry.insert(0, "Poznań")

# dni
dniLabel = Label(
    frame,
    text="Liczba dni:",
    font=label_font,
    bg=label_bg,
    anchor="e"
)
dniLabel.place(relx=label_x, rely=0.42, relwidth=label_width, relheight=row_height)
dniCombo = ttk.Combobox(
    frame,
    values=[1, 2, 3, 7, 14],
    state="readonly",
    font=input_font
)
dniCombo.place(relx=input_x, rely=0.42, relwidth=input_width, relheight=row_height)
dniCombo.set(1)

# zmienna
zmiennaLabel = Label(
    frame,
    text="Zmienna:",
    font=label_font,
    bg=label_bg,
    anchor="e"
)
zmiennaLabel.place(relx=label_x, rely=0.59, relwidth=label_width, relheight=row_height)
zmiennaCombo = ttk.Combobox(
    frame,
    values=["temperatura", "wilgotnosc", "opady", "wiatr"],
    state="readonly",
    font=input_font
)
zmiennaCombo.place(relx=input_x, rely=0.59, relwidth=input_width, relheight=row_height)
zmiennaCombo.set("temperatura")



#Funkcja przesyłająca dane i wywołująca odpowiednie funkcje z nimi
def zatwierdz_dane():
    miasto = miastoEntry.get()
    liczba_dni = dniCombo.get()
    zmienna = zmiennaCombo.get()
    if miasto == "":
        print("Nie wpisano miasta")
        return
    liczba_dni = int(liczba_dni)
    city = get_city(miasto)
    latitude = city["latitude"]
    longitude = city["longitude"]
    lokalizacja_text.set(
        f"Pogoda dla: {city['name']}, {city['country']} | "
        f"szerokość: {round(latitude, 4)} | długość: {round(longitude, 4)}"
    )
    df = get_weather(latitude, longitude, liczba_dni)
    stats = calculate_statistics(df)
    show_statistics(stats)
    plot(df, zmienna)


# Przycisk do zatwierdzania danych
zatwierdzButton = Button(
    frame,
    text="Analizuj",
    font=("Arial", 12, "bold"),
    bg="#4f8fba",
    fg="white",
    command=zatwierdz_dane
)
zatwierdzButton.place(
    relx=0.40,
    rely=0.78,
    relwidth=0.50,
    relheight=0.11
)

# informacja o lokalizacji
lokalizacja_text = StringVar()
lokalizacja_text.set("Brak pobranych danych pogodowych")

lokalizacjaLabel = Label(
    root,
    textvariable=lokalizacja_text,
    font=("Arial", 11, "bold"),
    bg="#ffffff",
    fg="#333333"
)

lokalizacjaLabel.place(
    relx=0.5,
    rely=0.35,
    relwidth=0.62,
    relheight=0.04,
    anchor="n"
)
frame.place(relx=0.5, rely=0.04, relwidth=0.55, relheight=0.30, anchor="n")

#ramka na wykres
wykresFrame = Frame(root, bg="#ffffff")
wykresFrame.place(relx=0.05, rely=0.40, relwidth=0.62, relheight=0.50)

#ramka na statystyki
statystykiFrame = Frame(root, bg="#ffffff")
statystykiFrame.place(relx=0.70, rely=0.40, relwidth=0.25, relheight=0.50)
statystykiLabel = Label(
    statystykiFrame,
    text="Statystyki",
    font=("Arial", 14, "bold"),
    bg="#ffffff"
)
statystykiLabel.pack(pady=8)
statystykiTabela = ttk.Treeview(
    statystykiFrame,
    columns=("miara", "wartosc"),
    show="headings",
    height=9
)
statystykiTabela.heading("miara", text="Miara")
statystykiTabela.heading("wartosc", text="Wartość")
statystykiTabela.column("miara", width=210, anchor="w")
statystykiTabela.column("wartosc", width=70, anchor="center")
statystykiTabela.pack(fill=BOTH, expand=True, padx=10, pady=10)

root.mainloop()