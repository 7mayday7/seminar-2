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


def print_message(message: str) -> None:
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def new_contact() -> Contact:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    return Contact(name, phone, comment)
