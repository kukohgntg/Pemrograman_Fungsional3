random_list = [3.1, 105, 2.7, 'Hello', 5.5, 'Python', 'World', 'AI', 737, 412]

def check_type(value):
    if isinstance(value, float):
        return 'float'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, str):
        return 'string'

data_float = tuple(filter(lambda x: check_type(x) == 'float', random_list))
data_int = list(filter(lambda x: check_type(x) == 'int', random_list))
data_string = list(filter(lambda x: check_type(x) == 'string', random_list))

def map_int_to_dict(item):
    ratusan = item // 100
    puluhan = (item % 100) // 10
    satuan = item % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data_int_mapped = map(map_int_to_dict, data_int)

print("Data Float : ", data_float)
print("Data Int : ")
for item in data_int_mapped:
    print(item)
print("Data String : ", data_string)