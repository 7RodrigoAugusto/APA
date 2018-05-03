# Realização da leitura do arquivo
def abreArquivo():
	txt = open('instancias_mochila/mochila1000.txt','r').readlines()
	array = []
	i = 0
	for item in txt:
		if i == 0: #Num de objetos e Capacidade da mochila
			vetor = item.split(' ')
			num_objs = int(vetor[0])
			capacidade = int(vetor[1])
			i = i + 1
			pass
		else:
			array.append(item.strip('\n').split(' '))	#Removo o \n de cada elemento do array
	
	return array,num_objs,capacidade
	
# Algoritmo de ordenação	
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
	array, num_objs, capacidade = abreArquivo()
	
	print("A capacidade da mochila é de:",capacidade)
	
	array_peso = []
	array_valor = []
	array_correlacao = []
	for i in array:
		array_correlacao.append(int(i[1])/int(i[0]))
		array_peso.append(int(i[0]))
		array_valor.append(int(i[1]))
	
	#print("Vetor de pesos", array_peso)
	#print("Vetor de valores", array_valor)
	
	array_correlacao_original = []
	for i in array_correlacao:
		array_correlacao_original.append(i)
	
	
	array_correlacao = insertionSort(array_correlacao,len(array_correlacao))
	array_correlacao = list(reversed(array_correlacao))
	
	#print("Array correlação (valor/peso) original", array_correlacao_original)
	#print("Array correlacao (valor/peso) ordenado",array_correlacao)
	
	
	
	#Variáveis auxiliar
	
	soma_peso = 0
	soma_aux = 0
	mochila_valor = []
	mochila_peso = []
	mochila_produto = []
	
	# Enquanto soma_peso < capacidade:
	for item in array_correlacao:
		# Encontro o peso do elemento no array ordenado.
		for i in range(0,len(array_correlacao_original)):
			if array_correlacao_original[i] == item:
				mochila_valor.append(array_valor[i])
				mochila_peso.append(array_peso[i])
				soma_aux = soma_peso
				soma_peso = soma_peso + array_peso[i]
				
				if soma_peso > capacidade: # Se a soma dos pesos ultrapassou a capacidade, eu volto para o último valor da soma antes do estouro
					soma_peso = soma_aux
					mochila_valor = mochila_valor[:-1]
					mochila_peso = mochila_peso[:-1]
				break
	
	
	print("Valor dos produtos que entram na mochila:", mochila_valor)
	print("Peso dos produtos que entram na mochila:", mochila_peso)
	
	
	print("A soma dos valores desse produto é de:",sum(mochila_valor))
	print("O peso final inserido na mochila é de:",soma_peso)
	
	return 0
	
main()
