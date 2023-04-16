import text_fields as txt
from classes import Contact


def main_menu() -> int:
    print(txt.main_menu)
    while True:
        choice = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def show_contacts(book: list[Contact], message: str) -> None:
    print('\n' + '-' * 70)
    if book:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact}')
    else:
        print(message)
    print('-' * 70 + '\n')
