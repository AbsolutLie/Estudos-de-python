#Este programa calcula o produto interno de dois vetores dados

print("Diga a dimensão do espaço vetorial")
dimension = int(input())

info_1 = "Informe a coordenada {i} do vetor 1"
info_2 = "Informe a coordenada {j} do vetor 2"

vetor_1 = []
vetor_2 = []

for i in range(1,dimension+1):
    print(info_1.format(i = i))
    x = float(input(">"))
    vetor_1.append(x)

for j in range(1,dimension+1):
    print(info_2.format(j = j))
    y = float(input(">"))
    vetor_2.append(y)

inner_product = float()
for i in range(0,dimension):
    inner_product = inner_product + vetor_1[i]*vetor_2[i]

print(inner_product)



