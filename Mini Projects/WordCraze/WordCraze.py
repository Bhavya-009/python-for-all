import random
import requests

def get_words_by_length(length):
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

    try:
        response = requests.get(url)
        response.raise_for_status()
        all_words = response.text.splitlines()

        words = [w.lower() for w in all_words if len(w) == length and w.isalpha()]
        print(f"✅ Loaded {len(words)} words of length {length}.")
        return words

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch words: {e}")
        return []

def choose_word(length):
    words = get_words_by_length(length)
    if not words:
        print("⚠️  Falling back to default words.")
        fallback = {
            3 : ["cat", "sun", "bat", "dog", "joy"],
            4 : ["tree", "love", "moon", "fish", "door"],
            5 : ["apple", "chair", "train", "grass", "smile"],
            6 : ["planet", "bottle", "animal", "garden", "friend"],
            7 : ["picture", "journey", "blanket", "capture", "freedom"]
        }
        words = fallback[length]
    return random.choice(words)


def user_guess(length):
    while True:
        guess = input(f"Enter your {length}-letter guess: ").lower().strip()
        if not guess.isalpha():
            print("⚠️  Only alphabetic characters are allowed!")
            continue
        if len(guess) != length:
            print(f"⚠️  Please enter exactly {length} letters!")
            continue
        return guess


def display_feedback(guess, target):
    result = []
    for i in range(len(target)):
        if guess[i] == target[i]:
            result.append(f"{guess[i]}✔")
        elif guess[i] in target:
            result.append(f"{guess[i]}❕")
        else:
            result.append(f"{guess[i]}✘")
    print("🔍 Feedback:", " ".join(result))


def word_guess_game():
    while True:
        try:
            length = int(input("Choose difficulty (3-7 letters): "))
            if length in (3,4,5,6,7):
                break
            else:
                print("⚠️  Enter a number between 3 and 7.")
        except ValueError:
            print("⚠️  Enter a valid number.")

    word = choose_word(length)
    max_tries = 6

    for attempt in range(1, max_tries + 1):
        print(f"\n⏳ Attempt {attempt}/{max_tries}")
        guess = user_guess(length)
        display_feedback(guess, word)

        if guess == word:
            print(f"\n🎉 Congratulations! You guessed the word '{word}' in {attempt} tries!")
            return

    print(f"\n🚩 Out of tries! The correct word was: {word}")


if __name__ == "__main__":
    while input("\n▶️  Start Playing (y/n)? ").lower() == "y":
        word_guess_game()
    print("\n👋 Thanks for playing! Goodbye.")
