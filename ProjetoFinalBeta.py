#	----	Projeto Final APA	----
#	Código Final APA - Rodrigo Augusto Vasconcelos Sarmento - 11218021
#	----						----	


#	----	Bibliotecas
#Para realizar a escolha aleatória de uma aresta
import random


#	---	Utilizado para o vertex cover
#	-	Conjunto de vértices
#	-	Set de vértices que abrange a menor quantidade de arestas possível
conj_vertices = set()
vertices_aux = []

#	---	Utilizado somente para calcular o grau dos vértices
conj_vertex = set()
dic_vertices = {}

#	----	Classe aresta
class aresta:
     def __init__(self, u, v):
         self.u = u
         self.v = v
         
#	-----	Conjunto que contém todas as arestas         
conj_arestas = []


#	-----	Função para abrir arquivos e criar o conjunto de arestas
def abreArquivo():
	txt = open('frb30-15-mis/frb30-15-1.mis','r').readlines()
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
	

#	----------	FUNÇÕES QUE MANIPULAM AS LISTAS E SETS DE VÉRTICES	----------
	
#	-----	Cria conjunto de todos os vértices	
def cria_vertices():
	for item in conj_arestas:
		vertices_aux.append(item.u)
		vertices_aux.append(item.v)
	return
	
	
#	-----	Calcula o grau de importância de cada vértice
def vertex_grau():
	# - Conj_vertex é utilizado apenas no inicio para adicionar pela primeira vez
	# os elementos ao dicionário e realizar a sua contagem corretamente.
	for aresta in reversed(conj_arestas):
		if	aresta.u not in conj_vertex:
			conj_vertex.add(aresta.u)
			dic_vertices[aresta.u] = 0
		if aresta.v not in conj_vertex:
			conj_vertex.add(aresta.v)
			dic_vertices[aresta.v] = 0
		if aresta.u in conj_vertex:
			dic_vertices[aresta.u] = dic_vertices[aresta.u] + 1
		if aresta.v in conj_vertex:
			dic_vertices[aresta.v] = dic_vertices[aresta.v] + 1
		else: 
			pass
	return


#	-----	Retorna um dos melhores vértices que possua uma aresta no conjunto de arestas
def vertex_melhor():
	aux_maior = 0
	aux_vertice = 0
	for item in dic_vertices:
		if dic_vertices[item] > aux_maior: 
			aux_maior = dic_vertices[item]	# - Adiciona o grau daquele vértice para a variável maior
			aux_vertice = int(item)			# - Adiciona a chave para a variável vértice
			
	return aux_vertice	# Retorna um dos melhores vértices


#	----- Limpa o dicionário e conj_vertex para recalcular o grau de cada vértice
def limpa():
	# - Limpa set de vertex
	conj_vertex.clear()
	
	# - Limpa dicionário
	# - Percorro todos os vértices existentes no lugar de arestas
	for item in vertices_aux:
		dic_vertices[item] = 0
	return


#	----------	************************************	----------


#	----------	FUNÇÕES QUE MANIPULAM A CLASSE ARESTA	----------

#	-----	Função para printar as arestas durante os testes
def print_arestas():
	print(" ------------------------------ \n")
	print("Quantidade de arestas:",len(conj_arestas))
	print("Arestas existentes: \n")
	for obj in conj_arestas:
		print(obj.u,obj.v)
	
	print(" ------------------------------ \n")
	return	
	

#	-----	Escolho uma aresta que contenha o melhor vértice escolhido na função anterior	
def	aresta_melhor(x):
	# - *** Acredito que adicionando apenas 1 dos vértices a solução já seja possível
	for item in conj_arestas:
		if int(item.u) == x:
			conj_vertices.add(item.u)
			#conj_vertices.add(item.v)
			break
		elif int(item.v) == x:
			#conj_vertices.add(item.u)
			conj_vertices.add(item.v)
			break
		else:
			pass
	return
	

#	-----	Remover arestas que contenham elementos dos vértices já escolhidos
def remove_arestas():
	for item in reversed(conj_arestas):
		#print(item.u,item.v)
		if item.u in conj_vertices:
			#print("Remove", item.u, item.v)
			conj_arestas.remove(item)
		elif item.v in conj_vertices:
			#print("Remove", item.u, item.v)
			conj_arestas.remove(item)
		else:
			#print("Fica", item.u, item.v)
			pass 
	return
		
#	----------	************************************	----------


#	----------	VERTEX COVER	----------
#	-----	Função que excluí arestas e adiciona vértices em um conjunto
def vertex_cover():	

	# - Enquanto existirem arestas
	while conj_arestas:	
	
		# - Print da quantidade de arestas
		#print_arestas()
		
		# - Calcula o grau de importância de cada vértice naquele momento
		vertex_grau()
		#print("Dicionário dos vértices com seu grau:",dic_vertices)
		
		# - Encontro o vértice com maior grau
		# Fazer um if na hora de escolher o vértice para testar se ele é realmente necessário
		melhor = vertex_melhor()
		#print("Melhor vértice: ",melhor)
		
		# - Escolho uma aresta que contenha esse vértice
		melhor_aresta = aresta_melhor(melhor)
		#print("Aresta escolhida:", conj_vertices)
	
		# - Conjunto de vértices final
		#print("Conj de vértices: ",conj_vertices)
		
		# - Remover arestas que contenham elementos dos vértices já escolhidos
		# - nao remove a aresta dos que ainda nao foram escolhidos?
		remove_arestas()
		
		# - Limpa dicionário e set_vertex, para que novamente seja feita a contagem do grau
		limpa()
		#quit()
		#print("\n")
	return	
#	----------	************************************	----------

		
#	-----	main
def main():

	# - Abre o arquivo e cria os elementos da classe aresta
	elementos, qtd_vertices, qtd_arestas = abreArquivo()
	print("Quantidade inicial de vértices: \n",qtd_vertices)
	print("Inicialmente temos:",len(conj_arestas),"arestas\n")
	
	cria_vertices()
	
	# - Apresenta o conjunto de arestas atual
	#print_arestas()	
	
	# - Função para a realização da cobertura de vértices
	vertex_cover()
	
	# - Print do conjunto final de vértices
	print("Conjunto final de vértices escolhidos: \n",conj_vertices)		
	print("Tamanho:\n",len(conj_vertices))	
	
	return
	
	
main()
