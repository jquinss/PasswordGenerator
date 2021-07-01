import tkinter as tk
from tkinter import ttk
from password_generator import PasswordGenerator
import pyperclip


class PasswordGeneratorFrame(tk.Frame):
    DEFAULT_TOTAL_CHARS = 12
    INCREMENT = 1

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__pwd_generator = PasswordGenerator()
        self.__max_lower_case = self.__pwd_generator.LOWER_CASE_ASCII_DECIMAL_MAX - \
                                self.__pwd_generator.LOWER_CASE_ASCII_DECIMAL_MIN + 1
        self.__max_upper_case = self.__max_lower_case
        self.__max_digits = self.__pwd_generator.MAX_NUM_CHARS - self.__pwd_generator.MIN_NUM_CHARS + 1
        self.__max_special = len(self.__pwd_generator.SPECIAL_CHARS)
        self.__total_chars = self.DEFAULT_TOTAL_CHARS
        self.__initialize_ui_components()
        self.__initialize_default_values()

    def __initialize_ui_components(self):
        self.__initialize_spinboxes()
        self.__initialize_labels()
        self.__initialize_entries()
        self.__initialize_buttons()

    def __initialize_spinboxes(self):
        self.__lower_case_spinbox = ttk.Spinbox(self, from_=0, to=self.__max_lower_case, increment=self.INCREMENT,
                                                width=3)
        self.__upper_case_spinbox = ttk.Spinbox(self, from_=0, to=self.__max_upper_case, increment=self.INCREMENT,
                                                width=3)
        self.__digits_spinbox = ttk.Spinbox(self, from_=0, to=self.__max_digits, increment=self.INCREMENT,
                                            width=3)
        self.__special_spinbox = ttk.Spinbox(self, from_=0, to=self.__max_special, increment=self.INCREMENT,
                                             width=3)
        self.__lower_case_spinbox.grid(row=1, column=0, padx=15, pady=5)
        self.__upper_case_spinbox.grid(row=2, column=0, pady=5)
        self.__digits_spinbox.grid(row=3, column=0, pady=5)
        self.__special_spinbox.grid(row=4, column=0, pady=5)
        self.__lower_case_spinbox.config(command=self.__update_total_chars)
        self.__upper_case_spinbox.config(command=self.__update_total_chars)
        self.__digits_spinbox.config(command=self.__update_total_chars)
        self.__special_spinbox.config(command=self.__update_total_chars)

    def __initialize_labels(self):
        description_label = ttk.Label(self, text="Create a random password using the criteria below:")
        lower_case_label = ttk.Label(self, text="Number of lower-case characters (a-z)")
        upper_case_label = ttk.Label(self, text="Number of upper-case characters (A-Z)")
        digits_label = ttk.Label(self, text="Number of digits (0-9)")
        special_label = ttk.Label(self, text="Number of special characters (!,#,$,%,',..)")
        total_chars_label = ttk.Label(self, text="Total number of characters")
        description_label.grid(row=0, columnspan=2, padx=15, pady=5, sticky="W")
        lower_case_label.grid(row=1, column=1, sticky="W")
        upper_case_label.grid(row=2, column=1, sticky="W")
        digits_label.grid(row=3, column=1, sticky="W")
        special_label.grid(row=4, column=1, sticky="W")
        total_chars_label.grid(row=5, column=1, sticky="W")

    def __initialize_entries(self):
        self.__total_chars_entry = ttk.Entry(self, width=5, state="disabled")
        self.__pwd_entry = ttk.Entry(self)
        self.__total_chars_entry.grid(row=5, column=0, pady=5)
        self.__pwd_entry.grid(row=7, column=0, columnspan=2, pady=5)

    def __initialize_buttons(self):
        generate_pwd_btn = ttk.Button(self, text="Generate password", command=self.__generate_pwd)
        copy_to_clipboard_btn = ttk.Button(self, text="Copy to clipboard", command=self.__copy_pwd_to_clipboard)
        generate_pwd_btn.grid(row=6, columnspan=2, pady=5)
        copy_to_clipboard_btn.grid(row=8, columnspan=2, pady=5)

    def __get_num_chars_per_category(self):
        num_chars_per_category = {"lower": int(self.__lower_case_spinbox.get()),
                                  "upper": int(self.__upper_case_spinbox.get()),
                                  "number": int(self.__digits_spinbox.get()),
                                  "special": int(self.__special_spinbox.get())}
        return num_chars_per_category

    def __calculate_total_chars(self):
        total = 0
        for value in self.__get_num_chars_per_category().values():
            total += value
        self.__total_chars = total

    def __update_total_chars_entry(self):
        self.__total_chars_entry.config(state="enabled")
        self.__total_chars_entry.delete(0, tk.END)
        self.__total_chars_entry.insert(0, self.__total_chars)
        self.__total_chars_entry.config(state="disabled")

    def __update_total_chars(self):
        self.__calculate_total_chars()
        self.__update_total_chars_entry()

    def __initialize_default_values(self):
        num_chars_per_category = self.__pwd_generator.get_num_chars_per_category(self.__total_chars)
        self.__lower_case_spinbox.set(num_chars_per_category.get("lower"))
        self.__upper_case_spinbox.set(num_chars_per_category.get("upper"))
        self.__digits_spinbox.set(num_chars_per_category.get("number"))
        self.__special_spinbox.set(num_chars_per_category.get("special"))
        self.__calculate_total_chars()
        self.__update_total_chars_entry()

    def __generate_pwd(self):
        num_chars_per_category = self.__get_num_chars_per_category()
        pwd = self.__pwd_generator.create_pwd(num_chars_per_category["lower"], num_chars_per_category["upper"],
                                              num_chars_per_category["number"], num_chars_per_category["special"])
        self.__pwd_entry.delete(0, tk.END)
        self.__pwd_entry.insert(0, pwd)

    def __copy_pwd_to_clipboard(self):
        pyperclip.copy(self.__pwd_entry.get())


class PasswordGeneratorUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Password Generator")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        PasswordGeneratorFrame(self).grid(row=0, column=0, sticky="")
        self.columnconfigure(0, weight=1)
