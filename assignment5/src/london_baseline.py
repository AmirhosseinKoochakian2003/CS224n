# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils

eval_corpus_path = "birth_dev.tsv"

eval_file = open(eval_corpus_path, 'r')
num_preds = len(eval_file.readlines())

predictions = ['London'] * num_preds

total, correct = utils.evaluate_places(eval_corpus_path, predictions)

if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('No targets provided!')
