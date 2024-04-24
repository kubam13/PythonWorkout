class StringKeyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key), value)


s1 = StringKeyDict()
s1[1] = 10
print(s1[1])
print(s1['1'])
