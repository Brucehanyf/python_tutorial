from test.name_function import get_format_name

print("Enter Q exit at any time to exit")
while True:
    first_name = input('please give me your first name')
    if first_name == 'Q':
        break
    last_name = input('please give me your last name')
    if last_name == 'Q':
        break
    full_name = get_format_name(first_name,last_name)
    print('your full_name is '+full_name)