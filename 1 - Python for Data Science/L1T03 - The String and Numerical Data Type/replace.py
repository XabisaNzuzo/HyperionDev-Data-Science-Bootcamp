# Declare sentence

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# This will replace the ! with blank space.

new_sentence = sentence.replace("!", " ")
print(new_sentence)

# This line comverts the sentance to UPPERCASE

uppercase_sentence = new_sentence.upper()

# This line reprints the sentance to UPPERCASE

print(uppercase_sentence)

# This prints out the sentence in reverse using slicing

reversed_sentence = sentence[::-1]
print(reversed_sentence)
