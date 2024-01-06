'''this assignment is about writing as many as i can good, simple and concise code '''
import math
import csv
def indian_style_formating(num):

    first, second, size = num, '', len(num)
    if '.' in num:
        first, second, size = num[:-3], num[-3:], size-3
    index = 3
    while index < len(first):
        first = first[:-index] + ',' + first[-index:]
        index += 3
    return first+second

def simple_interest(principal, term, rate):
    '''calcualte simple intrest'''
    si = principal * term * rate
    amount = principal + si
    return indian_style_formating(str(round(amount, 2)))

def compound_interest(principal, term, rate):
    '''calcualte compund itnerest'''
    amount = principal * ((1 + rate) ** term)
    return indian_style_formating(str(round(amount, 2)))

def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    if end_of_period == False:
        for _ in range(0, term):
            principal += payment
            si = principal * rate
            principal += si
        return indian_style_formating(str(principal))

    if end_of_period:
        for _ in range(0, term):
            si = principal * rate
            principal += payment
            principal += si
        return indian_style_formating(str(principal))

def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    if not end_of_period:
        rate /= 1 + rate
    emi = (future_value - present_value * (1 + rate) ** term) / ((1 + rate) ** term - 1)
    result = math.ceil(emi * 100) / 100
    return indian_style_formating(str(round(result, 2)))

def list_to_dict(data: list):
    '''list to dict'''
    d={}
    for i in data:
        for k,v in i.items():
            if k in d:
                d[k].append(v)
            else:
                d[k]=[v]
    return d

def dict_to_list(data):
    '''dict to list'''
    keys = list(data.keys())
    num_elements = len(data[keys[0]])
    
    result = []
    for i in range(num_elements):
        new_dict = {key: data[key][i] for key in keys}
        result.append(new_dict)
    
    return result

def files_innerjoin(filename1, filename2,output_filename, join_keys):
    data1={}
    with open(filename1,'r')as f:
        reader1=csv.DictReader(f)
        for row in reader1:
            key=tuple(row.get(key, None) for key in join_keys)
            data1[key]=row
    joined_data=[]
    with open(filename2,'r')as f:
        reader2=csv.DictReader(f)
        for row in reader2:
            key=tuple(row.get(key, None) for key in join_keys)
            if key in data1:
                joined_data.append(**data1[key],**row)

    with open(output_filename, 'w', newline='') as out_f:
        fieldnames=reader1.fieldnames + [f for f in reader2.fieldnames if f not in join_keys]
        writer=csv.DictWriter(out_f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(joined_data)





if __name__ == "__main__":
    print(simple_interest(123456, 23, 0.08))
    # print(compound_interest(123456, 23, 0.08))
    # print(savings_calculator(0, 1e8, 35, 0.10))
    # print(list_to_dict(data = [{"name": "a", "age": 21}, {"name": "b", "age": 43}]))
    # print(dict_to_list(data = {"name": ["a", "b"], "age": [21,43]}))
    # files_innerjoin(filename1='f1.csv',filename2='f2.csv',output_filename='out.csv',join_keys=['id'])