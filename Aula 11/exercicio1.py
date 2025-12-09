# primeiroNome= input("Digite o nome: ")
# segundoNome= input("Digite o segundo nome: ")

# nomeFormatado = f"{segundoNome}{primeiroNome}"
# print(nomeFormatado)

#EX 2:

# texto = "Python é interessante"
# palavras = texto.split()
# textoinvertido = " ".join(palavras[::-1])
                        
# print(textoinvertido)

texto1= "arara"
texto2= "ovo"

texto1_format = texto1.lower().replace(" ","")
texto2_format = texto2.lower().replace(" ","")

palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)
