class ipvf():
  #Com essa função a gente tira os pontos do ip.
  def viraInt(trasIp, vetInt):
    for i in range(4):
      y = int(trasIp[i])
      vetInt.append(y)
    #print(vetInt[0],".",vetInt[1],".",vetInt[2],".",vetInt[3])

  
  
  def converterd_b(n):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    binario = int(binario)
    return binario
