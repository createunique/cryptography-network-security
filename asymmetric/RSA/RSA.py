import random

def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(bits=16):
    """
    Generate a random prime number of a specified bit size.
    
    Args:
        bits (int): The bit size of the prime number (default is 16).
    
    Returns:
        int: A prime number.
    """
    while True:
        num = random.getrandbits(bits) | 1  # Ensure the number is odd
        if is_prime(num):
            return num

def compute_gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The GCD of the two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

def compute_mod_inverse(e, phi):
    """
    Compute the modular inverse of e modulo phi using the Extended Euclidean Algorithm.
    
    Args:
        e (int): The number to find the inverse of.
        phi (int): The modulus.
    
    Returns:
        int: The modular inverse of e modulo phi.
    """
    old_r, r = e, phi
    old_s, s = 1, 0
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    return old_s % phi  # Ensure the result is positive

def generate_keys(bits=16):
    """
    Generate RSA public and private keys.
    
    Args:
        bits (int): The bit size of the prime numbers (default is 16).
    
    Returns:
        tuple: A tuple containing the public key (e, n) and private key (d, n).
    """
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:  # Ensure p and q are distinct
        q = generate_prime(bits)
    
    n = p * q  # Compute the modulus
    phi = (p - 1) * (q - 1)  # Compute Euler's totient function
    
    e = 65537  # Commonly used value for e
    while compute_gcd(e, phi) != 1:  # Ensure e and phi are coprime
        e = random.randrange(3, phi, 2)  # Choose another odd number
    
    d = compute_mod_inverse(e, phi)  # Compute the private key
    
    return ((e, n), (d, n))

def encrypt_text(text, public_key):
    """
    Encrypt a text message using RSA.
    
    Args:
        text (str): The text to encrypt.
        public_key (tuple): The public key (e, n).
    
    Returns:
        list: A list of encrypted numbers.
    """
    e, n = public_key
    encrypted = []
    for char in text:
        encrypted.append(pow(ord(char), e, n))
    return encrypted

def decrypt_text(encrypted, private_key):
    """
    Decrypt an encrypted message using RSA.
    
    Args:
        encrypted (list): The list of encrypted numbers.
        private_key (tuple): The private key (d, n).
    
    Returns:
        str: The decrypted text.
    """
    d, n = private_key
    decrypted = []
    for num in encrypted:
        decrypted.append(chr(pow(num, d, n)))
    return ''.join(decrypted)

def encrypt_number(number, public_key):
    """
    Encrypt a number using RSA.
    
    Args:
        number (int): The number to encrypt.
        public_key (tuple): The public key (e, n).
    
    Returns:
        int: The encrypted number.
    
    Raises:
        ValueError: If the number is greater than or equal to the modulus.
    """
    e, n = public_key
    if number >= n:
        raise ValueError("Number must be less than the modulus for encryption.")
    return pow(number, e, n)

def decrypt_number(encrypted_number, private_key):
    """
    Decrypt an encrypted number using RSA.
    
    Args:
        encrypted_number (int): The encrypted number.
        private_key (tuple): The private key (d, n).
    
    Returns:
        int: The decrypted number.
    """
    d, n = private_key
    return pow(encrypted_number, d, n)

def main_menu():
    """
    Display a menu-driven interface for RSA key generation, encryption, and decryption.
    """
    public_key = None
    private_key = None
    while True:
        print("\nMenu:")
        print("1. Generate and display RSA keys")
        print("2. Encrypt and decrypt a text")
        print("3. Encrypt and decrypt a number")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            while True:
                bits = input("Enter the bit size for primes (default 16): ").strip()
                if not bits:
                    bits = 16
                    break
                try:
                    bits = int(bits)
                    if bits < 8:
                        print("Bit size too small. Using minimum 8 bits.")
                        bits = 8
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            public_key, private_key = generate_keys(bits)
            print("\nPublic Key (e, n):", public_key)
            print("Private Key (d, n):", private_key)
        
        elif choice == '2':
            if public_key is None or private_key is None:
                print("Error: Please generate keys first using option 1.")
                continue
            text = input("Enter the text to encrypt: ")
            encrypted = encrypt_text(text, public_key)
            print("\nEncrypted ciphertext:", encrypted)
            decrypted = decrypt_text(encrypted, private_key)
            print("Decrypted text:", decrypted)
        
        elif choice == '3':
            if public_key is None or private_key is None:
                print("Error: Please generate keys first using option 1.")
                continue
            try:
                number = int(input("Enter a number to encrypt: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
            n = public_key[1]
            if number >= n:
                print(f"Error: Number must be less than the modulus {n}.")
                continue
            try:
                encrypted_num = encrypt_number(number, public_key)
                print("\nEncrypted number:", encrypted_num)
                decrypted_num = decrypt_number(encrypted_num, private_key)
                print("Decrypted number:", decrypted_num)
            except ValueError as e:
                print(e)
        
        elif choice == '4':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main_menu()
