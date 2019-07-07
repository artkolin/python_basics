"""
Simple word count
"""

def word_count(text):
    """
    Get text and return dictionary
    :param text:
    :return:
    """
    text = text.strip().split(' ')
    dict = {}
    for word in text:
        print(word)
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict



if __name__ == "__main__":
    user_text = input('Provide a text: ')
    print(word_count(user_text))
