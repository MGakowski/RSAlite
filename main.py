# -*- coding: UTF-8 -*-
import math
from random import randint

numbertotest = int()
primefound = 0
lamdaN = int()
e = int()


def test_prime(a):
    b = round(math.sqrt(a))
    while b != 1:
        if a % b == 0:
            print(str(a) + " is not prime. Divides by " + str(int(b)))
            break
        else:
            b -= 1
    else:
        print(str(a) + " confirmed as prime.")


def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def compute_e():
    divisor = int(round(math.sqrt(numbertotest)))
    while divisor != 1:
        if numbertotest % divisor == 0:
            break
        else:
            divisor -= 1
    else:
        print(str(numbertotest) + " is prime and =e")
        global e
        e = int(numbertotest)
        global primefound
        primefound = int(numbertotest)


def modInverse(e, lamdaN):
    e = e % lamdaN;
    for q in range(1, lamdaN):
        if ((e * q) % lamdaN == 1):
            return q
    return 1


# Accept message and confirm primes
m = int(input("Message to encrypt: (Digits only)"))
p = int(input("First prime: "))
test_prime(p)
q = int(input("Second prime: "))
test_prime(q)

# Generate public key
n = p * q  # Second half of public key
lamdaN = int(compute_lcm(int(p - 1), int(q - 1)))
while primefound == 0:
    generaterandomnumber = int(randint(1, int(lamdaN)))
    numbertotest = generaterandomnumber
    compute_e()
print("Public key is e=" + str(e) + ", n=" + str(n))

# Generate private key (D, N)
d = int(modInverse(e, lamdaN))
print("Private key is d=" + str(d) + ", n=" + str(n))

# Encrypt message as CipherText
mtoe = m ** e
c = mtoe % n
print("Ciphertext=" + str(c))

# Decrypt ciphertext
ctod = c ** d
dec = ctod % n
print("Decrypted ciphertext " + str(dec))

# Print Steps:
print("")
print("Steps and Formulas involved:")
print("Public Key Generation:")
print("p = " + str(p))
print("q = " + str(q))
print("n = p*q")
print("n = " + str(n))
print("Lamda" + "(n) = lcm (p − 1, q − 1)")
print("Lamda" + "(" + str(n) + ") = lowest common multiple (" + str(p) + " − 1, " + str(q) + " − 1)")
print("Lamda" + "(" + str(n) + ") = " + str(lamdaN))
print("e = prime(rand(1, " + "Lamda" + "(n)))")
print("e = prime(rand(1, " + str(n) + "))")
print("e = " + str(e))
print("Public Key = e, n")
print("Public Key = " + str(e) + ", " + str(n))
print("")
print("Message Encryption:")
print("m = message/plaintext")
print("m = " + str(m))
print("c = m^e mod n")
print("c = " + str(m) + "^" + str(e) + " mod " + str(n))
print("c = " + str(mtoe) + " mod " + str(n))
print("c = " + str(c))
print("")
print("Private Key Generation:")
print("d = e modular inverse " + "Lamda" + "(n)")
print("d = " + str(e) + " modular inverse " + "Lamda" + "(" + str(n) + ")")
print("d = " + str(e) + " modular inverse " + str(lamdaN))
print("d = " + str(d))
print("Private Key = d, n")
print("Private Key = " + str(d) + ", " + str(n))
print("")
print("Message Decryption:")
print("m = c^d mod n")
print("m = " + str(c) + "^" + str(d) + " mod " + str(n))
print("m = " + str(dec))
