class WordCounter:
    def __init__(self, file_path):
        # Store the path as a string (or pathlib.Path) and open it later.
        # `file.path(...)` is not a valid Python call, which caused the NameError.
        self.file = file_path
    #F:\oodveda_intern\Level 1\Word Counter
    # To Read the content of a file
    def read_file(self):
        try:
            with open(self.file, encoding="utf-8") as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    # To Split the content into words and count them
    def count_words(self):
        count = 0
        content = self.read_file()
        if content is not None:
            words = content.split()
            count = len(words)
            return count
        else:
            return 0
if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    word_counter = WordCounter(file_path)
    word_count = word_counter.count_words()
    print(f"The number of words in the file is: {word_count}")
    