import PyPDF2
import csv

class DecryptPDF:

    def __init__(self):
        self.pdfReader = None
        self.exampleFile = None
        self.exampleReader = None
        self.ExampleData = None
        self.original_text = None
        self.key = None
        self.SYMBOLS = None
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

    def get_original_text(self):
        self.original_text = self.exampleData[1][0]
    
    def get_key(self):
        self.key = int(input("Enter the key (an integer): "))

    def symbols_for_decryption(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

    def extract_password(self):
        self.password = ''
        for symbol in self.original_text:
            if symbol in self.SYMBOLS:
                symbolIndex = self.SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + self.key
                if translatedIndex >= len(self.SYMBOLS):
                    translatedIndex = translatedIndex - len(self.SYMBOLS)
                self.password += self.SYMBOLS[translatedIndex]
            else:
                self.password += symbol

    def unlock_pdf(self):
        self.pdfReader.decrypt(f'{self.password}')
        self.pageObj = self.pdfReader.pages[0]

    def get_text_from_PDF(self):
        page_text = self.pageObj.extract_text()
        print(f"\n{page_text}")

    def create_decrypted_file(self):
        with open('decrypted_file1.pdf', 'wb') as decrypted_file:
            writer = PyPDF2.PdfWriter()
            writer.add_page(self.pageObj)
            writer.write(decrypted_file)

        print("\n\t---DECRYPTED FILE CREATED---")
    
    def run(self):
        self.open_reader()
        self.open_csv_file()
        self.create_reader_object()
        self.convert_object_to_list()
        self.get_original_text()
        self.get_key()
        self.symbols_for_decryption()
        self.extract_password()
        self.unlock_pdf()
        self.get_text_from_PDF()
        self.create_decrypted_file()

if __name__ == '__main__':
    decrypt = DecryptPDF()
    decrypt.run()