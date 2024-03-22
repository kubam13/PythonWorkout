def sum_hex(list_of_strings):
    return sum((int(element, 16) for element in list_of_strings))


hex_list = ['0x20', '0x7f', '0x1', '0xdd']
print(sum_hex(hex_list))