from PIL import Image
import math

novel_path = 'res/novol.txt'
cover_path = 'res/cover.jpg'
output_path = 'res/novol.bmp'

def encode():
    f = open(novel_path, encoding="utf-8")
    text = f.read()
    f.close()
    
    str_len = len(text)
    width = math.ceil(str_len**0.5)
    im = Image.new("RGB", (width, width), 0x0)
    
    cover = Image.open(cover_path)
    cover.thumbnail((width,width))
    cover = cover.convert('L')
    w,h = cover.size
    wmax = max(w,h)
    wmin = min(w,h)
    cover = cover.crop(((w-wmin)/2,(h-wmin)/2,(w-wmin)/2+wmin,(h-wmin)/2+wmin))
    cover = cover.resize((width,width))
    cover_src = cover.load()

    x, y = 0, 0
    for i in text:
        index = ord(i)
        rgb = ( cover_src[x,y],  (index & 0xFF00) >> 8,  index & 0xFF)
        im.putpixel( (x, y),  rgb )
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    im.save(output_path)
    return im

if __name__ == '__main__':
    encode()
    # with open(novel_path, encoding="utf-8") as f:
    #     all_text = f.read()
    #     im = encode(all_text, )
    #     im.save("{}_layout.bmp".format('.'.join(filename.split('.')[:-1])))
