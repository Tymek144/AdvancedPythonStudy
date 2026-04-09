import matplotlib as mpl
import numpy as np
import pylab

title = input("Podaj tytuł wykresu")
a = float(input("Podaj a"))
b = float(input("Podaj b"))
first_x = float(input("Podaj początek zakresu"))
last_x = float(input("Podaj koniec zakresu"))
if_grid = input("Czy ma być wyświetlona siatka? True or False").lower() == "true"

x = np.arange(first_x, last_x + 1)
y = a*x+b
pylab.plot(x, y)
pylab.title(title)
pylab.grid(if_grid)
pylab.show()