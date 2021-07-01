from password_generator import PasswordGenerator


class Menu:
    def __init__(self):
        self.menu_text = """Choose an option:
1. Generate a quick strong password
2. Generate a custom password
3. Quit"""
        self.menu_options = {"1": self.generate_quick_pwd, "2": self.generate_custom_pwd, "3": self.quit}
        self.pwd_generator = PasswordGenerator()

    def __show_menu(self):
        print(self.menu_text)

    def __choose_option(self):
        choice = input("Your selection: ")
        action = self.menu_options.get(choice)
        if action:
            action()
        else:
            print("{0} is not a valid choice".format(choice))

    def run(self):
        while True:
            self.__show_menu()
            self.__choose_option()

    def generate_quick_pwd(self):
        max_num_chars = self.pwd_generator.MAX_NUM_CHARS
        min_num_chars = self.pwd_generator.MIN_NUM_CHARS

        num_chars = self.__validate_int_range("Enter the number of characters: ", min_num_chars, max_num_chars)

        password = self.pwd_generator.create_quick_strong_pwd(num_chars)
        print("Generated password:", password)

    def generate_custom_pwd(self):
        max_letter = self.pwd_generator.LOWER_CASE_ASCII_DECIMAL_MAX - self.pwd_generator.LOWER_CASE_ASCII_DECIMAL_MIN + 1
        max_numeric = self.pwd_generator.MAX_NUM_CHARS - self.pwd_generator.MIN_NUM_CHARS + 1
        max_special = len(self.pwd_generator.SPECIAL_CHARS)

        num_lower_chars = self.__validate_int_range("Select the number of lower-case characters: ", 1, max_letter)
        num_upper_chars = self.__validate_int_range("Select the number of upper-case characters: ", 1, max_letter)
        num_numeric_chars = self.__validate_int_range("Select the number of numeric characters: ", 1, max_numeric)
        num_special_chars = self.__validate_int_range("Select the number of special characters: ", 1, max_special)

        password = self.pwd_generator.create_pwd(num_lower_chars, num_upper_chars,
                                                 num_numeric_chars, num_special_chars)
        print("Generated password:", password)

    def quit(self):
        print("Bye bye..")
        exit(0)

    def __validate_int_range(self, text, min, max):
        while True:
            try:
                number = int(input(text))
                if min <= number <= max:
                    return number
                else:
                    print("The number must be between {0} and {1}".format(min, max))
            except ValueError:
                print("That is not a valid number")
