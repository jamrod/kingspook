import os

pics = os.listdir('assets/img/art')

for pic in pics:
    name = pic[0:-4]
    strng = f"""---
name: {name}
path: "/assets/img/art/{pic}"
---
"""
    file_name = 'pages/art/' + name + '.md'
    with open(file_name, 'w') as new_file:
        new_file.write(strng)
