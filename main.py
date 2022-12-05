import tkinter
import tkinter.constants as cs


def _create_tk():
    window = tkinter.Tk()
    window.title("Schnee")
    window.geometry("480x400")  # width, height
    window.resizable(False, False)
    return window


def _layout_tk():
    func = GUIFunc()
    test_button_1 = tkinter.Button(text="Welcome", command=func.print_welcome)

    # Layout: can use pack(relative)/grid(row)/place(absolute)

    # side = top/bottom/right/left
    test_button_1.pack(side=cs.TOP)

    test_button_2 = tkinter.Button(text="Test2")
    test_button_2.place(x=200, y=200, anchor=cs.CENTER)

    # Can't use grid, when using the pack
    # test_button_3 = tkinter.Button(text="Test3")
    # test_button_3.grid(row=0, column=0)


class GUIFunc:

    @staticmethod
    def print_welcome():
        label = tkinter.Label(text="Hello, World")
        label.pack(side=cs.TOP)


if __name__ == '__main__':
    window = _create_tk()
    _layout_tk()
    window.mainloop()
