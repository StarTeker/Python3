def fac(n):
     if n == 0:
          return 1
     return fac(n-1) * n
 
    
k=int(input("Введите число, факториал которого нужно найти"))
print(fac(k));