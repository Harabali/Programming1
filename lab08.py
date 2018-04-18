import string


#MAIN
#EX1:
# dict = {"Bob":"dog", "Henry":"cat", "Thomas":"lamb"}
#
# print(dict["Bob"])
# print(len(dict))
#
# print("cat" in dict)
#
# a = dict
#
# dict["Bob"]="fish"
#
# for k in dict:
#     print(k, 'is a', dict[k])


def clearRow(str):
    newR = ''
    for ch in str:
        if ch not in string.punctuation and ch!='\n':
            newR+=ch.lower()
    return newR

#EX2:
# fin = open('input.txt','r')
# dict = {}
# for row in fin:
#     row = clearRow(row)
#     for word in row.split(' '):
#         if word in dict:
#             dict[word] += 1
#         else:
#             dict[word] = 1
#
# for k in dict:
#     print(k,': ', dict[k])
#
# fin.close()

def dateConvert(str):
    # dict = {"JAN":1, "FEB":2, "MAR":3, "APR":4, ""}....
    month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    nums = range(1,13)
    dic = dict(zip(month,nums))
    parts = str.split('-')
    if int(parts[2]) <= 18:
        year = '20'+parts[2]
    else:
        year = '19'+parts[2]
    return (int(year),dic[parts[1]],int(parts[0]))

#EX3:
# str = input("Give me a date in format (dd-MMM-yy): ")
# print(dateConvert(str))

#EX4:
dict = {}
for d1 in range(1,7):
    for d2 in range(1,7):
        if d1+d2 in dict:
            dict[d1+d2].append((d1,d2))
        else:
            dict[d1+d2] = [(d1,d2)]

for k,v in dict.items():
    print(k,':',len(v),':',v)