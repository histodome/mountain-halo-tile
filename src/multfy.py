import os
from PIL import Image
import PIL.ImageChops as IC
import numpy as Np
import cv2

# 读取slope和relief
img_r = Image.open(r'/Users/duanqigeng/Desktop/gis_data/sichuan_relief.tif')
img_s = Image.open(r'/Users/duanqigeng/Desktop/gis_data/sichuan_slope.tif')
# 第一次正片叠底输出rs_RGB
img_rs = IC.multiply(img_r, img_s)

# 添加Alpha通道,输出rs_RGBA
# img_rs = img_rs.convert("RGBA")

# 输出rs
img_rs.save(r'/Users/duanqigeng/Desktop/gis_data/rs.jpg')

# 读取灰度山体阴影
cv_h = cv2.imread(r'/Users/duanqigeng/Desktop/gis_data/sichuan_hillshade.tif', cv2.IMREAD_GRAYSCALE)
# 将灰度图转化为RGB
cv_h_RGB = cv2.cvtColor(cv_h, cv2.COLOR_GRAY2RGB)

# 将RGB转化为RGBA
# cv_h_RGBA = cv2.cvtColor(cv_h_RGB, cv2.COLOR_RGB2RGBA)

# 设置透明度
# r_h, g_h, b_h, a_h = cv2.split(cv_h_RGBA)
# a_h[:, :] = 125
# cv_h_RGBA = cv2.merge([r_h, g_h, b_h, a_h])

# 输出带有透明度的山体阴影
cv2.imwrite(r'/Users/duanqigeng/Desktop/gis_data/h.jpg', cv_h_RGB)

# PIL读取带有透明度的山体阴影
img_h = Image.open(r'/Users/duanqigeng/Desktop/gis_data/h.jpg')
img_o = IC.multiply(img_rs, img_h)
# img_o = img_o.convert('RGB')
img_o.save(r'/Users/duanqigeng/Desktop/gis_data/output.jpg')