import cv2
import dropbox
import time
import random

start_time = time.time()
def snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("Snapshot has been taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN"
    file =image_name
    file_from = file
    file_to="/testFolder/"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File has been successfully uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = snapshot()
            upload_file(name)

main()