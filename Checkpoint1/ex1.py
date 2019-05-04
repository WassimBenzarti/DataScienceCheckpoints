text = input("Hello, please talk\n")
print("Your talk is {} chars long".format(len(text)))
print("words={}, spaces={}".format(
  len(text.split(" ")),
  text.count(" ")
))