#	----	Projeto Final APA	----
#	Código Final APA - Rodrigo Augusto Vasconcelos Sarmento - 11218021
#	----						----	


#	----	Bibliotecas
#Para realizar a escolha aleatória de uma aresta
import random
import timeit
from timeit import default_timer as timer

# - Conjunto com todas as melhores soluções existentes
conj_solucao = []
vetores_solucao = []
vetores_solucao_extra = []
vetores_solucao_final = []


# - Conjunto dos melhores vértices, ele é criado uma vez e vai diminuindo com os loops
conj_melhores = set()

# IMPORTANTE
conj_grasp = set()


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

#	----- Escolhe um vértice aleatório dentre os de melhor grau
def vertex_random():
	aux = []
	for i in conj_grasp:
		aux.append(i)
		
	aux_vertice = random.choice(aux)
	#print("Removo:",aux_vertice)
	conj_grasp.remove(aux_vertice) 
	#print(conj_grasp)
	return aux_vertice

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

# - Ordena os graus	
def ordena():
	A = []
	for item in dic_vertices:
		A.append(dic_vertices[item])
	# Selection sort
	for i in range(len(A)):
		min_idx = i
		for j in range(i+1, len(A)):
			if A[min_idx] > A[j]:
				min_idx = j        
		A[i], A[min_idx] = A[min_idx], A[i]
    	
	return	A	

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
#	-----	Função que excluí arestas e adiciona vértices em um conjunto que representa os melhores vértices para cobertura
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
					
		#print("Melhor vértice: ",melhor_v)
		
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




# ---------- VERIFICA SE RESPEITA COVER	--------
#	---- Função que testa se a solução encontrada com a troca de vértices respeita a condição
def respeita_cover(vetor_teste):
	remove_arestas_vnd(vetor_teste)
	if not conj_arestas:
		#print("Funcionou:",vetor_teste)
		vetores_solucao_extra.append(vetor_teste)
	else:
		#print("Não funcionou:",vetor_teste)
		remove_arestas_todas()
	
	#print_arestas()
	return

# --- Verifica se respeita a condição de cover
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
#	----------	************************************	----------
	
	
	
# ---------- EXTRA --------	
#	---	Troca os vértices
def vnd(elementos):
	vetor_teste = []
	aux = 0
	#	-----	VND	-----
	# - Crio as arestas novamente para poder fazer a conferência dentre as melhores soluções
	for item in vetores_solucao:
		# - Testar se da pra ter uma nova solucao alterando alguns dos vertices
		#print("Testando novas soluções a partir de:",item)
		for x in item:
			#print(x)
			for aresta in conj_arestas:
				#if aux == 10:
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
						v1 = vetor_teste
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
						#print(vetor_teste)
						respeita_cover(vetor_teste)
						v1 = vetor_teste
						cria_arestas(elementos)
						vetor_teste = []
							
	return	v1
	
# - Remove vertex
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
	
