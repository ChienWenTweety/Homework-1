import hashlib

# Hash function: applies a mathematical function 
# to the input(message) to produce an output(digest), with a fixed length
#Any function that can be used to map data of arbitrary size to data of a fixed size


#Cryptographic hash funtion: A special class of hash function.
#Most cryptographic hash functions are designed to take a string of any length as input and produce a fixed-length hash value.
#Five main properties of cryptographic hash functions:
#1 it is deterministic so the same message always results in the same hash
#2 it is quick to compute the hash value for any given message
#3 it is infeasible to generate a message from its hash value except by trying all possible messages
#4 a small change to a message should change the hash value so extensively that the new hash value appears uncorrelated with the old hash value
#5 it is infeasible to find two different messages with the same hash value
#The following is an example of cryptographic hash function SHA-2, which was designed by the United States National Security Agency (NSA)
hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)