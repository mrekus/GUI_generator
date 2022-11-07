import cv2
from generator.code_strings import frame_size, name_main, imports


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
        height, width = self.read_dimensions()
        if self.checkbox_state == 1:
            fname = "generated.py"

            with open(fname, "w") as f:
                f.write(imports.tk + "\n\n")
                f.write(frame_size.frame_mainloop + "\n")
                f.write(name_main.name_main.format(width=width, height=height))
