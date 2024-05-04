import secrets
import string

letters = string.ascii_letters

special_chars = string.punctuation

digits = string.digits

selection_list = letters + digits + special_chars

password_len = 12

password = ''
for i in range(password_len):
    password += ''.join(secrets.choice(selection_list))

print("Your Temporary Password:", password)
