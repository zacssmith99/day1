def greet(mame):
    print(f"hello: {mame}")
    print("welcome to world")
greet("mama")

def hello(name):
    print(f"nice to meet you {name}")
hello("jj")


def calculate_avg(scores):
    if len(scores)==0:
        return 0
    return sum(scores)/len(scores)
scores=[55,4,56]
result=calculate_avg(scores)#fun call p thone tr
print(result)



def totalscore(score):
    sum(score)
score=[11,22,33]
a=totalscore(score)
print(a)
def averagescore(score):
    if len(score)==0:
        return 0
    else:
        return sum(score)/len(score)
score=[55,67,67]
result=averagescore(score)
print(result)




def classify_score(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"
print(classify_score(90))
print(classify_score(55))
print(classify_score(25))

def count_passed(scores):
    passcount=0
    if scores>=40:
        passcount+=1
print(count_passed(45))


scores = [70, 85, 90]
scores.append(95)
print(scores)
scores[0] = 75
print(scores)
scores.remove(85)
print(scores)
print("Count:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))
        
scores=[55,80,35,90,65]
scores.append(75)
print(scores)
scores[2]=85
print(scores)
print(max(scores))
print(min(scores))

print(sum(scores)/len(scores))
for score in scores:
    if (score >=80 ):
        print("average",score)
        
        
#dictionaries
student = {
"name": "Su Su",
"age": 20,
"score": 88,
"passed": True
}
print(student["name"])
print(student["score"])
print(student["passed"])

student["course"] = "Python for AI"
student["score"] = 92
print(student.get("name"))
print(student.get("grade", "Not assigned"))
print(student)

