import main_example
print("import_example.py is being run.")

main_example.main()
# This line won't be executed when the script is imported,
# because the main_example.py script checks if it's being run directly.
