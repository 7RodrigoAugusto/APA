#	----	Projeto Final APA	----
#	Código Final APA - Rodrigo Augusto Vasconcelos Sarmento - 11218021
#	----						----	


#	----	Bibliotecas
#Para realizar a escolha aleatória de uma aresta
import random

# - Conjunto com todas as melhores soluções existentes
conj_solucoes = set()

# - Conjunto dos melhores vértices, ele é criado uma vez e vai diminuindo com os loops
conj_melhores = set()


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




def print_tudo():
	print("Conj de vertices:",conj_vertices,"\n")
	print("Conj de vertices aux:",vertices_aux,"\n")
	print("Conj de vertex:",conj_vertex,"\n")
	print("Dicionario vertices:",dic_vertices,"\n")
	return

#	-----	Função para abrir arquivos e criar o conjunto de arestas
def abreArquivo():
	#frb30-15-mis/frb30-15-1.mis
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
	




#	----------	FUNÇÕES QUE MANIPULAM AS LISTAS E SETS DE VÉRTICES	----------
	
#	-----	Cria conjunto de todos os vértices para auxiliar na função limpa()
def cria_vertices():
	for item in conj_arestas:
		if item.u not in vertices_aux:
			vertices_aux.append(item.u)
		if item.v not in vertices_aux:
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

#	-----	Retorna um dos  melhores vértices, função particular utilizada somente dentro de VERTEX_COVER()
def vertex_melhor_elemento():
	aux_maior = 0
	aux_vertice = 0
	for item in dic_vertices:
		if dic_vertices[item] > aux_maior: 
			aux_maior = dic_vertices[item]	# - Adiciona o grau daquele vértice para a variável maior
			aux_vertice = int(item)			# - Adiciona a chave para a variável vértice
			
	return aux_vertice	# Retorna um dos melhores vértices

#	-----	Retorna o melhor grau do dicionário
def vertex_melhor_grau():
	aux_maior = 0
	for item in dic_vertices:
		if dic_vertices[item] > aux_maior: 
			aux_maior = dic_vertices[item]	# - Adiciona o grau daquele vértice para a variável maior
			
	return	aux_maior	# Retorna um dos melhores vértices
	
#	-----	Retorna um dos melhores vértices evitando escolher um daqueles que já foi utilizado
def vertex_melhor_main():
	aux_maior = 0
	aux_vertice = 0
	for item in dic_vertices:
		if dic_vertices[item] > aux_maior: 
			# - Ele só escolhe o melhor se ele ainda estiver no conjunto melhores
			if item in conj_melhores:
				aux_maior = dic_vertices[item]	# - Adiciona o grau daquele vértice para a variável maior
				aux_vertice = int(item)			# - Adiciona a chave para a variável vértice
				# - Remove do conjunto de melhores
				conj_melhores.remove(item)
			else:
				pass
			
	return aux_vertice	# Retorna um dos melhores vértices

#	-----	Retorna a quantidade de vértices existentes com aquele melhor grau e um conjunto com esses melhores
def vertex_melhores():
	melhor_grau = vertex_melhor_grau()
	qtd_maior = 0
	aux_maior = 0
	aux_vertice = 0
	for item in dic_vertices:
		if dic_vertices[item] == melhor_grau: 
			conj_melhores.add(item)
			qtd_maior = qtd_maior+1
			
	return qtd_maior	

#	-----	Limpa o dicionário e conj_vertex para recalcular o grau de cada vértice utilizada dentro de VERTEX_COVER()
def limpa_vertex_grau():
	# - Limpa set de vertex
	conj_vertex.clear()
	
	# - Limpa dicionário
	# - Percorro todos os vértices existentes no lugar de arestas
	dic_vertices.clear()
	#for item in vertices_aux:
	#	dic_vertices[item] = 0
	return

#	-----	Limpa tudo
def limpa_total():
	# - Limpa conj_vertices
	conj_vertices.clear()
	
	# - Limpa set de vertex
	conj_vertex.clear()
	
	# - Limpa dicionário
	dic_vertices.clear()
	#for item in vertices_aux:
	#	dic_vertices[item] = 0
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
	# Realmente funciona, pois se já tá ligado ao vértice principal então ele já está sendo tocado e não precisa ser adicionado ao conjunto de vértices final
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

#	-----	Cria o conjunto de arestas que sempre é excluido após a utilização do vertex cover
def cria_arestas(objs):
	for item in objs:
		conj_arestas.append(aresta(item[1],item[2]))
	return
		
#	----------	************************************	----------




