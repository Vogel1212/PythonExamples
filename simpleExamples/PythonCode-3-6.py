#studying while and for
#
# escreve um programa com 2 variables, var1 = um pequeno numero, var2 um numero maior, var3 tambem pequeno. 
# faz um loop ( pode ser while ou for) imprimir var1 (print) se pode dividir com var3. caso nao, nao imprimir nada.  
# addicionar var1 com 1 ( nao var3). continuar ate var1 nao mais é menor que var2. output pra variables 1,20,3 ( usa outros numers, isso é meu exemplo) : 3,6,9,12,15,18
#
#exemplo desafio 2

#var1,var2,var3 = 1,20,3
#while var1 / var2:
#    print(var1)
#    var1 += var1
import operator


var1,var2 = 7,3

r=var1 % var2
#print("mod: ", r)

if (var1 % var2) == 0:
    print("true")

elif (var1 % var2) == 1:
    print("false")

#while var1 < var3:
    #print (operator.mod(var1,var2))
