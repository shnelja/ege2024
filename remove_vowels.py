vowels = 'aeiouAEIOU'

def disemvowel(string_):
    for c in string_:
        if c in vowels:
            string_ = string_.replace(c, '', 1)
    return string_

print(disemvowel('This website is for losers LOL!'))