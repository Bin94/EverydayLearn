from PIL import Image, ImageDraw, ImageFont

def add_number(img,number):
    #打开图片
    image = Image.open(img)
    image.show()

    #加数字
    draw = ImageDraw.Draw(image)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)
    color = "#ff0000"
    width, height = image.size
    if number > 9:
        size = 40
    else:
        size = 20
    draw.text((width-size-5,0),str(number),font=myfont, fill=color)

    #保存
    image.save('result.jpg','jpeg')
    image.show()
    return 0

if __name__ == '__main__':
    numberstr = input('number:')
    image = 'hhh.jpg'
    number = int(numberstr)
    add_number(image,number)