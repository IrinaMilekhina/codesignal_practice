"""
You are given two strings: pattern and source. The first string pattern contains only the symbols 0
and 1, and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern.

We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring.
– Where there is a 1 in the pattern, there is a consonant in the substring.

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
– “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches
 this pattern: 0 matches a, 1 matches m, and 0 matches a.
– “010” doesn’t match source[1..3] = "maz"
– “010” matches source[2..4] = "azi"
– “010” doesn’t match source[3..5] = "zin"
– “010” doesn’t match source[4..6] = "ing"

For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
– There are no double vowels in the string "codesignal", so it’s not possible for any of its
substrings to match this pattern.

Guaranteed constraints:
1 ≤ source.length ≤ 103
1 ≤ pattern.length ≤ 103
This is a pattern-matching question where instances of a pattern need to be found inside of a larger
 array. It has the advantage of testing several fundamental programming skills at once:
 traversing multiple arrays with nested loops, working with subarrays, and performing basic
 collections/string operations.

Note that the guaranteed constraints in this question indicate that the candidate shouldn’t worry
about optimizing their solution.
"""
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

source_1 = 'amazing'
pattern_1 = '010'

source_2 = 'codesignal'
pattern_2 = '100'


def check_pattern(pat: str, val: str) -> int:
    for p, v in zip(pat, val):
        """
        0 = vowel
        1 = consonant
        """
        vow_flag = v in vowels
        if int(p) and vow_flag or not int(p) and not vow_flag:
            return 0
    return 1


def q_sol(s: str, p: str) -> int:
    result = 0
    if len(p) <= len(s):
        options = []
        for i in range(len(s) - len(p) + 1):
            options.append(s[i:i + 3])
        for el in options:
            result += check_pattern(pat=p, val=el)
    return result


print(q_sol(source_1, pattern_1))
print(q_sol(source_2, pattern_2))
