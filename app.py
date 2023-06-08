goals = int(input("Enter the total number of goals: "))
target = int(input("Enter your daily target: "))
goals_acheived = int(input("Enter the number of goals achieved today: "))

goals_left = goals - goals_acheived

if goals_left < target:
    print("You're a superstar! Keep it up!")

elif goals_left == target:
    print("Great job!")

else:
    print("Keep at it!")

target_hit = goals_acheived >= target
if target_hit == True:
    print("You hit today's target")

else:
    print("Only " + str(target - goals_acheived) + " goals left to hit today's target!")

if goals_left > 0:
    print("You have only " + str(goals_left) + " goals left to accomplish on your list")

elif goals_left == 0:
    print("Great Job! You have no more goals left")

else:
    print("Error, we can't find your goals")
