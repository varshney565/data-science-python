#Table of 4
for i in range(1,11,1):
    # print(f"4*{i} = {4*i}")
    print("4*{} = {}".format(i,4*i))

print("-"*20)

for i in range(1,4):
    for j in range(1,4):
        print(i,j)
    print("***")

print("-"*20)
#probability of getting 'x' when rolling two dices
for x in range(1,13):
    count = 0;
    for one in range(1,7):
        for two in range(1,7):
            if one + two == x:
                count += 1
    print("probability of getting {} is {}".format(x,round(count/36*100,2)))