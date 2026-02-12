def cifrar(texto, deslocamento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        
        # Criptografar letras maiúsculas
        if char.isupper():
            resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
        # Criptografar letras minúsculas
        elif char.islower():
            resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
        else:
            resultado += char  # Mantém espaços e símbolos
            
    return resultado

# Testando o código
mensagem = input("Digite a mensagem: ")
chave = int(input("Digite o valor do deslocamento (ex: 3): "))

print("Mensagem Criptografada:", cifrar(mensagem, chave))