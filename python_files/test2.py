print 'time to play hangman'
secret = 'crocodile'
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns == 0:
      print 'The answer is', secret