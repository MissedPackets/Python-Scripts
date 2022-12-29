fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  # continue is the equivalent of "skipping an array item"
  text="print('{0} {1}')".format(x,fruits[1])
  print(text)
      # print(text)
