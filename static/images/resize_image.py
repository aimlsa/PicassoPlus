from PIL import Image
tar_image = Image.open('teaser.png')
tar_hgt, _ = tar_image.size

lists = ['PicassoNet++', 's3dis', 'shape_analysis', 'scannet', 'scenes']

for name in lists:
    image = Image.open(name+'.png')
    hgt, wid = image.size

    resized_image = image.resize((tar_hgt, int(wid*tar_hgt/hgt)))
    resized_image.save(name+'_resize.png')

