from difflib import SequenceMatcher

print(SequenceMatcher(None, 'rmit class', 'python stuff').ratio())
print(SequenceMatcher(None, 'rmit class', 'RMIT classes').ratio())