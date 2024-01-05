import math

# def indian_style_formating(num):
#     num_str=str(num)

#     while len(num_str)

# print(indian_style_formating(12345))


def simple_interest(principal, term, rate):
    si = principal * term * rate
    amount = principal + si
    return round(amount, 2)


def compound_interest(principal, term, rate):
    amount = principal * ((1 + rate) ** term)
    return round(amount, 2)


def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    if end_of_period == False:
        for _ in range(0, term):
            principal += payment
            si = principal * rate
            principal += si
        return principal

    if end_of_period:
        for _ in range(0, term):
            si = principal * rate
            principal += payment
            principal += si
        return principal


def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    if not end_of_period:
        rate /= 1 + rate
    emi = (future_value - present_value * (1 + rate) ** term) / ((1 + rate) ** term - 1)
    result = math.ceil(emi * 100) / 100
    return round(result, 2)

def list_to_dict(data: list):
    d={}
    for i in data:
        # print(i)
        for k,v in i.items():
            # print(k,v)
            if k in d:
                d[k].append(v)
            else:
                d[k]=[v]
    return d

    # result={ k:[v] for i in data for k,v in i.items() }
    # return result


if __name__ == "__main__":
    # print(simple_interest(123456, 23, 0.08))
    # print(compound_interest(123456, 23, 0.08))

    # print(compound_interest_with_payments(0,100,2,10,True))
    # print(compound_interest_with_payments(0, 368970.52, 35, 0.10))
    # print(compound_interest_with_payments(0, 100000, 35, 0.10))
    # print(savings_calculator(0, 1e8, 35, 0.10))
    print(list_to_dict(data = [{"name": "a", "age": 21}, {"name": "b", "age": 43}]))
