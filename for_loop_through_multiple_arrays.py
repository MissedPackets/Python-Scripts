fruits = ["apple", "banana", "cherry"]
liquids = ["juice", "shake", "soda"]
for x,y in zip(fruits, liquids):
  if x == "banana":
      continue
  # continue is the equivalent of "skipping an array item"
  text="print('{0} {1}')".format(x,y)
  print(text)
  # print(x)
      # print(text)
