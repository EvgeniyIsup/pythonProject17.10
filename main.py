# array = range(10)
# array = list(map(lambda x: x**2, array))
# print(array)
#
#
# array = range(10)
# array = list(filter(lambda x: x%2==0, array))
# print(array)
#
#
# from functools import reduce
# array = range(1,10)
# array = reduce(lambda x,y: x*y, array,1)
# print(array)
#
# print(1*2*3*4*5*6*7*8*9)


# with open("test.txt","w", encoding = "utf-8") as file:
#     file.write("hello world")
#
# with open("test.txt","r", encoding = "utf-8") as file:
#     print(file.read())


with open("некийтекстовый файл.txt","r", encoding = "utf-8") as file:
    # print(file.read())
    anyText = file.read()
    digits = list(filter(lambda x: str.isdigit(x), anyText))
    countDigit = len(digits)
    print(f"колво цифр:{countDigit}")


