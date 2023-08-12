# service/batcher.py

from typing import Iterator
import itertools

from torch import LongTensor, Tensor, tensor, BoolTensor

from service.voc import Voc, EOS_token, PAD_token

class Batcher:

    def indexes_from_sentence(voc: Voc, sentence: str) -> list:

        return [voc.word_2_index[word] for word in sentence.split(' ')] + [EOS_token]
    
    def zero_padding(iterator: Iterator, fill_value=PAD_token) -> list:

        return list(itertools.zip_longest(*iterator, fillvalue=fill_value))
    
    def binary_matrix(iterator: Iterator, value=PAD_token) -> list:

        matrix = []

        for i, seq in enumerate(iterator):

            matrix.append([])

            for token in seq:

                if token == PAD_token:

                    matrix[i].append(0)

                else:

                    matrix[i].append(1)

        return matrix
    
    def input_var(sentences: list, voc: Voc) -> tuple[LongTensor, Tensor]:
        
        indexes_batch = [Batcher.indexes_from_sentence(voc, sentence) for sentence in sentences]

        lenghts = tensor([len(indexes) for indexes in indexes_batch])

        pad_list = Batcher.zero_padding(indexes_batch)

        pad_var = LongTensor(pad_list)

        return pad_var, lenghts
    
    def output_var(sentences: list, voc: Voc) -> tuple[LongTensor, BoolTensor, int]:
        
        indexes_batch = [Batcher.indexes_from_sentence(voc, sentence) for sentence in sentences]

        max_target_len = max(len(indexes) for indexes in indexes_batch)

        pad_list = Batcher.zero_padding(indexes_batch)

        mask = Batcher.binary_matrix(pad_list)
        mask = BoolTensor(mask)

        pad_var = LongTensor(pad_list)

        return pad_var, mask, max_target_len
    
    def train_data_batch(voc: Voc, pair_batch: list) -> tuple[LongTensor, Tensor, LongTensor, BoolTensor, int]:

        pair_batch.sort(key=lambda x: len(x[0].split(' ')), reverse=True)

        input_batch, output_batch = [], []

        for pair in pair_batch:

            input_batch.append(pair[0])
            output_batch.append(pair[1])

        inp, lengths = Batcher.input_var(input_batch, voc)

        output, mask, max_target_len = Batcher.output_var(output_batch, voc)

        return inp, lengths, output, mask, max_target_len
    
    
    