import random


def strength(password):
    if len(password) < 8 or (password.isalpha() or password.isdigit()):
        return "Weak"
    else:
        return "Strong"


def generate_password():
    password = ''
    while len(password) < 8:
        password += str(random.randint(1, 99))
        password += random.choice('abcdefghijklmnopqrstuvwxyz')
    return password


def main():
    password = input("Enter a password: ")
    print(strength(password))

    if strength(password) == 'Weak':
        response = input("your password is too weak, want me to make a good one for you? (yes/no): ")

        if response.lower() == 'yes':
            print(generate_password())
            print('Just remember to save it somewhere safe!')

        else:
            print('Try again!')

    else:
        print("Ayee your password is strong! Good job!")


if __name__ == '__main__':
    main()
