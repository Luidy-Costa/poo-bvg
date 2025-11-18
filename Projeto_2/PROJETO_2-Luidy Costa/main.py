from src.classes import Cliente, Veiculo, SeguroCarro, SeguroMoto
from datetime import date

cliente1 = Cliente("João Silva","000.111.222-33")

carro1 = Veiculo(2025,"Toyota","Corolla","preto","aaa1a11")

seguro1 = SeguroCarro(carro1,cliente1,date(2025,1,1))

cliente1.exibir_informacoes()

carro1.exibir_detalhes()

seguro1.calcular_valor(1500,1.1)

seguro1.verificar_vigencia()