import os
import zipfile

#需要压缩的文件夹
input_path = "../img/product_1"
#压缩后存放位置
output_path = '../img_zipper'
#压缩后的文件名
output_name = 'product_1.zip'
f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
filelists = []
files = os.listdir(input_path)
for file in files:
    if os.path.isdir(input_path + '/' + file):
        filelists.append(input_path + '/' + filelists)
    else:
        filelists.append(input_path + '/' + file)

for file in filelists:
    f.write(file)
# 调用了close方法才会保证完成压缩
f.close()
print(output_path + r"/" + output_name)
