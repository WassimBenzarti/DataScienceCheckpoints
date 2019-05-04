print("Put a word here")
word = input()

print("\nUsing [::-1] reverse")
print("Palindrome"
 if word == word[::-1] else "Not palindrome")

print("\nUsing reversed")
print("Palindrome"
 if word == "".join(reversed(word)) else "Not palindrome")