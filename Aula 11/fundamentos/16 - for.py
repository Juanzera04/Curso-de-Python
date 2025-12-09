moviesList = ["Titanic","The Godfather","Inception","Jurassic Park"]

# 1 - Iterando valores de uma lista

for movie in moviesList:
    print(movie)

# Quando a condição é atendida, o loop é encerrado
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

# quando a condição for atendida, o loop vai para a próixma interação
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

# 4 - Aavliação do filme:
movieName = input("Digite o nome do filme:\n")
moveiRating = int(input("Digite quantas avaliações deseja fazer\n"))

total = 0

for i in range(moveiRating):
    note = float(input("Digite a nota do filme:\n"))
    total += note

if moveiRating > 0:
    avarage = total / moveiRating
else:
    avarage = 0

print(f"A média de avaliação do filme {movieName}, é: {avarage:.2f}")
