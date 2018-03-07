#Funcao para abertura do arquivo
def abreArquivo():
	txt = open('instancias-numericas/couting.txt','r').readlines()
	array = []
	for item in txt:
		array.append(int(item.strip('\n')))	#Removo o \n de cada elemento do array
		
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
	array = abreArquivo()
	tamanho = len(array)
	print("Array desordenado: \n")
	print(array,'\n')
	array = selectionSort(array,tamanho)
	print("Array ordenado: \n")
	print(array,'\n')
	
main()
