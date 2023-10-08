#using argparse(friendly commmand line interface)
def hello(name , language):
    greetings = {
        'English' : 'Hello',
        'Spanish' : 'Hola',
        'German' : 'Hallo'
    }

    msg = f'{greetings[language]} {name.capitalize()}!'
    print(msg)


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        prog='Age',
        description='Displays the age of a person..'
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, 
        help='helps get the age of a person'
    )
    parser.add_argument(
        '-l', '--lang', metavar='lang',choices=['English', 'Spanish', 'German'], 
        required=True , help='gets the name of the language...'
    )

    arg = parser.parse_args()

    hello(arg.name , arg.lang)