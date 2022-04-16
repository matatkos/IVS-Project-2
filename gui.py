from tkinter import *
from tkinter import messagebox
import math

window = Tk()
window.title("The Compact Calculator")
#window.geometry("200x150")

canvas = Canvas(width = 361, height = 100)

buffer_numbers = ""
buffer = []
index = 0
operations_set = False
is_root = False
is_sinus = False
is_cosinus = False
expect_operand = True

#function calculates the result of an expression stored in buffer
def calculate():
    global buffer
    global buffer_numbers
    expression = ""
    for i in range(len(buffer)):
        expression += str(buffer[i])
    result = round(eval(expression) , 6) #rounding to 6 decimal digits
    buffer_numbers = ""
    buffer.clear()

    #if result has only zeros after comma, function returns integer
    if ((result*10)%10) == 0:
        buffer.append(int(result))
        return int(result)
    #if it contains decimals we return it as it is
    buffer.append(result)
    return result

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
    return fact

def equal():
    global buffer
    buffer.append(buffer_numbers)
    text_box.delete('1.0', END)
    text_box.config(state="normal")
    #if buffer empty, printing out 0
    if buffer[0] == "":
        text_box.delete('1.0', END) #deletes previous zero
        write(0)
        return
    #deletes content of text box
    text_box.delete('1.0', END)
    text_box.config(state='disabled')
    #pritns out result
    print(buffer)
    write(calculate())
    return

def write(char):
    text_box.config(state="normal")
    text_box.insert('end', char, "default")
    text_box.config(state="disabled")
    return


def send(symbol):
    #setting variables to global
    #so function can overwrite them
    global buffer_numbers
    global buffer
    global index
    global operations_set
    global is_root
    global is_sinus
    global is_cosinus
    global expect_operand

    if type(symbol) in (int, float):
        expect_operand = False
        is_sinus = False
        is_cosinus = False
        #if operation is nth root inverse current symbol
        if is_root:
            buffer.append(float(1/symbol)) #index of root
            is_root = False                #we set the is_root bool back to false

        #pridavam do stringoveho bufferu cisla, ktore sa retazia
        else:
            buffer_numbers += str(symbol)
        # ked pride cislo po operacii, bool sa bastavi na False
        operations_set = False
    else:
        if expect_operand:
            return
        #akonahle dostaneme nieco ine ako cislo, predchadzajuce cisla
        #sa premenia na int a ulozia do bufferu
        if buffer_numbers != "":
            is_sinus = False
            is_cosinus = False
            buffer.append(int(buffer_numbers))

        buffer_numbers = "" #strinogvy buffer sa resetuje

        if symbol in ("+", "-", "/", "*", "^", "s") and not(operations_set):
            is_sinus = False
            is_cosinus = False
            #if given symbol is ^ (pow), functions prints out "^" but buffer gets "**"
            if symbol == "^":
                buffer.append("**")
            #if given symbol is nth root, buffer gets "**" symbol and is root is set to True so the next operand is index of root
            elif symbol == "s":
                buffer.append("**")
                is_root = True
            else:
                buffer.append(symbol)
            operations_set = True
        #if operation is already set, and another operation is given, the new
        #one overwrites previous one
        elif symbol in ("+", "-", "/", "*", "^", "s") and operations_set:
            is_sinus = False
            is_cosinus = False
            buffer[-1] = symbol
        #operations that dont cancel eachother out:
        elif symbol == "!":
            is_sinus = False
            is_cosinus = False
            buffer[-1] = factorial(buffer[-1])
        elif symbol == "sin":
            if is_sinus or is_cosinus:
                return
            is_sinus = True
            buffer[-1] = math.sin(math.radians(buffer[-1]))
        elif symbol == "cos":
            if is_sinus or is_cosinus:
                return
            is_cosinus = True
            buffer[-1] = math.cos(math.radians(buffer[-1]))


    #at the end we write out the symbol so it displays on the screen
    write(symbol)
    return

#function clears text box only
def clear_tb():
    text_box.config(state="normal")
    text_box.delete('1.0', END)
    text_box.config(state='disabled')
    return

#function clears the text box and buffer
def clear():
    global buffer
    global buffer_numbers
    #clearing the text box
    clear_tb()

    #clearing the buffer
    buffer = []
    buffer_numbers=""
    return


def show_help():
    top = Toplevel(canvas)
    top.geometry("750x250")
    top.title("HELP")
    message='''
    SYNTAX:
        ROOT: x root n -> nth root of a number x i.e. 4 root 2 = 2'''
    text = Text(top, height=50, width=250)
    text.grid(row=0, column=0)
    text.insert('1.0', message)
    return


