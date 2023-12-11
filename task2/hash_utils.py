import hashlib

def shf24(text):
    hash256 = hashlib.sha256(text.encode())
    return int(hash256.hexdigest(), 16) % (2 ** 24)

def shf48(text):
    hash256 = hashlib.sha256(text.encode())
    return int(hash256.hexdigest(), 16) % (2 ** 48)

def shf64(text):
    hash256 = hashlib.sha256(text.encode())
    return int(hash256.hexdigest(), 16) % (2 ** 64)

######## You don't need this function #######
def shf96(text): 
    hash256 = hashlib.sha256(text.encode())
    return int(hash256.hexdigest(), 16) % (2 ** 96)
