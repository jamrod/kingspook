# Kingspook.com

## Technologies

Built with 11ty, Liquid and Bootstrap

### Eleventy commands

'npm run build' or 'eleventy'
'npm serve' or 'eleventy --serve'
runs on port 8080
'npm run deploy' to upload

## Layout

- About
- Gallery
  - Individual pics

## Links

Deployed Site : [kingspook.com]
Git Repo: [github.com/jamrod/kingspook]

## Things Learned

I used Bootstrap mostly for responsive design.
Bootstrap had an issue with chrome on mobile and the images not resizing correctly:

- To Fix: I needed to wrap everything in my header in a div with class="container" and have the class on the images to "img-fluid"

I used Python to create md files for the art work and to update them when I made changes. Liquid and 11ty can use the .md files to create pages on the final site, the files just have data as tags wrapped in "---" marks. I initially created a Python script to loop through the folder containing the art files and create .md files for each one so it could have its own page.

In order to paginate all the images I created a linked-list with all the .md files by setting 'previous' and 'next' values. I had tried to order them with numbers or setting them all to the same dates but it hadn't worked out because liquid and Python were not sorting the arrays the same. So I linked them all together by incrementing the date by a day with each file and removing the page number. Liquid sorts by date so the order they appear in the gallery will match the order if you click through one at a time.
Here's the script to do it:

```
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
```
