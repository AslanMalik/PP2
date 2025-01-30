
def unique_word(spisok):
    unique_spisok = []
    for c in spisok:
        if c.lower() not in [word.lower() for word in unique_spisok]:
            unique_spisok.append(c)
    return unique_spisok

word_list = input().split()
print(unique_word(word_list))