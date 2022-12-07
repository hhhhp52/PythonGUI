import tkinter as tk
import tkinter.constants as cs


def _create_tk():
    app = tk.Tk()
    app.title("Schnee")
    app.geometry("480x400")  # width, height
    app.resizable(False, False)
    return app


def _init_layout_tk():
    GUIFunc()
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
        self.homepage_frame = None
        self.after_login_frame = None
        self.welcome_button = welcome_button
        self.reset_button = None

    def print_welcome(self):
        if self.after_login_frame is None:
            if self.welcome_button:
                self.welcome_button.destroy()
                self.welcome_button = None
            if self.homepage_frame:
                self.homepage_frame.destroy()
                self.homepage_frame = None

            reset_button = tk.Button(text="Reset", command=self.reset_frame)
            reset_button.pack(side=cs.BOTTOM)
            after_login_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=200, height=200)
            after_login_frame.pack(anchor=cs.CENTER)
            label = tk.Label(after_login_frame, text="歡迎登入")
            label.pack(anchor=cs.CENTER)

            self.reset_button = reset_button
            self.after_login_frame = after_login_frame

    def reset_frame(self):
        if self.homepage_frame is None:
            if self.reset_button:
                self.reset_button.destroy()
                self.reset_button = None
            if self.after_login_frame:
                self.after_login_frame.destroy()
                self.after_login_frame = None

            welcome_button = tk.Button(text="Welcome", command=self.print_welcome)
            welcome_button.pack(side=cs.TOP)
            homepage_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=200, height=200)
            homepage_frame.pack(anchor=cs.CENTER)
            label = tk.Label(homepage_frame, text="Hello, World")
            label.pack(anchor=cs.CENTER)

            self.welcome_button = welcome_button
            self.homepage_frame = homepage_frame


if __name__ == '__main__':
    window = _create_tk()
    _init_layout_tk()
    window.mainloop()
