from tkinter import * # biblioteka GUI
root = Tk() # Utworzenie obiektu okna
root.title('MyGUIApp') # tytuł okna
canvas = Canvas(root, height=800, width=600) # Obiektu canvas zawiera wszystkie elementy GUI
canvas.pack() # Umieszczenie canvas w oknie

background_image = PhotoImage(file='altum.png')
background_label = Label(root, image=background_image) #
background_label.place(relwidth=1, relheight=1) # Umieszczenie Label z obrazkiem w canvas (okno programu)
# relwidth szerokość Label równa szerokości okna
# relheight wysokość Label równa wysokości okna

# tworzenie ramki by pozycjonować w niej elementy
frame = Frame(root, bg='#ffffff')
frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n') # Wsadzenie Frame w canvas
# anchor - punkt odniesienia, 'n' to górny punkt

labelOne = Label(frame) # obiekt Label dla tekstu
labelOne.place(relx=0.05, rely=0.15, relwidth=0.18, relheight=0.3)
labelOne.configure(text="Label One") # Nadanie obiektowi Label tekst
entryOne = Entry(frame, font=40)
entryOne.place(relx=0.25, rely=0.15, relwidth=0.3, relheight=0.3)

labelTwo = Label(frame)
labelTwo.place(relx=0.05, rely=0.55, relwidth=0.18, relheight=0.3) # Umieszczenie obiektu Label w obiekcie Frame
labelTwo.configure(text="Label One")
entryTwo = Entry(frame, font=40)
entryTwo.place(relx=0.25, rely=0.55, relwidth=0.3, relheight=0.3)

entryOne.insert(0, "Hello") # Wstawienie tekstu do obiektu Entry o nazwie entryOne
entryTwo.insert(0, "Hi") # Wstawienie tekstu do obiektu Entry o nazwie entryTwo

def printTextEnteredInEntryOne():
    print(entryOne.get()) # Wyświetlenie tekstu wpisanego w Entry


printInputButton = Button(frame, text="Print Text", command=printTextEnteredInEntryOne) # Utworzenie Button i przypisanie do niego funkcji o nazwie printTextEnteredInEntryOne
printInputButton.place(relx=0.6, rely=0.16, relwidth=0.35, relheight=0.7) # Umieszczenie Button w Frame

secondFrame = Frame(root, bg='#ffffff')
secondFrame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')

selectedOption = StringVar(root, 'FIRST_OPTION') # StringVar zawiera wybraną opcję z listy

def printSelectedOption(): # Funkcja wyświetlq wybraną opcję z listy
    print(selectedOption.get()) #


optionOne = Radiobutton(secondFrame, text="GEVON USDT", variable=selectedOption, value='GEVONUSDT') # Radiobutton zawiera opcję z listy i podpina ją do obiektu StringVar o nazwie selectedOption
optionOne.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.3)
optionTwo = Radiobutton(secondFrame, text="ETH USDT", variable=selectedOption, value='ETHUSDT')
optionTwo.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.3)
printSelectButton = Button(secondFrame, text="Button One", command=printSelectedOption) # przypisanie do Button funkcji printSelectedOption
printSelectButton.place(relx=0.6, rely=0.16, relwidth=0.35, relheight=0.7)
root.mainloop()