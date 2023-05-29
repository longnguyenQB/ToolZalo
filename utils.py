import time
import random
import re
import json
import email
import imaplib


def choice_reaction():
    list_reaction = ['Thích', 'Yêu thích', 'Thương thương']
    return random.choice(list_reaction)


def sleep_very_short():
    return time.sleep(random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))


def sleep_short():
    return time.sleep(random.choice(range(2, 5)))


def sleep_long():
    return time.sleep(random.choice(range(5, 10)))


def sleep_very_long():
    return time.sleep(random.choice(range(8, 20)))


def sleep_very_very_long():
    return time.sleep(random.choice(range(20, 60)))


# def get_comment_from_post(post_url, cookies_profile):
#     post_list = []
#     for post in get_posts(post_urls=[post_url],
#                           options={
#                               "comments": True,
#                               "reactions": True
#                           },
#                           cookies=cookies_profile):
#         post_list.append(post)
#     list_comment = [
#         post_list[0]['comments_full'][i]['comment_text']
#         for i in range(len(post_list[0]['comments_full']))
#     ]
#     with open('./name_vn.txt', 'r', encoding="utf8") as f:
#         names = [word[:-1] for word in f]
#     pattern1 = '|'.join([r"\b" + name + r"\b" for name in names])
#     list_comment = [
#         comment for comment in pattern1
#         if not re.search(pattern1, comment.lower())
#     ]
#     return list_comment


# Vẽ frame message
def _one_frame(text):                 # text is supposed to be a list of lines
    lt = len(text[0])
    horz = '+' + '-'*lt + '+'         # Make the horizontal line +-------+
    result = [horz]                   # Top of the frame
    for line in text:
        result.append('|'+line+'|')  # Add the borders for each line
    result.append(horz)               # Bottom of the frame
    return result


def frame(text, repeat, thickness):
    text = [" %s " % text]*repeat       # add spaces and repeat as a list
    for i in range(thickness):
        text = _one_frame(text)       # draw one frame per iteration
    return '\n'.join(text)            # join lines


def open_txt(path):
    with open(path, 'r', encoding="utf8") as f:
        content = [word[:-1] for word in f]
    f.close()
    return content


def write_txt(path, content):
    with open(path, 'w', encoding="utf8") as f:
        for line in content:
            f.write(f"{line}\n")
    f.close()


def read_js(path):
    f = open(path, "r", encoding='utf-8')
    data = json.loads(f.read())
    return data


def write_js(data, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def gen_name(name_vn):
    anphabelt = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    name_anphabelt = ''
    name_number = ''
    for _ in range(random.randint(1, 6)):
        name_anphabelt += random.choice(anphabelt)
    for _ in range(random.randint(1, 6)):
        name_number += random.choice(number)
    name = random.choice(name_vn) + random.choice(
        ['_', '.']) + name_anphabelt + random.choice(['_', '.', '']) + name_number
    return name


def gen_password():
    anphabelt = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    password_anphabelt = ''
    password_number = ''
    for _ in range(random.randint(6, 10)):
        password_anphabelt += random.choice(anphabelt)
        password_number += random.choice(number)
    return '@' + password_anphabelt + password_number


def get_code_email(EMAIL, PASSWORD):
    SERVER = 'outlook.office365.com'

    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    x = mail.select('inbox', readonly=True)
    num = x[1][0].decode('utf-8')
    # from here you can start a loop of how many mails you want, if 10, then num-9 to num
    resp, lst = mail.fetch(num, '(RFC822)')
    body = lst[0][1]
    email_message = email.message_from_bytes(body)
    return email_message['Subject'][:6]
