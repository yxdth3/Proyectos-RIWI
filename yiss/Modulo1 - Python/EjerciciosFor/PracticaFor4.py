        
#Muestre solo los múltiplos de 3 del rango
suma=0
for i in range(1,101):
    
    if i % 2 != 0 and i % 3 != 0:
        suma += i
        print(i)
print(f"La  suma de los números impares, no multiplos de 3 es {suma}")