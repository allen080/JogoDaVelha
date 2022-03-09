from os import system

def main():
	#Função principal e inicial do programa
	print('\n1) Novo Jogo\n2) Instruções\n3) Sair\n')
	
	while True:
		try:
			inicial = int(input('Opção: '))
			if inicial<1 or inicial>3:
				raise ValueError				
			break

		except ValueError:
			print('Digite uma das opções acima')

	if inicial==1:
		novo_jogo()
	elif inicial==2:
		instrucoes()
	else:
		print('\nSaindo do programa.')
		exit()
	
def novo_jogo():
	#Inicia um novo jogo
	players = [input('\nNome do Player 1 (X): '),input('Nome do Player 2 (O): ')]
	posicoes = [' ' for i in range(9)]
	vez = 1

	interface(posicoes)
	
	while not verifica_ganhou(posicoes):

		if ' ' not in posicoes:
			print('Velha! O jogo deu empate.\n')
			jogar_novamente()

		print('Rodada do Player %s'%players[0])
		while True:
			try:
				jogada = int(input('posição -> '))

				if jogada<1 or jogada>9:
					raise ValueError
				elif posicoes[jogada-1]!=' ':
					print('Essa posição ja foi usada')
					continue

				break	
			except ValueError:
				print('invalido. digite uma posição entre 1 e 9')

		players.reverse()
		if vez==1:
			posicoes[jogada-1] = 'X'
			vez=2
		else:
			posicoes[jogada-1] = 'O'
			vez=1

		interface(posicoes)
	
	print('Vencedor: %s\n'%players[1])
	jogar_novamente()

def instrucoes():
	#Limpa a tela e exibe as instruções de como funciona o programa
	system('cls')
	print('\nPara escolher a posição, utilize os numeros a seguir:\n')
	interface([1,2,3,4,5,6,7,8,9])
	print('\nA cada rodada, o player escolhe uma posição para jogar com seu sinal X ou O.')
	main()

def interface(pos):
	# Recebe uma lista e exibe a interface do Jogo da Velha com os valores dessa lista.
	print()
	print(' %s|%s|%s'%(pos[0],pos[1],pos[2]))
	print(' ----- ')
	print(' %s|%s|%s'%(pos[3],pos[4],pos[5]))
	print(' ----- ')
	print(' %s|%s|%s'%(pos[6],pos[7],pos[8]))
	print()

def verifica_ganhou(elem):
	#Recebe uma lista com os valor sendo "X","O" ou " ", e verifica se um dos jogadores ganhou
	if elem[0]==elem[1]==elem[2] and elem[0]!=' ':
		ganhar = True
	elif elem[3]==elem[4]==elem[5] and elem[3]!=' ':
		ganhar = True
	elif elem[6]==elem[7]==elem[8] and elem[6]!=' ':
		ganhar = True
	elif elem[0]==elem[3]==elem[6] and elem[0]!=' ':
		ganhar = True
	elif elem[1]==elem[4]==elem[7] and elem[1]!=' ':
		ganhar = True
	elif elem[2]==elem[5]==elem[8] and elem[2]!=' ':
		ganhar = True	
	elif elem[0]==elem[4]==elem[8] and elem[0]!=' ':
		ganhar = True
	elif elem[2]==elem[4]==elem[6] and elem[2]!=' ':
		ganhar = True 
	else:
		ganhar = False

	return ganhar

def jogar_novamente():
	#Pergunta ao usuario se ele deseja jogar novamente ou sair
	while True:
		jogar = input('Deseja jogar novamente(j) ou Sair(s): ').lower()
		if jogar=='s':
			print('\nSaindo do jogo')
			exit()

		elif jogar=='j':
			novo_jogo()
		else:
			print('invalido.')


if __name__=='__main__':
	print('Programa Jogo da Velha!')
	main()