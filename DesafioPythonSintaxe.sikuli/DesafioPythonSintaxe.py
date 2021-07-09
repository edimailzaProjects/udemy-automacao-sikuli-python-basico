# -*- coding: utf-8 -*-

precoCarro = 6.0
precoMoto = 3.0

horasEstacionado = 1
ehCarro = True
totalAPagar = 0

if(horasEstacionado<=1):
    print("Estacionamento grátis")
    totalAPagar=horasEstacionado*precoCarro
else:
    if ehCarro:
        print("Carro")
        print(totalAPagar)
    else:
        print("Moto")
        print(totalAPagar)