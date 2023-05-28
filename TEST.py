v = None
my_range = list(range(v))
print(sum(my_range, v) + pow(v, v, v)) #820
def num_failed(the_number_failed):
    my_num_result = list(range(1, the_number_failed)) # the number result can't accpect in reange and 0
    for number in my_num_result:
        my_range = list(range(number))
        if sum(my_range, number) + pow(number, number, number) == the_number_failed:
            return number

num_failed = num_failed(820)
print(num_failed)

