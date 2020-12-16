def file_write(file, tasks):
	with open(file, "w") as fp:
		for i in tasks:
			fp.write("%s\n" % i)


def file_read(file):
    tasks = []
    with open(file, "r") as fp:
        t1=fp.readlines()
        for x in t1:
            tasks.append(x.rstrip('\n'))
    return tasks