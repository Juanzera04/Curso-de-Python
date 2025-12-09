filmsList = ["Pinóquio", "Toy Story", "Kung Fu Panda", "Shrek 2"]
abc = ["C","A","B"]

#Método para contar lista
print(len(filmsList))

#Recuperar um item da lista pelo nome   
print(filmsList.index("Shrek 2"))

#Adicionar um item ao final da lista
filmsList.append("O senhor dos anéis")
print(filmsList)

#colocar em ordem alfabética
abc.sort()
print(abc)

#Copia de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pinóquio")
print(filmsCopy)

#remove todos os itens da lista
filmsList.clear()
print(filmsList)

