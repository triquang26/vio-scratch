# VIO-Scratch (ROS 2 Project)

Dự án này là một ví dụ cơ bản về hệ thống Publisher-Subscriber trong ROS 2, kết hợp giữa hai ngôn ngữ: **C++** và **Python**.

## 🏗️ Cấu trúc thư mục
- `src/inertial_vo`: Package C++ chứa node Publisher (`cpp_pub`).
- `src/inertial_vo_py`: Package Python chứa node Subscriber (`py_sub`).

## 🛠️ Yêu cầu hệ thống
- Đã cài đặt **ROS 2** (Humble, Foxy, hoặc bản tương đương).
- Đã cài đặt công cụ source build: `colcon`, `ament_cmake`.

## 🚀 Hướng dẫn cài đặt và chạy

### 1. Build project
Mở terminal tại thư mục gốc của dự án (`vio-scratch`) và thực hiện build:

```bash
# Source môi trường ROS 2 (Ví dụ với Humble)
source /opt/ros/humble/setup.bash

# Build project
colcon build
```

### 2. Chạy các Node

Để chạy dự án, bạn cần mở **2 terminal** riêng biệt.

#### Terminal 1: Chạy Python Subscriber
Terminal này sẽ đứng đợi để nhận dữ liệu.
```bash
source install/setup.bash
ros2 run inertial_vo_py py_sub
```

#### Terminal 2: Chạy C++ Publisher
Terminal này sẽ gửi 100 số (từ 1 đến 100) vào topic.
```bash
source install/setup.bash
ros2 run inertial_vo cpp_pub
```

## 🎥 Kết quả mong đợi
- **Terminal C++**: Hiển thị log `C++ đang gửi: '1'`, `C++ đang gửi: '2'`, ...
- **Terminal Python**: Hiển thị log `Python nhận được: 1`, `Python nhận được: 2`, ...

---
**Lưu ý**: Đừng quên source `install/setup.bash` mỗi khi mở terminal mới hoặc sau khi build lại code.
