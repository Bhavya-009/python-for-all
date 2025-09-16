import random
import os
from datetime import datetime


class RockPaperScissors:
    def __init__(self):
        self.score = 0
        self.play_rounds = 0
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.options = ["Rock 🪨", "Paper 📄", "Scissor ✂️"]
        self.filename = "my_scores.txt"
        self.score_file()

    def score_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("\n--->  🪨  📄 ✂️   <---\n")

    def get_rounds(self):
        while True:
            try:
                user_rounds = int(input("\nBest of (3/5/7) rounds OR Custom rounds (0): "))
                if user_rounds in (0, 3, 5, 7):
                    if user_rounds == 0:
                        play = int(input("\nHow many rounds do you want to play?: "))
                        if play <= 0:
                            print("\nPlease enter a positive number!")
                            continue
                        print("\nLET'S PLAY!", "\n1: Rock 🪨  2: Paper 📄 3: Scissor ✂️")
                        return play
                    else:
                        print("\nLET'S PLAY!", "\n1: Rock 🪨  2: Paper 📄 3: Scissor ✂️")
                        return user_rounds
                else:
                    print("\nEnter valid rounds.")
            except ValueError:
                print("\nInvalid input, please enter a number!")


    def play_round(self, play, round_number):
        computer_choice = random.randint(1, 3)
        try:
            user_input = int(input("\nEnter your choice (1/2/3): "))
            if user_input in (1, 2, 3):
                print(f"🎯 Round {round_number}/{play}")

                if computer_choice == user_input:
                    self.draw += 1
                    print("Draw 🤝")
                elif (computer_choice == 1 and user_input == 3) or \
                     (computer_choice == 2 and user_input == 1) or \
                     (computer_choice == 3 and user_input == 2):
                    self.lose += 1
                    print("You Lose ❌")
                else:
                    self.win += 1
                    self.score += 1
                    print("You Win 🥇")

                print("Your choice     :", self.options[user_input - 1])
                print("Computer choice :", self.options[computer_choice - 1])
            else:
                print("\nInvalid Input (must be 1, 2, or 3)")
        except ValueError:
            print("\nInvalid Value (must be a number)")

    def save_and_show_score(self):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{self.score}/{self.play_rounds} | {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")

        with open(self.filename, "r", encoding="utf-8") as f:
            print("\n📋 Leaderboard:")
            print(f.read())

    def show_final_result(self):
        print("\n🏆 Final Score:", f"{self.score}/{self.play_rounds}")
        if self.win > self.lose:
            print(f"📈 Wins : {self.win}, Loses : {self.lose}, Draws : {self.draw}")
        elif self.lose > self.win:
            print(f"📉 Wins : {self.win}, Loses : {self.lose}, Draws : {self.draw}")
        else:
            print(f"😐 Wins : {self.win}, Loses : {self.lose}, Draws : {self.draw}")

        win_rate = int((self.win / self.play_rounds) * 100) if self.play_rounds else 0
        print(f"📊 Win Rate : {win_rate}%")

    def start_game(self):
        print("\nLet's play Rock Paper Scissors!\nType:\n1: Rock 🪨\n2: Paper 📄\n3: Scissor ✂️")

        rounds = self.get_rounds()
        self.play_rounds = rounds

        for round_number in range(1, (rounds + 1)):
            self.play_round(rounds, round_number)

        self.show_final_result()
        self.save_and_show_score()


if __name__ == "__main__":
    while True:
        play_again = input("\nStart playing? (y/n): ").lower()
        if play_again == "y":
            game = RockPaperScissors()
            game.start_game()
        else:
            print("🥳 Thank you for playing!")
            break