#	----------	VERTEX COVER	----------
#	-----	Função que excluí arestas e adiciona vértices em um conjunto
def vertex_cover(melhor_main):	

	# - Limpo antes de começar o loop pois o dicionário foi criado antes e deve estar limpo para vertex grau
	# - * Vou parar de limpar pra seguir o conselho do melhor grau
	#limpa_vertex_cover()
	
	# - Variável para evitar a realização do vertex_grau() no primeiro loop
	aux = 0	
	# - Utiliza de cara o melhor escolhido no main
	melhor_v = melhor_main
	# - Enquanto existirem arestas
	while conj_arestas:	
	
		# - Print da quantidade de arestas
		#print_arestas()
		
		# - Só começa depois do primeiro loop
		if aux > 0:
			# - Calcula o grau de importância de cada vértice naquele momento
			vertex_grau()
			
			#print("Dicionário dos vértices com seu grau:",dic_vertices)
		
			# - Encontro o vértice com maior grau
			melhor_v = vertex_melhor_elemento()
					
		print("Melhor vértice: ",melhor_v)
		
		# - Escolho uma aresta que contenha esse vértice
		melhor_aresta = aresta_melhor(melhor_v)
		#print("Aresta escolhida:", conj_vertices)
	
		# - Conjunto de vértices final
		#print("Conj de vértices: ",conj_vertices)
		
		# - Remover arestas que contenham elementos dos vértices já escolhidos
		remove_arestas()
		
		# - Limpa dicionário e set_vertex, para que novamente seja feita a contagem do grau
		limpa_vertex_grau()
		
		# - Incrementa aux para realizar seu proprio calculo de grau
		aux = aux +1	
		
	return	
#	----------	************************************	----------


		
#	-----	main
def main():

	# - Abre o arquivo e cria os elementos da classe aresta
	elementos, qtd_vertices, qtd_arestas = abreArquivo()
	#	----------	 INFORMAÇÕES	--------------
	print("	----- INFORMAÇÕES ----- \n")
	print("Quantidade inicial de vértices: \n",qtd_vertices)
	print("Inicialmente temos:",len(conj_arestas),"arestas\n")
	
	# - Cria lista dos vértices para ajudar na função limpa()
	cria_vertices()
	print("Vertices_aux:",vertices_aux,"\n")
	
	# - Apresenta o conjunto de arestas atual
	print_arestas()	
	
	# - Calcula o grau de cada vértice, para definir quantos loops serão feito em busca de uma nova solução
	vertex_grau()
	print("Grau de todos os vértices: ",dic_vertices,"\n")
	
	# - Calcula quantos vértices com o maior grau possível existem, para realizar um loop testando todas as possibilidades de troca
	# - Cria um conjunto com os melhores vértices iniciais
	qtd_melhores = vertex_melhores()
	
	print("Conjunto dos melhores:",conj_melhores,"\n")
	
	print("Quantidade de elementos com o maior grau:",qtd_melhores,"\n")
	
	#	----------	FIM INFORMAÇÕES	--------------
	
	
	# - Limpa para começar o vertex_cover
	limpa_vertex_grau()
	
	
	#	----------	MAIN	--------------
	
	# - Função para a realização da cobertura de vértices
	# - while tentando as novas soluções trocando meus vértices e testando
	print("	----- Início do Loop -----\n")
	
	# - Enquanto existirem melhores
	while conj_melhores:
		#print("Loop:", qtd_melhores,"\n")
		
		# - Calcula o grau de cada vértice
		# - Cria o dicionário
		vertex_grau()
		
		# - Pega um dos melhores elementos
		melhor_main = vertex_melhor_main()
		
		# - Retorna um vetor de binário que vai me fazer evitar de utilizar 
		# o mesmo elemento no começo do próximo teste
		vertex_cover(melhor_main)
		
		# - Print do conjunto final de vértices escolhidos pelo vertex_cover
		print("Conjunto final de vértices escolhidos:",conj_vertices)		
		print("Tamanho:",len(conj_vertices))
		
		# - Adiciono a solucao ao conjunto de solucoes	
		conj_solucoes.add(len(conj_vertices))
		
		# - Prepara para a próxima iteração do loop
		qtd_melhores = qtd_melhores - 1
		
		# - Refaz o conjunto de arestas que é destruido ao fim de vertex_cover()
		cria_arestas(elementos) 
		
		# - Limpa tudo para que seja possível rodar vertex_cover() novamente
		limpa_total()	
		
		# - Teste de checagem para a próxima iteração
		#print("Pronto para a próxima iteração:\n")
		#print_tudo()	#não é só zerar o dicionário é recriar ele
		#print(" Fim \n")	
	
		#	----------	FIM MAIN	--------------
		
	print("O conjunto de soluções é o seguinte:",conj_solucoes,"\n")
	
	return
	
	
main()
