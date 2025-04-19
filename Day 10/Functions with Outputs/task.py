def format_name(f_name, l_name):
    f_name = list(f_name)
    l_name = list(l_name)
    f_name[0] = f_name[0].upper()
    l_name[0] = l_name[0].upper()
    # f_name.title() <- no need to convert to list
    # l_name.title()
    return "".join(f_name) + " " + "".join(l_name)

f_name =  input("What's your first name?\n").lower()
l_name = input("What's your last name?\n").lower()

name = format_name(f_name, l_name)

print(name)