class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self, key)


f1 = FlexibleDict()

f1['a'] = 100
print(f1['a'])

f1[1] = 50
print(f1[1])

f1['1'] = 50
print(f1[1])

f1[1] = 50
print(f1['1'])
