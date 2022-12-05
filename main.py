import tkinter
import tkinter.constants as cs


def _create_tk():
    window = tkinter.Tk()
    window.title("Schnee")
    window.geometry("480x400")  # width, height
    window.resizable(False, False)
    return window


def _init_layout_tk():
    func = GUIFunc()
    welcome_button = tkinter.Button(text="Welcome", command=func.print_welcome)
    reset_button = tkinter.Button(text="Reset", command=func.reset_frame)
    # Layout: can use pack(relative)/grid(row)/place(absolute)

    # side = top/bottom/right/left
    welcome_button.pack(side=cs.TOP)
    reset_button.pack(side=cs.BOTTOM)
    # test_button_2 = tkinter.Button(text="Test2")
    # test_button_2.place(x=200, y=200, anchor=cs.CENTER)

    # Can't use grid, when using the pack
    # test_button_3 = tkinter.Button(text="Test3")
    # test_button_3.grid(row=0, column=0)


class GUIFunc:

    def __init__(self, frame=None):
        self.frame = frame

    def print_welcome(self):
        if self.frame is None:
            frame = tkinter.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=200, height=200)
            frame.pack(anchor=cs.CENTER)
            self.frame = frame
            label = tkinter.Label(frame, text="Hello, World")
            label.pack(side=cs.TOP)

    def reset_frame(self):
        self.frame.destroy()
        self.frame = None


if __name__ == '__main__':
    window = _create_tk()
    _init_layout_tk()
    window.mainloop()
