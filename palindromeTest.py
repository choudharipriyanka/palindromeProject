import unittest


def count_palindrome(str):

    # create empty 2-D matrix that counts
    # all palindrome substring. dp[i][j]
    # stores counts of palindromic
    # substrings in st[i..j]
    n = len(str)
    dp = [[0 for x in range(n)]
          for y in range(n)]

    # P[i][j] = true if substring str[i..j]
    # is palindrome, else false
    P = [[False for x in range(n)]
         for y in range(n)]

    # palindrome of single length
    for i in range(n):
        P[i][i] = True

    # palindrome of length 2
    for i in range(n - 1):
        if (str[i] == str[i + 1]):
            P[i][i + 1] = True
            dp[i][i + 1] = 1

    # Palindromes of length more than 2.
    # We start with a gap of length 2 and fill DP
    # table in a way that the gap between starting and
    # ending indexes increase one by one by
    # outer loop.
    for gap in range(2, n):

        # Pick a starting point for the current gap
        for i in range(n - gap):

            # Set ending point
            j = gap + i

            # If current string is palindrome
            if (str[i] == str[j] and P[i + 1][j - 1]):
                P[i][j] = True

            # Add current palindrome substring ( + 1)
            # and rest palindrome substring (dp[i][j-1] +
            # dp[i+1][j]) remove common palindrome
            # substrings (- dp[i+1][j-1])
            if (P[i][j] == True):
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] + 1 - dp[i + 1][j - 1])
            else:
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] - dp[i + 1][j - 1])

    # return total palindromic substrings
    return dp[0][n - 1]



def check_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards"""
    # implement check_palindrome_iterative and check_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    return check_palindrome_iterative(text)


def check_palindrome_iterative(text):
    # TODO: implement the check_palindrome function iteratively here
    # once implemented, change check_palindrome to call check_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    # First, setting up 2 pointer. First and last pointer.

    first_pointer = 0
    last_pointer = len(text) - 1
    # iteration through when the first index is less than the last index
    while(first_pointer <= last_pointer):

    # set up different while loop condition to do comparison
    # test different condition of the palindrome cases
    #
        # Get letters only
        while not text[first_pointer].isalpha():
            first_pointer += 1
            if first_pointer > len(text) - 1:
                return True
        while not text[last_pointer].isalpha():
            last_pointer -= 1
            if last_pointer < 0:
                return True

        # Not same, return
        if(text[first_pointer].lower() != text[last_pointer].lower()):
            return False

        first_pointer += 1
        last_pointer -= 1

    return True



class MyTestCase(unittest.TestCase):

    def test_check_palindrome_with_mirrored_strings(self):
        # simple palindromes that are mirrored strings
        assert check_palindrome('') is True  # base case
        assert check_palindrome('A') is True  # base case
        assert check_palindrome('BB') is True
        assert check_palindrome('LOL') is True
        assert check_palindrome('noon') is True
        assert check_palindrome('radar') is True
        assert check_palindrome('racecar') is True


    def test_check_palindrome_with_mixed_casing(self):
        # palindromes with mixed leter casing
        assert check_palindrome('Bb') is True
        assert check_palindrome('NoOn') is True
        assert check_palindrome('Radar') is True
        assert check_palindrome('RaceCar') is True

    def test_check_palindrome_with_whitespace(self):
        # palindromes with whitespace
        assert check_palindrome('taco cat') is True
        assert check_palindrome('race car') is True
        assert check_palindrome('race fast safe car') is True

    def test_check_palindrome_with_whitespace_and_mixed_casing(self):
        # palindromes with whitespace and mixed letter casing
        assert check_palindrome('Taco Cat') is True
        assert check_palindrome('Race Car') is True
        assert check_palindrome('Race Fast Safe Car') is True


    def test_check_palindrome_with_non_palindromic_strings(self):
        assert check_palindrome('AB') is False  # even length
        assert check_palindrome('ABC') is False  # odd length
        assert check_palindrome('doge') is False
        assert check_palindrome('monkey') is False
        assert check_palindrome('chicken, monkey!') is False

    def test_count_palindrome_with_palindromic_sub_strings(self):
        assert count_palindrome("ababababa")==16, "is True"
        assert count_palindrome("aba")==1, "is True"

if __name__ == '__main__':
    unittest.main()

