import random

def play_game():
    secret_number = random.randint(1, 10)
    guesses = 0

    print("\n🎯 I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses += 1

            match guess:
                case g if g == secret_number:
                    print(f"🎉 Congratulations! You guessed it in {guesses} tries.")
                    break

                case g if g > secret_number:
                    print("📉 Oops, your guess is a bit high. Try again!")

                case g if g < secret_number:
                    print("📈 Nope, your guess is a bit low. Give it another shot!")

        except ValueError:
            print("⚠️ Please enter a valid number.")

while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("👋 Thanks for playing! See you next time.")
        break