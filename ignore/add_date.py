import os

art_s = os.listdir('pages/art/s')

for file in art_s:
    filename = f"pages/art/s/{file}"
    print(filename)
    str = f"""date: 2020-05-01
---
"""
    new_content = ''
    with open(filename, 'r') as read_file:
        count = 0
        for line in read_file:
            text = line
            if line == '---\n':
                count += 1
                if count == 2:
                    text = str
            new_content += text

    with open(filename, 'w') as write_file:
        write_file.write(new_content)
