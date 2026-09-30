def save_text(text):

    file = open("corrected_text.txt", "a")
    file.write(text)
    file.write("\n")
    file.close()

    print("Text has been saved.")


def view_saved_text():

    try:
        file = open("corrected_text.txt", "r")
        text = file.read()
        file.close()

        if text == "":
            print("The file is empty.")
        else:
            print("Saved text:")
            print(text)

    except FileNotFoundError:
        print("The file does not exist.")


def clear_saved_text():

    choice = input("Type yes to clear the file: ")

    if choice == "yes":
        file = open("corrected_text.txt", "w")
        file.write("")
        file.close()
        print("The file is now empty.")
    else:
        print("Nothing changed.")
