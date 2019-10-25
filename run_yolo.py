import os
import glob
from shutil import copyfile, move

images = sorted(glob.glob("/home/mzins/Dataset/rgbd_dataset_freiburg2_desk/rgb/*.png"))

os.chdir("/users/mzins/dev/darknet/")
cmd = "./darknet detect cfg/yolov3.cfg yolov3.weights "

output_dir = "/home/mzins/Dataset/rgbd_dataset_freiburg2_desk/rgb_detections/"


N = len(images)
for i, img in enumerate(images):
    name = os.path.splitext(os.path.basename(img))[0]
    print(cmd + img + " -out " + name)
    os.system(cmd + img + " -out " + name)
    
    move(name + ".jpg", os.path.join(output_dir, name + ".jpg"))
    move(name + ".txt", os.path.join(output_dir, name + ".txt"))
    print(img, " done", i, " / ", N)
    
    
    