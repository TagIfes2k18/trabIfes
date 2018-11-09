from functions import ipvf


vetInt = []

vetBin = []

#IpCliente = "192.168.15.18" 
IpCliente = input("Informe um IP: ")
trasIp = IpCliente.split(".") #Aqui ele pega o IP e elemina os pontos.

print("==== CALCULADORA DE IPV4 ====")
print("\n Seu IP: {}".format(IpCliente))
print("\n")
ipvf.viraInt(trasIp, vetInt)

for i in range(4):
    x = vetInt[i]
    a = ipvf.converterd_b(x)
    vetBin.append(a)
print(vetBin[0],".",vetBin[1],".",vetBin[2],".",vetBin[3])
