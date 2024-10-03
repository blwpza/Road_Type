import subprocess
#AI เเยกประเภทถนน
# ตั้งค่า argument สำหรับ detect.py
weights_path = 'best.pt'
img_size = 640
conf_threshold = 0.08
source = '/home/tunz/PycharmProjects/Road_linux/img'  # โฟลเดอร์ที่เก็บภาพที่ต้องการตรวจจับ

# สร้างคำสั่งที่ต้องการใช้
command = f"python /home/tunz/PycharmProjects/Road_linux/yolov5/detect.py --weights {weights_path} --img {img_size} --conf {conf_threshold} --source {source}"

# รัน detect.py และจับผลลัพธ์
result = subprocess.run(command, shell=True, capture_output=True, text=True)

# พิมพ์ผลลัพธ์หรือข้อผิดพลาด
print("stdout:", result.stdout)
print("stderr:", result.stderr)

print(f"การประมวลผลเสร็จสิ้น ผลลัพธ์ถูกบันทึกในโฟลเดอร์ runs/detect")


