def is_leap(year):
    leap = False
    a = year
    if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
        leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))