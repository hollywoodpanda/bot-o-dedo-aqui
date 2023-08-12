# main.py

import os
import random

from dotenv import load_dotenv
from service.device import Device
from service.corpus import Corpus
from service.assembler import Assembler
from service.trimmer import Trimmer
from service.batcher import Batcher

print('👉️ bot-o-dedo-aqui 👈️')

load_dotenv()

print(f'Device: {Device().value}')

corpus = Corpus()

print(f'Corpus {corpus.corpus_name}\r\n')
print('---'*15)
corpus.print_lines('utterances.jsonl')

formatted_corpus = corpus.format_corpus()

print('---'*15)
print(f'Formatted corpus: {formatted_corpus}')

print('---'*15)
destination_path = os.path.join('data', corpus.corpus_name, 'training_data')
voc, pairs = Assembler.prepare_training_data(corpus.corpus_name, formatted_corpus)

print(f'Pairs {len(pairs)}')
for pair in pairs[:10]:
    print(pair)

# Trimming pairs
pairs = Trimmer.trim_rare_words(voc, pairs)

print('---'*15)
print(f'Trimmmed pairs ({len(pairs)})')

for pair in pairs[:10]:
    print(pair)

print(f"\r\n{'---'*15}\r\n{'---'*15}\r\n")

little_tiny_batch_size = 5

batches = Batcher.train_data_batch(voc, [random.choice(pairs) for _ in range(little_tiny_batch_size)])

input_variable, lengths, target_variable, mask, max_target_len = batches

print(f'input_variable :: {input_variable}')
print(f'lengths :: {lengths}')
print(f'target_variable :: {target_variable}')
print(f'mask :: {mask}')
print(f'max_target_len :: {max_target_len}')
