import cv2
import generator.code_strings
import widget_finder


class FrameGenerator:
    def __init__(self, image, checkbox_state):
        self.image = image
        self.checkbox_state = checkbox_state

    def read_dimensions(self):
        img = cv2.imread(self.image, cv2.IMREAD_COLOR)
        height = img.shape[0]
        width = img.shape[1]
        return height, width

    def generate_frame(self):
        fname = "generated.py"
        buttons = generator.code_strings.button_class.create_button_class(2)
        with open(fname, "w") as f:
            f.write(generator.code_strings.imports.tk + "\n\n")
            for button in buttons.values():
                f.write(button + "\n")

        button1x, button1y, button2x, button2y = widget_finder.button_info()
        with open(fname, "a") as f:
            f.write(
                generator.code_strings.frame_class.frame_class.format(
                    frame_number=1,
                    button1x=button1x[0],
                    button1y=button1y[0],
                    button2x=button2x[0],
                    button2y=button2y[0],
                    button1_width=len(button1x),
                    button1_height=len(button1y),
                    button2_width=len(button2x),
                    button2_height=len(button2y)
                )
                + "\n"
            )

        height, width = self.read_dimensions()
        if self.checkbox_state == 1:
            with open(fname, "a") as f:
                f.write(
                    generator.code_strings.frame_size.frame_mainloop.format(
                        frame_number=1, width=width, height=height
                    )
                    + "\n"
                )
                f.write(generator.code_strings.name_main.name_main)
