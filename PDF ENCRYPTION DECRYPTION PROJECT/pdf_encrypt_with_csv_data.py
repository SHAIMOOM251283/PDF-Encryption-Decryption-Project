import PyPDF2
import csv

class EncryptPDF:

    def __init__(self):
        self.pdfFile = None
        self.pdfReader = None
        self.pdfWriter = None
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

    def encrypt(self):
        exampleFile = open('data.csv')
        exampleReader = csv.reader(exampleFile)
        exampleData = list(exampleReader)
        self.password = exampleData[1][1]

    def create_encrypted_file(self):
        self.pdfWriter.encrypt(f'{self.password}')
        resultPdf = open('encrypted_file1.pdf', 'wb')
        self.pdfWriter.write(resultPdf)
        resultPdf.close()
        self.pdfFile.close()

        print("\t---ENCRYPTED FILE CREATED---")
    
    def run(self):
        self.open_file()
        self.create_reader_object()
        self.create_writer_object()
        self.copy_pages_to_new_file()
        self.encrypt()
        self.create_encrypted_file()

if __name__ == '__main__':
    encrypt = EncryptPDF()
    encrypt.run()