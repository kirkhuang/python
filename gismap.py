import os
from PIL import Image
import collections

path = "D:\\GisMap\\_alllayers\\L12\\"
queue = []
# queue.append(path)
list = []

IMAGE_SIZE = 256  # 每张小图片的大小
IMAGE_ROW = 12  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 14  # 图片间隔，也就是合并成一张图后，一共有几列

# print(to_image.save(IMAGE_SAVE_PATH))

queue = collections.deque()
# 进队

queue.append(path)
while len(queue) != 0:
    # 出队数据
    dirPath = queue.popleft()
    # 找出所有的文件
    filesList = os.listdir(dirPath)

    for fileName in filesList:
        # 绝对路径
        fileAbsPath = os.path.join(dirPath, fileName)
        # 判断是否是目录，是目录就进队，不是就打印
        if os.path.isdir(fileAbsPath):
            print("目录：" + fileName)
            queue.append(fileAbsPath)
        else:
            list.append(os.path.join(dirPath, fileName))
            # print("普通文件：" + fileName)

print(list)

to_image = Image.new(
    'RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图

n = 0

for i in range(0, IMAGE_ROW):
    for j in range(0, IMAGE_COLUMN):
        to_image.paste(Image.open(list[n]), (j * IMAGE_SIZE, i * IMAGE_SIZE))
        n += 1

# to_image.paste(Image.open(list[0]), (0, 0))
# to_image.paste(Image.open(list[1]), (256, 0))
# to_image.paste(Image.open(list[2]), (0, 256))
# to_image.paste(Image.open(list[3]), (256, 256))

to_image.save(r'D:\\GisMap\\_alllayers\\final.png')
