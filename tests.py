from functions.get_files_info import get_files_info
import unittest 

class TestGetFile(unittest.TestCase):
    def test_get_files_info(self):
        result = get_files_info("calculator", ".")
        print("--- Actual Result ---")
        print(result)
        print("--- Expected Result ---")

        expected_result = """Result for current directory:
- main.py: file_size=564 bytes, is_dir=False
- tests.py: file_size=1330 bytes, is_dir=False
- pkg: file_size=63 bytes, is_dir=True
"""
        assert result == expected_result

if __name__ == '__main__':
    unittest.main()
