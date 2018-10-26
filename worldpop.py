import matplotlib.pyplot as plt
import tkinter

hfont = {'fontname':'Lato'}

years = [1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

plt.plot(years, pops, color=(255/255, 100/255, 100/255), linewidth=6.0)
plt.ylabel("Population by Billions")
plt.xlabel("Growth by Year")
plt.title("Population Growth", pad=20, **hfont)
plt.show()