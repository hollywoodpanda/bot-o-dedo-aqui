# service/trimmer.py

from service.voc import Voc

class Trimmer:

    def trim_rare_words(voc: Voc, pairs: list, MIN_COUNT = 3):

        voc.trim(MIN_COUNT)

        keep_pairs = []

        for pair in pairs:

            input_sentence = pair[0]
            output_sentence = pair[1]

            keep_input = True
            keep_output = True

            for word in input_sentence.split(' '):

                if word not in voc.word_2_index:

                    keep_input = False
                    break

            for word in output_sentence.split(' '):

                if word not in voc.word_2_index:

                    keep_output = False
                    break

            if keep_input and keep_output:
                keep_pairs.append(pair)

        # TODO: Use a logger!
        print(f'Trimmed from {len(pairs)} to {len(keep_pairs)}, {len(keep_pairs) / len(pairs):.4f}')

        return keep_pairs
        