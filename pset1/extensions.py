# declairing jpg/jpeg
include_jpg = ('.jpg', '.jpeg')
jpeg = ('jpeg')

# declairing gif/png
include_image = ('.gif', '.png')
image = ('image/')

#declairing pdf/zip
include_application = ('.pdf', '.zip')
application = ('application/')

#declairing text
include_text = ('.txt')
text = ('text/plain')

# taking user input
user_input = input('filename: ').lower().strip()

# spliting input before and after (.)
parts = user_input.rsplit('.', 1)

# conditional output
if len(parts) > 1 and user_input.endswith(include_jpg) :
    extension = parts[0].replace(parts[0], image)
    print(extension + jpeg)

elif len(parts) > 1 and user_input.endswith(include_image) :
    extension = parts[0].replace(parts[0], image)
    print(extension + (parts[1]))

elif len(parts) > 1 and user_input.endswith(include_image) :
    extension = parts[0].replace(parts[0], image)
    print(extension + (parts[1]))

elif len(parts) > 1 and user_input.endswith(include_application) :
    extension = parts[0].replace(parts[0], application)
    print(extension + (parts[1]))

elif len(parts) > 1 and user_input.endswith(include_text) :
    extension = parts[0].replace(parts[0], text)
    print(extension)

else:
    print('application/octet-stream')