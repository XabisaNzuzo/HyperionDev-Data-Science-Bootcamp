import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define garden path sentences
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The cat chased the mouse on the table.",
    "The bank by the river is closed today."
]

# Tokenize and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Entity: {token.ent_type_}")
    print()

# Explain entities
print(spacy.explain("PERSON"))
print(spacy.explain("ORG"))

# Comment on two entities
# 1. Entity: PERSON
# Explanation: This entity represents a person's name.
# Did it make sense in terms of the word associated with it? Yes, it makes sense as it correctly identified names like "Mary" and "Jill."

# 2. Entity: ORG
# Explanation: This entity represents an organization, company, or institution.
# Did it make sense in terms of the word associated with it? Yes, it makes sense as it correctly identified "Band-Aid" and "Mississippi" as entities related to organizations or locations.

#%%
