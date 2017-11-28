try:
    open("does not exist.txt")
except ZeroDivisionError:
    print("sorry not sorry")
except FileNotFoundError as e:
    print(e.filename, "is not a file breh")