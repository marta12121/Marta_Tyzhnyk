def solution(number):
    m = range(1,number)
    n = []
    for i in m :
        if i % 3==0 or i % 5 == 0 :
            n.append(i)
    return sum(n)
print(solution(10))