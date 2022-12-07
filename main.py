import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox

import constants
from api import api
from utils.helper import get_host_by_env


class LoginGUIFunc:

    def __init__(self):
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None
        self.env_variable = None

    def login_layout_init(self):
        env_variable = tk.StringVar()
        env_variable.set("env")
        login_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        env_label = tk.Label(login_frame, text="Environment: ")
        env_label.grid(row=0, column=0)
        local_radio_button = tk.Radiobutton(
            login_frame, variable=env_variable, text="local", value=constants.LOCAL
        )
        local_radio_button.select()
        local_radio_button.grid(row=0, column=1)
        dev_radio_button = tk.Radiobutton(
            login_frame, variable=env_variable, text="development", value=constants.DEV
        )
        dev_radio_button.grid(row=0, column=2)
        staging_radio_button = tk.Radiobutton(
            login_frame, variable=env_variable, text="staging", value=constants.STAGING
        )
        staging_radio_button.grid(row=0, column=3)
        account_label = tk.Label(login_frame, text="Account: ")
        account_label.grid(row=1, column=0)
        account_entry = tk.Entry(login_frame)
        account_entry.grid(row=1, column=1)
        password_label = tk.Label(login_frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.grid(row=2, column=1)
        login_button = tk.Button(login_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=1)
        clear_button = tk.Button(login_frame, text="Clear", command=self.clear)
        clear_button.grid(row=3, column=2)
        login_frame.pack(anchor=cs.CENTER)
        self.login_frame = login_frame
        self.account_entry = account_entry
        self.password_entry = password_entry
        self.env_variable = env_variable

    def clear(self):
        self.login_frame.destroy()
        self.account_entry.destroy()
        self.password_entry.destroy()
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None
        self.env_variable = None
        self.login_layout_init()

    def login(self):
        account = self.account_entry.get()
        password = self.password_entry.get()
        env = self.env_variable.get()
        host = get_host_by_env(env)

        if host and account and password:
            # For test:
            flag = True
            if flag:
                messagebox.showinfo("Success", "Login Success")
                _init_homepage_layout(env, account, password)
            else:
                data = dict(
                    account=account,
                    password=password
                )

                flag, message, data = api.login(host, data)
                if flag:
                    messagebox.showinfo("Success", "Login Success")
                    _init_homepage_layout(env, account, password)
                else:
                    messagebox.showerror("Failed", "Login Failed")

        else:
            messagebox.showerror("Failed", "Login Failed")

    def destroy_login_layout(self):
        self.login_frame.destroy()
        self.account_entry.destroy()
        self.password_entry.destroy()
        self.login_frame = None
        self.account_entry = None
        self.password_entry = None
        self.env_variable = None


class HomePageGUIFunc:

    def __init__(self, env=None, account=None):
        self.homepage_frame = None
        self.env = env
        self.account = account

    def homepage_layout_init(self):
        homepage_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        env_label = tk.Label(homepage_frame, text="Environment: ")
        env_label.grid(row=0, column=0)
        env_show_label = tk.Label(homepage_frame, text=self.env)
        env_show_label.grid(row=0, column=1)
        account_label = tk.Label(homepage_frame, text="Account: ")
        account_label.grid(row=0, column=2)
        account_show_label = tk.Label(homepage_frame, text=self.account)
        account_show_label.grid(row=0, column=3)

        content_label = tk.Label(homepage_frame, text="Hi, {account}, Welcome to generator".format(account=self.account))
        content_label.grid(row=1, column=3)

        logout_button = tk.Button(homepage_frame, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=0)
        clear_button = tk.Button(homepage_frame, text="Clear", command=self.clear)
        clear_button.grid(row=2, column=1)
        homepage_frame.pack(anchor=cs.CENTER)
        self.homepage_frame = homepage_frame

    def clear(self):
        self.homepage_frame.destroy()
        self.homepage_frame = None
        self.homepage_layout_init()

    def logout(self):
        _init_login_layout()

    def destroy_homepage_layout(self):
        self.homepage_frame.destroy()
        self.homepage_frame = None
        self.account = None
        self.env = None


login_gui_func = LoginGUIFunc()
homepage_gui_func = HomePageGUIFunc()


def _create_tk():
    app = tk.Tk()
    app.title("Generator Beta")
    app.geometry("720x480")  # width, height
    app.resizable(False, False)
    return app


def _init_homepage_layout(env, account, password):
    login_gui_func.destroy_login_layout()
    print(env, account, password)
    homepage_gui_func.env = env
    homepage_gui_func.account = account
    homepage_gui_func.homepage_layout_init()


def _init_login_layout(first_init=False):
    if not first_init:
        homepage_gui_func.destroy_homepage_layout()
    login_gui_func.login_layout_init()


if __name__ == '__main__':
    app = _create_tk()
    _init_login_layout(first_init=True)
    app.mainloop()
