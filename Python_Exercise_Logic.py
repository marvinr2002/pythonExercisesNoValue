
#Write a function that takes one argument: the height of a pyramid (a positive integer),
## and prints a centered pyramid made of asterisks (*)

"""
print("Give me a positive integer")
height = int(input())
def c_pyramid(height):
    pyramid_size = 0
    pyramid_spaces = " "
    pyramid_asterisc = "* "
    pyramid_space_between = height    
    while pyramid_size < height:
        pyramid_size += 1
        pyramid_space_between -= 1
        print(pyramid_spaces * pyramid_space_between, pyramid_asterisc * pyramid_size)
c_pyramid(height)
"""

# Write a function that takes one argument: the height of a pyramid (a positive integer),
# and prints a centered hollow pyramid made of asterisks (*)

print("Give me a positive integer")
height = int(input())
def c_pyramid(height):
    pyramid_size = 0
    pyramid_spaces = " "
    pyramid_space_between = height    
    while pyramid_size < height:
        pyramid_size += 1
        pyramid_space_between -= 1
        print(pyramid_spaces * pyramid_space_between, end="")
        if pyramid_size == 1:
            print("*")
        elif pyramid_size == height:
            print("* " * pyramid_size)
        else:
            inner_spaces = (pyramid_size - 2) * 2 + 1
            print("*" + " " * inner_spaces + "*")
c_pyramid(height)
