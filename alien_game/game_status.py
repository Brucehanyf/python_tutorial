# 追踪游戏统计信息的类
class GameStats():
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 在任何情况加都不应重置最高得分
        self.high_score =0

        self.reset_stats(False)
        # 游戏刚启动时处于非活动状态
        self.game_active = False


    '''
         初始化在游戏运行期间可能变化的统计信息
         @:param start False 初始化 True 游戏开始 
    '''
    def reset_stats(self, start):

        self.ships_left = self.ai_settings.ship_limit
        # 初始化分数
        self.score = 0
        # 初始化等级
        self.level = 1

        self.game_active = start