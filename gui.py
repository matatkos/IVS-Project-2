import tkinter
window = tkinter.Tk()
window.title("The Calculator")

canvas = tkinter.Canvas(width = 361, height = 500)
canvas.pack()


#CONSTANTS
go_right = 90
go_left = -90
go_up = -55
go_down = 55

#creating grid
canvas.create_rectangle(2,498,359,225, width=2)
for i in range(5):
    for j in range(4):
        go_up_vector = i*go_up
        go_right_vector = j*go_right
        canvas.create_line(2 + go_right_vector, 225, 2 + go_right_vector, 498, width=2 )
        canvas.create_line(2, 445 + go_up_vector, 359, 445 + go_up_vector, width=2)

#adding numbers into grid
def write_number_grid(text, x, y):
    canvas.create_text(x, y, text = text, font = ('Arial',30))

number = 1
for i in range(3):
    for j in range(3):
        go_right_vector = j * go_right
        go_up_vector = (i+1) * go_up
        write_number_grid(number, 47 + go_right_vector, 472 + go_up_vector)
        number += 1

#adding "0"
write_number_grid(0, 47,472)
#adding "="
write_number_grid("=",47+(3*go_right), 472)
#adding "+"
write_number_grid("+",47+(3*go_right),472 + go_up)
#adding "-"
write_number_grid("-",47+(3*go_right),472 +2* go_up)
#adding "*"
write_number_grid("*",47+(3*go_right),472 +3* go_up)


canvas.mainloop()


