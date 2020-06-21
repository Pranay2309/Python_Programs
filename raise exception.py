class PaisaNahiHaiException(Exception):
    def __init__(self,arg):
        self.msg=arg
    

bal=500
withdrawal=1000

if bal>withdrawal:
    print("collect your money please")
else:
    raise PaisaNahiHaiException("udhar le lo")
    
