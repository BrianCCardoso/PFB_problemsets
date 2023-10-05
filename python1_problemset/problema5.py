import sys

fav_things = {"book":"Jitterbug Perfume","song":"Tom Petty - I wont Back Down","tree":"Cedar","organism":"dog"}


print(fav_things["book"])

fav_thing = "book"

print(fav_things[fav_thing])
print(fav_things["tree"])
print(fav_things["organism"])

for x,key in enumerate(fav_things):
    print(x,key,sep="\t")

selecao = input("Digite a chave que voce deseja consultar no dicionario: ")

print(f"A sua chave é {selecao} e o valor dela é {fav_things[selecao]}")

arg1 = input("Digite o nome da sua chave: ")
arg2 = input("Digite o valor da sua chave")

fav_things[arg1] = arg2

for i, chave in enumerate(fav_things):
    print(i, chave, fav_things[chave],sep="\t")