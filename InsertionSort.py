#Funcao para abertura do arquivo
def abreArquivo():
	txt = open('instancias-numericas/couting.txt','r').readlines()
	array = []
	for item in txt:
		array.append(int(item.strip('\n')))	#Removo o \n de cada elemento do array
		
	return array

def insertionSort(A,n):
	i = 1
	while i < n:
		j = i
		while j>0 and A[j-1]>A[j]:
			aux = A[j]
			A[j] = A[j-1]
			A[j-1] = aux
			j = j - 1
		i = i + 1
		
	return A
		

def main():
	print('Insertion Sort Program \n')
	array = abreArquivo()
	tamanho = len(array)
	print("Array desordenado: \n")
	print(array,'\n')
	array = insertionSort(array,tamanho)
	print("Array ordenado: \n")
	print(array,'\n')
	
main()

