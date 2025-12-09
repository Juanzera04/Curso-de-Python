# 1 - Função para imprimir uma mensagem

def welcome():
    print("Bem vindo ao sistema de filmes!")

for i in range(10):
    welcome()

# 2 - Calcular a média de notas
def calculate_avarege():
    num_ratings = int(input("Digite quantas avaliações deseja fazer por filme:\n"))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota do filme:\n"))
        total += note

    if num_ratings > 0:
        avarage = total / num_ratings
    else:
        avarage = 0

    return  avarage

print(f"A média de avaliação desse filme é: {calculate_avarege():.2f}")

# 3 - Função para cadastrar um filme:

def create_movie():
    name = input("Digite o nome do filme: \n")
    yearLaunch = input("Digite o ano de lançamento: \n")
    rating = float(input("Digite a nota do filme: \n"))
    moviePrice = float(input("Digite o preço do filme:\n"))

    print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f}")

create_movie()
create_movie()

