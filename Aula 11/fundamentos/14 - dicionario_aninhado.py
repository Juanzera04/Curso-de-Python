escalcoes = {
    "Palmeiras":["Weverton","Giay","Gomez","Fuchs","Piquerez","Emi Martinez","Andreas Pereira","Felipe Anderson","Maurício","Flaco Lopez","Vitor Roque"],
    "Flamengo":["Rossi","Varela","Léo Ortiz","Léo Pereira","Alex Sandro","Pulgar","Jorginho","Arrascaeta","Carrascal","Samuel Lino","Pedro"]
}

opçoes = {
    1:"Palmeiras",
    2:"Flamengo"
}

escolha = int(input(f"Diga qual time deseja saber a escalação, essas são as opções:\n 1: {opçoes[1]}\n 2: {opçoes[2]}\n"))
timeSelecionado = opçoes[escolha]
print(f"\nA escalação do {timeSelecionado} é a seguinte:\n")

for escalaçao in escalcoes[timeSelecionado]:
    print(escalaçao)

