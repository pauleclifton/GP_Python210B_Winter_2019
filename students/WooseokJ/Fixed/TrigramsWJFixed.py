import random
import string


#takes the words from the given file and returns it in a list
def read_data(filename):
    with open(filename, 'r') as f_input:
        row_index = []
        for j, line in enumerate(f_input):
            if line[0:4] == '*** ':
                row_index.append(j)
        f_input.seek(0)
        data_list = f_input.readlines()[row_index[0]+1:row_index[1]]
        data = " ".join(data_list)
    return data

#part 1 of fixing the words ficing capitals and punctuation
def make_words(data):
    words = data.split()
    proper_nouns_list = clean_text(text_file)
    no_capital = []
    for word in words:
        if word.islower():
            no_capital.append(word)
        elif word[0] + word[1:].lower() in proper_nouns_list:
            no_capital.append(word[0]+word[1:].lower())
        else:
            no_capital.append(word.lower())
    punctuation = []
    for word in no_capital:
        punctuation.append(strip_punctuation(word))
    return punctuation

#part 2 of cleaning the words fixes other weird words seen
def clean_text(file):
    fixed_words = []
    with open(file) as f:
        header = False
        for lines in f:
            if lines.startswith('***') or lines.startswith('\n'):
                header = True
                continue
            else:
                words = lines.rstrip('\n').split()
                for word in words:
                    if word.isupper() and len(word) > 1:
                        continue
                    elif word.startswith('www') or word.startswith('http'):
                        continue
                    elif '[' in word or ']' in word :
                        continue
                    else:
                        fixed_words.append(word.strip('()').strip('""'))
    return fixed_words


def strip_punctuation(word):
    punctuation = ''
    for i, letter in enumerate(word):
        if letter not in string.punctuation or \
                (i in range(1, len(word)-1) and word[i-1] not in string.punctuation
                 and word[i+1] not in string.punctuation):
            punctuation += letter
    return punctuation


def build_trigrams(words):
    trigrams = {}
    for i in range(len(words)-2):
        pair = tuple(words[i:i + 2])
        follower = words[i + 2]
        if pair not in trigrams:
            trigrams[pair] = [follower]
        else:
            trigrams[pair] += [follower]
    return trigrams


def build_text(word_pairs, words):
    key_text = (words[0], words[1])
    new_text = list(key_text)
    word_count = 0
    while True:
        key_text = tuple(new_text[-2:])
        if word_count > 1000:
            break
        elif key_text in word_pairs:
            new_text += [random.choice(word_pairs[key_text])]
            word_count += 1
        else:
            break
    return new_text

#complies all the fixes and words and makes it into a triagram with 100 length and makes the file output
def compile_list(new_text):
    with open('output.txt', 'w') as f_output:
        line = new_text[0]
        for word in new_text[1:]:
            if len(word)+len(line)+1 <= 100:
                line = line + ' ' + word
            else:
                line += '\n'
                f_output.write(line)
                line = word
        f_output.write(line)


if __name__ == "__main__":
    text_file = 'sherlock.txt'
    data_str = read_data(text_file)
    words_lst = make_words(data_str)
    word_pairs_dict = build_trigrams(words_lst)
    new_text_lst = build_text(word_pairs_dict, words_lst)
    compile_list(new_text_lst)
