#Funcao para abertura do arquivo
def abreArquivo():
	txt = open('instancias-numericas/simples.txt','r').readlines()
	array = []
	for item in txt:
		array.append(int(item.strip('\n')))	#Removo o \n de cada elemento do array
		
	return array

def heapify(arr, n, i):
    maior = i  
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 

    if l < n and arr[i] < arr[l]:
        maior = l
 
   
    if r < n and arr[maior] < arr[r]:
        maior = r
 
    
    if maior != i:
        arr[i],arr[maior] = arr[maior],arr[i]  
 
        heapify(arr, n, maior)
 

def heapSort(arr):
    n = len(arr)
 
    
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
   
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)	
    
    return arr
	
	
def main():
	print('Quicksort Program \n')
	array = abreArquivo()
	print("Array desordenado: \n")
	print(array,'\n')
	array = heapSort(array)
	print("Array ordenado: \n")
	print(array,'\n')
	return
	
main()
