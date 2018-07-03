from PIL import Image

im = Image.open(input("Enter file path: "))

def dist(f, t):
	return int((abs(f[0]-t[0])**2 + abs(f[1]-t[1])**2 + abs(f[2]-t[2]))**0.5)

d = im.size
out = Image.new('RGB', d, (255,255,255))
r = 190
for i in range(d[0]):
	for j in range(d[1]):
		p = im.getpixel((i,j))
		if ((p[0] == 255 and p[1] == 255 and p[2] == 204) or (p[0] == 249 and p[1] == 239 and p[2] == 164)) : #preprocessing 1
			out.putpixel((i,j), (255,255,0))
		elif p[0] == 204 and p[1] == 255 and p[2] == 51: #preprocessing 2
			out.putpixel((i,j), (0,255,0))
		else: #preprocessing 3 (monotonizing 2)
			out.putpixel((i,j), (0,0,0))


out.rotate(180).save("ttpxt.png")
