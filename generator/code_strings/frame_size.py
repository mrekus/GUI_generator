frame_mainloop = """
def main():
    window = tk.Tk()
    window.geometry("{width}x{height}")
    window.resizable(False, False)
    window.title("test")
    window.mainloop()"""
