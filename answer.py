"""this assignment is about writing as many as i can good, simple and concise code """
import math
import csv


def indian_style_formating(num):
    """to get comma in indian style"""

    first, second = num, ""

    if "." in num:
        first, second = num[:-3], num[-3:]

    i = 3
    while i < len(first):
        first = first[:-i] + "," + first[-i:]
        i += 3

    return first + second


def simple_interest(principal, term, rate):
    """calcualte simple intrest"""
    si = principal * term * rate
    amount = principal + si
    return indian_style_formating(str(round(amount, 2)))


def compound_interest(principal, term, rate):
    """calcualte compund itnerest"""
    amount = principal * ((1 + rate) ** term)
    return indian_style_formating(str(round(amount, 2)))


def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    """ci with extra payment"""
    if end_of_period is False:
        for _ in range(0, term):
            principal += payment
            si = principal * rate
            principal += si
        return indian_style_formating(str(round(principal, 2)))

    if end_of_period:
        for _ in range(0, term):
            si = principal * rate
            principal += payment
            principal += si
        return indian_style_formating(str(round(principal, 2)))


def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    """calcualting fixed payemnt"""
    if not end_of_period:
        rate /= 1 + rate
    emi = (future_value - present_value * (1 + rate) ** term) / ((1 + rate) ** term - 1)
    result = math.ceil(emi * 100) / 100
    return indian_style_formating(str(round(result, 2)))


def list_to_dict(data):
    """List to dict"""
    d = {}
    for i in data:
        for k, v in i.items():
            if k in d:
                d[k].append(v)
            else:
                d[k] = [v]
    return d


def dict_to_list(data):
    """dict to list"""
    keys = list(data.keys())
    num_elements = len(data[keys[0]])

    result = []
    for i in range(num_elements):
        new_dict = {key: data[key][i] for key in keys}
        result.append(new_dict)

    return result


def files_innerjoin(filename1, filename2, **kwargs):
    """inner join"""
    join_keys = kwargs.get("join_keys")
    output_filename = kwargs.get("output_filename", "results.csv")

    data1 = {}
    with open(filename1, "r", encoding="utf-8") as f:
        reader1 = csv.DictReader(f)
        for row in reader1:
            key = tuple(row.get(key, None) for key in join_keys)
            data1[key] = row

    joined_data = []
    with open(filename2, "r", encoding="utf-8") as f:
        reader2 = csv.DictReader(f)
        for row in reader2:
            key = tuple(row.get(key, None) for key in join_keys)
            if key in data1:
                data1[key].update(row)
                joined_data.append(data1[key].copy())

    fieldnames_set = set(reader2.fieldnames) - set(join_keys)
    fieldnames = reader1.fieldnames + list(fieldnames_set)

    with open(output_filename, "w", encoding="utf-8", newline="") as out_f:
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(joined_data)


def files_leftouterjoin(filename1, filename2, **kwargs):
    """left outer join"""
    join_keys = kwargs.get("join_keys")
    output_filename = kwargs.get("output_filename", "results.csv")

    data1 = {}
    with open(filename1, "r", encoding="utf-8") as f:
        reader1 = csv.DictReader(f)
        for row in reader1:
            key = tuple(row.get(key, None) for key in join_keys)
            data1[key] = row

    joined_data = []
    with open(filename2, "r", encoding="utf-8") as f:
        reader2 = csv.DictReader(f)
        for row in reader2:
            key = tuple(row.get(key, None) for key in join_keys)
            if key in data1:
                data1[key].update(row)
                joined_data.append(data1[key].copy())
            else:
                updated_row = row.copy()
                updated_row.update({key: None for key in reader1.fieldnames})
                joined_data.append(updated_row)

    fieldnames_set = set(reader1.fieldnames) | set(reader2.fieldnames) - set(join_keys)
    fieldnames = list(fieldnames_set)

    with open(output_filename, "w", encoding="utf-8", newline="") as out_f:
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(joined_data)


def files_rightouterjoin(filename1, filename2, **kwargs):
    """right outer join"""
    join_keys = kwargs.get("join_keys")
    output_filename = kwargs.get("output_filename", "results.csv")

    data1 = {}
    with open(filename1, "r", encoding="utf-8") as f:
        reader1 = csv.DictReader(f)
        for row in reader1:
            key = tuple(row.get(key, None) for key in join_keys)
            data1[key] = row

    joined_data = []
    with open(filename2, "r", encoding="utf-8") as f:
        reader2 = csv.DictReader(f)
        for row in reader2:
            key = tuple(row.get(key, None) for key in join_keys)
            if key in data1:
                data1[key].update(row)
                joined_data.append(data1[key].copy())
            else:
                joined_data.append({**{key: None for key in reader1.fieldnames}, **row})

    fieldnames_set = set(reader1.fieldnames) - set(join_keys) | set(reader2.fieldnames)
    fieldnames = list(fieldnames_set)

    with open(output_filename, "w", encoding="utf-8", newline="") as out_f:
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(joined_data)


def split_file(filename, split_cols):
    """Split a large csv file on values of one or more columns
    into multiple files"""
    data_dict = {}

    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames

        for row in reader:
            key = tuple(row[col] for col in split_cols)
            if key not in data_dict:
                data_dict[key] = [row]
            else:
                data_dict[key].append(row)

    for key, data in data_dict.items():
        output_filename = "_".join(str(value) for value in key) + ".csv"
        with open(output_filename, "w", newline="", encoding="utf-8") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    print(simple_interest(123456, 23, 0.08))
    print(compound_interest(123456, 23, 0.08))
    print(compound_interest_with_payments(0, 100000, 35, 0.10))
    print(savings_calculator(0, 1e8, 35, 0.10))
    print(list_to_dict(data=[{"name": "a", "age": 21}, {"name": "b", "age": 43}]))
    print(dict_to_list(data={"name": ["a", "b"], "age": [21, 43]}))
    files_leftouterjoin("file1.csv", "file2.csv", join_keys=["id"])
    files_rightouterjoin("file1.csv", "file2.csv", join_keys=["id"])
    files_innerjoin("file1.csv", "file2.csv", join_keys=["id"])
    split_file("input.csv", ["city", "is_married"])
