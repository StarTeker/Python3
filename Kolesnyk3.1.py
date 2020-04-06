import os

def count(fname):
    freqs = {}
    with open(fname) as f:
        for line in f:
            for char in line:
                
                freqs.setdefault(char, 0)
                freqs[char] += 1
    return freqs                      

fname=input('Введите название файла ')
            
print(count(fname))            