#file opening and reading and closing

host = open('C:/Haswin info/python/IF else.py')
print("current position : {}".format(host.tell()))
print(host.read())

print('current position : {}'.format(host.tell()))
print(host.read())

host.seek(0)
print("current position : {}".format(host.tell()))
print(host.read())
