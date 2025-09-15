word = input().strip()
if len(word) > 0:
    first_char = word[0]
    if first_char.islower():
        first_char = first_char.upper()
    result = first_char + word[1:]
    print(result)
else:
    print(word)