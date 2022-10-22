from tkinter import *


def press_number_button(number):
    global equation_text
    global equal_pressed
    if equal_pressed is True:
        reset()
    if equation_text == "0":
        equation_text = str(number)
    else:
        equation_text = equation_text + str(number)
    equation_label.set(equation_text)
    total_equation_label.set(total_equation_text)


def press_function_button(expression):
    global type_chose
    global history_text
    global equation_text
    if type_chose == 1:
        global expression_operator
        global total_equation_text
        global number_1
        global number_2
        if not expression_operator:
            if '.' in equation_text:
                number_1 = float(equation_text)
            else:
                number_1 = int(equation_text)

            equation_text = ""
            expression_operator = expression
            total_equation_text = str(number_1) + " " + expression
            total_equation_label.set(total_equation_text)

        else:
            if '.' in equation_text:
                number_2 = float(equation_text)
            else:
                number_2 = int(equation_text)

            temp_number_1 = number_1

            if expression_operator == "+":
                number_1 = number_1 + number_2
            elif expression_operator == "-":
                number_1 = number_1 - number_2
            elif expression_operator == "*":
                number_1 = number_1 * number_2
            elif expression_operator == "/":
                number_1 = number_1 / number_2

            history_text = str(temp_number_1) + " " + str(expression_operator) + " " + str(number_2) + " = " + str(number_1) + "\n" + history_text
            history_label.set(history_text)

            equation_text = ""
            expression_operator = expression
            total_equation_text = str(number_1) + " " + expression
            total_equation_label.set(total_equation_text)
            equation_label.set(str(number_1))
    else:
        if equation_text == "0":
            equation_text = str(expression)
        else:
            equation_text = equation_text + str(expression)
        equation_label.set(equation_text)


def press_equal_button():
    global type_chose
    global equation_text
    global history_text
    global result
    global number_1
    global equal_pressed
    if type_chose == 1:
        global expression_operator
        global total_equation_text
        global number_2
        equal_pressed = True
        if expression_operator:
            if equation_text == "":
                number_2 = number_1
            else:
                if '.' in equation_text:
                    number_2 = float(equation_text)
                else:
                    number_2 = int(equation_text)
            equation_text = ""
            total_equation_text = total_equation_text + " " + str(number_2) + " ="
            total_equation_label.set(total_equation_text)

            if expression_operator == "+":
                result = number_1 + number_2
            elif expression_operator == "-":
                result = number_1 - number_2
            elif expression_operator == "*":
                result = number_1 * number_2
            elif expression_operator == "/":
                result = number_1 / number_2
        else:
            if '.' in equation_text:
                number_1 = float(equation_text)
            else:
                number_1 = int(equation_text)
            result = number_1
            total_equation_text = str(number_1) + " ="

        equation_label.set(str(result))
        history_text = total_equation_text + " " + str(result) + "\n" + history_text
        history_label.set(history_text)

        total_equation_text = ""
        expression_operator = ""
    else:
        equal_pressed = True
        result = eval(equation_text)
        equation_label.set(str(result))
        total_equation_text = " ".join(equation_text) + " ="
        total_equation_label.set(" ".join(equation_text) + " =")
        history_text = total_equation_text + " " + str(result) + "\n" + history_text
        history_label.set(history_text)


def reset():
    global expression_operator
    global total_equation_text
    global equation_text
    global number_1
    global number_2
    global equal_pressed
    equal_pressed = False
    expression_operator = ""
    total_equation_text = ""
    equation_text = ""
    number_1 = 0
    number_2 = 0
    equation_label.set(equation_text)
    total_equation_label.set(total_equation_text)


def press_negative_button():
    global equation_text
    if '.' in equation_text:
        equation_text = str(-float(equation_text))
    else:
        equation_text = str(-int(equation_text))
    equation_label.set(equation_text)


def press_delete_button():
    global equation_text
    length = len(equation_text)
    if length == 1:
        equation_text = "0"
    else:
        equation_text = equation_text[:length - 1]
    equation_label.set(equation_text)


def press_type_button():
    global type_chose
    if type_chose == 1:
        type_chose = 2
        type_label.set("Type: Multiple")
        type_Single["state"] = "normal"
        type_Multiple["state"] = "disabled"
        reset()
    else:
        type_chose = 1
        type_label.set("Type: Single")
        type_Single["state"] = "disabled"
        type_Multiple["state"] = "normal"
        reset()


screen = Tk()
screen.title("Simple Calculator")
screen.configure(background='gray')
screen.geometry("500x650")

