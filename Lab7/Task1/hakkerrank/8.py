if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res = []
    for i in range(x + 1):
        for j in range(y + 1):
            arr = []
            for k in range(z + 1):
                if i + j + k == n:
                    continue    
                arr.append(i)
                arr.append(j)
                arr.append(k)
                res.append(arr)
                arr = []
        
    print(res)