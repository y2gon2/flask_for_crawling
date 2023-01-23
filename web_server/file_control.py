
def save_file(result, code):
    path = "./web_server/data/%s.txt" % code
    with open(path, 'w') as f:
        f.write(str(result))

# save_file({"code":"1234"}, "005930")