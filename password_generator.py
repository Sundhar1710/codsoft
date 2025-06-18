import random as r
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "@#$%^&?/"
use_for = lower_case + upper_case + number + symbols
length_for_pass = int(input("Enter length of the password :"))
password = "".join(r.sample(use_for, length_for_pass))
print(f"Your Generated Password is :  {password}")