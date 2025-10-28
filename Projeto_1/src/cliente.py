#criando a classe
class Cliente:
    #definindo os atributos com encapsulamento(__)
    def __init__ (self, nome, idade, saldo ):
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo

    #definindo o metodo para mostrar as informações do cliente
    def mostrar_cliente(self):
        print("\n","-"*40,"\n")
        print(f"Cliente:{self.__nome}\nIdade:{self.__idade}\nSaldo:{self.__saldo}")
        print("\n","-"*40,"\n")
    
    #Definindo o metodo que atualiza o saldo da instancia
    def atualizar_saldo(self,valor):
        self.__saldo += valor
        print("\n","Saldo atualizado com sucesso","\n")