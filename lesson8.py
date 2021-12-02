
if __name__ == '__main__':
    print('tack1:')
    movie = input('Enter movie: ')
    def favourite_movie(string):
        print(f'My favourite movie: {string}')
    favourite_movie(movie)

    print('tack2:')
    def make_country(key, value):
        new_dict = {}
        new_dict.update({key: value})
        return new_dict

    num = int(input("How many countries? "))
    question = 'Enter country:'
    _question = 'Enter capital:'
    dict_country = {}
    i = 0
    while i < num:
        enter = str(input(question))
        if enter:
            sec_enter = str(input(_question))
        else:
            print('err')
            break
        if sec_enter:
            dict_country.update(make_country(enter, sec_enter))
        else:
            print('err')
            break
        i += 1
    print(dict_country)

    print('tack3:')
    operation = input('Enter operation:')


    def make_operation(operation, *args):
        if operation == '+':
            i = 2
            answer = args[0] + args[1]
            while i < len(args):
                answer = answer + args[i]
                i += 1
        elif operation == '-':
            i = 2
            answer = args[0] - args[1]
            while i < len(args):
                answer = answer - args[i]
                i += 1
        elif operation == '*':
            i = 2
            answer = args[0] * args[1]
            while i < len(args):
                answer = answer * args[i]
                i += 1
        elif operation == '/':
            i = 2
            answer = args[0] / args[1]
            while i < len(args):
                answer = answer / args[i]
                i += 1
        else:
            print('Operation error')
        return answer
    print(make_operation(operation, 2, 5, 2, 6))


