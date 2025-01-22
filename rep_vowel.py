sentence = "Python is fun and Python is easy to learn!"
vowels = "aeiou"
new_sentence = ""

for letter in sentence:
    if letter.lower() in vowels:
        new_sentence += letter.upper()
    else:
        new_sentence += letter

print(new_sentence)
