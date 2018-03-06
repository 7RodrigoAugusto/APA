from random import randint


def makeArray(n):
	array = []
	for i in range(0,n):
		array.append(randint(0,100))
		
	return array
	

def selectionSort(a,n):
	for j in range(0,n-1):
		min = j
		i  = j +1
		for i in range(j,n):
			if a[i]<a[min]:
				min = i
		if min != j:
			aux = a[j]
			a[j] = a[min]
			a[min] = aux
			
	return a
		

def main():
	print('Selection Sort Program \n')
	tamanho = int(input('Tamanho do array \n'))
	array = makeArray(tamanho)
	print(array)
	array = selectionSort(array,tamanho)
	print(array)
	
main()
