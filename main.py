import tkinter as tk
import tkinter.constants as cs

from api import api
from utils.helper import get_host_by_env


def _create_failed_tk():
    failed_login_app = tk.Tk()
    failed_login_app.title("Login Failed")
    failed_login_app.geometry("240x200")  # width, height
    failed_login_app.resizable(False, False)
    failed_label = tk.Label(failed_login_app, text="Login Failed")
    failed_label.pack(fill=cs.BOTH)
    return failed_login_app


def _create_tk():
    app = tk.Tk()
    app.title("Generator Beta")
    app.geometry("720x480")  # width, height
    app.resizable(False, False)
    return app


def _init_homepage_layout(env, account, password):
    print("_init_homepage_layout")
    print(env, account, password)
    # HomePageGUIFunc()


def _init_login_layout():
    LoginGUIFunc()


class LoginGUIFunc:

    def __init__(self):
        env_variable = tk.StringVar()
        env_variable.set("env")
        home_page_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        env_label = tk.Label(home_page_frame, text="Environment: ")
        env_label.grid(row=0, column=0)
        local_radio_button = tk.Radiobutton(home_page_frame, variable=env_variable, text="local", value="local")
        local_radio_button.select()
        local_radio_button.grid(row=0, column=1)
        dev_radio_button = tk.Radiobutton(home_page_frame, variable=env_variable, text="development", value="dev")
        dev_radio_button.grid(row=0, column=2)
        staging_radio_button = tk.Radiobutton(home_page_frame, variable=env_variable, text="staging", value="stg")
        staging_radio_button.grid(row=0, column=3)
        account_label = tk.Label(home_page_frame, text="Account: ")
        account_label.grid(row=1, column=0)
        account_entry = tk.Entry(home_page_frame)
        account_entry.grid(row=1, column=1)
        password_label = tk.Label(home_page_frame, text="Password: ")
        password_label.grid(row=2, column=0)
        password_entry = tk.Entry(home_page_frame)
        password_entry.grid(row=2, column=1)
        login_button = tk.Button(home_page_frame, text="Login", command=self.login)
        login_button.grid(row=3, column=1)
        home_page_frame.pack(anchor=cs.CENTER)
        self.home_page_frame = home_page_frame
        self.account_entry = account_entry
        self.password_entry = password_entry
        self.env_variable = env_variable

    def login(self):
        account = self.account_entry.get()
        password = self.password_entry.get()
        env = self.env_variable.get()
        host = get_host_by_env(env)
        if host:
            data = dict(
                account=account,
                password=password
            )

            flag, message, data = api.login(host, data)
            if flag:
                _init_homepage_layout(env, account, password)
            else:
                failed_login_app = _create_failed_tk()
                failed_login_app.mainloop()

        else:
            failed_login_app = _create_failed_tk()
            failed_login_app.mainloop()


if __name__ == '__main__':
    app = _create_tk()
    _init_login_layout()
    app.mainloop()
