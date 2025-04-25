def main():
    try:
        user_input = input("Enter text to write to the file: ")
        with open("output.txt", "w") as file:
            file.write(user_input + "\n")

        append_input = input("Enter additional text to append: ")
        with open("output.txt", "a") as file:
            file.write(append_input + "\n")

        print("\nFinal file content:")
        with open("output.txt", "r") as file:
            print(file.read())
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
main()

"""
#BONUS
import os

def run_main(filename):
    try:
        # Check file status first
        file_has_content = check(filename)

        # Get user input
        user_input = input("Enter text to write to the file: ")
        append_input = input("Enter additional text to append: ")

        # Write initial content
        with open(filename, "a" if file_has_content else "w") as file:
            if file_has_content:
                file.write(f"\n{user_input}")
            else:
                file.write(f"{user_input}")

        # Append additional content
        with open(filename, "a") as file:
            file.write(f"\n{append_input}")

        # Display results
        if file_has_content: print(f"\nContent Added:\n{user_input}\n{append_input}")
        print("\nFinal file content:")
        with open(filename, "r") as file:
            print(file.read())

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def check(filename):
    try:
        if not os.path.exists(filename):
            return False

        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    consent = input(f"The file {filename} has existing content. Continue? (y/N) ").strip().lower()
                    if consent == "n":
                        print("Exiting...")
                        exit(0)
                    elif consent == "y":
                        return True
                    else:
                        print("Invalid option! Exiting...")
                        exit(0)
            return False

    except FileNotFoundError:
        print("File not found!")
        return False
    except PermissionError:
        print("Permission denied!")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


filename = input("Enter the name of the file (with extension): ").strip()
run_main(filename)
"""