# service/tokenizer.py

PAD_token = 0
SOS_token = 1
EOS_token = 2

class Voc:

    def __init__(self, name):
        
        self.name = name
        self.trimmed = False
        self.word_2_index = {}
        self.word_2_count = {}
        self.index_2_word = { PAD_token: 'PAD', SOS_token: 'SOS', EOS_token: 'EOS' }
        self.num_words = 3 # PAD, SOS, EOS

    def __add_word(self, word):
        
        if word not in self.word_2_index:

            self.word_2_index[word] = self.num_words

            self.word_2_count[word] = 1

            self.index_2_word[self.num_words] = word

            self.num_words += 1

        else:

            self.word_2_count[word] += 1

    def add_sentence(self, sentence):
            
        for word in sentence.split(' '):
            self.__add_word(word)

    def trim(self, min_count):

        if self.trimmed:

            return
        
        self.trimmed = True

        keep_words = []

        for key, value in self.word_2_count.items():

            if value >= min_count:

                keep_words.append(key)

        # TODO: 
        print(f'keep_words {len(keep_words)} / {len(self.word_2_index)} = {len(keep_words) / len(self.word_2_index):.4f}')

        self.word_2_index = {}
        self.word_2_count = {}
        self.index_2_word = { PAD_token: 'PAD', SOS_token: 'SOS', EOS_token: 'EOS' }
        self.num_words = 3 # Count default tokens

        for word in keep_words:

            self.__add_word(word)