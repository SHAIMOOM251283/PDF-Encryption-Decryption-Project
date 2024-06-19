import PyPDF2
import csv

class DecryptPDF:

    def __init__(self):
        self.pdfReader = None
        self.exampleFile = None
        self.exampleReader = None
        self.exampleData = None
        self.password = None
        self.pageObj = None

    def open_reader(self):
        self.pdfReader = PyPDF2.PdfReader(open('encrypted_file1.pdf', 'rb'))

    def open_csv_file(self):
        self.exampleFile = open('data.csv')
    
    def create_reader_object(self):
        self.exampleReader = csv.reader(self.exampleFile)

    def convert_object_to_list(self):
        self.exampleData = list(self.exampleReader)
    
    def extract_password(self):
        self.password = self.exampleData[1][1]

    def decrypt(self):
        self.pdfReader.decrypt(f'{self.password}')
        self.pageObj = self.pdfReader.pages[0]
    
    def get_text_from_PDF(self):
        page_text = self.pageObj.extract_text()
        print(f"\n{page_text}")
    
    def create_decrypted_file(self):
        with open('decrypted_file2.pdf', 'wb') as decrypted_file:
            writer = PyPDF2.PdfWriter()
            writer.add_page(self.pageObj)
            writer.write(decrypted_file)

        print("\n\t---DECRYPTED FILE CREATED---")
    
    def run(self):
        self.open_reader()
        self.open_csv_file()
        self.create_reader_object()
        self.convert_object_to_list()
        self.extract_password()
        self.decrypt()
        self.get_text_from_PDF()
        self.create_decrypted_file()

if __name__ == '__main__':
    decrypt = DecryptPDF()
    decrypt.run()