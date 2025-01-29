# Iterates through each character of the input string

def alternate_characters(input_string):
    result = []
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)

input_string1 = "Hello World"
print("Orininal: ",alternate_characters(input_string1))
print("Alternate case characters:", alternate_characters(input_string1))


# Alternates words using split()

def alternate_words(input_string):
    words = input_string.split()
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

input_string2 = "I am learning to code"
print("\nOriginal string:", input_string2)
print("Alternate case words:", alternate_words(input_string2))