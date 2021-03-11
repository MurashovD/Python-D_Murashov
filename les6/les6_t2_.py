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


def print_log(generator, spam_dict, log=False):
    try:
        while True:
            r = next(generator)
            if log:
                print(r)
            try:
                spam_dict[r[0]] += 1
            except KeyError:
                spam_dict[r[0]] = 1

    except IndexError:
        print("Успешно!")
        return spam_dict


spam = {}
top_spammer = ["", 0]

my_file = open("t1/nginx_logs.txt", "r", encoding="utf-8")
request = requests_generator(my_file)
print_log(request, spam)
my_file.close()

for i in spam.keys():
    if spam[i] >= top_spammer[1]:
        top_spammer = [i, spam[i]]

print("Топ спамер: {}, с кол-вом запросов: {}.".format(top_spammer[0], top_spammer[1]))
