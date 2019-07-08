# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("""

Selecione a opção desejada:

1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
	""")

opcao = int(input('Digite sua opção (1/2/3/4):'))

x = 0
y = 0

if(opcao not in [1,2,3,4]):
	print('A opção "%s" selecionada não disponível' %opcao)
else:
	x = int(input('Digite o primeiro número:'))
	y = int(input('Digite o segundo número:'))

soma = lambda x,y: x+y
subtracao = lambda x,y: x-y
divisao = lambda x,y: x/y
multiplicacao = lambda x,y: x*y

if(opcao == 1 ):
	print(soma(x,y))

if(opcao == 2 ):
	print(subtracao(x,y))

if(opcao == 3 ):
	print(multiplicacao(x,y))

if(opcao == 4 ):
	print(divisao(x,y))