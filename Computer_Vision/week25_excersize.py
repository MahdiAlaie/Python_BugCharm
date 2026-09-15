import cv2 as cv
import numpy as np
import os 

face_cascade = cv.CascadeClassifier("week26/haarcascade_frontalface_default.xml")

def get_img_path():

    while True:
        path = input("Please Enter your Pics folder path : ")

        if not os.path.isdir(path):
            print("there is no directory by this path!")
            continue

        files = os.listdir(path)

        img_list = []

        for file in files : 
            if file.lower().endswith(("jpg","jpeg","png")):
                img_list.append(file)

        if len(img_list) == 0 :
            print("there is no image in this path")
            continue

        return path,img_list

pics_path,img_list = get_img_path()

for i in range(len(img_list)):
     
     print(f"{i+1}) {img_list[i]}")

selcted_img = input("please select your image : ")

final_path = ""

while final_path == "":
    try:
        selcted_img = int(selcted_img)
        if selcted_img in range(len(img_list)+1):
            final_path = pics_path +"\\"+ img_list[selcted_img-1]
            print(final_path)
            img = cv.imread(final_path)
            selcted_img = img_list[selcted_img-1]

        else:
            print("please enter the correct number")
            selcted_img = input("please select your image : ")
    except ValueError:
        if selcted_img in img_list:
            final_path = pics_path +"\\"+ selcted_img
            print(final_path)
            img = cv.imread(final_path)
        else:
            selcted_img = input("please enter correct name : ")

def func_gray (frame):
    return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

def face_detection(gray_frame,frame):
    face_list = face_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=5)

    for i,(x,y,w,h) in enumerate(face_list):
        cv.rectangle(frame,(x,y),(w+x,y+h),(90,250,40),thickness= 2)
        cv.putText(frame,f"FACE {i+1}",(x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(90,90,90),2)

    return frame

def func_resize(frame,scale):
    height = int(frame.shape[1]*scale)
    width = int(frame.shape[0]*scale)

    dimension = (height,width)
    resized = cv.resize(frame,dimension,interpolation=cv.INTER_AREA) 
    return face_detection(func_gray(resized),resized)

def func_filter(frame,color):
    blue,green,red = cv.split(frame)
    blank = np.zeros(img.shape[:2],dtype="uint8")
    if color == "red":
        red_channel = cv.merge([blank,blank,red])
        return face_detection(func_gray(frame),red_channel)
    elif color == "green":
        green_channel = cv.merge([blank,green,blank])
        return face_detection(func_gray(frame),green_channel)
    elif color == "blue":
        blue_channel = cv.merge([blue,blank,blank])
        return face_detection(func_gray(frame),blue_channel)
    else:
        print("can't filter this channel right now!")

def func_edge(frame):
    blured_img = cv.GaussianBlur(frame,(7,7),4.3)
    edge_detection = cv.Canny(blured_img,100,150)
    return face_detection(edge_detection,edge_detection)



apllications = {"resize image" : [0.2,0.5,0.8,1.2,1.5,2],
                "grayscale image" : True,
                "color filtering" : ["red","green", "blue"],
                "edge detection" : True}

for a in range(len(apllications.keys())):
     print(f"{a+1}){list(apllications.keys())[a]}")



while True:
    selected_apllication = input("what are you looking for:")
    try:
        selected_apllication = int(selected_apllication)
        if selected_apllication in range(len(apllications.keys())+1):
            break
        else:
            print("please choose correct aplication!")
    except ValueError:
        if selected_apllication in apllications.keys():
            break
        else:
            print("please choose correct aplication!")

try:
    selected_apllication = int(selected_apllication)
    if selected_apllication-1 == 0:
        for s in range(len(apllications["resize image"])):
            print(apllications['resize image'][s])
        while True:
            selected_scale = input("Choose your scale: ")
            try:
                selected_scale = float(selected_scale)
                if selected_scale in apllications["resize image"]:
                    break
                else:
                    print("please choose correct scale!")
            except ValueError:
                print("please choose correct scale!")

        cv.imshow(selcted_img,func_resize(img,float(selected_scale)))
        cv.waitKey(0)

    elif selected_apllication-1 == 1:
        cv.imshow(selcted_img,face_detection(func_gray(img),func_gray(img)))
        cv.waitKey(0)

    elif selected_apllication -1 == 2:
        for c in range(len(apllications["color filtering"])):
            print(f"{c+1}){apllications['color filtering'][c]}")
        while True:
            selected_color = input("what color you want to filtr:")
            try:
                selected_color = int(selected_color)
                if selected_color in range(len(apllications["color filtering"])+1):
                    selected_color = apllications["color filtering"][selected_color-1]
                    choosen_channel = func_filter(img,selected_color)
                    cv.imshow(selcted_img + selected_color,choosen_channel)
                    cv.waitKey(0)
                    break
                else:
                    print("please choose correct color!")

            except ValueError:
                if selected_color in apllications["color filtering"]:
                    choosen_channel = func_filter(img,selected_color)
                    cv.imshow(selcted_img + selected_color,choosen_channel)
                    cv.waitKey(0)
                    break
                else:
                    print("please choose correct color!")

    elif selected_apllication - 1 == 3:
        cv.imshow(selcted_img + "Canny" ,func_edge(img))
        cv.waitKey(0)

except ValueError:
    if selected_apllication == "resize image":
        for s in range(len(apllications["resize image"])):
            print(apllications['resize image'][s])
        while True:
            selected_scale = input("Choose your scale: ")
            try:
                selected_scale = float(selected_scale)
                if selected_scale in apllications["resize image"]:
                    break
                else:
                    print("please choose correct scale!")
            except ValueError:
                    print("please choose correct scale!")
        
        cv.imshow(selcted_img,func_resize(img,float(selected_scale)))
        cv.waitKey(0)
    elif selected_apllication == "grayscale image":
        cv.imshow(selcted_img,func_gray(img))
        cv.waitKey(0)

    elif selected_apllication ==  "color filtering":
        for c in range(len(apllications["color filtering"])):
            print(f"{c+1}){apllications['color filtering'][c]}")
        while True:
            selected_color = input("what color you want to filtr:")
            try:
                selected_color = int(selected_color)
                if selected_color in range(len(apllications["color filtering"])+1):
                    selected_color = apllications["color filtering"][selected_color-1]
                    choosen_channel = func_filter(img,selected_color)
                    cv.imshow(selcted_img + selected_color,choosen_channel)
                    cv.waitKey(0)
                    break
                else:
                    print("please choose correct color!")

            except ValueError:
                if selected_color in apllications["color filtering"]:
                    choosen_channel = func_filter(img,selected_color)
                    cv.imshow(selcted_img + selected_color,choosen_channel)
                    cv.waitKey(0)
                    break
                else:
                    print("please choose correct color!")

    elif selected_apllication  == "edge detection":
        cv.imshow(selcted_img + "Canny" ,func_edge(img))
        cv.waitKey(0)
