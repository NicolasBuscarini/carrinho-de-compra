cod= 3
c = 0
total= 0
while cod != 0:
    cod = int(input("Digite o numero do código do produto: "))
    qt = float(input("Digite a quantidade de compra do produto: "))
    if cod == 1:
        preço = float(0,5)
        c += 1*qt
    elif cod == 2:
        preço = float(1)
        c += 1*qt
    elif cod == 4:
        preço = float(4)
        c += 1*qt
    elif cod == 5:
        preço = float(7)
        c += 1*qt
    elif cod == 4:
        preço = float(9)
        c += 1*qt
        
    elif cod ==0 :
         print ("""*******************************************************************
********************** Fim das compras! ***************************
*******************************************************************     """)
    else:
        print ("""*******************************************************************
*************** Código invalido! Tente outro código ***************
*******************************************************************     """)
        preço = 0
    total = float( total + (preço*qt))
print(" Total de produtos no carrinho: ", c)
print(" Valor total das comprar: R$", total)
