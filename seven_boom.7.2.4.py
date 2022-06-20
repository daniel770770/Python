
def seven_boom(end_number):
    x= [0] 
    for i in range(1, end_number+1):
        x.append(i)
        if i%7 == 0:
            x[i] = "boom"
    k=7 
    for i in range(1, end_number+1, 1):
        if i == k: 
            x[i]= "boom"
            k = k + 10
    return x
t= (seven_boom(40))
print(t)
