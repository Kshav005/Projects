from PIL import Image, ImageDraw, ImageFont, ImageFilter


with Image.open("profileimage.jpg") as img : 
    imgcropped = img.crop((0, 0, 1000, 600))
    image_resized = img.resize((900, 500))
    imgmain = image_resized.filter(ImageFilter.GaussianBlur(radius=4))
    
    draw = ImageDraw.Draw(imgmain)
    font1 = ImageFont.truetype("arial.ttf", 40)
    draw.text((100, 100), text="Name : ", font=font1, fill="white")
    draw.text((250, 100), text="Jackson ", font=font1, fill="white")
    imgmain.show()
    
