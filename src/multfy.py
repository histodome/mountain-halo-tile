import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
import PIL.ImageChops as IC
import PIL.ImageEnhance as IE #对比度
import os
import cv2

# 输出山体阴影图
os.system("gdaldem hillshade -az 60 -z 1 '/Users/duanqigeng/Desktop/gis_data/global.tif' '/Users/duanqigeng/Desktop/gis_data/hillshade.tif'")

# 输出坡度坡向
os.system("gdaldem slope '/Users/duanqigeng/Desktop/gis_data/global.tif' '/Users/duanqigeng/Desktop/gis_data/slopes.tif'")

# 坡度坡向黑白反转
os.system("gdaldem color-relief '/Users/duanqigeng/Desktop/gis_data/slopes.tif' '/Users/duanqigeng/Desktop/gis_data/color-slope.txt' '/Users/duanqigeng/Desktop/gis_data/slope.tif'")

# 删除坡度坡向
# os.remove()

# 输出山体晕染图
os.system("gdaldem color-relief '/Users/duanqigeng/Desktop/gis_data/global.tif' '/Users/duanqigeng/Desktop/gis_data/color-relief.txt' '/Users/duanqigeng/Desktop/gis_data/relief.tif'")

# 读取slope和relief
img_r = Image.open(r'/Users/duanqigeng/Desktop/gis_data/relief.tif')
img_s = Image.open(r'/Users/duanqigeng/Desktop/gis_data/slope.tif')

# 读取灰度山体阴影(灰度图)
img_h = cv2.imread(r'/Users/duanqigeng/Desktop/gis_data/hillshade.tif', cv2.IMREAD_GRAYSCALE)
# 将灰度图转化为RGB
img_h = cv2.cvtColor(img_h, cv2.COLOR_GRAY2RGB)

# 第一次正片叠底输出rs_RGB
img_rs = IC.multiply(img_r, img_s)
# cv2转成pillow
img_h = Image.fromarray(img_h)
en = IE.Brightness(img_h)
img_h = en.enhance(1.5)  # 变亮
img_o = IC.multiply(img_rs, img_h)
img_o.save(r'/Users/duanqigeng/Desktop/gis_data/output.png')

# 删除山体阴影、坡度坡向、晕染图、dem原始数据
# os.remove()