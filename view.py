import text_fields as txt
from classes import Contact


def main_menu() -> int:
    print(txt.main_menu)
    while True:
        choice = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
