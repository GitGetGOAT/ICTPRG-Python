num = 0
count = 1
while num < 10:
    num = num+count
    count=count+1
    print(num)
    num=num-(count)
# while True:
#     with open('numbersforcalc.txt', 'a') as outfile:
#         number = (number + 1)
#         if number == count:
#             break
#         else:
#         print(number,"\n",file=outfile)

# infile= open('numbersforcalc.txt', 'r')
# lines= infile.readlines()
# print(lines.strip())