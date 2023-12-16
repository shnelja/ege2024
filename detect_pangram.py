def is_pangram(s):
    s = s.lower()
    s = s.replace(' ', '')
    all_letters = 'qwertyuiopasdfghjklzxcvbnm'
    counters = []
    for i in range(len(all_letters)):
        count = 0
        for c in s:
            if all_letters[i] == c:
                count += 1
        counters += [count]
    if 0 not in counters:
        return True
    return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))