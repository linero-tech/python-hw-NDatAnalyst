from to_do import TODO


def task10(password):
    import re

    while True:
        password = input('enter a new password: ')
        result = password
        if (len(password) < 6 or len(password) > 10):
            print('Your password should be between 6-10 characters.')
        elif not re.search("[A-Z]", password):
            print('Your password should include at least one capital letter.')
        elif not re.search('[a-z]', password):
            print('Your password should include at least one lower case letter.')
        elif not re.search('[0-9]', password):
            print('Your password should include at least one number.')
        elif not re.search('[$#@]', password):
            print('Your password should include at least one of these signs: $#@')
        else:
            print('Your password is valid.')
        return result

if __name__ == "__main__":
    print(task10(password=''))