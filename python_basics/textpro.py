def sentence_maker(phrase):
    interrogatives = ("how", "why", "when", "what")
    if phrase.lower().startswith(interrogatives):
        phrase += '?'
    else:
        phrase += '.'
    return phrase.capitalize()

#print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
