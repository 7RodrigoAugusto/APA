#	----	Projeto Final APA	----
#	Código Final APA - Rodrigo Augusto Vasconcelos Sarmento - 11218021
#	----						----	


#	----	Bibliotecas
#Para realizar a escolha aleatória de uma aresta
import random

# - Conjunto com todas as melhores soluções existentes
conj_solucao = []
vetores_solucao = []

vetores_solucao_extra = []

vetores_solucao_final = []

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
	txt = open('frb30-15-mis/teste3.mis','r').readlines()
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
			#conj_vertices.add(item.v)	# - ***** IMPORTANTE
			break
		elif int(item.v) == x:
			#conj_vertices.add(item.u)	# - ***** IMPORTANTE
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

#	-----	Remover arestas VND que contenham elementos dos vértices já escolhidos
def remove_arestas_vnd(vetor_aux):
	for item in reversed(conj_arestas):
		#print(item.u,item.v)
		if item.u in vetor_aux:
			#print("Remove", item.u, item.v)
			conj_arestas.remove(item)
		elif item.v in vetor_aux:
			#print("Remove", item.u, item.v)
			conj_arestas.remove(item)
		else:
			#print("Fica", item.u, item.v)
			pass 
	return

# - Remove todas as arestas	
def remove_arestas_todas():
	for item in reversed(conj_arestas):	
		conj_arestas.remove(item)

#	-----	Cria o conjunto de arestas que sempre é excluido após a utilização do vertex cover
def cria_arestas(objs):
	for item in objs:
		conj_arestas.append(aresta(item[1],item[2]))
	return
		
#	----------	************************************	----------


#	----------	VERTEX COVER	----------
#	-----	Função que excluí arestas e adiciona vértices em um conjunto
def vertex_cover():	

	# - Enquanto existirem arestas
	while conj_arestas:	
		# - Calcula o grau de importância de cada vértice naquele momento
		vertex_grau()
		melhor_v = vertex_melhor_elemento()
		
		# - Escolho uma aresta que contenha esse vértice
		melhor_aresta = aresta_melhor(melhor_v)
		#print("Aresta escolhida:", conj_vertices)
	
		
		# - Remover arestas que contenham elementos dos vértices já escolhidos
		remove_arestas()
		
		# - Limpa dicionário e set_vertex, para que novamente seja feita a contagem do grau
		limpa_vertex_grau()
			
	return	
#	----------	************************************	----------


#	---- Função que testa se a solução encontrada com a troca de vértices respeita a condição
def respeita_cover(vetor_teste):
	#print(vetor_teste)
	# - Se respeitar adiciona ele no vetores_solucao_extra
	# - Vejo se ele consegue excluir todas as arestas e no final cria novamente
	#print_arestas()
	#print("Testando soluções")

	remove_arestas_vnd(vetor_teste)
	if not conj_arestas:
		#print("Funcionou:",vetor_teste)
		vetores_solucao_extra.append(vetor_teste)
	else:
		#print("Não funcionou:",vetor_teste)
		remove_arestas_todas()
	
	#print_arestas()
	return

def respeita_cover_final(vetor_teste):
	#print(vetor_teste)
	# - Se respeitar adiciona ele no vetores_solucao_extra
	# - Vejo se ele consegue excluir todas as arestas e no final cria novamente

	remove_arestas_vnd(vetor_teste)
	if not conj_arestas:
		#print("Funcionou:",vetor_teste)
		vetores_solucao_final.append(vetor_teste)
	else:
		#print("Não funcionou:",vetor_teste)
		remove_arestas_todas()
	
	#print_arestas()
	return	
	

