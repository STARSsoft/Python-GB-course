'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

def fibo_gen():
    n1,n2=0,1
    while (True):
        yield n1
        n1,n2=n2,n2+n1
        

fg=fibo_gen() 
for i in range(10):   
  print (next(fg),end=" ")
   
      
    
