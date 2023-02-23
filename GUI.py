from tkinter import *
from calcs import *


def create_gui():
    # Initialize Tkinter GUI

    root = Tk()
    root.geometry("500x400")
    frame = Frame(root)
    frame.pack(fill=BOTH,expand=TRUE)

    # Parent Create the display window - Label Widget
    label = Label(frame, text="Press Any Key", width=30, bg="WHITE", relief=SUNKEN, padx=0, anchor=E)
    label.pack(side=TOP,fill=BOTH)

    # Parent Button Frames - Frame Widget containg buttons below Lable Widget
    button_frames = Frame(frame, bd=4, width=30,bg="orange")
    button_frames.pack(side=TOP ,fill=BOTH,expand=True)

    # Child Number Keypad Frame  - Frame Widget within Frame Widget
    number_keypad_frame = Frame(button_frames, bd=4, height=25, width=25,bg="red")
    number_keypad_frame.pack(side=LEFT,fill=BOTH,expand=True)

    # Child Operator Keypad Frame  - Frame Widget within Frame Widghet
    operator_keypad_frame = Frame(button_frames, bd=4, height=25, width=25,bg="blue")
    operator_keypad_frame.pack(side=LEFT,fill=BOTH,expand=True)

    
    # Create Number Pad 0-9
    number_keys = [["7", "8", "9"], ["4"," 5", "6"], ["1","2", "3"], ["0"]]

    for key_row in number_keys:
        for key_colum in key_row:
            row_index = number_keys.index(key_row)
            column_index = key_row.index(key_colum)
            new_buttons = Button(number_keypad_frame, text=key_colum, command=lambda name=key_colum: update_window(name,label))
            new_buttons.grid(row=row_index,column=column_index, sticky='NSEW')

            number_keypad_frame.columnconfigure(column_index,weight=1)
            number_keypad_frame.rowconfigure(row_index, weight=1)

    # Create Operation Pad
    operation_keys = [["(", ")", "+"], ["-", "/", "*"], ["CE","<--","="]]
    for key_row in operation_keys:
        for key_colum in key_row:
            row_index=operation_keys.index(key_row)
            column_index=key_row.index(key_colum)
            new_buttons = Button(operator_keypad_frame, text=key_colum, command=lambda name=key_colum: update_window(name,label),)
            new_buttons.grid(row=row_index,column=column_index, sticky='NSEW')

            operator_keypad_frame.columnconfigure(column_index,weight=1)
            operator_keypad_frame.rowconfigure(row_index, weight=1)
    
    
    root.title("Simple Calculator")

    root.mainloop()


