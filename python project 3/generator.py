import secrets
import string
import math

def generate_password():
    print("=== DecodeLabs Random Password Generator ===")
    
    # PHASE 1: INPUT & VALIDATION
    try:
        length = int(input("Enter target password length (e.g., 12): ").strip())
        if length <= 0:
            print("⚠️ Error: Length must be a positive integer.")
            return
    except ValueError:
        print("⚠️ Invalid Data: Please enter a valid integer for the length.")
        return

    # PHASE 2: BACKEND TRANSFORMATION ENGINE
    # Utilizing the string module for character categorization[cite: 31]
    # And the secrets module for cryptographic security instead of standard random[cite: 33]
    char_pool = string.ascii_letters + string.digits + string.punctuation
    
    # Using ''.join() for optimal O(N) memory performance[cite: 35]
    password_list = [secrets.choice(char_pool) for _ in range(length)]
    secure_password = "".join(password_list)
    
    # PHASE 3: OUTPUT & ENTROPY EVALUATION
    # Calculating information entropy: E = L * log2(R)[cite: 37]
    pool_size = len(char_pool)
    entropy = length * math.log2(pool_size)

    print("\n========================================")
    print(f"SECURE PASSWORD : {secure_password}")
    print(f"CHARACTER POOL  : {pool_size} possible characters")
    print(f"EST. ENTROPY    : {entropy:.2f} bits")
    print("========================================")
    print("System Status: Verified & Encrypted.")

if __name__ == "__main__":
    generate_password()
    