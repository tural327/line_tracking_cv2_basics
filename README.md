# line_tracking_cv2_basics

For track lines I decided to find shape of line from each side of images 

- [x] Function (marked) created for find each part of veiw angel from car
- [X] vertices created for each left and right sides
- [main] ![](https://github.com/tural327/line_tracking_cv2_basics/blob/main/main.png)
- [left] ![](https://github.com/tural327/line_tracking_cv2_basics/blob/main/left.png)
- [right] ![](https://github.com/tural327/line_tracking_cv2_basics/blob/main/right.png)
- [x] Line edges detection
- 1. image converted to gray img
- 2. Shapes detected by using cv2.Canny
* Second next part:
- [x] image devides cropped_image1 and cropped_image2 and each of them have params of left and right line params
- [X]  lines arrays was found by using cv2.HoughLinesP
* End of the part each line arrays were added main image

# For apply all of this added def line() func
* [Result](https://www.linkedin.com/feed/update/urn:li:ugcPost:6790387384916750336/)

- [main] ![](https://github.com/tural327/line_tracking_cv2_basics/blob/main/res_project.png)
