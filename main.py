import tkinter as tk
import tkinter.constants as cs
from tkinter import messagebox

import constants
from domain import domain
from entity.user import user
from util.helper import get_host_by_env


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
            flag = domain.login_flow(host, account, password)
            if flag:
                messagebox.showinfo("Success", "Login Success")
                _init_homepage_layout(env, account)
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
        # func button frame
        self.glucose_frame = None
        self.bp_frame = None

    def homepage_layout_init(self):
        homepage_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        env_label = tk.Label(homepage_frame, text="Environment: {env}".format(env=self.env))
        env_label.grid(row=0, column=0)
        account_label = tk.Label(homepage_frame, text="Account: {account}".format(account=self.account))
        account_label.grid(row=0, column=1)
        clear_button = tk.Button(homepage_frame, text="Clear", command=self.clear)
        clear_button.grid(row=0, column=2)
        logout_button = tk.Button(homepage_frame, text="Logout", command=self.logout)
        logout_button.grid(row=0, column=3)
        content_label = tk.Label(
            homepage_frame,
            text="Hi, {first_name} {last_name}, Welcome to generator".format(
                first_name=user.first_name,
                last_name=user.last_name
            )
        )
        content_label.grid(row=1, column=1)
        generate_glucose_button = tk.Button(
            homepage_frame,
            text="Glucose Auto Generator",
            command=self.glucose_generator_layout
        )
        generate_glucose_button.grid(row=2, column=0)
        generate_bp_button = tk.Button(
            homepage_frame,
            text="BP Auto Generator",
            command=self.bp_generator_layout
        )
        generate_bp_button.grid(row=2, column=1)
        homepage_frame.pack(anchor=cs.CENTER)
        self.homepage_frame = homepage_frame

    def clear(self):
        self.homepage_frame.destroy()
        self.homepage_frame = None
        self.clear_func_frame()
        self.homepage_layout_init()

    def clear_func_frame(self):
        if self.glucose_frame:
            self.glucose_frame.destroy()
            self.glucose_frame = None
        if self.bp_frame:
            self.bp_frame.destroy()
            self.bp_frame = None

    def destroy_homepage_layout(self):
        self.homepage_frame.destroy()
        self.homepage_frame = None
        self.account = None
        self.env = None

    def logout(self):
        user.reset_user()
        self.clear_func_frame()
        _init_login_layout()

    @staticmethod
    def _time_choose_layout(frame):
        time_choose_label = tk.Label(frame, text="請針對下方進行填寫")
        time_choose_label.grid(row=1, column=0)
        before_meal_breakfast_label = tk.Label(frame, text="早餐前")
        before_meal_breakfast_label.grid(row=2, column=0)
        before_meal_breakfast_entry = tk.Entry(frame)
        before_meal_breakfast_entry.grid(row=2, column=1)
        after_meal_breakfast_label = tk.Label(frame, text="早餐後")
        after_meal_breakfast_label.grid(row=2, column=2)
        after_meal_breakfast_entry = tk.Entry(frame)
        after_meal_breakfast_entry.grid(row=2, column=3)
        before_meal_lunch_label = tk.Label(frame, text="午餐前")
        before_meal_lunch_label.grid(row=3, column=0)
        before_meal_lunch_entry = tk.Entry(frame)
        before_meal_lunch_entry.grid(row=3, column=1)
        after_meal_lunch_label = tk.Label(frame, text="午餐後")
        after_meal_lunch_label.grid(row=3, column=2)
        after_meal_lunch_entry = tk.Entry(frame)
        after_meal_lunch_entry.grid(row=3, column=3)
        before_meal_dinner_label = tk.Label(frame, text="晚餐前")
        before_meal_dinner_label.grid(row=4, column=0)
        before_meal_dinner_entry = tk.Entry(frame)
        before_meal_dinner_entry.grid(row=4, column=1)
        after_meal_dinner_label = tk.Label(frame, text="晚餐後")
        after_meal_dinner_label.grid(row=4, column=2)
        after_meal_dinner_entry = tk.Entry(frame)
        after_meal_dinner_entry.grid(row=4, column=3)
        wakeup_label = tk.Label(frame, text="晨起")
        wakeup_label.grid(row=5, column=0)
        wakeup_entry = tk.Entry(frame)
        wakeup_entry.grid(row=5, column=1)
        bedtime_label = tk.Label(frame, text="就寢")
        bedtime_label.grid(row=5, column=2)
        bedtime_entry = tk.Entry(frame)
        bedtime_entry.grid(row=5, column=3)
        midnight_label = tk.Label(frame, text="半夜")
        midnight_label.grid(row=6, column=0)
        midnight_entry = tk.Entry(frame)
        midnight_entry.grid(row=6, column=1)
        other_label = tk.Label(frame, text="其他")
        other_label.grid(row=6, column=2)
        other_entry = tk.Entry(frame)
        other_entry.grid(row=6, column=3)

    def glucose_generator_layout(self):
        self.clear_func_frame()
        glucose_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=400)
        glucose_title_label = tk.Label(glucose_frame, text="Glucose Generator")
        glucose_title_label.grid(row=0, column=0)
        time_choose_label = tk.Label(glucose_frame, text="請針對下方進行填寫")
        time_choose_label.grid(row=1, column=0)
        # row: start from 2 to end 6
        self._time_choose_layout(glucose_frame)
        glucose_frame.pack(side=cs.TOP)
        self.glucose_frame = glucose_frame

    def bp_generator_layout(self):
        self.clear_func_frame()
        bp_frame = tk.Frame(relief=cs.RIDGE, borderwidth=2, padx=2, pady=2, width=400, height=200)
        bp_title_label = tk.Label(bp_frame, text="Bp Generator")
        bp_title_label.grid(row=0, column=0)
        # row: start from 1 to end 6
        self._time_choose_layout(bp_frame)
        bp_frame.pack(side=cs.TOP)
        self.bp_frame = bp_frame


login_gui_func = LoginGUIFunc()
homepage_gui_func = HomePageGUIFunc()


def _create_tk():
    app = tk.Tk()
    app.title("Generator Beta")
    app.geometry("1024x768")  # width, height
    app.resizable(False, False)
    return app


def _init_homepage_layout(env, account):
    login_gui_func.destroy_login_layout()
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
