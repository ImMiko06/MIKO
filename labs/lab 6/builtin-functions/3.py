def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]  


user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("palindrome")
else:
    print("not polindrom")