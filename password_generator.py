from math import ceil
import random


class PasswordGenerator:
    LOWER_CASE_ASCII_DECIMAL_MIN = 97
    LOWER_CASE_ASCII_DECIMAL_MAX = 122
    UPPER_CASE_ASCII_DECIMAL_MIN = 65
    UPPER_CASE_ASCII_DECIMAL_MAX = 90
    NUMBER_ASCII_DECIMAL_MIN = 48
    NUMBER_ASCII_DECIMAL_MAX = 57
    SPECIAL_CHARS = ["!", "#", "$", "%", "'", "(", ")", "+", ",", "-", ".", "/", ":",
                     "?", "@", "[", "\\", "]", "^", "_", "{", "}", "~"]
    MIN_NUM_CHARS = 6
    MAX_NUM_CHARS = 20

    PERCENTAGE_UPPER = 0.25
    PERCENTAGE_NUMBER = 0.15
    PERCENTAGE_SPECIAL = 0.10

    def create_pwd(self, num_lower, num_upper, num_numeric, num_special):

        lower_chars = self.__get_unique_rand_chars_from_range(num_lower, self.LOWER_CASE_ASCII_DECIMAL_MIN,
                                                              self.LOWER_CASE_ASCII_DECIMAL_MAX)
        upper_chars = self.__get_unique_rand_chars_from_range(num_upper, self.UPPER_CASE_ASCII_DECIMAL_MIN,
                                                              self.UPPER_CASE_ASCII_DECIMAL_MAX)
        numeric_chars = self.__get_unique_rand_chars_from_range(num_numeric, self.NUMBER_ASCII_DECIMAL_MIN,
                                                                self.NUMBER_ASCII_DECIMAL_MAX)
        special_chars = self.__get_unique_rand_chars_from_list(num_special, self.SPECIAL_CHARS)
        merged_char_list = self.__merge_lists(lower_chars, upper_chars, numeric_chars, special_chars)
        self.__randomize_list(merged_char_list)

        password = self.__join_list_elements(merged_char_list)

        return password

    def create_quick_strong_pwd(self, num_chars):
        num_chars_per_category = self.get_num_chars_per_category(num_chars)
        password = self.create_pwd(num_chars_per_category["lower"], num_chars_per_category["upper"],
                                   num_chars_per_category["number"], num_chars_per_category["special"])
        return password

    def get_num_chars_per_category(self, num_chars):
        num_upper_chars = ceil(num_chars * self.PERCENTAGE_UPPER)
        num_numeric_chars = ceil(num_chars * self.PERCENTAGE_NUMBER)
        num_special_chars = ceil(num_chars * self.PERCENTAGE_SPECIAL)
        num_lower_chars = num_chars - num_upper_chars - num_numeric_chars - num_special_chars
        num_chars_per_category = {"lower": num_lower_chars, "upper": num_upper_chars, "number": num_numeric_chars,
                                  "special": num_special_chars}
        return num_chars_per_category

    def __get_rand_int(self, min, max):
        return random.randint(min, max)

    def __get_rand_char(self, min, max):
        return str(chr(self.__get_rand_int(min, max)))

    def __get_unique_rand_chars_from_range(self, num_chars, min, max):
        unique_chars = []
        while len(unique_chars) < num_chars:
            rand_char = self.__get_rand_char(min, max)
            if rand_char not in unique_chars:
                unique_chars.append(rand_char)
        return unique_chars

    def __get_unique_rand_chars_from_list(self, num_chars, char_list):
        return random.sample(char_list, num_chars)

    def __merge_lists(self, *args):
        merged = []
        for list in args:
            merged.extend(list)
        return merged

    def __randomize_list(self, list):
        random.shuffle(list)

    def __join_list_elements(self, list):
        return ''.join(list)
