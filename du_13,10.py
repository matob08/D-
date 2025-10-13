import tkinter
from tkinter import ttk

#Radiobutton
okno1 = tkinter.Toplevel()
okno1.title('Radiobutton - ukážka')
okno1.geometry('500x350')  # väčšie okno

v = tkinter.StringVar()
v.set('BB')

mesta = [('Banská Bystrica', 'BB'), ('Bratislava', 'BA'),
         ('Košice', 'KE'), ('Nitra', 'NR')]

def vypis():
    label_vysledok.config(text='Vybral si: ' + v.get())

tkinter.Label(okno1, text='Vyber svoje mesto:', font=('Arial', 12, 'bold')).pack(pady=10)

for mesto, skratka in mesta:
    rb = tkinter.Radiobutton(okno1, text=mesto, value=skratka,
                             variable=v, command=vypis, font=('Arial', 11))
    rb.pack(anchor='w', padx=30)

label_vysledok = tkinter.Label(okno1, text='Vybral si: BB', font=('Arial', 11))
label_vysledok.pack(pady=15)

#Checkbutton
okno2 = tkinter.Toplevel()
okno2.title('Checkbutton - ukážka')
okno2.geometry('500x350')

def vypis_predmety():
    text = (predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()).strip()
    label_predmety.config(text='Máte vybraté: ' + (text if text else 'nič'))

tkinter.Label(okno2, text='Z ktorého predmetu idete maturovať?', font=('Arial', 12, 'bold')).pack(pady=10)

predmet1 = tkinter.StringVar()
predmet2 = tkinter.StringVar()
predmet3 = tkinter.StringVar()

check1 = tkinter.Checkbutton(okno2, text='slovenský jazyk a literatúra',
                             onvalue='SJL', offvalue='', variable=predmet1,
                             command=vypis_predmety, font=('Arial', 11))
check2 = tkinter.Checkbutton(okno2, text='anglický jazyk',
                             onvalue='AJ', offvalue='', variable=predmet2,
                             command=vypis_predmety, font=('Arial', 11))
check3 = tkinter.Checkbutton(okno2, text='matematika',
                             onvalue='MAT', offvalue='', variable=predmet3,
                             command=vypis_predmety, font=('Arial', 11))

check1.pack(anchor='w', padx=30)
check2.pack(anchor='w', padx=30)
check3.pack(anchor='w', padx=30)

label_predmety = tkinter.Label(okno2, text='Máte vybraté: nič', font=('Arial', 11))
label_predmety.pack(pady=15)

#Scale
okno3 = tkinter.Toplevel()
okno3.title('Scale - ukážka')
okno3.geometry('600x400')

canvas = tkinter.Canvas(okno3, width=550, height=250, bg='white')
canvas.pack(pady=10)

rx, ry = 100, 50
x, y = 275, 125
canvas.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green', tags='oval')

def zmena1(event):
    global rx
    rx = scale1.get()
    prekresli()

def zmena2(event):
    global ry
    ry = scale2.get()
    prekresli()

def prekresli():
    canvas.coords('oval', [x-rx, y-ry, x+rx, y+ry])

tkinter.Label(okno3, text='Meníš veľkosť elipsy posuvníkmi', font=('Arial', 12, 'bold')).pack()

scale1 = tkinter.Scale(okno3, from_=10, to=250, orient='horizontal', length=450,
                       command=zmena1, label='Polomer X')
scale1.pack(pady=5)
scale1.set(rx)

scale2 = tkinter.Scale(okno3, from_=10, to=200, orient='vertical',
                       length=200, command=zmena2, label='Polomer Y')
scale2.place(x=530, y=100)
scale2.set(ry)

#Spinbox
okno4 = tkinter.Toplevel()
okno4.title('Spinbox - ukážka')
okno4.geometry('400x250')

tkinter.Label(okno4, text='Vyber deň v týždni:', font=('Arial', 12, 'bold')).pack(pady=10)

dni = ['Pondelok', 'Utorok', 'Streda', 'Štvrtok', 'Piatok', 'Sobota', 'Nedeľa']
den = tkinter.StringVar(value=dni[0])

spin = tkinter.Spinbox(okno4, values=dni, textvariable=den, font=('Arial', 12), width=15)
spin.pack(pady=15)

#Listbox
okno5 = tkinter.Toplevel()
okno5.title('Listbox - ukážka')
okno5.geometry('500x400')

canvas2 = tkinter.Canvas(okno5, width=300, height=150, bg='white')
canvas2.pack(pady=10)

def prefarbi(event):
    oznacene = listbox1.curselection()
    if oznacene:
        farba = listbox1.get(oznacene)
        canvas2.config(bg=farba)

def pridaj():
    listbox1.insert('end', entry1.get())

def vymaz():
    oznacene = listbox1.curselection()
    if oznacene:
        listbox1.delete(oznacene)

tkinter.Label(okno5, text='Vyber farbu zo zoznamu:', font=('Arial', 12, 'bold')).pack(pady=10)

listbox1 = tkinter.Listbox(okno5, font=('Arial', 11), height=6, width=20)
listbox1.pack()

for f in ['red', 'green', 'blue', 'yellow', 'white', 'orange', 'purple']:
    listbox1.insert('end', f)

listbox1.bind('<Double-Button-1>', prefarbi)

tkinter.Label(okno5, text='Pridaj vlastnú farbu:', font=('Arial', 11)).pack(pady=5)
entry1 = tkinter.Entry(okno5, font=('Arial', 11))
entry1.pack()
tkinter.Button(okno5, text='Pridaj', command=pridaj, width=10).pack(pady=2)
tkinter.Button(okno5, text='Vymaž', command=vymaz, width=10).pack(pady=2)

#Combobox
okno6 = tkinter.Toplevel()
okno6.title('Combobox - ukážka')
okno6.geometry('400x250')

tkinter.Label(okno6, text='Vyber krajinu:', font=('Arial', 12, 'bold')).pack(pady=10)

krajiny = ['Slovensko', 'Česko', 'Poľsko', 'Maďarsko', 'Rakúsko']
combo = ttk.Combobox(okno6, values=krajiny, font=('Arial', 12), width=20)
combo.pack(pady=15)

def zobraz(event):
    label_vysl.config(text='Vybral si: ' + combo.get())

combo.bind('<<ComboboxSelected>>', zobraz)

label_vysl = tkinter.Label(okno6, text='Vybral si: nič', font=('Arial', 11))
label_vysl.pack(pady=10)

#Hlavné okno
okno = tkinter.Tk()
okno.title('Ukážky widgetov - väčšie okná')
okno.geometry('400x150')

tkinter.Label(okno, text='Toto je hlavné okno programu.', font=('Arial', 12, 'bold')).pack(pady=40)

okno.mainloop()