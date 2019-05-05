# Sorry I can't do it with a for loop :p
def palindrome(word):
    length = len(word)
    if (length <= 1): return True
    if (word[0] == word[length - 1]):
        return palindrome(word[1:-1])
    else:
        return False


print("Palindrome" if palindrome("Wassim") else "Non palindrome")
print("Palindrome" if palindrome("kook") else "Non palindrome")
print("Palindrome" if palindrome("loooool") else "Non palindrome")


# Okay fine, I will do it a for loop
def palindromeForLoop(word):
    length = len(word)  #Saving for less calculations
    for i in range(int(length / 2)):
        if (word[i] != word[length - 1 - i]):
            return False
    return True


print("Palindrome" if palindromeForLoop("Wassim") else "Non palindrome")
print("Palindrome" if palindromeForLoop("kook") else "Non palindrome")
print("Palindrome" if palindromeForLoop("loooool") else "Non palindrome")
