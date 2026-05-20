def char_remover(sentence, position):
    new_sentence = sentence[0]
    removed_chars = ""
    
    for index in range(1, len(sentence)):
        if index % position != 0:
            new_sentence += sentence[index]
        else:
            removed_chars += sentence[index]
            
    return new_sentence + removed_chars

# Taking user input
sentence = input("Sentence: ")
position = int(input("Position: "))

# Function call
print(char_remover(sentence, position))