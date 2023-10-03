import string

line = input()

# generates abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

indexes = [line.find(ch) for ch in chars if line.count(ch) == 1]

print(*sorted(indexes))