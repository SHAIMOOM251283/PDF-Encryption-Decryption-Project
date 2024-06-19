import pandas as pd

class CreateDatabase:

    def __init__(self):
        self.original_text = None
        self.key = None
        self.SYMBOLS = None
        self.translated = None
        self.dt = None

    def get_original_text(self):
        self.original_text = input('Enter Text: ')

    def get_key(self):
        self.key = int(input("Enter the key (an integer): "))

    def symbols_for_encryption(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

    def encrypt(self):
        self.translated = ''
        for symbol in self.original_text:
            if symbol in self.SYMBOLS:
                symbolIndex = self.SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + self.key
                if translatedIndex >= len(self.SYMBOLS):
                    translatedIndex = translatedIndex - len(self.SYMBOLS)
                self.translated += self.SYMBOLS[translatedIndex]
            else:
                self.translated += symbol

        print(self.translated)

    def create_data_frame(self):
        self.df = pd.DataFrame({
            'Original Text': [self.original_text],
            'Translated Text': [self.translated]
        })

    def save_to_csv_file(self):
        self.df.to_csv('data.csv', index=False)

        print("CSV file 'data.csv' created successfully.")
    
    def run(self):
        self.get_original_text()
        self.get_key()
        self.symbols_for_encryption()
        self.encrypt()
        self.create_data_frame()
        self.save_to_csv_file()

if __name__ == '__main__':
    encrypt = CreateDatabase()
    encrypt.run()