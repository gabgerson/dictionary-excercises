# put your code here.

def get_words(file_name):


    text_file = open(file_name)

    word_list = []
    
    for line in text_file:

        line = line.rstrip()

        word = line.split(" ")

        word_list.extend(word)

    #file_name.close()
    return word_list


def count_words(file_name):

    word_list = get_words(file_name)
    word_counts = {}

    for word in word_list: 
        
        word_counts[word]  = word_counts.get(word, 0) + 1

    for k, v in word_counts.items():

        print(f"{k} {v}")



count_words("test.txt")
#print(count_words("twain.txt"))


