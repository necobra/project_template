import os
import pandas as pd


def input_text_from_console():
    """
    Function to input text from the console.

    Returns:
        str: text from the console.
    """
    return input("Enter text: ")

def read_text_from_file(filename):
    """
    Function to read text from a file.

    Args:
        filename (str): The name of the file to read from.
    Returns:
        str: text from the file.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        print(f"File '{filename}' does not exist.")
        return None

def read_text_from_file_pandas(filename):
    """
    Function to read text from a csv file using pandas.

    Args:
        filename (str): The name of the csv file to read from.
    Returns:
        str: text from the file.
    """
    if os.path.exists(filename):
        data = pd.read_csv(filename)
        return data.to_string(index=False)
    else:
        print(f"File '{filename}' does not exist.")
        return None
