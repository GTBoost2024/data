import pygame
import psutil
import GPUtil
import time
import sys
import ctypes
import win32api
import win32con

# 初始化 Pygame
pygame.init()

# 设置窗口大小和位置
size = (500, 140)
screen = pygame.display.set_mode(size, pygame.NOFRAME)
screen.set_alpha(None)  # 使用透明度

# 字体设置
font = pygame.font.SysFont("Arial", 24)

# 背景颜色（微微灰底，部分透明）
background_color = (0, 0, 0, 100)  # RGBA, A = 100 表示部分透明

# 获取窗口句柄
hwnd = pygame.display.get_wm_info()["window"]

# 设置窗口为点击穿透
ctypes.windll.user32.SetWindowLongW(hwnd, win32con.GWL_EXSTYLE, 
    ctypes.windll.user32.GetWindowLongW(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # 获取系统信息
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    ram_usage = memory_info.percent
    fps = int(pygame.time.get_ticks() / 1000)  # 使用时间戳模拟 FPS
    
    # 获取 GPU 信息
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]  # 假设使用第一个 GPU
        gpu_info = f"GPU: {gpu.name}, Load: {gpu.load * 100:.1f}%, Mem: {gpu.memoryUsed:.1f}/{gpu.memoryTotal:.1f}MB"
    else:
        gpu_info = "GPU: Not Available"

    # 填充背景
    screen.fill(background_color)

    # 绘制信息
    info_text = [
        f"CPU Usage: {cpu_usage}%",
        f"RAM Usage: {ram_usage}%",
        f"FPS: {fps}",
        gpu_info
    ]
    
    for i, line in enumerate(info_text):
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10 + i * 30))

    # 更新屏幕
    pygame.display.update()

    # 延迟以减少 CPU 使用率
    time.sleep(0.1)

pygame.quit()
sys.exit()