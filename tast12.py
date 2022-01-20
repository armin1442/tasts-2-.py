scores = []

while True:
    score = float(input())
    if score == -1 :
        break
    scores.append(score)

average = sum(scores)  / len(scores)
print(average)