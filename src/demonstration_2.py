"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""

words = ["lambda", "school"]
order = "hlabcdefgijkmnopqrstuvwxyz"


def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str

    Output:
    bool
    """

    #  JESS's solution

    """ hashed_letters = {}
    count = 0
    for letter in alpha_order:
        hashed_letters[letter] = count
        count += 1
    # iterate the array
    for word in range(len(words) - 1):

        # iterate the first word
        for letter in range(len(words[word])):
            # create variables for the letters to check
            first_letter = words[word][letter]
            second_letter = words[word + 1][letter]
            print('first', first_letter, 'second', second_letter)
            if hashed_letters[first_letter] < hashed_letters[second_letter] \
                    and len(words[word]) <= len(words[word + 1]):
                continue
            # if first word1[i] comes after 2nd word2[i] return False
            if hashed_letters[first_letter] > hashed_letters[second_letter]

    return True """

    alphabet_dict = {}

    for i in range(len(alpha_order)):
        character = alpha_order[i]
        alphabet_dict[character] = i
    print(alphabet_dict)

    for word_index in range(len(words) - 1):

        word_a = words[word_index]
        word_b = words[word_index + 1]
        for letter_index in range(len(word_a)):
            char_a = word_a[letter_index]
            char_b = word_b[letter_index]

            index_a = alphabet_dict[char_a]
            index_b = alphabet_dict[char_b]

            if index_a == index_b
            continue
            if index_a < index_b
            continue
            if index_a > index_b
            return False
    return True


are_words_sorted(words, order)

# PLAN
# compare pairs of words to make sure word 1 < word 2
# compare every letter in each word in the alphabet and the compare them to each other to determine if the order is correct

# Step 1: map each letter to numeric value in store in dict
# Step 2:
# iterate through words and compare pais of words to see if theyre in sorted order
# compare the first letters, if theyre different we know which one comes first /second
# if theyre the same compare the next two letter
# repeat
# if not return false
# Step 3: return true


# Dictionary Comprehension
alpha = 'abcdefg'
dictionary = {character: alpha.index(character) for character in alpha}

d2 = {}
for character in alpha:
    d2[character] = alpha.index(character)
