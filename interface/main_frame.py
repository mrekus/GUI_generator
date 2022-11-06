from tkinter import filedialog
import customtkinter as ctk
import os
import os.path


class MainFrame:
    def __init__(self, master):
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

        self.label_file_explorer.place(x=300, y=50)
        self.button_explore.place(x=50, y=100)

    def browse_files(self):
        filename = filedialog.askopenfilename(
            initialdir=f"{os.getcwd()}",
            title="Select a File",
            filetypes=[("Images (.png, .jpg, .jpeg)", ".png .jpg .jpeg")],
        )
        self.label_file_explorer.configure(
            text="Image Opened:\n" + os.path.basename(filename)
        )
