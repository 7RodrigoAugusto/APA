#Funcao para abertura do arquivo
def abreArquivo():
	txt = open('instancias-numericas/couting.txt','r').readlines()
	array = []
	for item in txt:
		array.append(int(item.strip('\n')))	#Removo o \n de cada elemento do array
		
	return array
	
def merge(arrayE,arrayD):
	final = []
	
	while arrayE or arrayD:
		if len(arrayE) and len(arrayD):
			if arrayE[0]<arrayD[0]:
				final.append(arrayE.pop(0))
			else:
				final.append(arrayD.pop(0))
				
		if not len(arrayE):
			if len(arrayD):
				final.append(arrayD.pop(0))
		if not len(arrayD):
			if len(arrayE):
				final.append(arrayE.pop(0))
	return final
	
	
def mergeSort(array):
	tamanho = len(array)
	if tamanho <2: 
		return array
	mid = tamanho/2
	arrayE = []
	arrayD = []
	for i in range(0,int(mid)):
		arrayE.append(array[i])
	for j in range(int(mid), tamanho):
		arrayD.append(array[j])
	
	array = merge(mergeSort(arrayE),mergeSort(arrayD))
	
	return	array
	
	
	
def main():
	print('Merge Sort Program \n')
	array = abreArquivo()
	tamanho = len(array)
	print("Array desordenado: \n")
	print(array,'\n')
	array = mergeSort(array)
	print("Array ordenado: \n")
	print(array,'\n')
	
	return

main()
