def requests_generator(file):
    line = file.readline().replace(" ", "")
    while line:
        line = file.readline().replace(" ", "")
        line = line.split("-")

        ip_ = line[0]
        method_ = line[2][line[2].find('"')+1:line[2].find('/', line[2].find('"'))]
        request_ = line[2][line[2].find('/', line[2].find('"')):line[2].find('"', line[2].find('/', line[2].find('"')))]

        data = (ip_, method_, request_)
        yield data


my_file = open("t1/nginx_logs.txt", "r", encoding="utf-8")
request = requests_generator(my_file)
try:
    while True:
        print(next(request))
except IndexError:
    print("End of file.")

my_file.close()
