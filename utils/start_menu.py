# utils/start_menu.py
from doctest import master

from settings import *

import pygame
import math


def draw_rounded_button(screen, rect, border_color, fill_color, border_radius, border_width=0):
    """绘制带圆角边框的按钮"""
    pygame.draw.rect(screen, fill_color, rect, border_radius=border_radius)  # 绘制填充颜色的矩形
    if border_width > 0:
        pygame.draw.rect(screen, border_color, rect, border_radius=border_radius, width=border_width)  # 绘制边框

def draw_volume_slider(screen: pygame.Surface, volume: float):
    """绘制音量滑块"""
    slider_width, slider_height = 200, 10
    slider_x, slider_y = (screen.get_width() // 2 - slider_width // 2, 300)
    slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)
    handle_radius = 10

    # 绘制滑块背景
    pygame.draw.rect(screen, COLORS['gray'], slider_rect)

    # 计算滑块手柄位置
    handle_x = slider_x + int(volume * slider_width)
    handle_y = slider_y + slider_height // 2

    # 绘制滑块手柄
    pygame.draw.circle(screen, COLORS['white'], (handle_x, handle_y), handle_radius)

    return slider_rect, handle_radius

def show_settings_menu(screen, background_image):
    """显示设置界面"""
    global VOLUME  # 引用全局变量 VOLUME
    select_sound = pygame.mixer.Sound(SELECT_PATH)
    select_sound.set_volume(10 * VOLUME)

    menu_font = pygame.font.Font(FONT_PATH, 48)  # 主菜单字体
    small_menu_font = pygame.font.Font(FONT_PATH, 20)  # 提示文字字体

    back_text = small_menu_font.render("返回", True, COLORS['black'])  # 返回按钮文本
    volume_text=menu_font.render("声音", True, COLORS['black'])  # 返回按钮文本
    VOLUME_BUTTON_SIZE = (120, 70)  # 返回按钮尺寸
    VOLUME_BUTTON_POSITION = (450, 200)  # 返回按钮位置
    volume_button_rect = pygame.Rect(VOLUME_BUTTON_POSITION, VOLUME_BUTTON_SIZE)  # 返回按钮区域


    BACK_BUTTON_SIZE = (100, 30)  # 返回按钮尺寸
    BACK_BUTTON_POSITION = (10, SCREEN_HEIGHT - 40)  # 返回按钮位置
    back_button_rect = pygame.Rect(BACK_BUTTON_POSITION, BACK_BUTTON_SIZE)  # 返回按钮区域

    while True:  # 进入设置界面循环
        screen.blit(background_image, (0, 0))  # 绘制背景图像
        draw_rounded_button(screen, back_button_rect, COLORS['black'], COLORS['gold'], border_radius=15,
                            border_width=3)  # 绘制返回按钮
        draw_rounded_button(screen, volume_button_rect, COLORS['black'], COLORS['gold'], border_radius=15,
                            border_width=3)  # 绘制返回按钮
        screen.blit(back_text, (back_button_rect.x + 10, back_button_rect.y + 5))  # 显示返回按钮文本
        screen.blit(volume_text, (volume_button_rect.x + 10, volume_button_rect.y + 5))  # 显示返回按钮文本

        # 绘制音量滑块
        slider_rect, handle_radius = draw_volume_slider(screen, VOLUME)

        pygame.display.flip()  # 更新屏幕显示

        for event in pygame.event.get():  # 处理事件
            if event.type == pygame.QUIT:  # 检测窗口关闭事件
                return False  # 返回 False 表示退出游戏
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
                if back_button_rect.collidepoint(pygame.mouse.get_pos()):  # 点击返回按钮
                    select_sound.play()
                    return True  # 返回 True 表示返回主菜单
                elif slider_rect.collidepoint(event.pos):  # 点击滑块
                    # 更新音量值
                    relative_x = event.pos[0] - slider_rect.x
                    VOLUME = max(0, min(1, relative_x / slider_rect.width))



