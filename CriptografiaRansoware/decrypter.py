import os
import pyaes        ## biblioteca de criptografia

## abrir o arquivo criptografado
file_name = "infos.txt.ransomwaretroll"       ## nome do alvo
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"           ## é a mesma chave usada para criptografar, agora usei para descriptografar
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "infos.txt"                  ## nome do file descriptografado
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
