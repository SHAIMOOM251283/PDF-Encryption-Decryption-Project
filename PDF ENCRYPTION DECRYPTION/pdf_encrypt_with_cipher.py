import PyPDF2

class EncryptPDF:

    def __init__(self):
        self.pdfFile = None
        self.pdfReader = None
        self.pdfWriter = None
        self.original_text = None
        self.key = None
        self.SYMBOLS = None
        self.password = None
    
    def open_file(self):
        self.pdfFile = open('main.pdf', 'rb')
        
    def create_reader_object(self):
        self.pdfReader = PyPDF2.PdfReader(self.pdfFile)
        
    def create_writer_object(self):    
        self.pdfWriter = PyPDF2.PdfWriter()
    
    def copy_pages_to_new_file(self):
        for pageNum in range(len(self.pdfReader.pages)):
            self.pdfWriter.add_page(self.pdfReader.pages[pageNum])

    def get_original_text(self):
        self.original_text = input("Enter Text for Password: ")
    
    def get_key(self):
        self.key = int(input("Enter the key (an integer): "))

    def encryption_symbols(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

    def encrypt(self):
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
        
        print(self.password)
    
    def create_encrypted_file(self):
        self.pdfWriter.encrypt(f'{self.password}')
        resultPdf = open('encrypted_file2.pdf', 'wb')
        self.pdfWriter.write(resultPdf)
        resultPdf.close()
        self.pdfFile.close()

        print("\n\t---ENCRYPTED FILE CREATED---")
    
    def run(self):
        self.open_file()
        self.create_reader_object()
        self.create_writer_object()
        self.copy_pages_to_new_file()
        self.get_original_text()
        self.get_key()
        self.encryption_symbols()
        self.encrypt()
        self.create_encrypted_file()

if __name__ == '__main__':
    encrypt = EncryptPDF()
    encrypt.run()
