scores=[]

print("Number of students?", end=" ")
nofStudent=int(input())

for i in range (1, (nofStudent+1)):
    print("Student " + str(i) + ":", end=" ")
    score=int(input())
    scores.append(score)

avg=sum(scores)/len(scores)
print(f"Average = {avg:0.2f}")

for i in range(1, (nofStudent+1)):
    a="*"
    print(a*scores[i-1])
