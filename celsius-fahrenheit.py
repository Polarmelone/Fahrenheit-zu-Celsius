from tkinter import *
from tkinter import ttk
import tkinter

#Fenster öffner (Brechstange)
def clicker():
    global Fenster
    Fenster = Tk()
    Fenster.title("Maßrechner")
    Fenster.geometry("250x200")
    Fenster.resizable(width=False, height=False)
    
    Fenster.config(bg="grey")
clicker()

Einheit = tkinter.StringVar()

#neuer_input als Fahrenheit 
def frage():
        neuer_input = eingabe.get()
        neuer_input = int(eingabe.get())
#Formel zur Berechnung von Fahrenheit zu Celsius
        berechnet = ((neuer_input - 32) * (5/9))
        Einheit.set(berechnet)

eingabe = Entry(Fenster)
ok_knopf = Button(text="Bestätigen", command=frage)

text = ttk.Label (Fenster, text="Fahrenheit eingeben:")
text.pack(side="top", fill="x")

eingabe.pack(side="top", fill="x")

celsius_ausgabe = ttk.Label (Fenster, textvariable=Einheit)
celsius_ausgabe.pack(side="top", fill="x")

ok_knopf.pack(side="bottom", fill="x")

Fenster.mainloop()