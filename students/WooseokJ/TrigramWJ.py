import sys 
import random

#takes the words from the given file and returns it in a list
def words_from_file(filename):
    with open(filename, 'r') as textfile: 
        return [word.strip('\n') for l in textfile.readlines() 
                for word in l.split(' ')] 
#from the list makes a dictiondary to mix it in the next process
def build_trigrams_dict(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair not in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair] += [follower]
    return trigrams
#this mixes the words to create the new text
def build_text(pairs):
    random_text = []
    while len(random_text) < len(pairs):
        random_key = random.choice(list(pairs.keys()))
        value = pairs.get(random_key)
        random_text.append(list(random_key))
        random_text.append(value)
        new_list = [item for fixedlist in random_text for item in fixedlist]
        clean_text = " ".join(new_list)
#this is a promot that asks for the file that we want to scramble make sure to add .txt at the end of the file
        return clean_text
if __name__ == '__main__':
    filename = input('Please enter a filename:')
    words = words_from_file(filename)
    trigrams = build_trigrams_dict(words)
    new_text = build_text(trigrams)
    print (new_text) 
