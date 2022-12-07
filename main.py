import tkinter as tk
import tkinter.constants as cs


def _create_tk():
    app = tk.Tk()
    app.title("Schnee")
    app.geometry("480x400")  # width, height
    app.resizable(False, False)
    return app


def _init_layout_tk():
    func = GUIFunc()
    reset_button = tk.Button(text="Reset", command=func.reset_frame)
    # Layout: can use pack(relative)/grid(row)/place(absolute)

    # side = top/bottom/right/left
    # test_button_2 = tkinter.Button(text="Test2")
    # test_button_2.place(x=200, y=200, anchor=cs.CENTER)

    # Can't use grid, when using the pack
    # test_button_3 = tkinter.Button(text="Test3")
    # test_button_3.grid(row=0, column=0)


class GUIFunc:

    def __init__(self):
        welcome_button = tk.Button(text="Welcome", command=self.print_welcome)
        welcome_button.pack(side=cs.TOP)
        self.frame = None
        self.welcome_button = welcome_button
        self.reset_button = None

    def print_welcome(self):
        if self.frame is None:
            frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=200, height=200)
            frame.pack(anchor=cs.CENTER)
            self.frame = frame
            label = tk.Label(frame, text="Hello, World")
            label.pack(side=cs.TOP)
            reset_button = tk.Button(text="Reset", command=self.reset_frame)
            reset_button.pack(side=cs.BOTTOM)
            self.reset_button = reset_button
            self.welcome_button.destroy()
            self.welcome_button = None

    def reset_frame(self):
        self.frame.destroy()
        self.frame = None
        self.reset_button.destroy()
        self.reset_button = None
        welcome_button = tk.Button(text="Welcome", command=self.print_welcome)
        welcome_button.pack(side=cs.TOP)
        self.welcome_button = welcome_button


if __name__ == '__main__':
    window = _create_tk()
    _init_layout_tk()
    window.mainloop()
