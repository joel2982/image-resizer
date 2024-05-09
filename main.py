import cv2

img = cv2.imread('image.jpg')
small_img = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow('Shrinked Image',small_img)
key = cv2.waitKey()

print(key)
cv2.imwrite('new_image.jpg',small_img)
if __name__ == '__main__':
    pass
