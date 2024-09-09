import random
from time import sleep
class Livro():
    def __init__(self,titulo,autor,anoPublicacao):
        self.titulo= titulo
        self.autor= autor
        self.anoPublicacao= anoPublicacao


livro1 = Livro("Harry Potter","J.K Rowling",2006)
livro2 = Livro("Biblía sagrada","Apostolos", "Desconhecido")
livro3 = Livro("Naruto","Masashi Kishimoto",1997)

print(livro1.titulo)
print(livro1.autor)
print(livro1.anoPublicacao)
print(livro2.titulo)
print(livro2.autor)
print(livro2.anoPublicacao)
print(livro3.titulo)
print(livro3.autor)
print(livro3.anoPublicacao)

print("=-="*55)
#Questão 2
class Produto:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.nome = args[0]
            self.preco = args[1]
        elif len(args) == 1:
            self.nome = args[0]
            self.preco = 0
        else:
            self.nome = kwargs.get('nome', 'produtonome')
            self.preco = kwargs.get('preco', 0)

    def exibir_informacoes(self):
        print(f"Nome do Produto: {self.nome}, Preço: R${self.preco:.2f}")

produto1 = Produto("Teclado", 100)
produto2 = Produto("Mouse")


produto1.exibir_informacoes()
produto2.exibir_informacoes()


#Questao 3

class contaBancaria():
    def __init__(self,numero,titular,saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def depositar(self):
        deposito= int(input("Quanto você deseja depositar?"))
        print("Carregando...")
        sleep(1)
        self.saldo+= deposito
        print("Depósito feito com sucesso! Verifique sua conta novamente!")

    def sacar(self):
        saque= int(input("Quanto você deseja sacar?"))
        print("Carregando...")
        sleep(1)
        if self.saldo ==0:
            print("Você não tem saldo! Realize um depósito antes de tentar a ação.")
            return self.depositar()
        if self.saldo<saque:
            print("Seu saldo é insuficiente! Por favor, verifique sua conta.")
        else:
            self.saldo-=saque
            print(f"Ação realizada com sucesso! \nQuantidade Sacada: R${saque} \nTotal na conta disponível: R${self.saldo}")
        
    def mostrarConta(self):
        print("Carregando...")
        sleep(1)
        print(f"Número da conta: {self.numero}\n Titular da conta: {self.titular}\n Saldo da conta: {self.saldo}")
    def menu(self):
        while True:
            acao= input("Qual das ações deseja fazer? \n1.Verificar informações bancárias\n2.Fazer um depósito\n3.Fazer um saque\n4.Sair")
            print("-="*20)
            if acao=="1":
                self.mostrarConta()
                print("-="*20)
            if acao=="2":
                self.depositar()
                print("-="*20)
            if acao=="3":
                self.sacar()
                print("-="*20)
            if acao=="4":
                print("Obrigado por usar o Banco Kaintral! Volte sempre!")
                print("-="*20)
                break

            continuar=input("Deseja fazer mais alguma ação? \n1.Sim\n2.Não")
            if continuar=="1":
                print("-="*20)
                continue
            elif continuar=="2":
                print("Obrigado por usar o Banco Kaintral. Volte sempre!")
                print("-="*20)
                break

nome= input("Qual seu nome?")

conta1= contaBancaria(random.randint(10,99),nome,0)
print("Bem vindo ao Banco Kaintral!")
conta1.menu()
    




        
    