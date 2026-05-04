# Part C: Scoring Systems

users = ["Ali", "Mohammed", "Amine"]
user_score = []
score = 0

for user in users:
    score = int(input(f"# Enter the score for {user} (0–10) : "))
    user_score.append(score)
    while score < 0 or score > 10:
        print("=> Please enter a number between 0 and 10 !")
        score = int(input(f"# Enter the score for {user} (0–10) : "))
    if score >= 8 and score <= 10:
        print("=> High score!")
    elif score < 8 and score >= 5:
        print("=> Medium score!")
    elif score < 5 and score >= 0:
        print("=> Low score!")

n = len(user_score)

for i in range(n):
    for j in range(0, n-i-1):
        if user_score[j] > user_score[j+1]:
            temp = user_score[j]
            user_score[j] = user_score[j+1]
            user_score[j+1] = temp

for i in range(n):
    print(user_score[i])

print("# The highest score : ",user_score[n-1])

