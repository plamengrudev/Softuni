import re

class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError(Exception):
    pass
class PasswordNoSpecialCharactersError(Exception):
    pass
class PasswordContainsSpacesError(Exception):
    pass

line=input()
while line!="Done":
    only_digits = bool(re.fullmatch(r"\d+", line))
    only_letters = bool(re.fullmatch(r"[A-Za-z]+", line))
    only_special = bool(re.fullmatch(r"[^A-Za-z0-9\s]+", line))
    no_special = bool(re.fullmatch(r"[A-Za-z0-9\s]+", line))
    if len(line)<8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    elif only_digits or only_letters or only_special:
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    elif no_special:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")
    elif re.search(r"\s",line):
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    print("Password is valid")
    line=input()