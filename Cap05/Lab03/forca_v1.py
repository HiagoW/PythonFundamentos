# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.i = 0
		self.right = list()
		self.wrong = list()
		self.hide_word()
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if (letter in self.right or letter in self.wrong):
			print("Voce já digitou essa letra")
			return
		elif letter in self.word:
			print("Você acertou!")
			self.right.append(letter)
			self.show = list(map(lambda x: x if x in self.right else '_', self.word))
		else:
			print("Você errou!")
			self.wrong.append(letter)
			self.i += 1
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.i == len(board)-1 or self.hangman_won():
			return True
		self.hangman_won()
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.show == list(self.word):
			return True
		return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		self.show = len(self.word) * '_'
		return
		
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.i])
		for i in self.show:
			print(i, end='')
		print()
		print("Certas: " + self.right.__str__())
		print("Erradas: " + self.wrong.__str__())

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while(not game.hangman_over()):
		game.print_game_status()
		entrada = input("Digite uma letra: ")
		game.guess(entrada)

	# Verifica o status do jogo
	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
