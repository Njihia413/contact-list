import unittest
import readFiles

class TestReadFiles(unittest.TestCase):
    #Test to see if data is being fetched from the text file
    def test_get_data(self):
        with open("test.txt","r") as handle:
            data = handle.read()
            self.assertEqual(data,readFiles.read_file("test.txt"))

    #Test to see if an exception is raised when a wrong file is inputted    
    def test_nonfile(self):
        self.assertEqual(None,readFiles.read_file("tests.txt"))        

if __name__ == "__main__":
    unittest.main()
