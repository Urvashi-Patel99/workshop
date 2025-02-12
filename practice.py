#WAP to check entered single character string is vowel or consonant
#WAP to check entered  three digit number is armstrong or not


s = input("Enter a single character string\n")

str_vowel = "aAeEiIoOuU"
str_consonant = "bBcCdDfFgGhHiIjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ"


if s in str_vowel:
 print ("its vowel ")
elif s in str_consonant:
 print("its consonant ")
else:
 print("Invalid Character")

