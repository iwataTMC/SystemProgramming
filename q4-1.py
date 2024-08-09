def hash1(s):
    if not s:
        return 0

    first_char = s[0]
    if first_char in "abcde":
        # a, b, c, d, eで始まる文字列は0-8のバケットに割り当て
        return (ord(first_char) - ord("a")) * 2 % 9
    else:
        # それ以外の文字で始まる文字列は9-11のバケットに割り当て
        return 9 + (ord(first_char) - ord("f")) % 3

