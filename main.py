def close10(x, y ):
    if abs(10 - x) < abs(10 - y):
        return(x)
    elif abs(10 - y) < abs(10 - x):
        return(y)
    else:
        return(0)

print(close10(5, 13))
print(close10(5, 15))
print(close10(1, 135))