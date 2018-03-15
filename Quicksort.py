
#Funcao para abertura do arquivo
def abreArquivo():
	txt = open('instancias-numericas/simples.txt','r').readlines()
	array = []
	for item in txt:
		array.append(int(item.strip('\n')))	#Removo o \n de cada elemento do array
		
	return array

def pegaLoHi(A,n):
	low =[]
	high = []
	for i in range(0,int(n/2)):
		low.append(A[i])
	
	for j in range(int(n/2),n):
		high.append(A[j])	
	
	return low,high

def introQuickSort(A,tamanho):
	quickSort(A,0,tamanho-1)
	return A

def quickSort(A,primeiro,ultimo):
	if primeiro<ultimo:
		p = partition(A,primeiro,ultimo)
		quickSort(A,primeiro,p-1)
		quickSort(A,p+1,ultimo)
	return


def partition(A,primeiro,ultimo):
	pivot = A[primeiro]	#Coloco o primeiro elemento sempre como pivot
	leftmark = primeiro+1 #A ponta da esquerda eh o primeiro elemento depois do pivot
	rightmark = ultimo	#A ponta da direita como ultimo elemento
	
	done = False

	while not done:
		#Enquanto o valor da esquerda for menor que o da direita e maior que o pivot
		#Incremento a posicao marcada como esquerda
		while leftmark <= rightmark and A[leftmark] <= pivot:
			leftmark = leftmark + 1
		
		#Enquanto o valor da direita for maior que o pivot e maior que o da esquerda
		#Decremento a posicao marcada como direita
		while A[rightmark] >= pivot and rightmark >= leftmark:
			rightmark = rightmark -1
		
		#Assim que a posicao marcada como direita for menor que	a posicao marcada por esquerda
		#Eu paro o meu while principal
		if rightmark <leftmark:
			done = True
			
		else:
			#Enquanto a posicao da direita nao eh menor que a posicao da esquerda
			#Troco os elementos marcados como esquerda e direita
			aux = A[leftmark]
			A[leftmark] = A[rightmark]
			A[rightmark] = aux
	
	#Agora que terminou, o primeiro vira a posicao do marcado como direita, que na verdade 
	#eh o primeiro elemento logo depois do antigo inicio
	aux = A[primeiro]
	A[primeiro] = A[rightmark]
	A[rightmark] = aux
	
	return rightmark


def main():
	print('Quicksort Program \n')
	array = abreArquivo()
	tamanho = len(array)
	print("Array desordenado: \n")
	print(array,'\n')
	array = introQuickSort(array,tamanho)
	print("Array ordenado: \n")
	print(array,'\n')
	return

main()
