import hashlib
import argparse
import time

# Function to crack a hash using a wordlist
def crack_hash(hash_to_crack, wordlist_file, algorithm):
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()

                # Select hashing algorithm
                if algorithm == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif algorithm == "sha256":
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print(f"[-] Unsupported algorithm: {algorithm}")
                    return

                print(f"Trying: {word} -> {hashed_word}")

                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return

        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print(f"[-] Wordlist file '{wordlist_file}' not found.")
    except Exception as e:
        print(f"[!] Error: {e}")

# Main function using argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔐 Crack MD5 or SHA256 password hashes using a wordlist.")

    parser.add_argument("--hash", required=True, help="The hashed password you want to crack.")
    parser.add_argument("--wordlist", required=True, help="Path to the wordlist file.")
    parser.add_argument("--algo", default="md5", choices=["md5", "sha256"], help="Hashing algorithm (default: md5)")

    args = parser.parse_args()

    print("[*] Starting password cracker...")
    start_time = time.time()

    crack_hash(args.hash, args.wordlist, args.algo)

    end_time = time.time()
    print(f"[✔] Done in {end_time - start_time:.2f} seconds.")
