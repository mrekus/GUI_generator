from tkinter import filedialog
import customtkinter as ctk
import os
import os.path
import generator


class MainFrame:
    def __init__(self, master):
        self.checkBox = ctk.IntVar()

        self.check = ctk.CTkCheckBox(text="Main Frame", variable=self.checkBox)
        self.label_file_explorer = ctk.CTkLabel(
            master, text="No image uploaded!", text_font=("courier", 12, "bold")
        )

        self.button_explore = ctk.CTkButton(
            master,
            text="Browse Files",
            height=50,
            compound="right",
            fg_color="#674ea7",
            hover_color="#a394ca",
            command=self.browse_files,
        )
        self.button_generate = ctk.CTkButton(
            master,
            text="Generate",
            height=50,
            compound="right",
            fg_color="#1aa13e",
            hover_color="#5EBD77",
            command=self.generate,
        )

        self.check.place(x=50, y=200)
        self.label_file_explorer.place(x=300, y=50)
        self.button_explore.place(x=50, y=130)
        self.button_generate.place(x=300, y=130)

    def browse_files(self):
        global file
        file = filedialog.askopenfilename(
            initialdir=f"{os.getcwd()}",
            title="Select a File",
            filetypes=[("Images (.png, .jpg, .jpeg)", ".png .jpg .jpeg")],
        )
        self.label_file_explorer.configure(
            text="Image Opened:\n" + os.path.basename(file)
        )

    def generate(self):
        image_path = os.path.abspath(file)
        generator.FrameGenerator(image_path, self.check.get()).generate_frame()
