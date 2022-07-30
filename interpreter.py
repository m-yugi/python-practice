import converter
while(True):
    n = input(">>>")
    res, error = converter.play('<stdio>', n)
    if(error):
        print(error.form())
    else:
        print(res)
