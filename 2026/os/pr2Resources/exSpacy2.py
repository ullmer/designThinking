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

str3, str4, str5, str6 = "apples", "oranges", "aardvarks", "elephants"
doc3, doc4, doc5, doc6 = nlp(str3), nlp(str4), nlp(str5), nlp(str6)

str7 = "African ant bear"
doc7 = nlp(str7)

score34 = doc3.similarity(doc4)
score35 = doc3.similarity(doc5)
score56 = doc5.similarity(doc6)
score57 = doc5.similarity(doc7)

printSim(str3, str4, score34)
printSim(str3, str5, score35)
printSim(str5, str6, score56)
printSim(str5, str7, score57)
 
#https://spacy.io/usage/spacy-101
#https://spacy.io/api/doc/
#https://campus.datacamp.com/courses/natural-language-processing-with-spacy/spacy-linguistic-annotations-and-word-vectors?ex=13

#python3 -m venv ~/venv
#source ~/venv/bin/activate
#python3 -m pip install spacy
#python3 -m spacy download en_core_web_md 
