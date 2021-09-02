text_file = "test.txt"
def read_file(text_file):

    try:
        with open(text_file,"r") as handle:
            data = handle.read()
            return data

    except FileNotFoundError:
        return None        