# importing the hashlib module
import hashlib

"""I copied this hash_file function (did a little tweaks in it to make it better). But the point is I still don't understand the logic used
in the hash_file function. What is hash object? What is chunk? What is  ( b'' )?"""


def hash_file(filename, ct):
   """"This function returns the (checksum type) hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.new(ct)

   # open file for reading in binary mode
   with open(filename, 'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

print("Important info about popular hashes: \n")
print("1. MD5 and SHA-1 should be avoided from a security point of view\n")
print("2. MD5 seems slow in general\n\n")

checksum_type = input(
    "\nWhat type of checksum do you want to apply (write it exactly as these options) ? {'sha512_224', 'sha256', 'sha3_384', 'shake_128', 'shake_256', 'ripemd160', 'sha3_512', 'sha1', 'blake2b', 'whirlpool', 'sha3_256', 'sha512', 'sha3_224', 'md5-sha1', 'mdc2', 'md5', 'sm3', 'md4', 'sha512_256', 'sha384', 'blake2s', 'sha224'}: ")

print("\nEnter the name of file to be hashed (should be in the same directory as this python file)")
file_name = input("And make sure you write the file's extension as well: ")

# file_name = input("\nEnter the name of file to be hashed (should be in the same directory as this python file ): ")

print("\nCalculating hash... (this may take some time if the file is very big)\n")
hash_value_local = hash_file(file_name, checksum_type)
print(f"locally calculated hash: {hash_value_local}")

print("\nyou have two options-")
print("1. paste the hash downloaded from source here")
print("2. or make sure the hash downloaded from source is pasted in 'downloaded_hash.txt' ")

while True:
    a = input("\nchoose option and press enter (1/2): ")
    if a == '1':
        hash_value_downloaded = input("\nPaste the copied/downloaded hash: ")
        hash_value_downloaded = hash_value_downloaded.strip()
        break
    elif a == '2':
        file_name2 = 'downloaded_hash.txt'
        with open(file_name2) as file2:
            hash_value_downloaded = file2.read()
            hash_value_downloaded = hash_value_downloaded.strip()
        break
    else:
        print("\n ERROR: you have to type either '1' or '2' ")


print(f"\nlocally calculated hash: {hash_value_local}")
print(f"downloaded hash value:\t {hash_value_downloaded}")

if hash_value_downloaded == hash_value_local:
    print("\nthe file is SAFE (hash of local file matches downloaded hash)\n")
else:
    print("\nthe file is NOT SAFE (hash of local file doesn't match downloaded hash)\n")

exit = input("(press enter to exit)")
