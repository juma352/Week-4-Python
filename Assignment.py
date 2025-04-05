def read_file(filename):
    """Reads content from a file with error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

def write_file(filename, content):
    """Writes content to a file with error handling."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{filename}'.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

def modify_content(content):
    """Modifies the file content (example: convert to uppercase)."""
    return content.upper()

def main():
    print("File Read & Write Program")
    input_filename = input("Enter the name of the file to read: ")
    
    content = read_file(input_filename)
    if content is None:
        return
    
    modified_content = modify_content(content)
    print("\nModified content:")
    print(modified_content)
    
    output_filename = input("\nEnter the name of the file to save the modified content: ")
    if write_file(output_filename, modified_content):
        print(f"\nSuccessfully wrote modified content to '{output_filename}'")

if __name__ == "__main__":
    main()
