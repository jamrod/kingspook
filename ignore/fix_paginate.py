import os


def get_date_list(month, day):
    day = int(day)
    day += 1
    month = month
    if day > 30:
        day = '01'
        month = '05'
    elif day < 10:
        day = f"0{day}"
    else:
        day = str(day)
    return [month, day]


def process_file(filename, prev, dates):
    date_string = f"date: 2020-{dates[0]}-{dates[1]}\n"
    new_line = f"previous: {prev}\n"
    new_content = ''
    count = 0

    with open(filename, 'r') as read_file:
        for line in read_file:
            text = line
            if 'number' in line:
                text = ''
            elif 'previous' in line:
                text = ''
            elif 'next' in line:
                text = ''
            elif 'date' in line:
                text = date_string
            elif '---' in line:
                count += 1
                if count > 1:
                    text = new_line
            new_content += text
        return new_content


month = '04'
day = 0
prev = ''

files_list = []

art_l = os.listdir('pages/art/l')
art_l.sort()

for i, file in enumerate(art_l):
    filename = f"pages/art/l/{file}"
    compiled_path = f"/{filename[0:-3]}/"
    if not '.json' in filename:
        dates = get_date_list(month, day)
        month = dates[0]
        day = dates[1]
        new_text = process_file(filename, prev, dates)
        prev = compiled_path
        if i > 0:
            files_list[-1][1] += f"next: {compiled_path}\n---\n"
        files_list.append([filename, new_text])


art_s = os.listdir('pages/art/s')
art_s.sort()

for i, file in enumerate(art_s):
    filename = f"pages/art/s/{file}"
    compiled_path = f"/{filename[0:-3]}/"
    if not '.json' in filename:
        dates = get_date_list(month, day)
        month = dates[0]
        day = dates[1]
        new_text = process_file(filename, prev, dates)
        prev = compiled_path
        files_list[-1][1] += f"next: {compiled_path}\n---\n"
        if i == len(art_s) - 1:
            new_text += 'next: \n---\n'
        files_list.append([filename, new_text])

for item in files_list:
    with open(item[0], 'w') as write_file:
        write_file.write(item[1])
