class Exercise16:

    def dict_diff(self, dict1, dict2):
        result_dict = {}
        for i in dict1.keys():
            if i in dict2.keys():
                if dict1[i] != dict2[i]:
                    result_dict.update({i: [dict1[i], dict2[i]]})
            else:
                result_dict.update({i: [dict1[i], 'None']})

        for i in dict2.keys():
            if i not in dict1.keys():
                result_dict.update({i: ['None', dict2[i]]})
        return dict(sorted(result_dict.items()))

    def merge_dicts(self, *args):
        result_dict = {}
        for arg in args:
            result_dict.update(arg)
        return result_dict

    def dict_even_odd(self, list):
        return dict(zip(list[::2], list[1::2]))

    def sample_function(self, variable):
        if variable > 5:
            return True
        else:
            return False

    def dict_partition(self, d, f):
        first_dict = {}
        second_dict = {}
        for key, value in d.items():
            if f(value):
                first_dict.update({key: value})
            else:
                second_dict.update({key: value})
        print(f'{first_dict}\n{second_dict}')


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'd': 4}
d5 = {'a': 13, 'b': 12, 'c': 14}
d6 = {'a': 31, 'b': 22, 'd': 3}
d7 = {'a': 31, 'b': 2, 'd': 4}
l = ('a', 1, 'b', 2, 'c', 3, 'd', 12)
sample_dict = {'a': 1, 'b': 25, 'c': 2, 'd': 5}

instance = Exercise16()
#print(instance.dict_diff(d1, d2))
#print(instance.merge_dicts(d1, d7))
#print(instance.dict_even_odd(l))
instance.dict_partition(sample_dict, instance.sample_function)
