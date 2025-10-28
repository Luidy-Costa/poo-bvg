#Importando a classe e os metodos nela contidos
from src.cliente import Cliente

#criando uma instancia, utilizando a classe e definindo os valores dos atributos
cliente1 = Cliente("luidy",42,1000.42)

#chamando a função que ira mostrar as informações especificamente do cliente 1
cliente1.mostrar_cliente()

#atualizando o valor contido dentro do atributo saldo do objeto cliente1
cliente1.atualizar_saldo(120)

#reimprimindo as informações para conferir se realmente foi atualizado
cliente1.mostrar_cliente()

