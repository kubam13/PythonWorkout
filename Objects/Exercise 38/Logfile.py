class Logfile:
    def __init__(self, filename):
        self.file = open(filename, 'w')


l1 = Logfile('test.txt')
l1.file.write('badum tss tss')