def show_about_menu(screen, background_image):
    """显示关于界面"""
    select_sound = pygame.mixer.Sound(SELECT_PATH)
    select_sound.set_volume(10 * VOLUME)
    while True:  # 进入关于界面循环
        big_menu_font = pygame.font.Font(FONT_PATH, 50)  # 标题背景字体
        menu_font = pygame.font.Font(FONT_PATH, 48)  # 主菜单字体
        small_menu_font = pygame.font.Font(FONT_PATH, 20)  # 提示文字字体

        screen.blit(background_image, (0, 0))  # 绘制背景图像
        back_text = small_menu_font.render("返回", True, COLORS['black'])  # 返回按钮文本
        BACK_BUTTON_SIZE = (100, 30)  # 返回按钮尺寸
        BACK_BUTTON_POSITION = (10, SCREEN_HEIGHT - 40)  # 返回按钮位置
        back_button_rect = pygame.Rect(BACK_BUTTON_POSITION, BACK_BUTTON_SIZE)  # 返回按钮区域

        # 使用新函数绘制关于信息
        draw_about_screen(screen, menu_font,big_menu_font, COLORS)

        draw_rounded_button(screen, back_button_rect, COLORS['black'], COLORS['gold'], border_radius=15,
                            border_width=3)  # 绘制返回按钮
        screen.blit(back_text, (back_button_rect.x + 10, back_button_rect.y + 5))  # 显示返回按钮文本

        pygame.display.flip()  # 更新屏幕显示

        for event in pygame.event.get():  # 处理事件
            if event.type == pygame.QUIT:  # 检测窗口关闭事件
                return False  # 返回 False 表示退出游戏
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
                if back_button_rect.collidepoint(pygame.mouse.get_pos()):  # 点击返回按钮
                    select_sound.play()
                    return True  # 返回 True 表示返回主菜单

