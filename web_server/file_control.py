
def save_file(result, code):
    path = "data/%s.txt" % code
    with open(path, 'w') as f:
        f.write(str(result))

# save_file({"code":"1234"}, "삼성전자")