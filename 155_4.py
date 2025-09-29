import tkinter
from random import randrange
canvas = tkinter.Canvas(height=300, width=500, bg="black")
canvas.pack()

canvas.create_text(260, 280, text="31           62           125          250         500          1K          2K          4K          8K         16K      [Hz]",
                   fill="light green")

frekvencie = (31, 62, 125, 250, 500, 1000, 2000, 4000, 8000, 16000)

def vykresli_stlpce():
    canvas.delete("stlpce")
    x = 20
    for i in range(10):
        vyska = randrange(50, 240)
        canvas.create_rectangle(x, vyska, x + 30, 265, fill="light green", tags="stlpce")
        x += 45
    canvas.after(200, vykresli_stlpce)

vykresli_stlpce()
canvas.mainloop()