import requests, os

def linkeditor(a, b):
    if b and a.endswith(b):
        return a[:-len(b)]
    return a

c = 0
fn = 'instagram{}.png'
while os.path.isfile(fn.format(c)):
    c += 1
fn = fn.format(c)

l = input('  >> The URL: ')
v = linkeditor(l, '?utm_source=ig_web_copy_link')
img = requests.get(f'{v}media/?size=l').content
with open(fn, 'wb') as f:
    f.write(img)

input('  >> Downloaded successfully!')
