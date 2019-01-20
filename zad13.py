import pandas as pd
import scipy.stats as st
import statistics
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
dane = pd.read_csv("C:\\Users\\Orlic\\Desktop\\kognitywistyka\\SemestrIII\\KCK\\zadanie13\\sub01trial09.csv")

kolumna1=dane["-0.066377610284342775"]
syg1=ag.pasmowozaporowy(kolumna1, 200, 49, 51)
syg12=ag.pasmowoprzepustowy(syg1, 200, 1, 50)

kolumna5=dane["0.1"]

#kod=[]
#listax=[]
#y=syg12.get_ylim()

#if y in syg12>0.1:
#    listax.append(syg12[plt.xlim])

    #kod.append(kolumna5(y))
plt.subplot(2,1,1)
plt.plot(kolumna1)
plt.xlabel('Czas [ms]')
plt.ylabel('Amplituda [mV]')
plt.subplot(2,1,2)
plt.plot(kolumna5)
plt.xlabel('Czas [ms]')
plt.ylabel('Wyświetlana cyfra [-]')
plt.show()

plt.subplot(2, 1, 1)
plt.plot(syg12)
plt.xlabel('Czas [ms]')
plt.ylabel('Amplituda [mV]')
plt.subplot(2,1,2)
plt.plot(kolumna5)
plt.xlabel('Czas [ms]')
plt.ylabel('Wyświetlana cyfra [-]')

plt.show()

print('Kod, który osoba "wymrugała": 2 5 3 5 3 1 4 3')
