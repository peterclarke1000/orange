import pdb
from turtle import pd

strInput = "geekyfecker"
# strInput = ""
# result = ""

def reverseString(text):
    result = ""
    for char in text:
        result = char + result
    return result

# def reverseString(txt):
#     index = len(txt)-1
#     result = ""
#     while index > 0:
#         result += txt[index]
#         index -= 1
#     return result

# def reverseString(txt):
#     pdb.set_trace()
#     result = ""
#     for i in range(len(txt)):
#         result = result + (txt[i])
#     return result

# here
# def reverseString(txt):
#     result = len(txt) == 0, txt, else "".join(reversed(txt))
#     return(result)

# def reverseString(txt):
#     result = ""
#     index = 0
#     while index < len(txt):
#         result = result + txt[index]
#         index += 1
#     return result



# for i in range(len(strInput)-1, -1, -1):
#     result = result + strInput[i]

# result = strInput[::-1]
# result = "".join(reversed(strInput))
# next(result)

print(reverseString(strInput))

