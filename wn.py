from nltk.corpus import wordnet

syns = wordnet.synset('bank')
# Sunset
print(syns[0].name())

# Just the word
print(syns[0].lemmas()[0].name())
# Definition
print(syns[0].definition())

# Examples
print(syns[0].examples())

synonyms = []
antonyms = []

for syns in wordnet.synset('good'):
    for l in syns.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

# word similarity

w1 = wordnet.synset("ship.0.01")
w2 = wordnet.synset("boat.0.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.0.01")
w2 = wordnet.synset("car.0.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.0.01")
w2 = wordnet.synset("cat.0.01")
print(w1.wup_similarity(w2))
