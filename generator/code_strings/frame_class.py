frame_class = """
class Frame{frame_number}:
    def __init__(self, master):
        self.master = master
        
        self.button1 = MyButton1(command="")
        self.button2 = MyButton2(command="")
        
        self.button1.place(x={button1x}, y={button1y}, width={button1_width}, height={button1_height})
        self.button2.place(x={button2x}, y={button2y}, width={button2_width}, height={button2_height})
"""