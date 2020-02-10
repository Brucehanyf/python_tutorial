import pygame
from alien_game.settings import Settings
from alien_game.ship import Ship
import alien_game.game_function as gf
from pygame.sprite import Group
from alien_game.game_status import GameStats
from alien_game.button import Button
from alien_game.scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 初始化设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 得分板
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建子弹编组
    bullets = Group()

    # 创建外星人集群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    '''开始游戏主循环'''
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets)
        if stats.game_active:
            # 重绘外星人位置
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            # 重绘子弹设置
            gf.update_bullets(bullets, ai_settings,stats, screen, sb, ship, aliens)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

'''  启动游戏'''
run_game()
