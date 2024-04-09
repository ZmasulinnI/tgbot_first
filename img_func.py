from PIL import Image, ImageOps
def add_logo(file_name):
    photo = Image.open(f"temp\\{file_name}.png")
    logo = Image.open('assets\logo.png')
    logo = ImageOps.contain(logo,(int(photo.size[0]/5),int(photo.size[1]/5)))
    margin = min(photo.size)* 0.05
    photo.paste(logo, (int(photo.size[0]-logo.size[0] - margin),int(photo.size[1]-logo.size[1] - margin)), mask=logo)
    photo.save(f"temp\\{file_name}.png")
