import os
from cryptography.fernet import Fernet

# *Encontrar archivos en el directorio actual

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == ".gitignore":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)