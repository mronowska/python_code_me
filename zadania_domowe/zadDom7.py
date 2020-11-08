def count_letters(word, points_list):
    common_letters = list(set(list(points_list)) & set(word))
    count = 0
    for char in word:
        for letter in common_letters:
            if char == letter:
                count += 1
    return count


word = input("Proszę bardzo o podanie wyrazu: ")
word_to_list = list(word)

#punktacja
#przyjmuję, że tylko te literki są wliczane do punktów, pozostałe to 0
point1 = "qwertyuiop"
point2 = "asdfghjkl"
point3 = "zxcvbnm"

result = count_letters(word, point1) * 1 + count_letters(word, point2) * 2 + count_letters(word, point3) * 3
print(result)