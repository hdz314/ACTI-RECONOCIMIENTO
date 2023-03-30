from cv_operations import take_photo
from interface import invock_ui

if '__main__' == (__name__):
    callback = lambda name: take_photo(name)
    invock_ui(callback)
