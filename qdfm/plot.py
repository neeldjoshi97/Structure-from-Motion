'''
Uses 'dense' module to get propagated key points and plots them over the
original image
'''
# internal modules
from .dense import getDenseMatches

# external modules
import cv2 as cv

def plotpoints(image, point_list):
    '''
    image:       input image in BGR format
    point_list:  list of (x, y) tuples representing coordinates to be marked on the image

    Returns a copy of the image with red circles drawn at each point in point_list
    '''
    # fluo = (21, 244, 238)
    red = (0, 0, 255)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
    for x, y in point_list:
        image = cv.circle(image, (x, y), radius=3, color=red, thickness=-1)
    return image

def run_qdfm(image_on_right, image_on_left, zncc_threshold=0.99999):
    '''
    image_on_right:   file path to the image that will be displayed on the right
    image_on_left:    file path to the image that will be displayed on the left

    Loads two images, computes dense matches between them, plots matched points,
    and displays the annotated images side by side in separate windows.
    '''
    first_image     = cv.imread(image_on_right)
    second_image    = cv.imread(image_on_left)

    list1, list2, _, _ = getDenseMatches(
        img1        = first_image,
        img2        = second_image,
        n_keypoints = 1,
        zncc_thresh = zncc_threshold
    )

    # plot points on resp. images
    first_image_plotted     = plotpoints(first_image, list1)
    second_image_plotted    = plotpoints(second_image, list2)

    cv.namedWindow('Image1')
    cv.namedWindow('Image2')
    cv.imshow('Image1', first_image_plotted)
    cv.imshow('Image2', second_image_plotted)
    cv.waitKey(0)
    cv.destroyAllWindows()
