#abrearquivo para arquivos que possuem separação por espaço
def abreArquivo_dij_space():
	txt = open('instncias_Dijkstra_Kruskal_e_PRIM/dij10.txt','r').readlines()
	array = []
	i = 0
	for item in txt:
		if i == 0:
			qtd_vertices = int(item)
			i = i + 1
			pass
		else:
			array.append(item.strip('\n').split(' '))	#Removo o \n de cada elemento do array
	
	return array,qtd_vertices

#abreArquivo, para arquivos que possuem separação tabulada
def abreArquivo_dij_tab():
	#txt = open('instncias_Dijkstra_Kruskal_e_PRIM/dij20.txt','r').readlines()
	#txt = open('instncias_Dijkstra_Kruskal_e_PRIM/dij40.txt','r').readlines()
	txt = open('instncias_Dijkstra_Kruskal_e_PRIM/dij50.txt','r').readlines()
	array = []
	i = 0
	for item in txt:
		if i == 0:
			qtd_vertices = int(item)
			i = i + 1
			pass
		else:
			array.append(item.strip('\n').split('\t'))	#Removo o \n de cada elemento do array
	
	return array,qtd_vertices	
	
#Heap Sort
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
 
    
    for i in range(n, -1, -1): #Vai de n até 0, subtraindo de 1 em 1
    	heapify(arr, n, i)
 
   
    for i in range(n-1, 0, -1): #Vai de n-1 até 1, subtraindo de 1 em 1
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)	
    
    return arr
	
#Algoritmo
#Classe aresta
class aresta:
	def __init__(self, a, b, p):
		self.elemento1 = a
		self.elemento2 = b
		self.peso = p	
	

def cria_arestas(elementos_dic,array_aux):
	vetor_aux = []
	for k in range(0, len(elementos_dic)):
		vetor_aux.append([])
		
	for i in elementos_dic:
		for j in range(0,len(elementos_dic)):
			if int(elementos_dic[i][j]) == array_aux[i][1]: # O elemento 1 sempre eh o menor
				vetor_aux[i] = aresta(i,j,array_aux[i][1])
				#print("Para o elemento:", i, ", temos a ligação com", j,"como a menor com valor:", array_aux[i][1])
				
	return vetor_aux


def main():
	
	#Abre arquivo com separação por espaço
	array,qtd_vertices = abreArquivo_dij_space()
	
	#Abre arquivo com separação por tabular
	#array,qtd_vertices = abreArquivo_dij_tab()
	
	
	# ---------- Cria dicinonário com os pesos de cada elemento para cada elemento ----------
	elementos = set()
	#Dicionario com a distancia de cada elemento para todos os outros
	elementos_dic = {} 
	
	 #Vai criando elemento 0, elemento 1, ...
	for i in range(0,qtd_vertices):
		elementos.add(i)
		elementos_dic[i] = []	
	
	aux_j = 0
	aux_i = qtd_vertices-1
	
	#Loop percorrendo todos os elementos iniciais e criando dicionário
	for j in array:
		#Acrescenta o peso zero para quando for a ligação do elemento com ele mesmo
		elementos_dic[aux_j].append(0)
		for i in j:
			#Acrescenta todos os pesos do elemento para os outros
			elementos_dic[aux_j].append(i)
			elementos_dic[aux_i].append(i)
			aux_i = aux_i -1
		aux_j = aux_j + 1
		aux_i = qtd_vertices-1
	elementos_dic[aux_j].append(0)	
	
	#Por fim teremos:
	#	Elemento: 0 Pesos: [0, '270', '3179', '2991', '2840', '3031', '3421', '3738', '4947', '6226']
	#	...
	
	#for i in range(0,len(elementos_dic)):
	#	print("Elemento:",i,"Pesos:",elementos_dic[i])
	
	# ---------- Array auxiliar ----------
	#Cria um conjunto de arrays vazio do tamanho do conjunto do número de elementos	
	array_aux = []
	for k in range(0, len(elementos_dic)):
		array_aux.append([])
	
	for i in range(0,len(elementos_dic)):
		for j in range(0,len(elementos_dic)):
			array_aux[i].append(int(elementos_dic[i][j]))
				
	# ---------- Sort no array auxiliar	----------
	for i in range(0,len(array_aux)):
		array_aux[i] = heapSort(array_aux[i])
		
	# ---------- O seguinte conjunto de instruções serve para criar as arestas com os menores pesos ----------
	# ---------- Compara cada elemento do array auxiliar já ordenado, com os elementos presentes no dicionário inicial ----------
	conj_arestas = cria_arestas(elementos_dic,array_aux)
	print("Essas são as arestas que compõem a MST\n")
	for a in range(0,len(conj_arestas)):
		print("[",conj_arestas[a].elemento1,"]","[", conj_arestas[a].elemento2,"]"," = ","Peso:", conj_arestas[a].peso)
	
	return 
	

main()
#Começo com a aresta de menor valor, e depois procuro a proxima com menor valor, sempre lembrando de evitar a formação de ciclos
#Se tiverem duas arestas com valor igual e que não formam ciclo eu posso pegar qualquer uma das duas


	
'''	
	9		8	7	6	5	 4	  3	   2 	1	0
0	270 3179 2991 2840 3031 3421 3738 4947 6226
1	2903 2715 2564 2755 3144 4153 5362 6641
2	504 655 908 1299 2237 3446 3682
3	151 423 723 2040 3249 3485
4	272 571 1888 3098 3334
5	241 1560 2770 3006
6	1617 2827 3063
7	1274 1510
8	236
9	
'''	
	
