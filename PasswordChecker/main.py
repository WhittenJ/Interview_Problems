import re

def passwordChecker(password):
        if(len(password) < 10):
            raise NotLongEnoughError(1101)
        result = re.match(r'[\.\w-]+$', password)
        if (result):
            return password
        else:
            raise InvalidPasswordError(1102)

class AppError(Exception): pass

class NotLongEnoughError(AppError):
    em = {1101: "Password is not long enough!"}

class InvalidPasswordError(AppError):
    em = {1102: "Password is invalid!  Must only contain letters, numbers, and/or periods."}