#!/usr/bin/python

import Image
import math
from operator import itemgetter

def nearest_color( pal, col ):
    difs = [(abs(c[0]-col[0]), abs(c[1]-col[1]), abs(c[2]-col[2])) for c in pal]
    deltas = [ math.sqrt(c[0]*c[0] + c[1]*c[1] + c[2]*c[2]) for c in difs]
    return pal[min(enumerate(deltas), key=itemgetter(1))[0]]

def main():
    im = Image.new('RGB', (400,800))

    if im.mode != 'RGB':
        im = im.convert('RGB')

    pixels = im.load()

    # https://en.wikipedia.org/wiki/Ordered_dithering

    mat4 = [[  1,  9,  3, 11],
            [ 13,  5, 15,  7],
            [  4, 12,  2, 10],
            [ 16,  8, 14,  6]]

    palette = [#(155,188, 15),
               #(139,172, 15),
               (155,188, 15),
               ( 15, 56, 15)]

    for i in range(0,800):
        pix = i * 255 / 800
        for j in range(0,400):
            oldpixel = pix + (pix * 1/17 * mat4[ j % 4][ i % 4 ])
            nearest = nearest_color(palette, (oldpixel, oldpixel, oldpixel))
            pixels[j,i] = nearest

    im.save("sample.png")

if __name__ == '__main__':
    main()

'''
TODO
====

 * gtk interface: color picker, ask how many
    import gtk
    csd = gtk.ColorSelectionDialog('Choose a color')
    csd.run()
    print(csd.colorsel)
 * config file for no gui?
 * random matrix size
'''
