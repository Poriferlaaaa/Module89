from cgi import test
from re import X
import ChessPieces_Detection as cd
from findepoint_pnp import chesspieceMaponBoard 

def test_call():
    pathimg = "H:/M89/ChessPieces_Detection/ChessPDetect/captureImg/1.jpg"
    x = cd.getdata()
    y = chesspieceMaponBoard(pathimg,x)
    return y

print(test_call())
