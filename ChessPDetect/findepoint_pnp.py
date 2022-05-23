from turtle import pos, position
import cv2
import numpy as np
from Detection.perspective import *
from Detection.sideDetection_HSV import *
import DetectionFunctions as df
from DetectAllPoints import *
from transform import order_points, poly2view_angle
from solve_pnp import *

# if __name__ == "__main__":

def chesspieceMaponBoard (pathimg,prePiont):
    count_train=(64*180) 
    name=25
    # img = cv2.imread(f'H:/M89/ChessPieces_Detection/saveImg/captureImgIso/ChessboardisoNo.154.jpg')
    img = cv2.imread(pathimg)
    # img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2,))
    clear_image, encoded_image, matrix = getMatrixFromImage(img)
    img,points,all_point=show_point_on_image(img, matrix)
    clusters = sorted(list(all_point), key=lambda k: k[0])
    sorted_points = []
    j = 0
    labels= ["a","b","c","d","e","f","g","h"]
    position=[]
    for i in range(1,10):
            points = sorted(clusters[j:i*9], key=lambda k: k[1])
            sorted_points += points
            j+=9
    for i in range(8):
        for j in range(8):
            try:
                cropped__img = img[int((sorted_points[(9*i)+j+9][1])):int((sorted_points[(9*i)+j+10][1])), int((sorted_points[(9*i)+j][0])):int((sorted_points[(9*i)+j+10][0]))]
                img_name = labels[i]+f"{8-j}"
                #int((sorted_points[(9*i)+j+9][1]))},{int((sorted_points[(9*i)+j+10][1]))
                #int((sorted_points[(9*i)+j][0]))},{int((sorted_points[(9*i)+j+10][0]))
                position.append([img_name,[int((sorted_points[(9*i)+j][0])),int((sorted_points[(9*i)+j+10][0]))],[int((sorted_points[(9*i)+j+9][1])),int((sorted_points[(9*i)+j+10][1]))]]  )
                # cv2.imwrite(f"Output/{img_name}", cropped__img)
            except:
                print("{} error!".format(img_name))
    #a8-a7-a6-a5.....b8
    # prediction=[['rook', (800, 572), 1], ['pawn', (560, 335), 1], ['knight', (619, 453), 1], ['king', (793, 402), 1], ['bishop', (621, 338), 1], ['pawn', (526, 190), 0], ['queen', (907, 407), 1], ['bishop', (730, 286), 0], ['knight', (684, 187), 0], ['rook', (621, 236), 0], ['queen', (789, 192), 0], ['king', (845, 291), 0]]
    prediction = prePiont #[['queen', (724, 573), 1], ['bishop', (846, 193), 0], ['knight', (544, 561), 1], ['pawn', (786, 466), 1], ['pawn', (795, 297), 0], ['rook', (900, 197), 0], ['rook', (904, 584), 1], ['bishop', (596, 563), 1], ['king', (784, 586), 1], ['knight', (585, 183), 0], ['king', (690, 192), 0], ['queen', (636, 189), 0]]
    result=[]
    final_result=[]
    for i in prediction :
        for check in position:
            if i[1][0] > check[1][0] and i[1][0] < check[1][1] and i[1][1] > check[2][0] and i[1][1] < check[2][1]:
                result.append(i[0])
                result.append(check[0])
                result.append(i[2])
                final_result.append(result)
                result=[]
    return final_result
    # print(final_result)
