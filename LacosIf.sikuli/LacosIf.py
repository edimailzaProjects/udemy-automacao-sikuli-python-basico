# -*- coding: utf-8 -*-
nome = "Edi"
minhasContasReceber = 50 * 5
minhasContasPagar = 50
dinheiro = True

if nome == "Edi":
    if minhasContasPagar >= minhasContasReceber and dinheiro==False:
        print("Devo, não nego. pago quando puder")
        print(dinheiro)
        print(minhasContasReceber - minhasContasPagar)
    elif minhasContasPagar == minhasContasReceber:
        print("Fiquei lisa!")
        dinheiro = False
        print(dinheiro)
        print(minhasContasReceber - minhasContasPagar)
    else:
        print("Partiu Comer!")
        print(dinheiro)
        print(minhasContasReceber - minhasContasPagar)
else:
    print("Meu dinheiro não é da sua conta")