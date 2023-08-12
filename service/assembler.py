# service/assembler.py

import unicodedata
import re
import os
from service.voc import Voc

class Assembler:

    def __unicode_to_ascii(text: str) -> str:

        return ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
    
    def __normalize_string(text: str) -> str:

        new_text = Assembler.__unicode_to_ascii(text.lower().strip())
        new_text = re.sub(r'([.!?])', r' \1', new_text)
        new_text = re.sub(r'[^a-zA-Z.!?]+', r' ', new_text)
        new_text = re.sub(r'\s+', r' ', new_text).strip()

        return new_text
    
    def __read_vocs(file_path: str, corpus_name: str) -> tuple:

        print('Reading lines...')
        
        lines = open(file_path, encoding=os.getenv('FORMATTED_UTTERANCES_ENCODING')).read().strip().split('\n')

        pairs = [[Assembler.__normalize_string(substring) for substring in line.split('\t')] for line in lines]

        voc = Voc(corpus_name)

        return voc, pairs
    
    def __filter_pair(pair: list) -> bool:

        return len(pair[0].split(' ')) < int(os.getenv('ASSEMBLING_MAX_LENGTH')) and len(pair[1].split(' ')) < int(os.getenv('ASSEMBLING_MAX_LENGTH'))
    
    def __filter_pairs(pairs: list) -> list:

        return [pair for pair in pairs if Assembler.__filter_pair(pair)]

    def prepare_training_data(corpus_name: str, file_path: str) -> tuple:

        voc, pairs = Assembler.__read_vocs(file_path, corpus_name)

        pairs = Assembler.__filter_pairs(pairs)

        for pair in pairs:

            voc.add_sentence(pair[0])
            voc.add_sentence(pair[1])

        # TODO: Use a logger!
        print(f'Counted words in preparing training data: {voc.num_words}')

        return voc, pairs