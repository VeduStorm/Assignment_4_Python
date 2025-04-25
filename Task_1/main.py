def main():
    try:
        with open("sample.txt", "r") as file:
            print("Contents of 'sample.txt':\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("!!ERROR The file 'sample.txt' does not exist or it is in a different folder!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()


"""
#BONUS
def main():
    try:
        a = str(input("Enter the file name (with extension): "))
        with open(a, "r") as file:
            print("Contents of 'sample.txt':\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"!!ERROR The file {a} does not exist or it is in a different folder!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
"""