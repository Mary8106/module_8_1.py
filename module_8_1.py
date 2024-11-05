def add_everything_up(a, b):
    try:
        if (isinstance(a, (int, float))) == True and (isinstance(b, (int, float))) == True:
            res = round(a + b, 3)
        else:
            res = a + b
        return res
    except TypeError:
        res = (str(a) + str(b))
        return res

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
