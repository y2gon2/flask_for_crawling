
def save_file(result, corp_name):
    path = "data/%s.txt" % corp_name
    with open(path, 'w') as f:
        f.write(str(result))