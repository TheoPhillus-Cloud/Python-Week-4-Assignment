def file_read_write():
    # Step 1: Prompt user for the filename
    input_file = input("Enter the filename to read from: ")

    try:
        # Step 2: Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
            print("Original content:\n", content)
        
        # Step 3: Modify the content (Example: Add a prefix to each line)
        modified_content = "Modified Content:\n" + content.replace('old', 'new')  # Replace 'old' with 'new'

        # Step 4: Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Modified content written to: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename and try again.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
file_read_write()