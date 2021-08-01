import time

def getNextGap(gap):
 
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return gap
 
# Função para ordenar o array usando CombSort
inicio = time.time()
def combSort(arr):
    n = len(arr)
 
    # Inicializa o gap
    gap = n
 
    # Inicializa como verdadeiro para executar o loop
    swapped = True
 
    while gap !=1 or swapped == 1:
 
        # Procura o próximo gap
        gap = getNextGap(gap)

        # Muda para falso para verificar se a troca aconteceu ou não
        swapped = False
 
        # Compara todos os elementos com a lacuna atual
        for i in range(0, n-int(gap)):
            if arr[i] > arr[i + int(gap)]:
                arr[i], arr[i + int(gap)]=arr[i + int(gap)], arr[i]
                swapped = True
 
fim = time.time()
# Array a ser ordenado
arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 35, 36, 38, 50, 60, 80, 90]
combSort(arr)
 
print ("Array ordenado:")
for i in range(len(arr)):
    print (arr[i]) 

print ("Tempo do algoritmo:", fim,"Segundos")