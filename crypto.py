from itertools import cycle
import base64

def main():
    while True:

        choice = input("Do you want to encrypt(1) or decrypt(2) a message?")

        if choice == "1":
            msg = input("Type your message here: ")
            psw = input("Type your password here: ")
            crypto = ""
            for x, y in zip(msg, cycle(psw)):
                a = ord(x)
                b = ord(y)
                c = a ^ b
                crypto += chr(c)
            crypto = crypto.encode()
            crypto = base64.b64encode(crypto)
            print("Here is your encrypted message:")
            crypto = str(crypto)
            crypto = crypto[2:-1]
            print(crypto)
            answer = input("Restart? (y/n): ")


        if choice == "2":
            msg = input("Type your encrypted message here: ")
            psw = input("Type your password here: ")
            msg = msg.encode()
            msg = base64.b64decode(msg)
            msg = msg.decode()
            clear = ""
            for x, y in zip(msg, cycle(psw)):
                a = ord(x)
                b = ord(y)
                c = a ^ b
                clear += chr(c)
            print("Here is your decrypted message:")
            print(clear)
            answer = input("Restart? (y/n): ")

        if answer.lower() == "n":
            print("Good bye!")
            break


if __name__ == '__main__':
    main()