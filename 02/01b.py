with open("input.txt", 'r') as  ins:
  total = 0
  for line in ins:
    words = line.split(' ')
    password = words[-1]
    char = words[1][0]
    mi,ma = words[0].split("-")

    if (password[int(mi)-1] == char or password[int(ma)-1] == char) and password[int(mi)-1] != password[int(ma)-1]:
      total+=1
print(total)
