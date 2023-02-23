## Update Display window after key press
def update_window(key_pressed,label):

        ## Initial key Press erases original text
        if "Press Any Key" in label.cget("text"):
            label.config(text=key_pressed)

        ## Equal sign key pressed 
        elif "=" in key_pressed:
            try:
                answer = eval(label.cget('text'))
            except:
                print("Error")
                window_text = label.cget('text')
                label.config(text="Error")
                ##time.sleep(3)
                label.config(text= window_text)
            else:
                label.config(text=str(answer))

        ## Backspace key is pressed
        elif "<--" in key_pressed:
            old_text = label.cget('text')
            original_text = old_text[0:-1]
            label.config(text=original_text)

        ## When number or operation key is pressed
        elif key_pressed.isalpha() != True:
            old_text = label.cget('text')
            new_text = old_text + key_pressed
            label.config(text=new_text)

        ## Clear key is pressed
        elif "CE" in key_pressed:
            label.config(text="Press Any Key")
        
        
        