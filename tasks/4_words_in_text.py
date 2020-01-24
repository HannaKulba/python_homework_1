text_array = input().split()
popular_word = ""
count_popular_word = 0
long_word = ""
length_long_word = 0

for word in text_array:
    if text_array.count(word) > count_popular_word:
        count_popular_word = text_array.count(word)
        popular_word = word

    if len(word) > length_long_word:
        length_long_word = len(word)
        long_word = word

print(popular_word, long_word)
