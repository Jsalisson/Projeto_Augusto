L_g = 5
dis_cliente = 10
km_L = 30 #quilometragem que a moto faz por litro
dis_parada = 13
dis_casa = 3
dias_mes = 20
repeticao = 1
manutencao = 2.5


#quantidade de km/L da moto em relação a gasolina
KM_l = (km_L/L_g) #6Km que vale a 1 real de gasolina

#soma de toda a Km do dia multiplicada pela quantidade de vezes que se faz o trajeto no dia
Km_t = (dis_cliente + dis_parada + dis_casa) * repeticao

KM = (Km_t/KM_l) # quanto a moto gasta no dia levando o passageiro

#multiplicar a quantidade de gasolina gasta no dia pela quantidade de dias do mês 
gasto = KM*dias_mes

lucro = gasto + (gasto*manutencao)

print(Km_t)
print(KM)
print(gasto)
print(lucro)
