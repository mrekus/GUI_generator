import customtkinter as ctk
import interface


def main():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")
    window = ctk.CTk()
    interface.MainFrame(window)
    window.geometry("900x450+800+400")
    window.resizable(False, False)
    window.title("GUI Generator")
    window.mainloop()


if __name__ == "__main__":
    main()
