from Utilities import *
from Parser import *
from Lines_Detector import *

path = os.getcwd()  # get the path of this project

# preprocessing the image
image = cv2.imread('Left_column.png')
processed_image = PreProcessing(image)

# line detection phase
line_segmentation(image, processed_image, path)

# parsing the xml file and creating the folder Ground_Truth
parser_xml(path)

# parsing the file txt of the prompte output
Ground_Truth, Prediction, Count = parser_txt()

# update the values of Ground_Truth, Prediction with th nmber of occurences
GT_Matrix, Pred_Matrix = create_matrix_list(Ground_Truth, Prediction, Count)

# create the matrix
create_Matrix(GT_Matrix, Pred_Matrix)