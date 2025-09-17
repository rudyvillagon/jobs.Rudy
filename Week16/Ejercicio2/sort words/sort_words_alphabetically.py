def sort_sentence(sentence):
    sort_words = ""
    
    final_sentence =  sentence.split("-")
    
    sort_words = sorted(final_sentence) 
    sort_words = "-".join((sort_words))
    return sort_words

