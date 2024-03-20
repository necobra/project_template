

def output_text_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): The text to output to the console.
    """
    print(text)

def write_text_to_file(text, filename):
    """
    Function to write text to a file.

    Args:
        text (str): The text to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as file:
        file.write(text)