text_box = Text(
    canvas,
    height=3,
    width=27,
    background='#DDDBDB'
)
text_box.tag_config('default',background='#DDDBDB', foreground="#000000")
text_box.config(state='disabled')

#row 1
button_sin = Button(canvas, text = "sin", height = 2, width= 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command = lambda: send(str("sin")))
button_sin.grid(row = 1, column = 0)

button_cos = Button(canvas, text = "cos", height = 2, width = 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command = lambda: send(str("cos")))
button_cos.grid(row = 1, column = 1)

button_f12 = Button(canvas, text = "f2", height = 2, width = 3, relief=FLAT,bd=2, activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1)
button_f12.grid(row = 1, column = 2)

button_clear = Button(canvas, text = "C", height = 2, width = 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command = lambda: clear())
button_clear.grid(row = 1, column = 3)

#row 2
#todo change
button_root = Button(canvas, text = "root", height = 2, width= 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command=lambda: send(str("s")))
button_root.grid(row = 2, column = 0)
#todo decide what should be displayed
button_power = Button(canvas, text = "^", height = 2, width = 3, relief=FLAT,bd=2, activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command=lambda: send(str("^")))
button_power.grid(row = 2, column = 1)

button_factorial = Button(canvas, text = "x!", height = 2, width = 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command= lambda: send(str("!")))
button_factorial.grid(row = 2, column = 2)

button_division = Button(canvas, text = "/", height = 2, width = 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1,  command= lambda: send(str("/")))
button_division.grid(row = 2, column = 3)

#row 3

button_7 = Button(canvas, text = "7", height = 2, width= 3, relief=FLAT,bd=2,activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(7)))
button_7.grid(row = 3, column = 0)

button_8 = Button(canvas, text = "8", height = 2, width = 3, relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(8)))
button_8.grid(row = 3, column = 1)

button_9 = Button(canvas, text = "9", height = 2, width = 3, relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(9)))
button_9.grid(row = 3, column = 2)

button_mul = Button(canvas, text = "*", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1,command = lambda: send(str("*")))
button_mul.grid(row = 3, column = 3)

#row 4
button_4 = Button(canvas, text = "4", height = 2, width= 3 ,relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1,command = lambda: send(int(4)))
button_4.grid(row = 4, column = 0)
#button_1f.pack()

button_5 = Button(canvas, text = "5", height = 2, width = 3 ,relief=FLAT,bd=2,activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(5)))
button_5.grid(row = 4, column = 1)
#button_2f.pack()

button_6 = Button(canvas, text = "6", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(6)))
button_6.grid(row = 4, column = 2)

button_minus = Button(canvas, text = "-", height = 2, width = 3, relief=FLAT,bd=2,activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command= lambda: send(str("-")))
button_minus.grid(row = 4, column = 3)

#row 5
button_1 = Button(canvas, text = "1", height = 2, width= 3,relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(1)))
button_1.grid(row = 5, column = 0)

button_2 = Button(canvas, text = "2", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(2)))
button_2.grid(row = 5, column = 1)

button_3 = Button(canvas, text = "3", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(3)))
button_3.grid(row = 5, column = 2)

button_plus = Button(canvas, text = "+", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command= lambda: send(str("+")))
button_plus.grid(row = 5, column = 3)

#row 6
button_comma = Button(canvas, text = ",", height = 2, width= 3,relief=FLAT, bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command= lambda: send(str(".")))
button_comma.grid(row = 6, column = 0)

button_0 = Button(canvas, text = "0", height = 2, width = 3,relief=FLAT,bd=2,activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1, command=lambda: send(int(0)))
button_0.grid(row = 6, column = 1)

button_equal = Button(canvas, text = "=", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#ffa31a',activeforeground="#292929", fg='#ffa31a', bg='#292929',highlightbackground="#292929", highlightthickness=1,command = lambda: equal())
button_equal.grid(row = 6, column = 2)
#button_equal.pack()

button_help = Button(canvas, text = "help", height = 2, width = 3,relief=FLAT,bd=2, activebackground='#292929',activeforeground="#ffa31a", fg='#292929', bg='#ffa31a',highlightbackground="#ffa31a", highlightthickness=1, command= lambda: show_help())
button_help.grid(row = 6, column = 3)


text_box.grid(row = 0, column = 0, columnspan = 4)








canvas.pack()


canvas.mainloop()
