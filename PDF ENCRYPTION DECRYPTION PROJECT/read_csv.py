import csv

class ExploreDatabase:

    def __init__(self):
        self.exampleFile = None
        self.exampleReader = None
        self.exampleData = None

    def open_csv_file(self): 
        self.exampleFile = open('data.csv')

    def create_reader_object(self):
        self.exampleReader = csv.reader(self.exampleFile)

    def convert_object_to_list(self):
        self.exampleData = list(self.exampleReader)

    def get_original_text(self):
        original_text = self.exampleData[1][0]
        print(original_text)

    def get_translated_text(self):
        translated_text = self.exampleData[1][1]
        print(translated_text)
    
    def run(self):
        self.open_csv_file()
        self.create_reader_object()
        self.convert_object_to_list()
        self.get_original_text()
        self.get_translated_text()

if __name__ == '__main__':
    explore = ExploreDatabase()
    explore.run()

