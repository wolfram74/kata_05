from spell_checker import *
import random

tester = SpellChecker()
words = ['fart', 'flatulence', 'sandwich', 'hug', 'tired']
print(tester.dictionary.items)
for word in words:
    print(word, tester.valid(word))

def random_word():
    letters = [chr(number) for number in range(97, 97+26)]
    return ''.join(random.sample(letters, 5))

hits = 0
included = []
for run in range(10**4):
    gibberish = random_word()
    if tester.valid(gibberish):
        hits+=1
        included.append(gibberish)

print(hits, included)