# - Define o filtro grasp *** Ainda com erro!		
def escolha_grasp(vetor_aux):
	tamanho = int(len(vetor_aux)/2)
	alfa = tamanho * 50/100
	print("Alfa de:",int(alfa))
	#quit()
	# - Elementos da melhor metade
	half = vetor_aux[tamanho:]
	#print(half)
	#print("Considerando que estavam na elementos da metade, valor do meu Grasp ")
	print("Testarei primeiramente com os seguintes vértices:")
	for item in dic_vertices:
		if int(dic_vertices[item]) in half:
			if len(conj_grasp) >= alfa:#tamanho:
				break
			else:
				conj_grasp.add(item)

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
	#print_arestas()	
	
	#	----------	FIM INFORMAÇÕES	--------------
	
	#Extra
	# - Calcula o grau de cada vértice, para definir quantos loops serão feito em busca de uma nova solução
	vertex_grau()
	# - Calcula quantos vértices com o maior grau possível existem, para realizar um loop testando todas as possibilidades de troca
	qtd_melhores = vertex_melhores()
	grau_ordenado = ordena()
	
	escolha_grasp(grau_ordenado)
	
	# - Limpa para começar o vertex_cover
	limpa_vertex_grau()

	# - Contagem do tempo
	print(conj_grasp)
	tamanho_grasp = len(conj_grasp)
	tempo_vc = 0
	tamanho_vc = 0
	
	#	----------	 VERTEX COVER SOLUÇÃO	--------------	
	while conj_grasp:
	
		# - Calcula o grau de cada vértice - Cria o dicionário
		vertex_grau()
		#print("Por enquanto temos os seguintes vértices para inicio de teste:",conj_grasp)
		# - Pega um dos melhores elementos
		#melhor_main = vertex_melhor_main()
		melhor_main = vertex_random()
		print("Testando com:",melhor_main)
		start = timer()#timeit.timeit()
		vertex_cover(melhor_main)
		end = timer()#timeit.timeit()
		print("Tempo VC:",end-start,"começando com vértice",melhor_main)
		tempo_vc = tempo_vc + end-start
		# - Coloco o tamanho da melhor solução encontrada até o momento
		conj_solucao.append(len(conj_vertices))
		tamanho_vc = tamanho_vc + len(conj_vertices)
	
		# - Dou append na melhor solução inicial
		vetores_solucao.append(list(conj_vertices))
		
		#print("Solução encontrada:",conj_vertices," Tamanho do vetor:", len(conj_vertices),"\n")
		print("Solução encontrada de tamanho:", len(conj_vertices),"\n")
		
		# - Prepara para a próxima iteração do loop
		qtd_melhores = qtd_melhores - 1
		
		# - Refaz o conjunto de arestas que é destruido ao fim de vertex_cover()
		cria_arestas(elementos) 
		
		# - Limpa tudo para que seja possível rodar vertex_cover() novamente
		limpa_total()	
	
	#	----------	FIM VC	--------------
	
	media_vc = tempo_vc/tamanho_grasp
	media_tamanho_vc = tamanho_vc/tamanho_grasp
	print("Média dos tempos rodando VC:",media_vc)
	print("Média dos tamanhos rodando VC:",media_tamanho_vc)
		
		
	#quit()
	print("O conjunto solução inicial é de tamanho:",conj_solucao,"\n")
	print("O conjunto de vetores por enquanto é o seguinte:",vetores_solucao,"\n")
	
	
	#	----------	 VND	--------------	
	print("	----------	VND	---------- \n")
	print("Com o VND pegarei mais soluções que respeitam a condição, porém ainda serão melhoradas com a remoção de vértices a seguir\n")
	
	zeta = 0 
	qtd = 10
	tempo_vnd = 0
	tamanho_vnd = 0
	while zeta < qtd:
		v1 = vnd(elementos)
		start = timer()#timeit.timeit()
		zeta = zeta +1
		end = timer()#timeit.timeit()
		tamanho_vnd = tamanho_vnd + len(v1)
		tempo_vnd = tempo_vnd + end-start
		print("Tempo VND:",end-start)
	media_vnd = tempo_vnd/qtd
	tamanho_vnd = tamanho_vnd/qtd
	print("Média dos tempos rodando VND:",media_vnd)
	print("Média dos tamanhos rodando VND:",tamanho_vnd)
	
	
	# - Prints após o VND e antes da remoção final de vértices
	print("Resultados iniciais:\n")
	print("O conjunto de vetores solução é o seguinte:",vetores_solucao,"\n")
	print("O conjunto de vetores solução extra, após o VND é:",vetores_solucao_extra,"\n")
	
	# - Calculo grau para utilizar na hora de excluir vertices
	vertex_grau()
	
	# - Função para ver se alguns vértices podem ser removidos, quando funcionar checa se respeita cover e
	# da append pra vetores_solucao_final
	remove_vertex(vetores_solucao,elementos)
	remove_vertex(vetores_solucao_extra,elementos)
	
	
	# - Prints finais
	print("Resultados melhorados das soluções após a remoção:", vetores_solucao_final)
	
	
	
	return
	
	
main()
