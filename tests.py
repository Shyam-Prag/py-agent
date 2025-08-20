from functions.get_files_info import get_files_info
import unittest 

class TestGetFile(unittest.TestCase):
    def test_get_files_info(self):
        result = get_files_info("calculator", ".")
        print("--- Actual Result ---")
        print(result)

        expected_result = """Result for current directory:
- main.py: file_size=564 bytes, is_dir=False
- tests.py: file_size=1330 bytes, is_dir=False
- pkg: file_size=63 bytes, is_dir=True
"""     
        print("--- Expected Result ---")
        print(expected_result)
        assert result == expected_result
    
    def test_get_file_info_pck_directory(self):
        result = get_files_info("calculator","pkg")
        print("--- Actual Result ---")
        print(result)
        

        expected_result = """Result for 'pkg' directory:
- calculator.py: file_size=1738 bytes, is_dir=False
- render.py: file_size=767 bytes, is_dir=False
"""
        print("--- Expected Result ---")
        print(expected_result)
        assert result == expected_result
    
    def test_non_existing_path(self):
        result = get_files_info("calculator", "/bin")
        print("--- Actual Result ---")
        print(result)

        expected_result = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        print("--- Expected Result ---")
        print(expected_result)

        assert result == expected_result
    
    def test_non_permitted_directory(self):
        result = get_files_info("calculator", "../")
        print("--- Actual Result ---")
        print(result)

        expected_result = 'Error: Cannot list "../" as it is outside the permitted working directory'
        print("--- Expected Result ---")
        print(expected_result)

        assert result == expected_result


if __name__ == '__main__':
    unittest.main()
