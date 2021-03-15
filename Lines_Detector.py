import numpy as np
import cv2
import os


def PreProcessing(image):
    # GRAYSCALE
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # new immage witch gray colour scale
    cv2.imshow('gray', gray)
    cv2.waitKey(0)

    # BINARY
    _, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('Binary', thresh)
    cv2.waitKey(0)

    # DILATION
    kernel = np.ones((1, 22), np.uint8)  # uint8 = unsigned intger (0 to 255)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imshow('Dilated', img_dilation)
    cv2.waitKey(0)
    return img_dilation


def line_segmentation(image, image_processed, path):
    # menage the path to save the folder
    print("The current working directory is %s" % path)

    path = path + r"\Segmentation"
    print(path)

    try:
        os.mkdir(path)  # create the directory used to store the xml files
    except OSError:
        print("Creation of the directory %s failed because already existed" % path)
    else:
        print("Successfully created the directory %s " % path)

    # find contours
    ctrs, hier = cv2.findContours(image_processed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)  # getting bounding box
        tmp_image = image.copy()
        roi = tmp_image[y:y + h, x:x + w]
        if w >= 5 and h >= 5:
            # save the file in the folder "segmentation"
            cv2.imwrite(os.path.join(path, "segment_no_" + str(i) + ".png"), roi)

    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)  # getting boundind box
        tmp_image = image.copy()
        roi = tmp_image[y:y + h, x:x + w]
        if w >= 5 and h >= 5:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # save the file in the folder "segmentation"
    cv2.imwrite(os.path.join(path,"final_bounded_box_image.png"), image)
    cv2.imshow('marked areas', image)
    cv2.waitKey(0)


