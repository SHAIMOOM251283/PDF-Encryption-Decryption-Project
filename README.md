# PDF Encryption/Decryption Project

This project provides a Python implementation for encrypting and decrypting PDF files using passwords generated from user input. The process enhances password protection by transforming user input into a complex password through a substitution cipher.

## Features
•	PDF Encryption: Encrypts an existing PDF file with a password generated from user input.
•	PDF Decryption: Decrypts the encrypted PDF file using the same user input and key to regenerate the password.
•	Enhanced Password Security: Utilizes a substitution cipher to transform the user input, adding complexity and obfuscation to the password.

## How It Works

### Encryption
1.	Complex Password Generation: During encryption, the user provides a text string and a numerical key. The text string is transformed using the key through a substitution cipher, creating a complex and less predictable password. This transformation process increases the complexity of the password, making it harder to guess or crack.
2.	Obfuscation: The transformation involves shifting each character in the input text by the value of the key within a predefined set of symbols (SYMBOLS). This obfuscates the original input, ensuring that even common phrases or words become unique and complex passwords.
3.	Diverse Symbol Set: By including a wide range of characters (upper and lower case letters, digits, and special characters), the resulting password is more diverse. This diversity increases the number of possible combinations, making brute-force attacks less feasible.

### Decryption
4.	Consistent Complexity: The decryption process mirrors the encryption process, using the same user input and key to regenerate the complex password. This ensures that the password complexity added during encryption is retained.
5.	Obfuscation: Just as in the encryption process, the decryption password is obfuscated through character shifting. This means that even if an attacker knows the original text input, they would still need to know the specific key to generate the correct password.
6.	Strength Against Brute Force: The requirement of both the original text and the specific key adds an additional layer of security. Without both pieces of information, an attacker cannot easily brute force the password. This increases the number of potential combinations, making it harder for attackers to guess the password.

## Summary
This project enhances password protection by transforming user input into a more complex and less predictable password. This transformation process involves a substitution cipher that shifts characters based on a user-provided key, adding layers of complexity and obfuscation to the password. By increasing password complexity and utilizing a diverse set of symbols, the project provides robust security for encrypted PDF files.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



