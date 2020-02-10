import sys
import pygame
from alien_game.settings import Settings
from alien_game.ship import Ship
from alien_game.button import Button
from alien_game.bullet import Bullet
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    button = Button(ai_settings,screen,"Play")

    # 创建子弹编组
    bullets = Group()

    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

    '''开始游戏主循环'''
    while True:
        # 每次循环都重绘屏幕
        ship.update()
        screen.fill(ai_settings.bg_color)
        # 绘制飞船
        ship.blitme()


        # 在飞船外边重绘所有子弹
        for bullet in bullets:
            bullet.draw_bullet()
        bullets.update()
        pygame.display.flip()

run_game()
