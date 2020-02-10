# survey 测试类
import unittest
from test.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """ 创建一个调查对象和一组答案，功使用的测试方法使用 """
        question = "what's language did you first learn to speak"
        self.my_survey = AnonymousSurvey(question)
        self.response = ['English', 'Chinese', 'Russia']
        # 可以用self.mysurvey.store_respinse(self.response[0]) 调用

    def test_store_single_response(self):
        """ 测试单个答案会被妥善的保存 """
        question = "what's language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.response)

    def test_stpre_three_response(self):
        """测试三个答案会被妥善的保存"""
        question = "what's language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'Russia']
        for response in responses:
            my_survey.store_response(response)
        self.assertIn('Russia', my_survey.response)
