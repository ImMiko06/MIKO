import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("Salam Alem")

if __name__ == "__main__":
    generate_files()