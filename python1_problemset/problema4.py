#exercicio 1 

lista_fav = ["futebol", "praia", "cerveja", "games", "coding"]

print(lista_fav)
print(lista_fav[2])

lista_fav[2] = "Evidencias"

lista_fav.append("oi")
lista_fav.insert(0,"oi")

lista_fav.insert(2,"oi")

print(lista_fav)

lista_fav.pop()
lista_fav.pop(0)
lista_fav.pop(2)

print(lista_fav)

frase = ", ".join(lista_fav) #o comando join cria uma string separando os itens com o argumento
print(frase)

#exercicio 2

taxa = "sapiens,erectus,neanderthalensis"

print(taxa)
print(taxa[1])
print(type(taxa))

print(taxa.split(","))

species = taxa.split(",")
print(species)
print(species[1])
print(type(species))

species.sort()
print(species)
species.sort(key=len, reverse=True)
print(species)

#exercicio 3
my_list = ["a", "b", "c"]
list_copy = my_list
list_copy.append("d")
print(my_list)

my_list2 = ["a", "b", "c"]
list_copy2 = my_list2.copy()
list_copy2.append("d")
print(my_list2)

#exercicio 4
a = 1
while a<=100:
    print(a)
    a+=1

#exercicio 5

a = 1
fatorial = 1
while a<=1000:

    fatorial = fatorial * a
    a+=1

print(fatorial)

#exercicio 6

list_ex6 = [101,2,15,22,95,33,2,27,72,15,52]
for i in list_ex6:
    if i % 2 == 0:
     print(i)   

#exercicio 7

soma_par = 0
somar_impar = 0
list_ex6.sort()
for i in list_ex6:
    print(i)
    if i % 2 == 0:
      soma_par+=i
    else:
      somar_impar+=i
print(f"Sum of even numbers = {soma_par} \nSum of odds = {somar_impar}")

#exercicio 8

for i in range(1,101):
   print(i)

#exercicio 9

lista_ex9 = [i for i in range(1,101)]
print(lista_ex9)

#exercicio 10

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

for i in range(num_1, num_2 + 1):
   if i % 2 != 0:
    print(i)

#exercicio 11
lista_ex11 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

for i in lista_ex11:
   print(len(i), i, sep="   ")

#exercicio 12

lista_ex12 = [(len(i), i) for i in lista_ex11]
print(lista_ex12)

#exercicio 13

lista_ex11 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

for x, i in enumerate(lista_ex11):
   print(x, len(i), i, sep="   ")

