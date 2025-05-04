import time

def buscaBinaria(sequencia, valor):
    inicio = comp = 0
    fim = len(sequencia) - 1

    while(inicio <= fim):
        comp += 1
        meio = (inicio + fim) // 2
        print("Procurando na posição: ", meio)
        time.sleep(0.4)
        valorMeio = sequencia[meio]
        print("Valor encontrado: ", valorMeio)
        time.sleep(0.4)
        if valorMeio == valor:
            print("\nDepois de ", comp," Comparações")
            return meio
        elif valorMeio > valor:
            fim = meio - 1

        else:
            inicio = meio + 1

    return None

tamanho = int(input("Qual o tamanho da sequencia?: "))
sequencia = [(i + 1) * 3 for i in range(tamanho)]
print("Números:", ' '.join(map(str, sequencia)))
valor = int(input("Escolha um valor: "))

print("O seu valor foi encontrado na posição: ",buscaBinaria(sequencia, valor))