def show_start_menu(screen, background_image):
    global VOLUME
    select_sound = pygame.mixer.Sound(SELECT_PATH)
    select_sound.set_volume(10 * VOLUME)
    # 加载并播放背景音乐
    pygame.mixer.music.load(START_PATH)  # 替换为你的 BGM 文件路径
    pygame.mixer.music.set_volume(VOLUME / 3)  # 设置音量（0.0 到 1.0）
    pygame.mixer.music.play(-1)  # -1 表示循环播放

    """显示开始菜单，提供动态效果和用户交互"""

    # 初始化字体对象
    menu_font = pygame.font.Font(FONT_PATH, 48)  # 主菜单字体
    small_menu_font = pygame.font.Font(FONT_PATH, 20)  # 提示文字字体
    big_menu_font = pygame.font.Font(FONT_PATH, 50)  # 标题背景字体

    # 渲染菜单文本
    start_text = menu_font.render("开始游戏", True, COLORS['black'])  # 开始按钮文本
    settings_text = small_menu_font.render("设置", True, COLORS['black'])  # 设置按钮文本
    about_text = small_menu_font.render("关于", True, COLORS['black'])  # 关于按钮文本
    title_text = menu_font.render("弓箭手传奇", True, COLORS['gold'])  # 主标题
    title_text_bk = big_menu_font.render("弓箭手传奇", True, COLORS['red'])  # 主标题背景
    quit_text = small_menu_font.render("退出游戏", True, COLORS['black'])  # 退出按钮文本
    back_text = small_menu_font.render("返回", True, COLORS['black'])  # 返回按钮文本

    # 定义按钮尺寸常量
    START_BUTTON_SIZE = (210, 75)  # 开始按钮尺寸
    SETTINGS_BUTTON_SIZE = (100, 50)  # 设置按钮尺寸
    ABOUT_BUTTON_SIZE = (100, 50)  # 关于按钮尺寸
    QUIT_BUTTON_SIZE = (100, 30)  # 退出按钮尺寸
    BACK_BUTTON_SIZE = (100, 30)  # 返回按钮尺寸

    # 定义按钮位置常量
    START_BUTTON_POSITION = (SCREEN_WIDTH // 2 - 105, SCREEN_HEIGHT // 2 - 40)  # 开始按钮位置
    SETTINGS_BUTTON_POSITION = (START_BUTTON_POSITION[0] - SETTINGS_BUTTON_SIZE[0] + 100,
                                START_BUTTON_POSITION[1] + START_BUTTON_SIZE[1] + 10)  # 设置按钮位置
    ABOUT_BUTTON_POSITION = (START_BUTTON_POSITION[0] + START_BUTTON_SIZE[0] - 100,
                             START_BUTTON_POSITION[1] + START_BUTTON_SIZE[1] + 10)  # 关于按钮位置
    QUIT_BUTTON_POSITION = (10, SCREEN_HEIGHT - 40)  # 退出按钮位置
    BACK_BUTTON_POSITION = (10, SCREEN_HEIGHT - 40)  # 返回按钮位置

    # 定义按钮区域
    start_button_rect = pygame.Rect(START_BUTTON_POSITION, START_BUTTON_SIZE)  # 开始按钮区域
    settings_button_rect = pygame.Rect(SETTINGS_BUTTON_POSITION, SETTINGS_BUTTON_SIZE)  # 设置按钮区域
    about_button_rect = pygame.Rect(ABOUT_BUTTON_POSITION, ABOUT_BUTTON_SIZE)  # 关于按钮区域
    quit_button_rect = pygame.Rect(QUIT_BUTTON_POSITION, QUIT_BUTTON_SIZE)  # 退出按钮区域
    back_button_rect = pygame.Rect(BACK_BUTTON_POSITION, BACK_BUTTON_SIZE)  # 返回按钮区域






    # 主循环
    clock = pygame.time.Clock()  # 创建时钟对象
    elapsed_time = 0  # 初始化经过时间
    hover_start = False  # 是否悬停在开始按钮上
    hover_quit = False  # 是否悬停在退出按钮上
    hover_settings = False  # 是否悬停在设置按钮上
    hover_about = False  # 是否悬停在关于按钮上

    while True:  # 主菜单循环
        delta_time = clock.tick(60) / 1000  # 计算帧间隔时间（秒）
        elapsed_time += delta_time  # 累计经过时间

        screen.blit(background_image, (0, 0))  # 绘制背景图像

        # 正弦函数控制标题缩放
        scale_factor = 1 + 0.1 * math.sin(elapsed_time * 2 * math.pi)  # 正弦波缩放因子
        scaled_title_text = pygame.transform.scale(
            title_text,
            (int(title_text.get_width() * scale_factor), int(title_text.get_height() * scale_factor))
        )  # 缩放主标题
        scaled_title_text_bk = pygame.transform.scale(
            title_text_bk,
            (int(title_text_bk.get_width() * scale_factor), int(title_text_bk.get_height() * scale_factor))
        )  # 缩放标题背景

        # 计算标题位置
        title_x = SCREEN_WIDTH // 2 - scaled_title_text.get_width() // 2  # 计算标题水平居中位置
        title_y = SCREEN_HEIGHT // 2 - 220  # 标题垂直位置

        # 绘制主标题及其背景
        screen.blit(scaled_title_text_bk, (title_x, title_y))  # 绘制标题背景
        screen.blit(scaled_title_text, (title_x + 5, title_y))  # 绘制主标题（带轻微偏移）

        # 鼠标悬停检测与按钮缩放
        mouse_pos = pygame.mouse.get_pos()  # 获取当前鼠标位置
        hover_start = start_button_rect.collidepoint(mouse_pos)  # 检测是否悬停在开始按钮上
        hover_quit = quit_button_rect.collidepoint(mouse_pos)  # 检测是否悬停在退出按钮上
        hover_settings = settings_button_rect.collidepoint(mouse_pos)  # 检测是否悬停在设置按钮上
        hover_about = about_button_rect.collidepoint(mouse_pos)  # 检测是否悬停在关于按钮上
        hover_back = back_button_rect.collidepoint(mouse_pos)  # 检测是否悬停在关于按钮上

        # 根据悬停状态调整按钮尺寸
        start_button_size = (
            int(START_BUTTON_SIZE[0] * 1.05 if hover_start else START_BUTTON_SIZE[0]),
            int(START_BUTTON_SIZE[1] * 1.05 if hover_start else START_BUTTON_SIZE[1])
        )
        settings_button_size = (
            int(SETTINGS_BUTTON_SIZE[0] * 1.05 if hover_settings else SETTINGS_BUTTON_SIZE[0]),
            int(SETTINGS_BUTTON_SIZE[1] * 1.05 if hover_settings else SETTINGS_BUTTON_SIZE[1])
        )
        about_button_size = (
            int(ABOUT_BUTTON_SIZE[0] * 1.05 if hover_about else ABOUT_BUTTON_SIZE[0]),
            int(ABOUT_BUTTON_SIZE[1] * 1.05 if hover_about else ABOUT_BUTTON_SIZE[1])
        )
        quit_button_size = (
            int(QUIT_BUTTON_SIZE[0] * 1.05 if hover_quit else QUIT_BUTTON_SIZE[0]),
            int(QUIT_BUTTON_SIZE[1] * 1.05 if hover_quit else QUIT_BUTTON_SIZE[1])
        )
        back_button_size = (
            int(QUIT_BUTTON_SIZE[0] * 1.05 if hover_back else QUIT_BUTTON_SIZE[0]),
            int(QUIT_BUTTON_SIZE[1] * 1.05 if hover_back else QUIT_BUTTON_SIZE[1])
        )

        # 根据调整后的尺寸重新定义按钮区域
        start_button_rect = pygame.Rect(
            (START_BUTTON_POSITION[0] - (start_button_size[0] - START_BUTTON_SIZE[0]) // 2,
             START_BUTTON_POSITION[1] - (start_button_size[1] - START_BUTTON_SIZE[1]) // 2),
            start_button_size
        )
        settings_button_rect = pygame.Rect(
            (SETTINGS_BUTTON_POSITION[0] - (settings_button_size[0] - SETTINGS_BUTTON_SIZE[0]) // 2,
             SETTINGS_BUTTON_POSITION[1] - (settings_button_size[1] - SETTINGS_BUTTON_SIZE[1]) // 2),
            settings_button_size
        )
        about_button_rect = pygame.Rect(
            (ABOUT_BUTTON_POSITION[0] - (about_button_size[0] - ABOUT_BUTTON_SIZE[0]) // 2,
             ABOUT_BUTTON_POSITION[1] - (about_button_size[1] - ABOUT_BUTTON_SIZE[1]) // 2),
            about_button_size
        )
        quit_button_rect = pygame.Rect(
            (QUIT_BUTTON_POSITION[0] - (quit_button_size[0] - QUIT_BUTTON_SIZE[0]) // 2,
             QUIT_BUTTON_POSITION[1] - (quit_button_size[1] - QUIT_BUTTON_SIZE[1]) // 2),
            quit_button_size
        )
        back_button_rect = pygame.Rect(
            (QUIT_BUTTON_POSITION[0] - (back_button_size[0] - QUIT_BUTTON_SIZE[0]) // 2,
             QUIT_BUTTON_POSITION[1] - (back_button_size[1] - QUIT_BUTTON_SIZE[1]) // 2),
            back_button_size
        )

        # 绘制按钮
        draw_rounded_button(screen, start_button_rect, COLORS['black'], COLORS['gold'], border_radius=20,
                            border_width=3)  # 绘制开始按钮
        draw_rounded_button(screen, settings_button_rect, COLORS['black'], COLORS['blue'], border_radius=15,
                            border_width=3)  # 绘制设置按钮
        draw_rounded_button(screen, about_button_rect, COLORS['black'], COLORS['green'], border_radius=15,
                            border_width=3)  # 绘制关于按钮
        draw_rounded_button(screen, quit_button_rect, COLORS['black'], COLORS['red'], border_radius=15,
                            border_width=3)  # 绘制退出按钮

        # 在按钮上绘制文本
        screen.blit(start_text, (start_button_rect.x + 10, start_button_rect.y + 10))  # 开始按钮文本
        screen.blit(settings_text, (settings_button_rect.x + 30, settings_button_rect.y + 13))  # 设置按钮文本
        screen.blit(about_text, (about_button_rect.x + 30, about_button_rect.y + 13))  # 关于按钮文本
        screen.blit(quit_text, (quit_button_rect.x + 10, quit_button_rect.y + 5))  # 调整退出按钮文本位置

        pygame.display.flip()  # 更新屏幕显示

        # 处理用户事件
        for event in pygame.event.get():  # 遍历事件队列
            if event.type == pygame.QUIT:  # 检测窗口关闭事件
                exit()  # 返回 False 表示退出游戏
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
                if start_button_rect.collidepoint(mouse_pos):  # 点击开始按钮
                    select_sound.play()
                    return True  # 返回 True 表示进入游戏
                elif settings_button_rect.collidepoint(mouse_pos):  # 点击设置按钮
                    select_sound.play()
                    if not show_settings_menu(screen, background_image):  # 显示设置界面
                        return False  # 如果设置界面返回 False，则退出游戏
                elif about_button_rect.collidepoint(mouse_pos):  # 点击关于按钮
                    select_sound.play()
                    if not show_about_menu(screen, background_image):  # 显示关于界面
                        return False  # 如果关于界面返回 False，则退出游戏
                elif quit_button_rect.collidepoint(mouse_pos):  # 点击退出按钮
                    exit()  # 返回 False 表示退出游戏


# 新增的函数实现
def draw_about_screen(screen, menu_font,big_menu_font,COLORS):

    title_text = menu_font.render("弓箭手传奇", True, COLORS['gold'])  # 主标题
    title_text_bk = big_menu_font.render("弓箭手传奇", True, COLORS['red'])  # 主标题背景


    # 计算标题位置
    title_x = SCREEN_WIDTH // 2 - title_text.get_width() // 2  # 计算标题水平居中位置
    title_y = SCREEN_HEIGHT // 2 - 280  # 标题垂直位置

    # 绘制主标题及其背景
    screen.blit(title_text_bk, (title_x, title_y))  # 绘制标题背景
    screen.blit(title_text, (title_x + 5, title_y))  # 绘制主标题（带轻微偏移）

    # 开发人员信息
    master_text = menu_font.render("开发人员", True, COLORS['black'])
    A_text = menu_font.render("程序：晓炙云溪", True, COLORS['black'])
    B_text = menu_font.render("设计：雨林霖", True, COLORS['black'])
    C_text = menu_font.render("策划：可能是黑某人吧", True, COLORS['black'])
    D_text = menu_font.render("美术：cheems", True, COLORS['black'])
    E_text = menu_font.render("%s"%VISION, True, COLORS['black'])

    # 居中绘制逻辑
    def blit_centered(text, y_offset):
        x = (SCREEN_WIDTH - text.get_width()) // 2  # 水平居中
        y = y_offset  # 垂直偏移
        screen.blit(text, (x, y))
    def blit_left(text, y_offset):
        x = 340  # 水平居中
        y = y_offset  # 垂直偏移
        screen.blit(text, (x, y))

    # 绘制标题和开发人员名单
    blit_centered(master_text, 100)  # "开发人员" 标题
    blit_left(A_text, 200)       # 第一条信息
    blit_left(B_text, 250)       # 第二条信息
    blit_left(C_text, 300)       # 第三条信息
    blit_left(D_text, 350)       # 第四条信息
    screen.blit(E_text,(910,540))  # 第四条信息