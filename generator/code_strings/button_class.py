def create_button_class(number):
    buttons = {}
    for i in range(1, number + 1):
        buttons[
            "button{0}".format(i)
        ] = """
class MyButton{num}(tk.Button):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.config()
""".format(num=i)
    return buttons