#	---	Troca os vértices
def vnd(elementos):
	vetor_teste = []
	aux = 0
	#	-----	VND	-----
	# - Crio as arestas novamente para poder fazer a conferência dentre as melhores soluções
	for item in vetores_solucao:
		#print("Testando vetor:",item)	
		# - Testar se da pra ter uma nova solucao alterando alguns dos vertices
		for x in item:
			#print(x)
			for aresta in conj_arestas:
				# - Delimitar a quantidade de loops
				#if aux == 5:
				#	break
				#aux = aux +1
				if x == aresta.u:
					#print("Elemento:",x," na aresta",aresta.u,aresta.v)
					if aresta.v not in item:
						#print("Vértice",aresta.v,"no lugar de",x)
						# - Cria vetor teste
						vetor_teste.append(aresta.v)
						for i in item:
							if i == x:
								pass
							else:
								vetor_teste.append(i)
						# - Para tirar a redundância eu confiro se os elementos do meu vetor teste são iguais a algum que tá na solução	
						respeita_cover(vetor_teste)
						cria_arestas(elementos)
						vetor_teste = []
						
				if x == aresta.v:
					#print("Elemento:",x," na aresta",aresta.u,aresta.v)
					if aresta.u not in item:
						#print("Vértice",aresta.u,"no lugar de",x)
						# - print("O vertice ligado a ele pode ser testado como uma troca")
						vetor_teste.append(aresta.u)
						for i in item:
							if i == x:
								pass
							else:
								vetor_teste.append(i)
						# - Para tirar a redundância eu confiro se os elementos do meu vetor teste são iguais a algum que tá na solução		
						respeita_cover(vetor_teste)
						cria_arestas(elementos)
						vetor_teste = []
						
						
	return				


def remove_vertex(vetor_teste,elementos):
	aux_teste = []
	aux = 0
	for item in vetor_teste:
		#print("Testando:",item)
		for x in range(aux, len(item)+1):
			for y in range(aux+1,len(item)):
				try:
					#print("Testando",item[x],"com ",item[y])
					for aresta in conj_arestas:
						item_aux = item
						#print("Testando:",item_aux)
						if (item[x] == aresta.u and item[y] == aresta.v) or (item[y] == aresta.u and item[x] == aresta.v):
							item_aux.remove(item[y]) 
							respeita_cover(item_aux)
							cria_arestas(elementos)
							item_aux = item
							item_aux.remove(item[x])
							respeita_cover(item_aux)
							cria_arestas(elementos)
							item_aux = item
					
				except:
					pass
			aux = aux+1
		aux = 0
	return	
		
		
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
	#	----------	FIM INFORMAÇÕES	--------------
	
	
	#	----------	 VERTEX COVER SOLUÇÃO	--------------	
	
	vertex_cover()
	
	# - Coloco o tamanho da melhor solução encontrada até o momento
	conj_solucao.append(len(conj_vertices))
	
	# - Dou append na melhor solução inicial
	vetores_solucao.append(list(conj_vertices))
		
	# - Refaz o conjunto de arestas que é destruido ao fim de vertex_cover()
	cria_arestas(elementos) 
		
	# - Limpa tudo para que seja possível rodar vertex_cover() novamente
	limpa_total()	
	
	#	----------	FIM VC	--------------
		
		
	print("O conjunto solução inicial é de tamanho:",conj_solucao,"\n")
	print("O conjunto de vetores por enquanto é o seguinte:",vetores_solucao,"\n")
	
	#	----------	 VND	--------------	
	print("	----------	VND	---------- \n")
	print("Com o VND pegarei mais soluções que respeitam a condição, porém ainda serão melhoradas com a remoção de vértices a seguir\n")
	
	vnd(elementos)
	
	# - Prints após o VND e antes da remoção final de vértices
	print("Resultados iniciais:\n")
	print("O conjunto de vetores solução inicial é o seguinte:",vetores_solucao,"\n")
	print("Resultados extras com a troca de vértices: \n")
	print("O conjunto de vetores solução extra, após o VND é:",vetores_solucao_extra,"\n")
	
	# - Calculo grau para utilizar na hora de excluir vertices
	vertex_grau()
	
	# - Função para ver se alguns vértices podem ser removidos, quando funcionar checa se respeita cover e
	# da append pra vetores_solucao_final
	remove_vertex(vetores_solucao,elementos)
	remove_vertex(vetores_solucao_extra,elementos)
	
	
	# - Prints finais
	print("Resultados com a remoção de vértices: \n")
	print("Resultados melhorados das soluções:", vetores_solucao_final)
	
	# - Tamanho da melhor solução
	#melhor_solucao = 10000
	#for x in vetores_solucao_final:
	#	if melhor_solucao>len(x):
	#		melhor_solucao = len(x)
	#		melhores_vertices = x
	
	#print("A melhor solução é:", melhores_vertices)
	#print("O melhor tamanho encontrado foi:",melhor_solucao)
			
	
	
	
	return
	
	
main()
