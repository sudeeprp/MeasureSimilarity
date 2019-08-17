import spacy
from scipy import spatial


def showAvgSentenceDistance(spec, test):
    print('---------------------')
    print(test)
    print('distance = ' + str(spatial.distance.cosine(nlp(spec).vector, nlp(test).vector)))

print('Loading pretrained embeddings')
nlp = spacy.load('en_core_web_md')
print('loaded')
spec = "Convert to DICOM for interoperability"
tests = [ 'converted object is DICOM compliant',
          'mandatory attributes should be present',
          'converted object has all attributes',
          'privacy attributes must not be logged']
for test in tests:
    showAvgSentenceDistance(spec, test)


# It's that simple - all of the vectors and words are assigned after this point
# Get the vector for 'text':
#print(doc[2].vector)
# Get the mean vector for the entire sentence (useful for sentence classification etc.)
#print("\nSentence mean vector")
#print(doc.vector)
