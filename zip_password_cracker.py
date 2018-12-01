import zipfile
filename = input('Enter zip filename (test.zip): ')
flag = False


def check(passwords):
    try:
        with zipfile.ZipFile(filename) as zf:
            password = passwords.encode('latin1')
            zf.extractall(pwd=password)
        return True
    except:
        return False


word_list = open(input('Enter passwords list filename (pass.txt): '), 'r')
wl = word_list.readlines()
for words in wl:
    p = words.strip()
    if check(p):
        print('Password Found : ' + p)
        flag = True
        break

if not flag:
    print('Password Not Found!')
