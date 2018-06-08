#Para realizar a escolha aleatória de uma aresta
import random

#Set de vértices que abrange a menor quantidade de arestas possível
conj_vertices = set()
#conj_vertices = []

#Classe aresta
class aresta:
     def __init__(self, u, v):
         self.u = u
         self.v = v

#Conjunto que contém todas as arestas         
conj_arestas = []


#abrearquivo para arquivos que possuem separação por espaço
def abreArquivo():
	txt = open('frb30-15-mis/frb30-15-1 copy.mis','r').readlines()
	array = []
	i = 0
	for item in txt:
		if i == 0:
			vetor_aux = item.strip('\n').split(' ')
			qtd_vertices, qtd_arestas= int(vetor_aux[2]),int(vetor_aux[3])
			i = i + 1
			pass
		else:
			vetor_aux = item.strip('\n').split(' ') 
			conj_arestas.append(aresta(vetor_aux[1],vetor_aux[2]))
			array.append(vetor_aux)	#Removo o \n de cada elemento do array
	
	return array, qtd_vertices, qtd_arestas


def print_arestas():
	print(" ------------------------------ \n")
	print("Quantidade de arestas:",len(conj_arestas))
	print("Arestas existentes: \n")
	for obj in conj_arestas:
		print(obj.u,obj.v)
	
	print(" ------------------------------ \n")
	return	
	


    #The variable neighborhood descent (VND) method is obtained if a change of neighborhoods is 
    #performed in a deterministic way. In the descriptions of its algorithms, we assume that an 
    #initial solution x is given. Most local search heuristics in their descent phase use very few 
    #neighbourhoods. The final solution should be a local minimum with respect to all k m 
    #a x {\displaystyle k_{max}} k_{{max}} neighbourhoods; hence the chances to reach a global 
    #one are larger when using VND than with a single neighbourhood structure. 	
	
	
	#Function VNS (x, kmax, tmax );
	# 1: repeat
	# 2:    k ← 1;
	# 3:    repeat
	# 4:       x' ←Shake(x, k) /* Shaking */;
	# 5:       x'' ← FirstImprovement(x' ) /* Local search */;
	# 6:       x ←NeighbourhoodChange(x, x'', k) /* Change neighbourhood */;
	# 7:    until k = k_max ;
	# 8:    t ←CpuTime()
	# 9: until t > t_max ;
	

def vertex_cover():
	
	#Utilizando lista
	#conj_vertices.append(int(conj_arestas[0].u))
	#conj_vertices.append(int(conj_arestas[0].v))
	
	#Utilizando set
	#Utilizo "char" mesmo, devido ao fato de conferir "in"
		
	#Enquanto existirem arestas
	while conj_arestas:
		#Adiciono arbitrariamente uma aresta
		aux = random.choice(conj_arestas) 
		conj_vertices.add(aux.u)
		conj_vertices.add(aux.v)
		
		#print("Conj de vértices: ",conj_vertices)
		
		#Agora devo remover as arestas que possuem ligação com esses vértices
		for item in conj_arestas:
			print(item.u,item.v)
			#Se eu quiser deixar as arestas dos vértices que pertencem
			if item.u in conj_vertices and item.v in conj_vertices:
				#print("Remove", item.u, item.v)
				conj_arestas.remove(item)
				#pass
			elif item.u in conj_vertices or item.v in conj_vertices:
				#print("Remove", item.u, item.v)
				conj_arestas.remove(item)
			else:
				#print("Fica", item.u, item.v)
				pass
						
	return	
	
	
def main():
	elementos, qtd_vertices, qtd_arestas = abreArquivo()
	print("Quantidade inicial de vértices: \n",qtd_vertices)
	
	
	#Trabalhando com a classe conjunto de arestas
	#print(conj_arestas[1].u,conj_arestas[1].v)
	
	#Algoritmo
	#1) Initialize the result as {}
	#2) Consider a set of all edges in given graph.  Let the set be E.
	#3) Do following while E is not empty
	#...a) Pick an arbitrary edge (u, v) from set E and add 'u' and 'v' to result
	#...b) Remove all edges from E which are either incident on u or v.
	#4) Return result 

	print("Inicialmente temos:",len(conj_arestas),"arestas\n")
	print_arestas()

	# --- PRECISO FICAR CHAMANDO ESSE FUNCAO VERTEX COVER ENQUANTO O OBJETIVO NÃO FOR ATINGIDO
	#while ... chama vertex cover
	vertex_cover()
	
	print("Conjunto final de vértices escolhidos: \n",conj_vertices)		
	print("Tamanho:\n",len(conj_vertices))	
	
	return
	
	
main()
