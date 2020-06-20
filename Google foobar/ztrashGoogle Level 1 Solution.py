def solution(h, q):
    def decr(numb):
        temp = numb[0]
        numb.clear()
        numb.append(temp - 1)

    finalList = list()
    numbers = 2 ** h
    ##number = numbers - 1
    number = list()
    number.append(numbers - 1)
    List = [0] * (numbers)
    index = 1
    List[1] = number[0]
    ##number -= 1
    decr(number)
    
    def rec(index, num):
        if (index < numbers) and (List[index] == 0):
            List[index] = num[0]
            ##num -= 1
            decr(num)
            rec((index * 2) + 1, num)
            rec((index * 2), num)
        
    rec((index * 2) + 1, number)
    rec((index * 2), number)
    #-----------------------------------------
    for x in q:
        if x in List:
            index = List.index(x)
            if (index / 2) < 1:
                finalList.append(-1)
            else:
                index /= 2
                index = int(index)
                finalList.append(List[index])
    return finalList

h = 3
q = [7,3,5,1]
answer = solution(h, q)
print(answer)
