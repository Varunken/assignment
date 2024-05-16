brand={'Iphone': {'iphone11': 150000,
                  'iphone12': 125000,
                  'iphone13': 100000,
                  'iphone14': 75000,
                  'iphone15': 50000},
        'Vivo': {'V30': 125000,
                 'V17': 100000,
                 'V15': 75000,
                 'V11': 50000},
        'Sony': 125000, 'Samsung': 100000, 'Redmi': 75000, 'Oppo': 50000}
print(brand)
for key,value in brand.items():
    if isinstance(value,dict):
        for j in value:
            print([key,j,value[j]])  
    else:
        print(key,value)
