saldo = 0
extrato = []
limite=500
n_saques=0 
LIMITES_SAQUE= 3

def saque():
  global saldo
  global extrato
  print('Qual Valor deseja sacar? :')
  valor=float(input('Valor:'))
  if saldo == 0 :
    print('Não possui valores disponiveis para saque!')
  elif valor > limite :
    print('Máx de valor de saque é 500, por favor tente novamente')
  elif valor < limite :
    saldo = saldo - valor 
    extrato.append(valor) 
    
    print('Seu novo saldo é :',saldo)
    print(extrato)
    
def deposito():
  global saldo
  global extrato
  print('Qual Valor deseja depositar? :')
  valor1=float(input('Valor:'))
  saldo = saldo + valor1
  extrato.append(valor1)
  
  print('Deposito Realizado com sucesso!')
  print('Seu saldo é : R$',saldo)

def main () :
  while True :
   print('-'*40)
   print('Seja Bem-Vindo ao Banco Daniel Moneys!')
   print('Escolha uma opção:')
   print('-'*40)
   print()
   print('[1]- Extrato')
   print('[2]- Saque')
   print('[3]- Deposito')
   print('[4]- Sair')

   resp=int(input('Sua opção:'))
   print()
   if resp == 1 :
     for elemento in extrato:
    print(" R$ {}".format(elemento).replace('.', ','))
   
   elif resp == 2 :
     global n_saques 
     n_saques +=1
     if n_saques > 3 :
       print('Limites de saque ultrapassado por favor tente amanhã')
     else:
       saque()
      
   elif resp == 3 :
     deposito()

   elif resp == 4 :
     break
  
   else :
    print('Opção invalida,por favor tente novamente')
  
main()