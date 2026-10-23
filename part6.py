for i in range(5):
    print(i)
scores = [70, 85, 60, 90, 45]
for score in scores:
    print("Score:", score)  
    
count=1
while count<=6:
    print(count)
    count+=2
    
scores = [30, 85, 23, 90, 45]
total = 0
for score in scores:
    total += score
    if score>=40:
        print("pass")
    else:
        print("fail")
average = total / len(scores)

print("Total:", total)
print("Average:", average)

scores = [30, 85, 23, 90, 45]
total = 0
passcount=0
failcount=0
for score in scores:
    total += score
    if score >= 40:
        passcount+=1
    else:
        failcount+=1
average=total/ len(scores)
print(total)
print(passcount)
print (failcount)
print(f"no pass: {passcount}")
print(f"no fail: {failcount}")




    