import subprocess
import os
import shutil
#AI ตรวจจับหลุมถนน เเละ เเยกประเภทถนน
def run_detection(weights, img_size, conf_threshold, source, project_name):
    command = f"python /home/tunz/PycharmProjects/Road_linux/yolov5/detect.py --weights {weights} --img {img_size} --conf {conf_threshold} --source {source} --project {project_name}"

    # รัน detect.py และจับผลลัพธ์
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # พิมพ์ผลลัพธ์หรือข้อผิดพลาด
    print(f"Running detection with weights: {weights}")
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)


# ตั้งค่า argument สำหรับ detect.py
img_size = 640
conf_threshold = 0.08
source = '/home/tunz/PycharmProjects/Road_linux/img'  # โฟลเดอร์ที่เก็บภาพที่ต้องการตรวจจับ

# โฟลเดอร์ชั่วคราวสำหรับบันทึกผลลัพธ์จากการตรวจจับประเภทถนน
temp_project = '/home/tunz/PycharmProjects/Road_linux/runs/detect_temp'

# รันโมเดลตรวจจับประเภทถนนและบันทึกผลลัพธ์ในโฟลเดอร์ชั่วคราว
run_detection('/home/tunz/PycharmProjects/Road_linux/best.pt', img_size, conf_threshold, source, temp_project)

# ใช้ผลลัพธ์จากการตรวจจับประเภทถนนเป็น input สำหรับการตรวจจับหลุมถนน
temp_output_dir = os.path.join(temp_project, 'exp')
if os.path.exists(temp_output_dir):
    run_detection('/home/tunz/PycharmProjects/Road_linux/holedetect.pt', img_size, conf_threshold, temp_output_dir, '/home/tunz/PycharmProjects/Road_linux/runs/detect')

# ลบโฟลเดอร์ชั่วคราว
shutil.rmtree(temp_project)

print(f"การประมวลผลเสร็จสิ้น ผลลัพธ์ถูกบันทึกในโฟลเดอร์ runs/detect")
