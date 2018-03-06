from random import randint


def makeArray(n):
	array = []
	for i in range(0,n):
		array.append(randint(0,100))
		
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
	tamanho = int(input('Tamanho do array \n'))
	array = makeArray(tamanho)
	print(array)
	array = insertionSort(array,tamanho)
	print(array)
	
main()

