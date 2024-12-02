import hashlib
def password(password) :
    sha256_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return sha256_hash
pwd = input("Enter : ")
hashed_pwd = password(pwd)
print(hashed_pwd)
