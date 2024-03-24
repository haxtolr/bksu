from tkinter import Tk, Frame, Label, Scale, Button, messagebox, StringVar, Entry, HORIZONTAL
from tkinter.ttk import Combobox
import serial
import serial.tools.list_ports
import time


class RobotArmControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Arm Control")

        # Serial Communication
        self.setup_serial_frame()

        # Robot Arm Frame
        self.setup_robot_arm()

        # Spacer Frame
        self.setup_spacer_frame(pady=20)

        # Buttons
        self.setup_buttons()

        # Position Combobox
        self.setup_position_combobox()

        # Spacer Frame
        self.setup_spacer_frame(pady=20)

    def setup_serial_frame(self):
        serial_frame = Frame(self.master, width=300)
        serial_frame.pack()

        serial_label = Label(
            serial_frame, text="Serial Port 를 선택하세요", bg="yellow", fg="black", padx=100)
        serial_label.pack()

        # 사용가능한 시리얼 포트 받아와 selected_port 변수에 첫번째 값 저장
        port_list = [
            port.device for port in serial.tools.list_ports.comports()]
        self.selected_port = StringVar()
        self.selected_port.set(
            port_list[len(port_list)-1] if port_list else "No ports available")

        # 시리얼 버튼과 콤보 박스를 포함할 프레임 생성
        serial_button_frame = Frame(serial_frame)
        serial_button_frame.pack()

        # Serial Port 선택 콤보 박스 생성 및 배치
        port_combobox = Combobox(serial_button_frame, values=port_list,
                            state="readonly", textvariable=self.selected_port)
        # 시리얼 버튼과 콤보 박스 사이에 5만큼의 패딩 추가
        port_combobox.pack(side='left', padx=(10, 5))
        port_combobox.bind("<<ComboboxSelected>>",
                        self.update_selected_port)  # 선택이 변경될 때마다 변수 업데이트

        # Open Serial 버튼 생성 및 배치
        open_serial_button = Button(serial_button_frame, text="Open Serial",
                                    height=2, width=15, fg="black", command=self.open_serial)
        # 시리얼 버튼과 콤보 박스 사이에 5만큼의 패딩 추가
        open_serial_button.pack(side='left', padx=(0, 5))

        # Close Serial 버튼 생성 및 배치
        close_serial_button = Button(serial_button_frame, text="Close Serial",
                        height=2, width=15, fg="black", command=self.close_serial)
        # 시리얼 버튼과 콤보 박스 사이에 5만큼의 패딩 추가
        close_serial_button.pack(side='left', padx=(0, 10))

    def update_selected_port(self, event):
        # 콤보박스의 선택값을 selected_port 변수에 업데이트
        self.selected_port.set(event.widget.get())

    def open_serial(self):
        # 사용자가 선택한 포트를 가져옴
        selected_port = self.selected_port.get()

        if selected_port:
            try:
                self.ser = serial.Serial(
                    port=selected_port, baudrate=115200, timeout=1)
                messagebox.showinfo("시리얼 연결", f"시리얼 포트 {selected_port}가 열렸습니다")
            except serial.serialutil.SerialException as e:
                messagebox.showerror("시리얼 연결 오류", f"시리얼 포트를 열 수 없습니다: {e}")
        else:
            messagebox.showwarning("시리얼 포트 선택", "시리얼 포트를 선택하세요.")

    def close_serial(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            self.ser.close()
            messagebox.showinfo("시리얼 연결", "시리얼 포트가 닫혔습니다")
        else:
            messagebox.showwarning("시리얼 연결", "시리얼 포트가 열려 있지 않습니다")

    def setup_robot_arm(self):
        arm_control_frame = Frame(self.master, width=300)  # 설정한 폭
        arm_control_frame.pack()

        arm_label = Label(
            arm_control_frame, text="Robot Arm Components", bg="yellow", padx=100)
        arm_label.pack()

        self.frame_scale, self.frame_entry = self.setup_joint_control(
            arm_control_frame, "Base")
        self.base_scale, self.base_entry = self.setup_joint_control(
            arm_control_frame, "Shoulder")
        self.shoulder_scale, self.shoulder_entry = self.setup_joint_control(
            arm_control_frame, "Upper arm")
        self.elbow_scale, self.elbow_entry = self.setup_joint_control(
            arm_control_frame, "Fore arm")

        arm_go_button = Button(arm_control_frame, text="Move Robot Arm", height=2,
                    width=15, bg="black", fg="white", command=self.move_robot_arm, padx=100)
        arm_go_button.pack()

    def setup_joint_control(self, parent, joint_name):
        joint_frame = Frame(parent)
        joint_frame.pack()

        joint_label = Label(joint_frame, text=joint_name,
                            width=15, bg="green", fg="yellow")
        joint_label.pack(side='left')

        joint_scale = Scale(joint_frame, from_=0, to=180,
                            length=200, orient=HORIZONTAL)
        joint_scale.pack(side='left')

        joint_entry = Entry(joint_frame, width=5)
        joint_entry.pack(side='left')

        # 초기값 설정
        joint_scale.set(90)
        joint_entry.insert(0, "90")

        # 값 변경 이벤트 처리
        def on_scale_change(event):
            joint_entry.delete(0, 'end')
            joint_entry.insert(0, str(joint_scale.get()))

        joint_scale.bind("<ButtonRelease-1>", on_scale_change)

        # Entry 변경 시 Scale에 반영
        def on_entry_change(event):
            try:
                value = int(joint_entry.get())
                if value < 0:
                    value = 0
                elif value > 180:
                    value = 180
                joint_scale.set(value)
            except ValueError:
                pass

        joint_entry.bind("<Return>", on_entry_change)
        joint_entry.bind("<Tab>", on_entry_change)

        return joint_scale, joint_entry

    def move_robot_arm(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            command = f"{self.frame_scale.get()},{self.base_scale.get()},{self.shoulder_scale.get()},{self.elbow_scale.get()}d"
            command_bytes = command.encode('utf-8')
            self.ser.write(command_bytes)
            print(command)
        else:
            messagebox.showwarning(
                "No Serial Connection", "Please open serial connection before sending commands.")

    def setup_spacer_frame(self, **kwargs):
        spacer_frame = Frame(self.master, width=300)  # 설정한 폭
        spacer_frame.pack(**kwargs)

    def setup_buttons(self):
        buttons_frame = Frame(self.master)
        buttons_frame.pack()

        save_position_button = Button(
            buttons_frame, text="Save Position", command=self.save_position)
        save_position_button.grid(row=0, column=0, padx=5)

        send_position_button = Button(
            buttons_frame, text="Send Position", command=self.send_position)
        send_position_button.grid(row=0, column=1, padx=5)

        delete_position_button = Button(
            buttons_frame, text="Delete Position", command=self.delete_position)
        delete_position_button.grid(row=0, column=2, padx=5)

        self.run_button = Button(
            buttons_frame, text="Run", command=self.send_all_positions_to_arduino)
        self.run_button.grid(row=0, column=3, padx=5)

    def save_position(self):
        position = f"{self.frame_scale.get()}, {self.base_scale.get()}, {self.shoulder_scale.get()}, {self.elbow_scale.get()}"
        self.saved_positions.append(position)
        self.position_combobox['values'] = self.saved_positions
        self.label.config(text="")  # 라벨 텍스트 지우기
        
    def delete_position(self):
        selected_position = self.position_combobox.get()
        if selected_position:
            self.saved_positions.remove(selected_position)
            self.position_combobox['values'] = self.saved_positions
            self.position_combobox.set("")  # 콤보박스 텍스트 지우기
            self.label.config(text="")  # 라벨 텍스트 지우기
    def send_position(self):
        selected_position = self.position_combobox.get()
        if selected_position:
            command = selected_position + "d"
            command_bytes = command.encode('utf-8')
            self.ser.write(command_bytes)
            print("Sent command:", command)
            self.label.config(text=command)  # 라벨 텍스트 지우기
        else:
            messagebox.showwarning(
                "No Position Selected", "Please select a position to send.")

    def send_all_positions_to_arduino(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            for index, position in enumerate(self.saved_positions):
                # 라벨 업데이트
                self.update_label_text(index)

                command = position + "d"
                command_bytes = command.encode('utf-8')
                self.ser.write(command_bytes)
                print("Sent command:", command)

        else:
            messagebox.showwarning(
                "No Serial Connection", "Please open serial connection before sending commands.")

    def setup_position_combobox(self):
        position_frame = Frame(self.master)
        position_frame.pack()

        self.saved_positions = []
        self.position_combobox = Combobox(position_frame)
        self.position_combobox.pack()

        # 라벨 추가
        self.label = Label(position_frame, text="RUN 버튼 클릭시, 전송정보 라벨", bg="black", fg="white")
        self.label.pack()
    def update_label_text(self, index):
        # 라벨 업데이트
        self.label.config(
            text=f"Sending position {index + 1}/{len(self.saved_positions)}")
        self.master.update()  # GUI 업데이트를 즉시 적용하기 위해 사용
        time.sleep(1)


if __name__ == "__main__":
    root = Tk()
    app = RobotArmControl(root)
    root.mainloop()
