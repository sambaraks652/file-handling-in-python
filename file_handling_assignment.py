try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Another line here.\n")
    print("File 'my_file.txt' created and written successfully.")
except PermissionError:
    print("Permission denied. Unable to create or write to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("\nContents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1.\n")
        file.write("More content.\n")
        file.write("Yet another line.\n")
    print("\nThree additional lines appended to 'my_file.txt'.")
except PermissionError:
    print("Permission denied. Unable to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.")