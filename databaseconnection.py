import psycopg2
import psycopg2.extras
import random


class DataBaseManager:

    @staticmethod
    def add_words_to_data_base():
        try:
            connection = psycopg2.connect(
                host='localhost',
                database='Words',
                user='postgres',
                password=''
            )
            try:
                cur = connection.cursor()

                with open('5letterwords.txt', 'r') as words_file:
                    for line in words_file:
                        word = line.strip()

                        postgres_insert_query = (' INSERT INTO words '
                                                 ' VALUES (%s)')

                        record_to_insert = (word,)
                        cur.execute(postgres_insert_query, record_to_insert)

                        connection.commit()

                cur.close()
                connection.close()
            except ConnectionError:
                print('adding error to the postgresql database')

        except ConnectionError:
            print('connection error with the postgresql database(insert)')

    @staticmethod
    def delete_words_from_data_base():
        try:
            connection = psycopg2.connect(
                host='localhost',
                database='Words',
                user='postgres',
                password=''
            )

            postgres_insert_query = 'DELETE FROM words'

            cur = connection.cursor()
            cur.execute(postgres_insert_query)

            connection.commit()

            cur.close()
            connection.close()

        except ConnectionError:
            print('connection error with the postgresql database(delete)')

    @staticmethod
    def select_one_word():

        number = random.randint(1, 5757)

        try:
            connection = psycopg2.connect(
                host='localhost',
                database='Words',
                user='postgres',
                password=''
            )

            postgres_insert_query = 'select * from words order by random() limit 1'

            cur = connection.cursor()
            cur.execute(postgres_insert_query)

            connection.commit()

            results = cur.fetchall()

            for row in results:
                correct_word = row[0]
                return correct_word

            cur.close()
            connection.close()

        except ConnectionError:
            print('connection error with the postgresql database(select word)')



