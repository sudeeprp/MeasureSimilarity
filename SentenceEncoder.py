

def sentence_embedding(nlp, sentence):
    embedded_tokens = []
    encoded_tokens = nlp(sentence)
    for token_encoding in encoded_tokens:
        if not all(v == 0 for v in token_encoding.vector):
            embedded_tokens.append(token_encoding.vector)
        else:
            print("TODO: lookup " + str(token_encoding) + ". ")
    return embedded_tokens
