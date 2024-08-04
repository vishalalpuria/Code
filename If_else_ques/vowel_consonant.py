# Check if a character is a vowel or a consonant

ch = input("Enter a character: ")

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")