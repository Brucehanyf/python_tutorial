# 游戏运行函数
import sys
import pygame
from alien_game.bullet import Bullet
from alien_game.alien import Alien
from time import sleep


def check_events(ai_settings, screen, stats, sb, play_button, ship, bullets):
    """ 响应键盘事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, sb, play_button, mouse_x, mouse_y)
    # 处理飞船移动参数
    ship.update()


def check_play_button(ai_settings, stats, sb, play_button, mouse_x, mouse_y):
    """ 在玩家单击Play按钮时开始新游戏"""
    # 并且在在游戏结束的是才可以重置
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # 重置游戏
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats(True)
        sb.prep_score_images()
        # 隐藏光标
        pygame.mouse.set_visible(False)


# 检测键盘按下
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.move_left = True
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 如果还没有都达到限制,就发射一颗子弹
    if len(bullets) < ai_settings.bullet_allow:
        # 创建一颗子弹 并将其加入编组Group中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# 检测键盘抬起
def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.move_left = False
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.move_down = False


def update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button):
    """更新屏幕上的图像,并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    # 重新绘制飞船
    ship.blitme()
    # 绘制子弹
    bullets.update()
    # 绘制外星人
    aliens.draw(screen)
    # 绘制得分版
    sb.draw_score_board()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()


def update_bullets(bullets, ai_settings, stats, screen, sb, ship, aliens):
    # 在飞船外边重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ 检查是否有子弹撞击外星人吗， 击中则删除相应的子弹和外星人"""
    collections = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collections:
        # 处理同一循环处理多个外星人的情况
        for aliens in collections.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        # 检查最高分
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 清空子弹
        # bullets.empty()
        ai_settings.increase_speed()
        # 如果整群外星人被消灭，就提高一个等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 创建单个外星人
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人群 """
    # TODO 为什么Alien 创建了两次
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 多层循环创建外星人
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_feet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时采取相应的措施"""
    for alien in aliens.copy():
        if alien.check_edges():
            change_feet_direction(ai_settings, aliens)
            break


def change_feet_direction(ai_setting, aliens):
    """ 将整群外星人下移, 并改变它们的方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.feet_drop_speed
    # 改变方向
    ai_setting.feet_direction *= -1


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """响应外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left 减1
        stats.ships_left -= 1
        # 更新飞船剩余数量
        sb.prep_ships()
        #  清空外形人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人， 并将飞船方到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship(screen)
        # 暂停0.5
        sleep(0.5)
    else:
        # 游戏结束
        stats.game_active = False
        # 重新显示鼠标
        pygame.mouse.set_visible(True)
        aliens.empty()
        bullets.empty()


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 检查是否有外星人到达了屏幕底端 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.y >= screen_rect.bottom:
            aliens.remove(alien)


def check_high_score(stats, sb):
    """ 检查是否诞生了新的最高分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕的边缘、并更新整群外星人的位置 """
    check_feet_edges(ai_settings, aliens)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
