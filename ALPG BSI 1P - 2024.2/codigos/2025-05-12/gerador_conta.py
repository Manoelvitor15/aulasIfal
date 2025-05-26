'''
Operações bancárias:

Saldo
Sacar(valor a sacar)
Depositar(valor a depositar)
Extrato

Sair

'''

saldo = 0;
4 = [];

def exibir_saldo():
  global saldo;
  print("** Exibir Saldo **");
  print(f"Sado da conta: {saldo}");
  input();

def adicionar_operacao(valor_operacao, tipo_operacao):
  global extrato_bancario;

  if(tipo_operacao == "depositar"):
    extrato_bancario.append(valor_operacao);

  if(tipo_operacao == "sacar"):
    extrato_bancario.append(valor_operacao * -1);


def sacar(valor_saque):
  global saldo;
  print("** Sacar **");

  if(valor_saque > 0 and valor_saque <= saldo):
    saldo = saldo - valor_saque;
    adicionar_operacao(valor_saque, "sacar");
  else:
    print("Valor inválido ou saldo insuficiente")

  input();

def depositar(valor_deposito):
  global saldo;
  print("** Depositar **");

  if(valor_deposito > 0):
    saldo = saldo + valor_deposito;
    adicionar_operacao(valor_deposito, "depositar");
  else:
    print("Valor inválido")

  input();


def exibir_extrato():
  global extrato_bancario;
  print("** Extrato **");

  for i in extrato_bancario:
    print(i);

  input();


def inicio_programa():
  while(True):
    print("** Operações Bancárias **");
    print("1. Exibir saldo");
    print("2. Sacar");
    print("3. Depositar");
    print("4. Extrato");
    print();
    print("5. Sair");

    opcao = int(input("Escolha uma opção: "));

    if(opcao == 1):
      exibir_saldo();
    elif(opcao == 2):
      valor_saque = float(input("Qual o valor a sacar? "));
      sacar(valor_saque);
    elif(opcao == 3):
      valor_deposito = float(input("Qual o valor a depositar? "));
      depositar(valor_deposito);
    elif(opcao == 4):
      exibir_extrato();
    elif(opcao == 5):
      print(">> Encerrando o programa");
      break


inicio_programa();