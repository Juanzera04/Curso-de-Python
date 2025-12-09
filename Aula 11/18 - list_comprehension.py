# # 1 - LIstando valores de 0 a 10 que sejam menores que 4

# listNums = [i for i in range (10) if i < 5]
# print(listNums)



# # 2 - Filmes que possuem a letra 'e' no título

# moviesWithE = [movie for movie in moviesList if 'u' in movie.lower()]
# print(moviesWithE)

# # 3 - Filmes que eu assisti

# moviesWatched = [movie for movie in moviesList if movie != "Jurassic Park"]
# print(moviesWatched)

moviesList = ["Titanic","The Park","Inception","Jurassic Park"]
# 4 - encontrando um filme pelo nome
while True:
    searchName = input("Digite o nome do filme para consultar na lista (ou 'sair' para encerrar)\n")
    if searchName.lower() == "sair":
        print("Programa encerrado, até logo!")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado com o nome: {searchName}:\n")
        for foundMovie in foundMovies:
            print(f"{foundMovie}\n")
    else:
        print(f"Nenhum filme foi encontrado com o nome '{searchName}\n'")