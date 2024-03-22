
def pig_latin_translation(function,filename):
    return ' '.join(function(word) for line in open(filename) for word in line.split())


print(pig_latin_translation(lambda x: x.upper(),'../../Files/second_sample.txt'))