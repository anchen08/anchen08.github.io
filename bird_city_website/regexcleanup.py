import re

# f = open("inputs.txt", 'r', encoding="utf-8")
# f_write = open("outputs.txt", "w")

# lines = f.readlines()
# print(lines)

# for line in lines:
#     # new = re.match(r'(?=\d)', line)
#     match = re.match(f'\d.\d.\d', line)
#     # new_text = re.sub(pattern, replacement, text)

#     if (match):
#         f_write.write("\n")
    
#     f_write.write(line)
#     # f_write.write(new)

# f.close()
# f_write.close()


# f = open("outputs.txt", "r")
# f_write = open("sorted.txt", "w")
# flag = False

# lines = f.readlines()
# for line in lines:
#     match = re.match(f'\d.\d.\d', line)

#     if (flag):
#         f_write.write(line.strip("\n"))
#         f_write.write("\n")

#     if (match):
#         flag = True
#         f_write.write(line.strip("\n"))
#         f_write.write(", ")
#     else:
#         flag = False

# f.close()
# f_write.close()

# f = open("status/sorted.txt", "r")
# f_write = open("new.csv", "w")

# lines = f.readlines()

# for line in lines:
#     line = line.strip("\n")

# lines.sort()

# for line in lines:
#     f_write.write(line)


# f.close()
# f_write.close()
f = open("new.txt", "r")
f_write = open("new_cleaned.txt",'w')
lines = f.readlines()

for line in lines:
    line = line[7:]
    print(line)
    f_write.write(line)

f.close()
f_write.close()


