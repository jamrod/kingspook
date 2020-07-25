import os

page_num = 0

art_l = os.listdir('pages/art/l')

for file in art_l:
    filename = f"pages/art/l/{file}"
    print(filename)
    str = f"number: {page_num}\n---"
    page_num += 1
    new_content = ''
    with open(filename, 'r') as read_file:
        for line in read_file:
            text = line
            if 'number' in line:
                text = str
            new_content += text

    with open(filename, 'w') as write_file:
        write_file.write(new_content)


art_s = os.listdir('pages/art/s')

for file in art_s:
    filename = f"pages/art/s/{file}"
    print(filename)
    str = f"number: {page_num}\n---"

    page_num += 1
    new_content = ''
    with open(filename, 'r') as read_file:
        for line in read_file:
            text = line
            if 'number' in line:
                text = str
            new_content += text

    with open(filename, 'w') as write_file:
        write_file.write(new_content)
