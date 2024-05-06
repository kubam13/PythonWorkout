class Summing:
    def __init__(self, *variables):
        self.variables = variables

    def mysum(self):

        if not self.variables:
            self.variables = 0
            return self.variables

        output = self.variables[0]
        for variable in self.variables[1:]:
            output += variable
        return output

    def mysum_bigger_than(self):

        if not self.variables:
            self.variables = 0
            return self.variables

        threshold = self.variables[0]
        for variable in self.variables[1:]:
            if variable > threshold:
                output = variable
                break

        for variable in self.variables[self.variables.index(output) + 1:]:
            if variable > threshold:
                output += variable

        return output

    def sum_numeric(self):

        output = 0

        for variable in self.variables:
            if isinstance(variable, int):
                output += variable
            elif variable.isnumeric():
                output += int(variable)
            else:
                pass
        return output

    def merge_dicts(self):

        result_dict = {}

        for dictionary in self.variables:
            for key, value in dictionary.items():
                if key in result_dict:
                    if isinstance(result_dict[key], list):
                        result_dict[key].append(value)
                    else:
                        result_dict[key] = [result_dict[key], value]
                else:
                    result_dict[key] = value

        return result_dict


sum = Summing(1,2,3,4)
bigger = Summing([1,2,3],[4,5,6])
numeric = Summing(10, 20, 'a', '30','bcd')
dict_list = Summing({'x': 10, 'y': 8}, {'a': 6, 'y': 4}, {'a': 2, 'c': 7}, {'l': 4, 'y': 0})

print(sum.mysum())
print(bigger.mysum_bigger_than())
print(numeric.sum_numeric())
print(dict_list.merge_dicts())