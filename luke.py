def get_luke(n):
    res = [2,1]
    for i in range(2, n):
        res.append(res[i-1]+res[i-2])
    return res

def get_fibb(n):
    lukes = get_luke(n+1)
    return (lukes[n-2]+lukes[n])//5

print(get_fibb(50))