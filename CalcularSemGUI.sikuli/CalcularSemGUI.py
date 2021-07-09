# -*- coding: utf-8 -*-
minhasContasReceber = 50 * 5
minhasContasPagar = 50
dinheiro = True

print(minhasContasReceber - minhasContasPagar)

if minhasContasPagar >= minhasContasReceber and dinheiro==False:
    print("Devo, não nego. pago quando puder")
    print(dinheiro)
elif minhasContasPagar == minhasContasReceber:
    print("Fiquei lisa!")
    dinheiro = False
    print(dinheiro)
else:
    print("Partiu Comer!")
    print(dinheiro)

        