# install publitio

from publitio import PublitioAPI

apireq = PublitioAPI('YOUR-API-KEY' , 'YOUR-API-Secret')

# For Uploading files

# uploading_file = apireq.create_file(file=open('test.png' , 'rb'),
#                                     title = 'My img',
#                                     description = 'This is my image ')

# print(uploading_file)
# print()
# print(uploading_file['id'])

# Time to delete the file

deletereq = apireq.delete_file('YOUR-FILE-ID')

print(deletereq)