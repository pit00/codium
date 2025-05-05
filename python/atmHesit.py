# https://www.codewars.com/kata/5d8108a41e94580023bd6419
def maximumThrill(atms: list[int]) -> int:
    maxThrill = max(atms) * 2
    
    size = range(len(atms))
    for i in size:
        for j in size:
            calc = atms[i] + atms[j] + abs(i - j)
            if calc > maxThrill:
                maxThrill = calc
    
    return maxThrill

maximumThrill(atms=[3, 1, 3])
# 8: $3 + $3 + $2 transferred between each (atms[0] and atms[2])
maximumThrill(atms=[2, 3, 4, 5])
# 10 :$5 + $5 + $0 transferred (atms[3] and atms[3] again)
maximumThrill(atms=[10, 10, 11, 13, 7, 8, 9])
# 26: $10 + $13 + $3 transfer between each (atms[0] and atms[3])
maximumThrill(atms=[2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8])
# 34: $10 + $12 + $12 transfer between each (atms[4] and atms[16])
