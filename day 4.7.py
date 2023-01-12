def countstrings(n, start):
    if n == 0:
        return 1
    count = 0
    for i in range(start, 5):
        count += countstrings(n - 1, i)
    return count
def countVowelStrings(n):
    #  char arr[5]={'a','e','i','o','u'};
    # starting from index 0 add the vowels to strings
    return countstrings(n, 0)
n = 1
print(countVowelStrings(n))



"""Count of lexicographically sorted strings of length 1 starting from characters a, e, i, o, and u is 1.
Count of strings of length 2 that are in lexicographical order starting from characters a, e, i, o, and u is given by:
The count of lexicographically sorted strings of length 2 starting from characters a is given by the count of the lexicographical strings of length 1 starting from character greater than or equal to a. Therefore, the count is 5.
The count of lexicographically sorted strings of length 2 starting from characters e is given by the count of the lexicographical strings of length 1 starting from character greater than or equal to e. Therefore, the count is 4.
The count of lexicographically sorted strings of length 2 starting from characters i is given by the count of the lexicographical strings of length 1 starting from character greater than or equal to i. Therefore, the count is 3.
The count of lexicographically sorted strings of length 2 starting from characters o is given by the count of the lexicographical strings of length 1 starting from character greater than or equal to o. Therefore, the count is 2.
The count of lexicographically sorted strings of length 2 starting from characters u is given by the count of the lexicographical strings of length 1 starting from character greater than or equal to u. Therefore, the count is 1.
Therefore, the total count of strings length 2 is given by: 5 + 4 + 3 + 2 + 1 = 15.
By observing the above pattern the count of strings of length N starting from each vowel character ch is given by the sum of the count of the lexicographical strings of length (N – 1) starting from character greater than or equal to ch."""