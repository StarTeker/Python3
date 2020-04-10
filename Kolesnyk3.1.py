def zsuv(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
 
nums = [int(i) for i in input('Введите список цифр: ').split()]
k=int(input('Введите число N, на которое сделать сдвиг списка: '))

zsuv(nums,k)
print(nums)
