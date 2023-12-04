import string

def word_frequency(sentence):
    words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# Testing the function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
