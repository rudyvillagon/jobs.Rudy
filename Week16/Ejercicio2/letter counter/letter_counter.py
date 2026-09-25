
def letter_counter(sentence):
    upper_count = 0
    lower_count = 0
    for letter_counter in sentence:
        if letter_counter.isupper():
            upper_count += 1
        elif letter_counter.islower():
            lower_count += 1
    return upper_count,lower_count

