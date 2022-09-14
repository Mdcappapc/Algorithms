import hashlib
print(hashlib.new(input("Algorithm : "),(input("Data : ").encode())).digest())