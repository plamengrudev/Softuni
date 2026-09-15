class Integer:

    def __init__(self,value: int):
        self.value=value
    
    @classmethod
    def from_float(cls,float_value):
        if not isinstance(float_value,float):
            return f'value is not a float'
        return cls(int(float_value))
    
    @classmethod
    def from_roman(cls,roman_value):
        roman = roman_value.upper()
        vals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        i = 0
        total = 0
        while i < len(roman):
            ch = roman[i]
            value = vals[ch]
            if i + 1 < len(roman):
                nxt = roman[i + 1]
                nxt_value = vals[nxt]
                if value < nxt_value:
                    total += (nxt_value - value)
                    i += 2
                    continue
            total += value
            i += 1

        return cls(total)
    
    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return f'wrong type'
        try:
            return cls(int(value))
        except ValueError:
            return f'wrong type'
        

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))