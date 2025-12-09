# 1 - Função para imprimir um nome completo
def full_name(firstName, lastName):
    print(f"o nome é: {firstName} {lastName}")

full_name("Juan", "Rodrigues")
full_name("Moisés", "Rodrigues")

# 2 - Função para somar dois números
def sum_nums(a,b):
    return a + b

print(f"O resultado da soma é {sum_nums(10,5)}")

# 3 - Função com parâmetro default
def address(country = "Brasil"):
    print(f"Eu moro em: {country}")

address()
address("Portugal")

# 4 - Função para avaliar o filme
def rate_movie(num_ratings, movieName):
    total = 0
    for i in range (num_ratings):
        note = float(input("Digite a nota do filme:\n"))
        total += note

    if num_ratings > 0:
        avarage = total / num_ratings
    else:
        avarage = 0

    print(f"A média de avaliação do filme '{movieName}' foi: {avarage:.2f}")

rate_movie(2, "Jurassic Park")