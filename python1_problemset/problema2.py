

seq = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"


if "ATG" in seq: # verifica se determinada sequencia está contida na sequencia principa
    print(True) #retorna verdadeiro se sim
else:
    print(False) #retorna falso se não

#teste do número positivo e negativo

valor = int(input("Digite um número: "))

if valor < 0:
    print("Negativo")
elif valor > 0 :
    print("Positivo")
    if valor < 50:
        print("Valor menor que 50")
    elif valor > 50:
        print("Valor maior que 50")
        if valor % 3 == 0:
            print("Divisível por 3")
else:
    print(0)

ano = int(input("Digite um ano para verificar se ele é bissexto: "))

if ano % 4 == 0 and ano % 100 != 0:
    print("Bissexto")
elif ano % 400 == 0:
    print("Bissexto")
else:
    print("Não é bissexto")