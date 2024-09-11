import sqlite3

from utils import database

USER_CHOICE = """
- 'a' to add a game
- 'l' to list games
- 'c' to mark game as completed
- 'd' to delete a game
- 'q' to quit
Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    database.create_game_table()
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_game()
        elif user_input == 'l':
            list_books()
        elif user_input == 'c':
            prompt_mark_as_finished()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command. Please try again.')

        user_input = input(USER_CHOICE)


def prompt_add_game():
    can_be_finished = 1
    name = input('Enter the title of the game: ').title()
    publisher = input('Enter the publisher of the game: ').title()


    try:
        database.add_game(name, publisher)
    except sqlite3.IntegrityError:
        print('This game is already in your collection.')

    can_be_finished_input = input('Can this game be "completed"? (yes / no): ')
    if can_be_finished_input.lower() == "no":
        database.game_cannot_be_completed(name)
    elif can_be_finished_input.lower() == "yes":
        pass
    else:
        print('Input not understood. Default (yes) is set.')


def list_books():
    read = ''
    games = database.get_all_games()
    for game in games:
        print(f"""
The title of the game is {game['name'].upper()}.
The publisher is {game['publisher'].upper()}.""")
        if game['can be finished'] == 1:
            read = 'You have finished this game.' if game['read'] else 'You have not finished this game.'
            print(read)
        elif game['can be finished'] == 0:
            read = ' '
            print(read)


def prompt_mark_as_finished():
    name = input('Enter the title of the game you finished: ').title()
    database.mark_as_finished(name)


def prompt_delete_book():
    name = input('Enter the title of the game you want to delete: ').title()
    database.delete_book(name)


menu()
