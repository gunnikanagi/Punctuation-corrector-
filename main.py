from punctuation import fix_punctuation, remove_extra_marks, add_full_stop
from text_check import capitalize_text, count_punctuation, check_text
from file_handler import save_text, view_saved_text, clear_saved_text

print("=================================")
print("     PUNCTUATION CORRECTOR")
print("=================================")

while True:

    print("\nChoose an option:")
    print("1. Correct Text")
    print("2. Check Text")
    print("3. Count Punctuation")
    print("4. Save Corrected Text")
    print("5. View Saved Text")
    print("6. Clear Saved Text")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        text = input("\nEnter your text: ")

        text = fix_punctuation(text)
        text = remove_extra_marks(text)
        text = capitalize_text(text)
        text = add_full_stop(text)

        print("\nCorrected Text:")
        print(text)

    elif choice == "2":

        text = input("\nEnter your text: ")

        print(check_text(text))

    elif choice == "3":

        text = input("\nEnter your text: ")

        total = count_punctuation(text)

        print("Total punctuation marks:", total)

    elif choice == "4":

        text = input("\nEnter your text: ")

        text = fix_punctuation(text)
        text = remove_extra_marks(text)
        text = capitalize_text(text)
        text = add_full_stop(text)

        save_text(text)

    elif choice == "5":

        view_saved_text()

    elif choice == "6":

        clear_saved_text()

    elif choice == "7":

        print("Thank you for using the program.")
        break

    else:

        print("Please enter a number between 1 and 7.")
