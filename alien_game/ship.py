# 飞船类
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        ''' 初始化飞船并设置其初始位置 '''
        self.screen = screen

        # 设置飞船参数
        self.ai_setings = ai_settings

        # 移动标识
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        # 飞船居中
        self.center_ship(screen)

    def update(self):
        '''根据移动标志移动飞船'''
        # 更新飞船的center值而不是rect值
        # 是指飞船不能越界 self.rect.right < self.screen_rect.right  self.rect.left > 0
        if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += self.ship_speed_factor
            self.center_x += self.ai_setings.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            # self.rect.centerx -= self.ship_speed_factor
            self.center_x -= self.ai_setings.ship_speed_factor
        if self.move_up and self.rect.centery > self.screen_rect.top:
            # self.rect.bottom -= self.ship_speed_factor
            self.center_y -= self.ai_setings.ship_speed_factor
        if self.move_down and self.rect.centery < self.screen_rect.bottom:
            # self.rect.bottom += self.ship_speed_factor
            self.center_y += self.ai_setings.ship_speed_factor
        # 根据self.center更新react对象
        self.rect.centerx = self.center_x
        self.rect.bottom = self.center_y

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self, screen):
        """ 让飞船在屏幕上居中"""
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值 飞船坐标
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.bottom)
