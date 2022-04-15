from tkinter import *
window = Tk()
window.title("The Compact Calculator")
#window.geometry("200x150")

canvas = Canvas(width = 361, height = 100)

buffer_numbers = ""
buffer = []
index = 0
operation_plus_minus = False

def equal():
    buffer.append(buffer_numbers)
    text_box.delete('1.0', END)
    text_box.insert('end', buffer)
    return

def write(char):
    text_box.insert('end', char)
    return


def send(symbol ):
    global buffer_numbers
    global buffer
    global index
    global operation_plus_minus

    if type(symbol) in (int, float):
        #pridavam do stringoveho bufferu cisla, ktore sa retazia
        buffer_numbers += str(symbol)
    else:
        #akonahle dostaneme nieco ine ako cislo, predchadzajuce cisla
        #sa premenia na int a ulozia do bufferu
        buffer.append(int(buffer_numbers))

        buffer_numbers = "" #strinogvy buffer sa resetuje


        if symbol in ("+", "-") and not(operation_plus_minus):
            operation_plus_minus = True
            buffer.append(symbol)
        elif symbol in ("+", "-") and operation_plus_minus:
            buffer[-1] = symbol
    write(symbol)
    return




def clear():
    global buffer
    global buffer_numbers
    text_box.delete('1.0', END)
    buffer = []
    buffer_numbers=""
    return

text_box = Text(
    canvas,
    height=3,
    width=27
)

#row 1
button_f10 = Button(canvas, text = "f", height = 2, width= 3)
button_f10.grid(row = 1, column = 0)

button_f11 = Button(canvas, text = "f", height = 2, width = 3)
button_f11.grid(row = 1, column = 1)

button_f12 = Button(canvas, text = "f", height = 2, width = 3)
button_f12.grid(row = 1, column = 2)

button_clear = Button(canvas, text = "C", height = 2, width = 3, command = lambda: clear())
button_clear.grid(row = 1, column = 3)

#row 2
button_f20 = Button(canvas, text = "f", height = 2, width= 3)
button_f20.grid(row = 2, column = 0)

button_f21 = Button(canvas, text = "f", height = 2, width = 3)
button_f21.grid(row = 2, column = 1)

button_f22 = Button(canvas, text = "f", height = 2, width = 3)
button_f22.grid(row = 2, column = 2)

button_division = Button(canvas, text = "/", height = 2, width = 3)
button_division.grid(row = 2, column = 3)

#row 3

button_7 = Button(canvas, text = "7", height = 2, width= 3)
button_7.grid(row = 3, column = 0)

button_8 = Button(canvas, text = "8", height = 2, width = 3)
button_8.grid(row = 3, column = 1)

button_9 = Button(canvas, text = "9", height = 2, width = 3)
button_9.grid(row = 3, column = 2)

button_mul = Button(canvas, text = "*", height = 2, width = 3, command = lambda: send(str("*")))
button_mul.grid(row = 3, column = 3)

#row 4
button_4 = Button(canvas, text = "4f", height = 2, width= 3 ,command = lambda: send(int(4)))
button_4.grid(row = 4, column = 0)
#button_1f.pack()

button_5 = Button(canvas, text = "5", height = 2, width = 3 , command = lambda: print("hello"))
button_5.grid(row = 4, column = 1)
#button_2f.pack()

button_6 = Button(canvas, text = "6", height = 2, width = 3)
button_6.grid(row = 4, column = 2)

button_minus = Button(canvas, text = "-", height = 2, width = 3, command= lambda: send(str("-")))
button_minus.grid(row = 4, column = 3)

#row 5
button_1 = Button(canvas, text = "1", height = 2, width= 3)
button_1.grid(row = 5, column = 0)

button_2 = Button(canvas, text = "2", height = 2, width = 3)
button_2.grid(row = 5, column = 1)

button_3 = Button(canvas, text = "3", height = 2, width = 3)
button_3.grid(row = 5, column = 2)

button_plus = Button(canvas, text = "+", height = 2, width = 3, command= lambda: send(str("+")))
button_plus.grid(row = 5, column = 3)

#row 6
button_comma = Button(canvas, text = ",", height = 2, width= 3)
button_comma.grid(row = 6, column = 0)

button_0 = Button(canvas, text = "0", height = 2, width = 3)
button_0.grid(row = 6, column = 1)

button_equal = Button(canvas, text = "=", height = 2, width = 3, command = lambda: equal())
button_equal.grid(row = 6, column = 2)
#button_equal.pack()

button_f63 = Button(canvas, text = "f", height = 2, width = 3)
button_f63.grid(row = 6, column = 3)


text_box.grid(row = 0, column = 0, columnspan = 4)








canvas.pack()


canvas.mainloop()

