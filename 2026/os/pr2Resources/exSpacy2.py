import spacy

def printSim(str1, str2, score):
  print("Similarity between <" + str1 + "> and <" + str2 + ">: " + str(score))

print("loading spacy model") 
nlp = spacy.load("en_core_web_md")  # or en_core_web_lg
print("model loaded")
 
str1 = "The cat sat on the mat."
str2 = "A kitten rested on a rug."
doc1, doc2 = nlp(str1), nlp(str2)

score = doc1.similarity(doc2)
printSim(str1, str2, score)

str3, str4, str5 = "apples", "oranges", "aardvarks"
doc3, doc4, doc5 = nlp(str3), nlp(str4), nlp(str5)

score34 = doc3.similarity(doc4)
score35 = doc3.similarity(doc5)

printSim(str3, str4, score34)
printSim(str3, str5, score35)
 
#https://spacy.io/usage/spacy-101
#https://spacy.io/api/doc/
#https://campus.datacamp.com/courses/natural-language-processing-with-spacy/spacy-linguistic-annotations-and-word-vectors?ex=13
#python -m spacy download en_core_web_md 
