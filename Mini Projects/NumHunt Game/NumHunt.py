import random
import os
import time
import datetime

print("Lets start the game !!", "Max attempts : 10")
print("\nEasy : 1 to 100 \nMedium : 1 to 500 \nHard : 1 to 1000 \nCustom : Enter your own Lower and Upper Bound")


def game():
    # Setting the answer as per the level
    while True:
        user_level_input = input("\nEasy(e), Medium(m), Hard(h), Custom(c) : ").lower()
        if user_level_input in ("e", "m", "h", "c"):
            if user_level_input == "e":
                computer_number = random.randint(1, 100)
            elif user_level_input == "m":
                computer_number = random.randint(1, 500)
            elif user_level_input == "h":
                computer_number = random.randint(1, 1000)
            elif user_level_input == "c":
                while True:
                    try:
                        lower_bound = int(input("Enter Lower Bound : "))
                        upper_bound = int(input("Enter Upper Bound : "))
                        if lower_bound >= upper_bound:
                            print("Upper bound must be greater than lower bound.")
                            continue
                        computer_number = random.randint(lower_bound, upper_bound)
                        break
                    except ValueError:
                        print("Enter valid number")
            break
        else:
            print("\nEnter valid level")
    print(computer_number)
    score = 10   # start with 10 points
    user_input = None

    # --- Hints ---
    hint_taken = False
    another_hint_taken = False
    hints = 0

    def hint():
        if computer_number % 2 == 0:
            print("💡 The answer is EVEN")
        else:
            print("💡 The answer is ODD")

    def another_hint():
        for i in range(2, 11):
            if computer_number % i == 0:
                print(f"💡 Divisible by {i}")

    def ask_hint():
        nonlocal score, hint_taken, hints
        if not hint_taken:
            want_hint = input("💡 Do you want a HINT (y/n) (reduces 1 point)? ")
            if want_hint.lower() == "y":
                hint()
                hint_taken = True
                hints += 1
                score = max(0, score - 1)

    def ask_another_hint():
        nonlocal score, another_hint_taken, hint_taken, hints
        if not another_hint_taken and hint_taken:
            want_another_hint = input("💡 Do you want another HINT (y/n) (reduces 1 point)? ")
            if want_another_hint.lower() == "y":
                another_hint()
                another_hint_taken = True
                hints += 1
                score = max(0, score - 1)

    # --- Game loop ---
    start = time.time()
    for guess in range(10):
        try:
            if score == 0:
                print("Your Score is 0! Game over.")
                break
            else:
                user_input = int(input("\nEnter your guess : "))
                if user_input > computer_number:
                    print("❌ OOPS! Your guess is HIGHER than the answer!",
                        f"\n⏳ Attempts left : {9 - guess}")
                    score -= 1 # lose 1 point per wrong try
                    ask_hint()
                    ask_another_hint()

                elif user_input < computer_number:
                    print("❌ OOPS! Your guess is LOWER than the answer!",
                        f"\n⏳ Attempts left : {9 - guess}")
                    score -= 1  # lose 1 point per wrong try
                    ask_hint()
                    ask_another_hint()

                else:
                    print("🎉 CONGRATSS! Your guess was CORRECT!",
                        f"guessed in {guess+1} tries")
                    break

            if guess == 9:
                print("\n❌ You ran out of guesses!")

        except ValueError:
            print("Enter valid number")

    end = time.time()

    time_taken = int(end - start)

    # Final score already reduced by guesses + hints
    final_score = max(0, score)

    if user_input == computer_number and time_taken <= 10:
        final_score += 1
        print("⚡ Speed Bonus! +1 points")

    def score_file(final_score):
        filename = "scores.txt"
        # Create file only once
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write("\n--- Leaderboard ---\n")
        # Append the new score
        with open(filename, "a") as f:
            f.write(f"{final_score} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n")
        # Show leaderboard
        with open(filename, "r") as f:
            print(f.read())

    print("\nYour final guess :", user_input,
          "\nComputer's number : ", computer_number,
          "\nHints taken : ", hints,
          "\nTime taken : ", time_taken, "seconds",
          "\nYour score : ", final_score)

    score_file(final_score)


def main():
    while True:
        game()
        play_again = input("\nDo you want to start the game again? (y/n): ").lower()
        if play_again == "y":
            continue
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
