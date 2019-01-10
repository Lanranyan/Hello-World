'''
1) Swap two Variables
'''

# a = 5
# b = 10
# print('a =',a, 'b =', b)
# print('a =', b, 'b =', a)

# a = b
# print("Now a is",a)
# b = a
# print("The new b is", b)

### Create a temporary variable temp
# temp = a    # save the value of a in the temp variable
# a = b    # a is getting the value of b
# b = temp
# print("The new variables a = ",a," b = ",b,"")  # Quotes go around what is shown with commas in between

####### Write all integers between 1 and 9 usig a while loop

# x = 1
# while x < 10:
#     print(x, '  ', end ='')
#     x = x + 1

# row = 1
# col = 1

# while row < 10:
#     while col < 5:
#         print(row,col,' ', end ='') #### Remember to add space in empty single quote
#         col = col + 1
#     print()
#     row = row + 1
#     col = 1

####### FIBONACCI SEQUENCE
# 1, 1, 2, 3, 5, 8, 13, 21,34,.. #ADdS Onto next number

x = 1
y = 1
cont = 'c'    ### "cont" is 'continue'

while cont == 'c':
    print('A new Fibon number is:',x+y)

    temp = x
    x = y
    y = y + temp
cont = input("If you want another number, press c or any other key.")