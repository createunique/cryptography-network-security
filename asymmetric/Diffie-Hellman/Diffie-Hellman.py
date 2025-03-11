prime = 23  #  prime number
base = 5    #primitive root modulo prime

# Secret keys for Alice and Bob
a_secret = 6
b_secret = 15

#A's public value: base^a_secret mod prime
a_public = pow(base, a_secret, prime)
print(f"A's public value sent to B: {a_public}")

#B's public value: base^bob_secret mod prime
b_public = pow(base, b_secret, prime)
print(f"Bob's public value sent to Alice: {b_public}")

#shared secret for A: b_public^a_secret mod prime
a_shared = pow(b_public, a_secret, prime)

#shared secret for B: a_public^b_secret mod prime
b_shared = pow(a_public, b_secret, prime)

# Verify that both shared secrets match
if a_shared == b_shared:
    print(f"Shared secret successfully established: {a_shared}")
else:
    print("Error: Shared secrets do not match.")
