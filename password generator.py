import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    try:
        plen = int(input("Enter password length\n"))       
        if plen <= 0:
                print("Invalid input.")
                plen = 12
    except ValueError:
        print("Invalid input. Using default length (12).")
        plen = 12
#Todo1: Handle Gibberish
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is: ")
    print("".join(random.sample(s, plen)))
    # print("".join(s[0:plen]))

