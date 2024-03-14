import sys
import unittest
import tempfile
import os
from main import main
import re


def is_success(str):
    return bool(re.search(r'\d', str))

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # 利用tempfile创建临时文件
        self.file1_or = tempfile.NamedTemporaryFile(delete=False)
        self.file1_pl = tempfile.NamedTemporaryFile(delete=False)
        self.file2_or = tempfile.NamedTemporaryFile(delete=False)
        self.file2_pl = tempfile.NamedTemporaryFile(delete=False)
        self.file3_or = tempfile.NamedTemporaryFile(delete=False)
        self.file3_pl = tempfile.NamedTemporaryFile(delete=False)
        self.file4_or = tempfile.NamedTemporaryFile(delete=False)
        self.file4_pl = tempfile.NamedTemporaryFile(delete=False)
        self.output_1 = tempfile.NamedTemporaryFile(delete=False)
        self.output_2 = tempfile.NamedTemporaryFile(delete=False)
        self.output_3 = tempfile.NamedTemporaryFile(delete=False)
        self.output_4 = tempfile.NamedTemporaryFile(delete=False)

        # 写入测试数据
        self.file1_or.write('秋日漫步，美景入心。'.encode())
        self.file1_pl.write('秋日漫步，美景入心。'.encode())

        self.file2_or.write("今天是星期天，天气晴，今天晚上我要去看电影。".encode())
        self.file2_pl.write("今天是周天，天气晴朗，我晚上要去看电影。".encode())

        self.file3_or.write("在这个炎炎夏日，阳光透过翠绿的树叶洒在宁静的小路上，空气中弥漫着淡淡的花香。"
                            "一群孩子在草地上追逐嬉戏，欢声笑语回荡在这片祥和的氛围中。"
                            "我悠闲地坐在树荫下，享受着这份难得的宁静与惬意，心中的烦忧似乎也随着微风轻轻飘散。".encode())
        self.file3_pl.write("在这炽热的夏日，阳光斑驳地穿过碧绿的树叶，洒落在蜿蜒的小径上。"
                            "空气中夹杂着丝丝花香，清新宜人。"
                            "一群孩童在青翠的草地上尽情玩耍，他们的欢笑声在温暖的空气中回荡。"
                            "我静静地坐在树荫之下，享受着这份难得的宁静与悠闲，心中的烦恼似乎也随着微风悄然消散。".encode())

        self.file4_or.write("在这个炎炎夏日，阳光透过翠绿的树叶洒在宁静的小路上，空气中弥漫着淡淡的花香。"
                            "一群孩子在草地上追逐嬉戏，欢声笑语回荡在这片祥和的氛围中。"
                            "我悠闲地坐在树荫下，享受着这份难得的宁静与惬意，心中的烦忧似乎也随着微风轻轻飘散。".encode())
        self.file4_pl.write("在这炽热的夏日午后，阳光透过碧绿的树叶，斑驳地洒落在静谧的小径上。"
                            "空气中弥漫着淡淡的花香，清新而宜人。"
                            "一群孩童在草地上尽情嬉戏，他们的欢笑声在温暖的空气中飘荡，为这宁静的时光增添了一抹生机与活力。"
                            "我坐在树荫下，静静享受这难得的宁静时光，让疲惫的心在微风中悄然放松。"
                            "此刻，所有的烦恼似乎都随风而去，只留下宁静与惬意在心间萦绕。".encode())

        self.file1_or.close()
        self.file1_pl.close()
        self.file2_or.close()
        self.file2_pl.close()
        self.file3_or.close()
        self.file3_pl.close()
        self.file4_or.close()
        self.file4_pl.close()

    def tearDown(self):
        # 测试结束后删除临时文件
        self.file1_or.close()
        self.file1_pl.close()
        self.file2_or.close()
        self.file2_pl.close()
        self.file3_or.close()
        self.file3_pl.close()
        self.file4_or.close()
        self.file4_pl.close()
        self.output_1.close()
        self.output_2.close()
        self.output_3.close()
        self.output_4.close()
        os.unlink(self.file1_or.name)
        os.unlink(self.file1_pl.name)
        os.unlink(self.file2_or.name)
        os.unlink(self.file2_pl.name)
        os.unlink(self.file3_or.name)
        os.unlink(self.file3_pl.name)
        os.unlink(self.file4_or.name)
        os.unlink(self.file4_pl.name)
        os.unlink(self.output_1.name)
        os.unlink(self.output_2.name)
        os.unlink(self.output_3.name)
        os.unlink(self.output_4.name)


    def test_main_cosine(self):
        # 修改命令行参数
        sys.argv = ['main.py', self.file1_or.name, self.file1_pl.name, self.output_1.name]
        # 运行函数
        main()
        # 检查输出文件
        with open(self.output_1.name, 'r') as f:
            result = f.read()
        self.assertTrue(is_success(result))

        # 修改命令行参数
        sys.argv = ['main.py', self.file2_or.name, self.file2_pl.name, self.output_2.name]
        # 运行函数
        main()
        # 检查输出文件
        with open(self.output_2.name, 'r') as f:
            result = f.read()
        self.assertTrue(is_success(result))

        sys.argv = ['main.py', self.file3_or.name, self.file3_pl.name, self.output_3.name]
        # 运行函数
        main()
        # 检查输出文件
        with open(self.output_3.name, 'r') as f:
            result = f.read()
        self.assertTrue(is_success(result))

        sys.argv = ['main.py', self.file4_or.name, self.file4_pl.name, self.output_4.name]
        # 运行函数
        main()
        # 检查输出文件
        with open(self.output_4.name, 'r') as f:
            result = f.read()
        self.assertTrue(is_success(result))

if __name__ == '__main__':
    unittest.main()



