count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("Loop ended")
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)
    numbers = [4, 2, 7, 1, 8, 3, 6]
search_for = 8

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}!")
        break
    print(f"Not {search_for}...")
    import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
       