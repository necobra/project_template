from app.io.input import read_text_from_file, read_text_from_file_pandas

class TestInputFunctions:
    def test_read_text_from_file(self):
        expected_result = 'My text'
        actual_result = read_text_from_file('test.txt')
        assert expected_result == actual_result

    def test_read_text_from_file_nonexistent(self):
        expected_result = None
        actual_result = read_text_from_file('test_nonexistent.txt')
        assert expected_result == actual_result

    def test_read_text_from_file_one_empty_line(self):
        expected_result = 'My text\n\nEnd'
        actual_result = read_text_from_file('test2.txt')
        assert expected_result == actual_result

    def test_read_text_from_file_pandas(self):
        expected_result = 'My text'
        actual_result = read_text_from_file_pandas('test.csv')
        assert expected_result == actual_result

    def test_read_text_from_file_pandas_nonexistent(self):
        expected_result = None
        actual_result = read_text_from_file_pandas('test_nonexistent.csv')
        assert expected_result == actual_result

    def test_read_text_from_file_pandas_one_empty_line(self):
        expected_result = 'My text\\n\\nEnd'
        actual_result = read_text_from_file_pandas('test2.csv')
        assert expected_result == actual_result
