# 🎯 WordCraze

**WordCraze** is a simple and fun word guessing game in Python.\
Your goal is to guess the correct word in limited attempts with helpful
feedback on your guesses.

------------------------------------------------------------------------

## 🚀 Features

-   Choose difficulty: 3 to 7 letter words\
-   Random word selection (fetched from a public word list or fallback
    words)\
-   Input validation (only alphabetic, correct length)\
-   Helpful feedback:
    -   ✔ Correct letter in correct position\
    -   ❕ Letter is in the word but wrong position\
    -   ✘ Letter is not in the word\
-   Up to 6 attempts per game\
-   Replay as many times as you want!

------------------------------------------------------------------------

## ⚡ How to Play

1.  Run the game: `bash     python wordcraze.py`

2.  Choose difficulty (3--7 letters).\

3.  Guess the word by typing a word of the chosen length.\

4.  Check feedback after each guess.\

5.  Win if you guess the correct word within attempts, or see the
    correct word if you run out of tries.

------------------------------------------------------------------------

## ✅ Example Gameplay

``` plaintext
▶️ Start Playing (y/n)? y  
Choose difficulty (3-7 letters): 5  

⏳ Attempt 1/6  
Enter your 5-letter guess: apple  
🔍 Feedback: a✘ p❕ p✘ l✔ e✔  

...  

🎉 Congratulations! You guessed the word 'place' in 4 tries!  
```

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.x\
-   `requests` library (for online word fetching)

Install dependencies with:

``` bash
pip install requests
```

------------------------------------------------------------------------

## 📚 Notes

-   If the word list is unavailable (network issues), the game uses a
    fallback word list.\
-   Designed for simple command-line fun and learning Python basics.

------------------------------------------------------------------------