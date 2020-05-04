def get_new_s(s):
    new_s = ''
    for i in s:
        if i == " ":
            new_s += '%s'
        else:
            new_s += i
    return new_s

print(get_new_s("We Are Happy"))