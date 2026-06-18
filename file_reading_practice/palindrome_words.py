"""
## 4. Find All Palindrome Words  *(Medium)*

=================================================
PALINDROME WORDS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every PALINDROME word (a word that reads the
same forwards and backwards).

Write a helper FUNCTION called `is_palindrome`
that takes a single word and returns True if
it is a palindrome, else False. Pass every
word in the file to this function ONE AT A
TIME.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
hello
noon
civic
python
deified
racecar
banana

Output Example:
level
radar
noon
civic
deified
racecar
Total palindromes: 6

-------------------------------------------------
Explanation:
- "level"    reversed -> "level"   -> palindrome
- "radar"    reversed -> "radar"   -> palindrome
- "hello"    reversed -> "olleh"   -> not
- "noon"     reversed -> "noon"    -> palindrome
- "civic"    reversed -> "civic"   -> palindrome
- "python"   reversed -> "nohtyp"  -> not
- "deified"  reversed -> "deified" -> palindrome
- "racecar"  reversed -> "racecar" -> palindrome
- "banana"   reversed -> "ananab"  -> not
=================================================

"""
def is_palindrome(word: str) -> bool:
    """Return True if word is a palindrome."""
    return word == word[::-1]


def find_palindromes(filename="sowpods.txt"):
    palindromes = []

    with open(filename, "r") as f:
        for word in f:
            word = word.strip().lower()
            if is_palindrome(word):
                palindromes.append(word)

    # Print results
    for p in palindromes:
        print(p)
    print("Total palindromes:", len(palindromes))


find_palindromes("sowpods.txt")
palindromes = find_palindromes("sowpods.txt")
if __name__ == "__main__":
        find_palindromes("sowpods.txt")



