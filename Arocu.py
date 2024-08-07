import numpy as np
import cv2
import cv2.aruco as aruco
import math
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
marker_id = 31
marker_img = aruco.drawMarker(aruco_dict, marker_id,500)
pic_name = "marker_6X6_250_" + str(marker_id) + ".jpg"
cv2.imwrite(pic_name,marker_img)
