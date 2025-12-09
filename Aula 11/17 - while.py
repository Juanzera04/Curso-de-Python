moviesList = ["Titanic","The Godfather","Inception","Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando o while
index = 0

while index < len(moviesList):
    print(moviesList[index])
    index +=1

# 2 - Quando a condiçãõ for atendida o loop será encerrado (Break)index = 0

index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(moviesList[index])
    index +=1

# 3 - Quando a condição for atendida o loop vai pra próxima condição 

index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1
        continue
    print(moviesList[index])
    index +=1

# 4 - Avaliação do curso com o WHILE

movieName = input("Digite o nome do filme:\n")
moveiRating = int(input("Digite quantas avaliações deseja fazer\n"))
total = 0
count = 0

while count < moveiRating:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if moveiRating > 0:
    avarage = total / moveiRating
else:
    avarage = 0

print(f"A média de avaliação do filme {movieName}, é: {avarage:.2f}")