equation_text = ""
history_text = ""
total_equation_text = ""
expression_operator = ""
type_label_text = "Type: Single"
number_1 = 0
number_2 = 0
result = 0
equal_pressed = False
total_equation_label = StringVar()
equation_label = StringVar()
type_label = StringVar()
type_label.set(type_label_text)
type_chose = 1
history_label = StringVar()

history_name = Label(screen, text="HISTORY", bg="darkgray", fg="red", height=2, width=23)
history_name.grid(column=4, row=0, padx=3, pady=3)

history_field = Label(screen, textvariable=history_label, bg="white", fg="black", height=39, width=23, anchor="n")
history_field.grid(column=4, row=1, rowspan=9)

type_text_field = Label(screen, textvariable=type_label, bg="white", fg="red", height=3, width=12)
type_text_field.grid(column=2, row=0, rowspan=2)

type_Single = Button(screen, text="Single Expression", fg="black", height=2, width=14, bg="white",
                     command=lambda: press_type_button())
type_Single.grid(column=0, row=0, columnspan=2, pady=3)
type_Single["state"] = "disabled"

type_Multiple = Button(screen, text="Multiple Expression", fg="black", height=2, width=14, bg="white",
                       command=lambda: press_type_button())
type_Multiple.grid(column=0, row=1, columnspan=2)

total_text_field = Label(screen, textvariable=total_equation_label, font=("Arial", 12), bg="gray", fg="white", width=34,
                         anchor="e")
total_text_field.grid(columnspan=4, column=0, row=2)

text_field = Label(screen, textvariable=equation_label, font=("Arial", 24), bg="white", width=16, height=2, anchor="e")
text_field.grid(columnspan=4, column=0, row=3)

button_1 = Button(screen, text=1, height=3, width=6, font=10, command=lambda: press_number_button(1))
button_1.grid(column=0, row=8)

button_2 = Button(screen, text=2, height=3, width=6, font=10, command=lambda: press_number_button(2))
button_2.grid(column=1, row=8)

button_3 = Button(screen, text=3, height=3, width=6, font=10, command=lambda: press_number_button(3))
button_3.grid(column=2, row=8)

button_4 = Button(screen, text=4, height=3, width=6, font=10, command=lambda: press_number_button(4))
button_4.grid(column=0, row=7, pady=5)

button_5 = Button(screen, text=5, height=3, width=6, font=10, command=lambda: press_number_button(5))
button_5.grid(column=1, row=7)

button_6 = Button(screen, text=6, height=3, width=6, font=10, command=lambda: press_number_button(6))
button_6.grid(column=2, row=7)

button_7 = Button(screen, text=7, height=3, width=6, font=10, command=lambda: press_number_button(7))
button_7.grid(column=0, row=6, padx=7)

button_8 = Button(screen, text=8, height=3, width=6, font=10, command=lambda: press_number_button(8))
button_8.grid(column=1, row=6)

button_9 = Button(screen, text=9, height=3, width=6, font=10, command=lambda: press_number_button(9))
button_9.grid(column=2, row=6, padx=7)

button_0 = Button(screen, text=0, height=3, width=6, font=10, command=lambda: press_number_button(0))
button_0.grid(column=1, row=9, pady=5)

button_plus_minus = Button(screen, text="+/-", height=3, width=6, font=10, command=lambda: press_negative_button())
button_plus_minus.grid(column=0, row=9)

button_dot = Button(screen, text=".", height=3, width=6, font=10, command=lambda: press_number_button("."))
button_dot.grid(column=2, row=9)

button_equal = Button(screen, text="=", bg="lightblue", height=3, width=6, font=10,
                      command=lambda: press_equal_button())
button_equal.grid(column=3, row=9)

button_plus = Button(screen, text="+", bg="white", height=3, width=6, font=10,
                     command=lambda: press_function_button("+"))
button_plus.grid(column=3, row=8)

button_minus = Button(screen, text="-", bg="white", height=3, width=6, font=10,
                      command=lambda: press_function_button("-"))
button_minus.grid(column=3, row=7)

button_multiply = Button(screen, text="*", bg="white", height=3, width=6, font=10,
                         command=lambda: press_function_button("*"))
button_multiply.grid(column=3, row=6)

button_divide = Button(screen, text="/", bg="white", height=3, width=6, font=10,
                       command=lambda: press_function_button("/"))
button_divide.grid(column=3, row=5)

button_delete = Button(screen, text="BACK", bg="white", height=3, width=6, font=10,
                       command=lambda: press_delete_button())
button_delete.grid(column=2, row=5, pady=5)

button_clear = Button(screen, text="CLEAR", bg="red", height=3, width=13, font=10, command=lambda: reset())
button_clear.grid(column=0, row=5, columnspan=2)

screen.mainloop()
