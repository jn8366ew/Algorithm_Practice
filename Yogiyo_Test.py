def f(S:str, C:str)-> str:
    # Separate name into First, Middle, and Last name.
    split_names = S.split(", ")
    strs = ''
    name_list = []
    email_list = []

    for name in split_names:

        name.split()[0]

        if len(name.split()) == 3:
            first = name.split()[0]
            middle = name.split()[1]
            last = name.split()[2]
            full_name = name.split()[0] + ' ' + name.split()[1] + ' ' + name.split()[2]
            email = '<' + name.split()[0].lower() + '.' + name.split()[2].lower() + '@' + C.lower() + '.com>'
            if email in email_list:
                temp = 1
                if ''.join(filter(str.isdigit, email)) == '':
                    email = '<' + name.split()[0].lower() + '.' + name.split()[2].lower() + str(
                        temp) + '@' + C.lower() + '.com>'
                else:
                    temp += int(''.join(filter(str.isdigit, email)))
                    email = '<' + name.split()[0].lower() + '.' + name.split()[2].lower() + str(
                        temp) + '@' + C.lower() + '.com>'




        else:
            first = name.split()[0]
            middle = ''
            last = name.split()[1]
            full_name = name.split()[0] + ' ' + name.split()[1]
            email = '<' + name.split()[0].lower() + '.' + name.split()[1].lower() + '@' + C.lower() + '.com>'
            if email in email_list:
                temp = 1
                if ''.join(filter(str.isdigit, email)) == '':
                    email = '<' + name.split()[0].lower() + '.' + name.split()[1].lower() + str(temp) + '@' + C.lower() + '.com>'
                else:
                    temp += int(''.join(filter(str.isdigit, email)))
                    email = '<' + name.split()[0].lower() + '.' + name.split()[1].lower() + str(temp) + '@' + C.lower() + '.com>'


        email_list.append(email)





        name_list.append(full_name + ' ' + email)

    strs = ', '.join(name_list)
    return strs


print(f("John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker", 'example'))

