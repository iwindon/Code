'''
Loops in python - Challenge 7
March 12, 2022
Ivan Windon
'''

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in shows:
    print(show)

for i in range(25,51):
    print(i)

for index, show in enumerate(shows):
    print(index)
    print(show)


num1 = [8,19,148,4]
num2 = [9,1,33,83]
ans = []

for i in num1:
    for j in num2:
        mult = i * j
        ans.append(i * j)
print(ans)

numbers = [15,25,8,3]

while True:
    answer = input("Guess a number or type q to quit: ")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed wrong")

