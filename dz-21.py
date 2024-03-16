def popular_words(text, words):
    l_text = text.lower()
    word_counts = {word.lower(): 0 for word in words}
    for word in l_text.split():
        if word in word_counts:
            word_counts[word] += 1
    return word_counts


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
