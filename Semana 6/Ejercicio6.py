

def sort_sentence():
    sort_words = ""
    sentence = "python-variable-funcion-computadora-monitor"
    final_sentence =  sentence.split("-")
    
    sort_words = sorted(final_sentence) 
    sort_words = "-".join((sort_words))
    return sort_words

result_sort = sort_sentence()
print((result_sort))
    