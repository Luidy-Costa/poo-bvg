from datetime import date
def linha():
    print("-"*60)
#criando a classe Cliente
class Cliente:
    #definindo o construtor da classe Cliente
    def __init__(self,nome,cpf):
        self.nome = nome
        self.__cpf  = cpf

    #criando o metodo que ira exibir as informações do cliente
    def exibir_informacoes(self):
        print(f'Nome:{self.nome}\nCPF:{self.__cpf}')
        linha()

#criando a classe carro
class Veiculo:
    #criando o costrutor da classe Carro
    def __init__(self,ano,marca,modelo,cor,placa):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.__placa = placa
    #criando o metodo para Exibir as informações do carro
    def exibir_detalhes (self):
        print(f"Ano:{self.ano}\nMarca:{self.marca}\nModelo:{self.modelo}\nCor:{self.cor}\nPlaca:{self.__placa}")
        linha()
    
    #criando o metodo para mudar a cor do carro
    def atualizar_cor(self,nova_cor):
        self.cor=nova_cor

#criando a classe Seguro
class SeguroVeiculo:
    def  __init__(self,veiculo,cliente,vigencia):
        self.veiculo = veiculo
        self.cliente = cliente
        self.valor = 0
        self.vigencia = vigencia
   
    def calcular_valor(self,base_valor,taxa):
        self.valor = base_valor * taxa
        print(f"Valor calculado agora é: {self.valor}")
        linha()

    def verificar_vigencia(self):
        hoje = date.today()
        if self.vigencia > hoje:
            print(f"O seu seguro esta em dia")
            linha()
            return True
        else:
            print(f"O seu seguro esta vencido")
            linha()
            return False
        
class SeguroCarro (SeguroVeiculo):
    #criando um metodo de calculo de valor de seguro especifico para o "SeguroCarro"
    def calcular_valor(self,base_valor,taxa):
    #calculando o valor utilizando um metodo herdado da classe mãe (SeguroVeiculo)
        super().calcular_valor(base_valor,taxa)
    
        print(f"calculando o valor do seguro com taxa adicional do veiculo (carro) ")
        self.valor += 50
        print(f"O valor final (carro): {self.valor}")
        linha()


class SeguroMoto(SeguroVeiculo):
    def calcular_valor(self,base_valor,taxa):
        super().calcular_valor(base_valor,taxa)

        print("calculando o valor do seguro com taxa adicional do veiculo(moto)")
        self.valor += 30
        print(f"valor final do seguro do veiculo (moto): {self.valor}")

