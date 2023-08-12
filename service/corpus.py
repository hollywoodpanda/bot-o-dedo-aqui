# service/corpus.py

import os
import json
import codecs
import csv

class Corpus:

    def __init__(self):
        self.corpus_name = os.getenv('CORPUS_NAME')
        self.corpus_path = os.path.join('data', self.corpus_name)
        self.utterances_file = os.path.join(self.corpus_path, 'utterances.jsonl')

    def print_lines(self, filename, n=10):
        
        with open(self.utterances_file, 'rb') as f:
            lines = f.readlines()
        
        for line in lines[:n]:
            
            print(line)

    def __load_line(self, line_json: dict) -> dict:
        
        line_obj = {}
        line_obj['line_id'] = line_json['id']
        line_obj['character_id'] = line_json['speaker']
        line_obj['text'] = line_json['text']

        return line_obj
    
    def __load_conversation(self, line_json: dict) -> dict:

        conversation_obj = {}
        conversation_obj['conversation_id'] = line_json['conversation_id']
        conversation_obj['movie_id'] = line_json['meta']['movie_id']

        return conversation_obj


    def __load_lines_and_conversations(self, filename):

        lines = {}
        conversations = {}

        with open(self.utterances_file, 'r', encoding=os.getenv('UTTERANCES_ENCODING')) as f:
            
            for line in f:

                line_json = json.loads(line)

                line_obj = self.__load_line(line_json)                
                lines[line_obj['line_id']] = line_obj

                if line_json['conversation_id'] not in conversations:
                    
                    conversation_obj = self.__load_conversation(line_json)
                    conversation_obj['lines'] = [line_obj]

                else:

                    conversation_obj = conversations[line_json['conversation_id']]
                    conversation_obj['lines'].insert(0, line_obj)

                conversations[conversation_obj['conversation_id']] = conversation_obj

        return lines, conversations
    
    def __extract_sentence_pairs(self, conversations):

        qa_pairs = []

        for conversation in conversations.values():

            for i in range(len(conversation['lines']) - 1):

                input_line = conversation['lines'][i]['text'].strip()
                target_line = conversation['lines'][i+1]['text'].strip()

                if input_line and target_line:

                    qa_pairs.append([input_line, target_line])

        return qa_pairs
    
    def format_corpus(self, filename='formatted_corpus.txt'):

        datafile = os.path.join(self.corpus_path, filename)

        delimiter = '\t'

        delimiter = str(codecs.decode(delimiter, 'unicode_escape'))

        lines = {}
        conversations = {}

        # TODO: Use a loggger!
        print('Transforming corpus into lines and conversations...')

        lines, conversations = self.__load_lines_and_conversations(self.utterances_file)

        # TODO: Use a logger!
        print('Writing newly formatted corpus...')

        with open(datafile, 'w', encoding=os.getenv('FORMATTED_UTTERANCES_ENCODING')) as outputfile:

            writer = csv.writer(outputfile, delimiter=delimiter)

            for pair in self.__extract_sentence_pairs(conversations):

                writer.writerow(pair)

        # TODO: Use a logger!
        print(f'Formatted corpus created successfully at {datafile}')
        
        return datafile