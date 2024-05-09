import cv2,os

img_path = os.path.normpath(input('Enter Image Path : ')) 
img = cv2.imread(img_path)
small_img = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow('Shrinked Image',small_img)
key = cv2.waitKey()

dir_name = os.path.dirname(img_path)
img_name = os.path.basename(img_path)
cv2.imwrite(os.path.join(dir_name,f'updated_{img_name}'),small_img)

if __name__ == '__main__':
    pass
