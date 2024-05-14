##RPi.GPIO 설치 (라즈베리파이 환경에서 아래의 코드를 실행해야 함.)
## pip install RPi.GPIO 가 설치 에러 난 경우
# 라즈베리파이에서 실행
# sudo apt install python3-dev python3-setuptools
# sudo apt updata
# sudo apt upgrade
## pip 설치가 안 될 경우 GitHub 레포지토리에서 소스를 받아 빌드하기
# git clone https://github.com/tomlins/rpi.gpio.git
# cd rpi.gpio
# sudo python3 setup.py install

import subprocess # 외부 프로세스를 실행하고 제어하기 위한 모듈
import time
import RPi.GPIO as GPIO # Raspberry Pi의 GPIO를 다루기 위한 모듈

#GPIO를 설정하고 초기화함
GPIO.setmode(GPIO.BCM)  #GPIO 핀 번호를 Broadcom SOC 채널 번호로 설정
time.sleep(0.1) 
GPIO.setup(20, GPIO.OUT) #GPIO 핀을 출력으로 설정
GPIO.output(20, GPIO.HIGH) #GPIO 핀을 HIGH로 설정하여 연결된 장치를 활성화함

time.sleep(0.05)
# SLAM drive 
launch_command = "roslaunch myagv_odometry myagv_active.launch"  # launch 패키지명/파일명 확인 필요
launch_command2 = "roslaunch myagv_navigation  myagv_slam_laser.launch"  # 새로운 터미널 창에서 프로세스를 실행
launch_command3 = "roslaunch myagv_teleop myagv_teleop.launch"  # 
subprocess.run(
    ['gnome-terminal', '-e', f"bash -c '{launch_command}; exec $SHELL'"])  # bash -c를 사용하여 명령을 실행
time.sleep(4)
## rviz로 LiDAR 실행 
#launch_command2 = "roslaunch ydlidar_ros_driver lidar_view.launch"

subprocess.run(
    ['gnome-terminal', '-e', f"bash -c '{launch_command2}; exec $SHELL'"]) # bash -c로 명령 실행 
time.sleep(4)
## 텔레오퍼레이션으로 제어하는 노드를 시작
# subprocess.run(
#    ['gnome-terminal', '-e', f"bash -c '{launch_command3}; exec $SHELL'"])  
