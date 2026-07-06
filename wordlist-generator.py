#!/usr/bin/env python3
"""
Custom Wordlist Generator - Cybersecurity Tool
Author:RUTH Mesafint
id: 1602351
"""

import sys

def generate_wordlist(first_name, birth_year, pet_name):
    """
    Generate password permutations from personal info.
    pet_name can be empty string if no pet.
    """
    candidates = set()
    
    # Base variations (start with name + year only)
    base_words = [
        first_name,
        f"{first_name}{birth_year}",
        f"{birth_year}{first_name}",
        f"{first_name}.{birth_year}",
        f"{first_name}_{birth_year}",
        f"{first_name}{birth_year}!",
        f"{first_name}@{birth_year}",
        f"{first_name.upper()}{birth_year}",
        f"{first_name.lower()}{birth_year}",
        f"{first_name.capitalize()}{birth_year}",
        f"{birth_year}{first_name}!",
    ]
    
    # Add pet variations ONLY if pet name is provided
    if pet_name:
        pet_variations = [
            pet_name,
            f"{first_name}{pet_name}",
            f"{pet_name}{first_name}",
            f"{first_name}{pet_name}{birth_year}",
            f"{birth_year}{first_name}{pet_name}",
            f"{pet_name}{birth_year}",
            f"{birth_year}{pet_name}",
        ]
        base_words.extend(pet_variations)
    
    # Common substitutions (leet speak)
    leet_map = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7']
    }
    
    # Add leet variations for each base word
    for word in base_words:
        candidates.add(word)
        for char, replacements in leet_map.items():
            if char in word.lower():
                for rep in replacements:
                    candidates.add(word.lower().replace(char, rep))
                    if word and word[0].isupper():
                        candidates.add(word.lower().replace(char, rep).capitalize())
    
    # Add birth year combos
    for suffix in ['', '!', '@123', '#', '123']:
        candidates.add(f"{first_name}{birth_year}{suffix}")
        if pet_name:
            candidates.add(f"{pet_name}{birth_year}{suffix}")
    
    # Add year without century
    year_short = birth_year[-2:]
    candidates.add(f"{first_name}{year_short}")
    candidates.add(f"{first_name}{year_short}!")
    if pet_name:
        candidates.add(f"{pet_name}{year_short}")
    
    return sorted(candidates)

def save_wordlist(wordlist, filename="wordlist.txt"):
    """Save generated wordlist to file."""
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
    return len(wordlist)

def main():
    print("=" * 50)
    print("CUSTOM WORDLIST GENERATOR - CYBER SECURITY TOOL")
    print("=" * 50)
    print("Purpose: Generate password candidates for authorized")
    print("penetration testing and password security audits.\n")
    
    try:
        first_name = input("[?] Enter first name: ").strip()
        birth_year = input("[?] Enter birth year (YYYY): ").strip()
        pet_name = input("[?] Enter pet name (press Enter if none): ").strip()
        
        if not first_name or not birth_year:
            print("\n[!] ERROR: First name and birth year are required.")
            sys.exit(1)
        
        if not birth_year.isdigit() or len(birth_year) != 4:
            print("\n[!] ERROR: Birth year must be 4 digits (e.g., 1992).")
            sys.exit(1)
        
        if int(birth_year) < 1900 or int(birth_year) > 2026:
            print("\n[!] ERROR: Birth year must be between 1900 and 2026.")
            sys.exit(1)
        
        print("\n[*] Generating wordlist...")
        wordlist = generate_wordlist(first_name, birth_year, pet_name)
        
        print("\n--- SAMPLE OUTPUT (first 15 passwords) ---")
        for i, word in enumerate(wordlist[:15], 1):
            print(f"{i:2}. {word}")
        
        print("...")
        
        filename = f"wordlist_{first_name.lower()}.txt"
        count = save_wordlist(wordlist, filename)
        
        print("\n" + "=" * 50)
        print(f"[✓] SUCCESS: Generated {count} passwords")
        print(f"[✓] Saved to: {filename}")
        print("[✓] Ready for use with password cracking tools")
        print("=" * 50)
        
        if not pet_name:
            print("\n[ℹ] Note: No pet name provided. Generated passwords use only name + year.")
        
    except KeyboardInterrupt:
        print("\n\n[!] Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
