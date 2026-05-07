import requests
import json
import pandas as pd
import mplfinance as mpl
from tkinter import *

def draw_candle_chart():
    symbol = symbolEntry.get()
    interval = intervalEntry.get()
    limit = limitEntry.get()
    url = f'https://api.mexc.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}'
    response = requests.get(url)
    responseBody = response.text
    responseBodyJson = json.loads(responseBody)
    print(responseBodyJson)

    formattedCandlesData = []

    for candle in responseBodyJson:
        x = {
            'time': candle[0],
            'open': float(candle[1]),
            'close': float(candle[4]),
            'high': float(candle[2]),
            'low': float(candle[3])
        }
        formattedCandlesData.append(x)

    df = pd.json_normalize(formattedCandlesData)
    df.time = pd.to_datetime(df.time, unit='ms')
    df = df.set_index('time')

    print(df.columns)
    print(df.head())

    mpl.plot(
        df,
        type="candle",
        title=f"Candle chart: {symbol}",
        style="yahoo",
        mav=(3, 6, 9)
    )

# GUI
root = Tk()
root.title('GUI-ŚWIECZKI')

canvas = Canvas(root, height=500, width=700)
canvas.pack()

frame = Frame(root, bg='#ffffff')
frame.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.45, anchor='n')

symbolLabel = Label(frame, text="Symbol")
symbolLabel.place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.15)

symbolEntry = Entry(frame, font=40)
symbolEntry.place(relx=0.35, rely=0.1, relwidth=0.55, relheight=0.15)
symbolEntry.insert(0, "GEVONUSDT")

intervalLabel = Label(frame, text="Interval")
intervalLabel.place(relx=0.05, rely=0.35, relwidth=0.25, relheight=0.15)

intervalEntry = Entry(frame, font=40)
intervalEntry.place(relx=0.35, rely=0.35, relwidth=0.55, relheight=0.15)
intervalEntry.insert(0, "30m")

limitLabel = Label(frame, text="Limit")
limitLabel.place(relx=0.05, rely=0.6, relwidth=0.25, relheight=0.15)

limitEntry = Entry(frame, font=40)
limitEntry.place(relx=0.35, rely=0.6, relwidth=0.55, relheight=0.15)
limitEntry.insert(0, "10")

button = Button(frame, text="Pobierz dane i narysuj wykres", command=draw_candle_chart)
button.place(relx=0.2, rely=0.82, relwidth=0.6, relheight=0.13)

root.mainloop()
