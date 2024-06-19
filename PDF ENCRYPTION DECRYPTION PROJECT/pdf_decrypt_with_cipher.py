import PyPDF2
from PyPDF2.errors import FileNotDecryptedError

class DecryptPDF:

    def __init__(self):
        self.pdfReader = None
        self.original_text = None
        self.key = None
        self.SYMBOLS = None
        self.password = None
        self.pageObj = None
    
    def reader(self):
        self.pdfReader = PyPDF2.PdfReader(open('encrypted_file2.pdf', 'rb'))

    def get_original_text(self):
        self.original_text = input("Enter Text for Password: ")

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
        while True:
            try:
                self.reader()
                self.get_original_text()
                self.get_key()
                self.symbols_for_decryption()
                self.extract_password()
                self.pdfReader.decrypt(f'{self.password}')
                self.pageObj = self.pdfReader.pages[0]
                break
            except FileNotDecryptedError:
                print("\nFile not decrypted. Please try again.")
    
    def get_text_from_PDF(self):
        page_text = self.pageObj.extract_text()
        print(f"\n{page_text}")
    
    def create_decrypted_file(self):
        with open('decrypted_file3.pdf', 'wb') as decrypted_file:
            writer = PyPDF2.PdfWriter()
            writer.add_page(self.pageObj)
            writer.write(decrypted_file)

        print("\n\t---DECRYPTED FILE CREATED---")
    
    def run(self):
        self.unlock_pdf()
        self.get_text_from_PDF()
        self.create_decrypted_file()

if __name__ == '__main__':
    decrypt = DecryptPDF()
    decrypt.run()