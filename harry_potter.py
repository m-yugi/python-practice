# def m(input1, input2, input3, count, temp_string):
#     if(input1 == temp_string):
#         return count
#     if(count % 2 == 0):
#         return m(input1, input2, input3, count+1, input1[len(input1)-input2::]+input1[0:len(input1)-input2])
#     else:
#         return m(input1, input2, input3, count+1, input1[len(input1)-input3::]+input1[0:len(input1)-input3])
def f(input1, input2, input3):
    count = 0
    temp_string = ""
    while(temp_string != input1):
        if(count % 2 == 0):
            temp_string = input1[len(input1)-input2::] + \
                input1[0:len(input1)-input2]
            print("input1: ", temp_string)
        else:
            temp_string = input1[len(input1)-input3::] + \
                input1[0:len(input1)-input3]
            print("input2: ", temp_string)
        count += 1
    return count


print(f("AbcDef", 1, 2))
