import string

palin_word = input("Type in a word and we'll see if it's a palindrome. ").lower()
palin_word = palin_word.replace(" ", "")

for d in string.punctuation:
    palin_word = palin_word.replace(d, "")

countA = 0
countB = -1
letterA = palin_word[countA]
letterB = palin_word[countB]

for letter in palin_word:
    if countA + 1 == len(palin_word):
        print("Yay. Palindrome!")
        break
    elif letterA == letterB:
        countA += 1
        countB -= 1
        letterA = palin_word[countA]
        letterB = palin_word[countB]

    else:
        print("Es no bueno.")
        break


