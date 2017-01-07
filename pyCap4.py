# Gavin Jan 6 2017 - Yet to test with 4 cams but should work

import cv2
import sys

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)
cam3 = cv2.VideoCapture(3)
cam4 = cv2.VideoCapture(4)

cv2.namedWindow("test1")
cv2.namedWindow("test2")
cv2.namedWindow("test3")
cv2.namedWindow("test4")

fo = open("farmBotImgData.csv", "a")

img_counter = 0
coOrdX = 0
coOrdY = 0
orient = 0

print ("This program is designed to collect photo data for use as a learning data set...")
print("You must input x & y co-ordinates as floating point values on prompt to successfully output an img")
print("When you are done click a frame and hit esc\nbut for now...\n")
print("Take a picture by pressing spacebar on a webcam frame!")

while True:


    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    ret3, frame3 = cam3.read()
    ret4, frame4 = cam4.read()

    cv2.imshow("test1", frame1)
    cv2.imshow("test2", frame2)
    cv2.imshow("test3", frame3)
    cv2.imshow("test4", frame4)

    if not (ret1 or ret2 or ret3 or ret4):
        break

    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        coOrdX = raw_input("Enter the x location: ")
        coOrdY = raw_input("Enter the y location: ")

        try:
            float(coOrdY)
            float(coOrdY)
        except ValueError:
            print("X & Y Co-Ordinates must be numbers(float), Picture has been discarded, take a new one!")
        else:
            print("\nGreat Shot! Definitely a keeper")

            img1_name = "cam1-frame_{}-{}-{}.png".format(img_counter, coOrdX, coOrdY)
            img2_name = "cam2-frame_{}-{}-{}.png".format(img_counter, coOrdX, coOrdY)
            img2_name = "cam3-frame_{}-{}-{}.png".format(img_counter, coOrdX, coOrdY)
            img2_name = "cam4-frame_{}-{}-{}.png".format(img_counter, coOrdX, coOrdY)

            cv2.imwrite(img1_name, frame1)
            cv2.imwrite(img2_name, frame2)
            cv2.imwrite(img3_name, frame3)
            cv2.imwrite(img4_name, frame4)

            coOrd = "{},{}\n".format(coOrdX, coOrdY)
            fo.write(coOrd)
            print("{} written!".format(img1_name))
            print("Hit space on an img to take another\n")
            img_counter += 1

cam1.release()
cam2.release()

cv2.destroyAllWindows()