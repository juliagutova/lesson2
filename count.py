from  collections import Counter

phones = ["Iphone", "Samsung", "LG", "Iphone", "Iphone", "LG"]

count = Counter(phones)
print(count["Hello"])

text = "Ехал грека через реку".lower().replace(' ', '')
count = Counter(text)
print(count)