import collections
import re
def f(S:str, C)-> str:
    # Separate name into First, Middle, and Last name.
    full_names = S.split(", ")
    e_names = re.sub(r'[^a-z, ]', '', S.lower()).split(", ")
    count_dict = collections.defaultdict(int)
    answer = []

    for _ in range(len(e_names)):
        fl_name = e_names[_].split()[0] + e_names[_].split()[-1]
        count_dict[fl_name] += 1
        email = '<' +  e_names[_].split()[0].lower() + '.' + \
                e_names[_].split()[-1].lower() + '@' + C.lower() + '.com>'
        if count_dict[fl_name] > 1:
            email = '<' +  e_names[_].split()[0].lower() + '.' +  \
                    e_names[_].split()[-1].lower() + \
                    str(count_dict[fl_name]) + '@' + C.lower() + '.com>'

        answer.append(full_names[_] + ' ' + email)

    return ', '.join(answer)


print(f("John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker", 'example'))

