textArray = [str(i) for i in input().split()]
popularWord = ""
countPopularWord = 0
longWord = ""
lengthLongWord = 0

for word in textArray:
    if textArray.count(word) > countPopularWord:
        countPopularWord = textArray.count(word)
        popularWord = word

    if len(word) > lengthLongWord:
        lengthLongWord = len(word)
        longWord = word

print(popularWord, longWord)
