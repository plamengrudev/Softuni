def palindrome(line, var: int):
    if var >= len(line) // 2:
        return f"{line} is a palindrome"

    if line[var] != line[-1 - var]:
        return f"{line} is not a palindrome"

    return palindrome(line, var + 1)