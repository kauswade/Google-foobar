def decr(num):
    temp = num[0]
    num.pop()
    num.append(temp - 1)

def solution(h, q):
    finalAnswers = list()
    numbers = 2 ** h
    number = list()
    number.append(numbers - 1)
    List = [0] * numbers
    index = 1
    List[index] = number[0]
    decr(number)

    def recur(index, number):
        if (index < numbers) and (List[index] == 0):
            List[index] = number[0]
            decr(number)
            recur((index * 2) + 1, number)
            recur(index * 2, number)

    recur((index * 2) + 1, number)
    recur(index * 2, number)
    #print(List)
    #---
    for x in q:
        index = List.index(x)
        if (index / 2) < 1:
            finalAnswers.append(-1)
        else:
            index /= 2
            index = int(index)
            finalAnswers.append(List[index])
    return finalAnswers

#---
# h = 3
# q = [7,3,5,1]

# h = 5
# q = [19,14,28]

# h = 3
# q = [1,4,7]

# print(solution(h, q))
