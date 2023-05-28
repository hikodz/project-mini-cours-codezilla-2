# make these lists into one list using unpacking operator
grades1 = [96, 78, 82, 80]
grades2 = [86, 92, 98, 90]
grades3 = [76, 88, 90, 72]
grades4 = [78, 86, 98, 88]
lis_new = [*grades1, *grades2, *grades3, *grades4]
lis_new.sort()
print(lis_new)

        

