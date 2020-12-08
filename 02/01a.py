with open("input.txt", 'r') as  ins:
  total = 0
  for line in ins:
    words = line.split(' ')
    password = words[-1]
    char = words[1][0]
    mi,ma = words[0].split("-")

    count = password.count(char)
    if count >= int(mi) and count <= int(ma):
      total+=1
print(total)
