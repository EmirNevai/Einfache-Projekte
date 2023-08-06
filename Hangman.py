import random

words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'goethe', 'mercedes-Benz', 'yunus emre', 'paris', 'orient']

word = random.choice(words)

display = ['_'] * len(word)

num_guesses = 6

incorrect_guesses = []

while num_guesses > 0 and '_' in display:
    print(' '.join(display))
    print(f'Incorrect guesses: {" ".join(incorrect_guesses)}')
    print(f'Guesses left: {num_guesses}')
    
    guess = input('Enter a letter: ').lower()
    
    if len(guess) != 1:
        print('Please enter a single letter.')
    elif guess in incorrect_guesses or guess in display:
        print('You already guessed that letter.')
    elif guess not in word:
        print('Incorrect!')
        num_guesses -= 1
        incorrect_guesses.append(guess)
    else:
        print('Correct!')
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

if num_guesses == 0:
    print('You lost!')
else:
    print(f'You won! The word was "{word}".')
