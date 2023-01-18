# Importing spacy and setting up module.
import spacy
nlp = spacy.load("en_core_web_md")

# cat monkey banana.
# Cat and monkey are both animals, monkeys love bananas. Cats and banana don't have much in common here.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# added bread and chocolate here.
# Similarities between cat monkey and banana detailed above.
# apple, bread, banana, and chocolate all foods.
# banana and bread similar because this is a type of cake.
# banana and apple similar because both fruits.
# Not sure why chocolate and cat has higher similarity than chocolate and monkey?
tokens = nlp('cat apple monkey banana bread chocolate ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#----------------------------------------------------
# Generally the differences between en_core_web_sm and en_core_web_md, are that the md model is larger and more accurate.
# Assume the sm refers to small, md to medium, and lg to large. Meaning there must be more words trained in the model.