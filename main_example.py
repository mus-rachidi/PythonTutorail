# Main Example
print("top main_example")
def main():
    print("This is the main function.")

if __name__ == "__main__":
    print("This script is being run directly.")
    print("Executing main function...")
    main()
    print("Main function executed.")
else:
    print("This script is being imported as a module.")
