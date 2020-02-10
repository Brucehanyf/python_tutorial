# 设置类
class Settings():
    '''存储外星人入侵所有的设置的类 '''
    def __init__(self):
        """ 初始化游戏的设置 """
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船移动的速度设置
        self.ship_speed_factor = 1.5
        self.ship_limit =  3

        #子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allow = 3

        # 外星人设置
        self.alien_speed_factor = 2
        self.feet_drop_speed = 10
        # fleet_direction 1 表示向右移动 -1表示向左移动
        self.feet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.sppedup_scale = 1.1

        # 外星人点数提高等级
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.feet_direction = 1
        # 记分
        self.alien_points = 5

    def increase_speed(self):
        """ 提高游戏速度 """
        self.ship_speed_factor *= self.sppedup_scale
        self.bullet_speed_factor *= self.sppedup_scale
        self.alien_speed_factor *= self.sppedup_scale
        self.alien_points = int(self.alien_points *self.score_scale)
