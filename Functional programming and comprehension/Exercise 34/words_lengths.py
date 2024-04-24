def words_lengths(file):
    return {len(word) for line in open(file) for word in line.split()}


print(words_lengths('../../Files/second_sample.txt'))
