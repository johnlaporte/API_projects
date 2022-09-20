from time import strftime,gmtime
def send():
    s_date = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    f = open("my.log", "a")
    f.write(s_date + ": send\n")
    f.close()
