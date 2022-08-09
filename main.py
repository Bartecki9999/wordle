
import time
from termcolor import colored

from databaseconnection import DataBaseManager


def main():
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='\n')

    correct_word = DataBaseManager.select_one_word()
    print(correct_word)

    while True:

        attempt = input('')

        if attempt == correct_word:
            print(colored('guessed', 'green', attrs=['reverse', 'blink']))
            break

        if len(attempt) == 5:
            for character in range(5):

                if attempt[character] == correct_word[character]:
                    print(colored(attempt[character], 'green'), end='')

                elif attempt[character] in correct_word:
                    print(colored(attempt[character], 'yellow'), end='')

                else:
                    print(colored(attempt[character], 'red'), end='')
            print('\n')
        else:
            print('Enter 5 letter word!')


if __name__ == '__main__':

    #DataBaseManager.add_words_to_data_base()
    #DataBaseManager.delete_words_from_data_base()
    main()

