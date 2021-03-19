from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similar("Cipher", "python stuff"))
print(similar("Cipher", "cypher"))