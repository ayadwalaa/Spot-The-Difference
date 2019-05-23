#In order to compute the difference between two images we’ll be utilizing the Structural Similarity Index, this
#exists in the follwoing library
#The trick is to learn how we can determine exactly where, in terms of (x, y)-coordinate location, the image differences are.
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2


