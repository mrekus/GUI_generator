frame_mainloop = """
def main():
    window = tk.Tk()
    Frame{frame_number}(window)
    window.geometry("{width}x{height}")
    window.resizable(False, False)
    window.title("test")
    window.mainloop()
"""
