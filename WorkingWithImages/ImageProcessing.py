from PIL import Image

python = Image.open("python.jpeg")

print(f"1: {type(python)}")
print(f"2: {python.size}")
print(f"3: {python.filename}")
print(f"4: {python.format_description}")
x = 0
y = 0
w = 600
h = 600
python_croped = python.crop((x, y, w, h))
python.paste(im=python_croped, box=(0, 0))
python_resized = python.resize((200, 200))
python_rotated = python.rotate(90)
python.putalpha(50)

python_croped.show()
python_resized.show()
python_rotated.show()
python.show()
python_resized.save("python_resized.jpeg")
