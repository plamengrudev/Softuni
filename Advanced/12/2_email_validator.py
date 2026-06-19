class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "org", "net"]

line = input()
while line != "End":
    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = line.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." not in domain_name:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    domain = domain_name.split(".")[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    line = input()