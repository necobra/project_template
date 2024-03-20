from app.io.input import input_text_from_console, read_text_from_file, read_text_from_file_pandas
from app.io.output import output_text_to_console, write_text_to_file


def main():
    text_console = input_text_from_console()
    output_text_to_console(text_console)
    write_text_to_file(text_console, "output_console.txt")

    text_file = read_text_from_file("input.txt")
    output_text_to_console(text_file)
    write_text_to_file(text_file, "output_file.txt")

    text_pandas = read_text_from_file_pandas("input.csv")
    output_text_to_console(text_pandas)
    write_text_to_file(text_pandas, "output_pandas.txt")
    return


if __name__ == '__main__':
    main()
