import os
from PIL import Image
import PIL.ImageChops as IC
import PIL.ImageEnhance as IE #对比度
import os
import cv2

# 输出山体阴影图
# os.system("gdaldem hillshade -az 45 -z 1 'sichuan.tif' 'hillshade.tif'")

# 输出坡度坡向
# os.system("gdaldem slope 'sichuan.tif' 'sichuan_slopes.tif'")

# 坡度坡向黑白反转
# os.system("gdaldem color-relief 'sichuan_slopes.tif' 'color-slope.txt' 'sichuan_slope.tif'")

# 删除坡度坡向
# os.remove()

# 输出山体晕染图
# os.system("gdaldem hillshade -az 45 -z 1.3 'sichuan.tif' 'hillshade.tif'")

# 读取slope和relief
img_r = Image.open(r'/Users/duanqigeng/Desktop/gis_data/sichuan_relief.tif')
img_s = Image.open(r'/Users/duanqigeng/Desktop/gis_data/sichuan_slope.tif')

# 读取灰度山体阴影(灰度图)
img_h = cv2.imread(r'/Users/duanqigeng/Desktop/gis_data/sichuan_hillshade.tif', cv2.IMREAD_GRAYSCALE)
# 将灰度图转化为RGB
img_h = cv2.cvtColor(img_h, cv2.COLOR_GRAY2RGB)

# 第一次正片叠底输出rs_RGB
img_rs = IC.multiply(img_r, img_s)
# cv2转成pillow
img_h = Image.fromarray(img_h)
en = IE.Brightness(img_h)
img_h = en.enhance(1.75)  # 变亮

img_o = IC.multiply(img_rs, img_h)
img_o.save(r'/Users/duanqigeng/Desktop/gis_data/output.jpg')

# 删除山体阴影、坡度坡向、晕染图、dem原始数据
# os.remove()