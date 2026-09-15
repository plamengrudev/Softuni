def vowel_filter(function):
    def wrapper():
        result=function()
        chars=[]
        for ch in result:
            if ch in ['a','i','e','o','y','u']:
                chars.append(ch)
        return chars

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())