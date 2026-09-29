import spacy
 
nlp = spacy.load("en_core_web_md")  # or en_core_web_lg
 
doc1 = nlp("The cat sat on the mat.")
doc2 = nlp("A kitten rested on a rug.")
 
score = doc1.similarity(doc2)
print(score)
 
#https://spacy.io/usage/spacy-101
#https://spacy.io/api/doc/
#https://campus.datacamp.com/courses/natural-language-processing-with-spacy/spacy-linguistic-annotations-and-word-vectors?ex=13
 
