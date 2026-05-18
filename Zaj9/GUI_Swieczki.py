from tkinter import *  # biblioteka pozwalająca utworzyć GUI
import requests
import json
import pandas as pd
import mplfinance as mpl


def standardize(fragment):
    values = fragment[['open', 'close']].values.flatten()
    min_val = values.min()
    max_val = values.max()

    if max_val - min_val == 0:
        return values * 0

    standardized = (values - min_val) / (max_val - min_val)
    return standardized


def run_program():
    symbol = symbolEntry.get()
    interval = selectedOption.get()
    limit = limitEntry.get()

    url = f'https://api.mexc.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'

    response = requests.get(url)
    responseBodyJson = json.loads(response.text)

    formattedCandlesData = []

    for candle in responseBodyJson:
        x = {
            'time': candle[0],
            'open': float(candle[1]),
            'high': float(candle[2]),
            'low': float(candle[3]),
            'close': float(candle[4])
        }

        formattedCandlesData.append(x)

    df = pd.json_normalize(formattedCandlesData)
    df.time = pd.to_datetime(df.time, unit='ms')
    df = df.set_index('time')
    df = df[['open', 'high', 'low', 'close']]

    print(df.head())
    print(df.tail())

    pattern = df.tail(10)
    pattern_standardized = standardize(pattern)

    window_size = 10
    tolerance = 0.15

    matched_fragment = None
    matched_index = None

    for i in range(0, len(df) - 2 * window_size):
        tested_fragment = df.iloc[i:i + window_size]
        tested_standardized = standardize(tested_fragment)

        differences = abs(pattern_standardized - tested_standardized)

        if all(differences <= tolerance):
            matched_fragment = tested_fragment
            matched_index = i
            break

    if matched_fragment is not None:
        print("Znaleziono podobny fragment!")
        print("Indeks początku fragmentu:", matched_index)
        print("Czas początku fragmentu:", matched_fragment.index[0])
        print("Czas końca fragmentu:", matched_fragment.index[-1])

        mpl.plot(
            pattern,
            type="candle",
            title="Wzorzec - ostatnie 10 świec",
            style="yahoo",
            mav=(3)
        )

        mpl.plot(
            matched_fragment,
            type="candle",
            title="Znalezione podobne 10 świec",
            style="yahoo",
            mav=(3)
        )

    else:
        print("Nie znaleziono dopasowania.")


root = Tk()  # Utworzenie podstawowego obiektu okna
root.title('GUI - świeczki')  # Nadanie tytułu okna

canvas = Canvas(root, height=800, width=600)
canvas.pack()

background_image = PhotoImage(file='altum.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#ffffff')
frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.25, anchor='n')

symbolLabel = Label(frame)
symbolLabel.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.2)
symbolLabel.configure(text="Symbol")

symbolEntry = Entry(frame, font=40)
symbolEntry.place(relx=0.35, rely=0.1, relwidth=0.55, relheight=0.2)
symbolEntry.insert(0, "GEVONUSDT")


limitLabel = Label(frame)
limitLabel.place(relx=0.05, rely=0.4, relwidth=0.25, relheight=0.2)
limitLabel.configure(text="Limit")

limitEntry = Entry(frame, font=40)
limitEntry.place(relx=0.35, rely=0.4, relwidth=0.55, relheight=0.2)
limitEntry.insert(0, "500")

printInputButton = Button(frame, text="Uruchom program", command=run_program)
printInputButton.place(relx=0.25, rely=0.72, relwidth=0.5, relheight=0.2)

secondFrame = Frame(root, bg='#ffffff')
secondFrame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor='n')

selectedOption = StringVar(root, '1m')

optionOne = Radiobutton(
    secondFrame,
    text="Interval 1m",
    variable=selectedOption,
    value='1m'
)

optionOne.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.5)

optionTwo = Radiobutton(
    secondFrame,
    text="Interval 5m",
    variable=selectedOption,
    value='5m'
)

optionTwo.place(relx=0.55, rely=0.25, relwidth=0.35, relheight=0.5)


root.mainloop()