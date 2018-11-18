import tkinter

def licz():
    a = float(dystans_entry.get())
    b = float(spalanie_entry.get())
    c = float(cena_entry.get())
    wynik.configure(text=a * b * c)


root = tkinter.Tk()

dystans_label = tkinter.Label(master=root, text="Dystans")
dystans_label.pack()
dystans_entry = tkinter.Entry(master=root)
dystans_entry.pack()

spalanie_label = tkinter.Label(master=root, text="Spalanie na km")
spalanie_label.pack()
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.pack()

cena_label = tkinter.Label(master=root, text="Cena")
cena_label.pack()
cena_entry = tkinter.Entry(master=root)
cena_entry.pack()

wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()

wynik = tkinter.Label(master=root, text="-")
wynik.pack()

policz_button = tkinter.Button(master=root, text="Policz", command=licz)
policz_button.pack()

root.title("Kalkulator")
root.mainloop()