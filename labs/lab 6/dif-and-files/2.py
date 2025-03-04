import os

def check_path_access(path):
    print(f"Checking path: {path}")
    print("Exists:", os.access(path, os.F_OK))  
    print("Readable:", os.access(path, os.R_OK))  
    print("Writable:", os.access(path, os.W_OK))  
    print("Executable:", os.access(path, os.X_OK))  

user_path = input("Enter the path: ")
check_path_access(user_path)