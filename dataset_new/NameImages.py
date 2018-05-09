"""
Author: aB9
Date:   05/06/18
"""

import os

def name_images():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    # print(base_dir)
    with_water_dir = os.path.join(base_dir,'water')
    without_water_dir = os.path.join(base_dir,'Without_water')

    #Change directory
    os.chdir(with_water_dir)
    all_images = os.listdir(with_water_dir)
    i =100

    for image in all_images:
        print(image)
        os.rename(with_water_dir+'/'+image, 'ab-{}.png'.format(i))
        i+=1



def main():
    name_images()


if __name__=='__main__':
    main()