# python 3
'''
只是一些pytest的简单例子，参照例子来写测试
'''
import pytest
import time


# 直接测试函数
def func(x):
    return x + 1


def testfunc():
    assert func(3) == 4


# 测试Class
class Test_Class:
    def test_one(self):
        x = "this"
        print('h在x里面')
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'he')


# 使用fixture
# 方式一：@pytest.fixture()，其他函数要来调用这个fixture，只是把它当做一个输入的参数而已。
@pytest.fixture()
def before():
    print('\nbefore each test')


def test_1(before):
    print('This is test 1.')


def test_2(before):
    print('This is test 2.')
    assert 0


# 方式二：@pytest.mark.usefixtures
# 每个函数前声明
@pytest.fixture()
def before_1():
    print('\nbefore 1')


@pytest.fixture()
def before_2():
    print('\nbefore 2')


@pytest.mark.usefixtures('before_1')
def test_11():
    print('This is test 11.')


@pytest.mark.usefixtures('before_2')
def test_22():
    print('This is test 22.')
    assert 0


# 类里面每个函数声明
class Test1:
    @pytest.mark.usefixtures('before_1')
    def test_3(self):
        print('This is test 3.')

    @pytest.mark.usefixtures('before_2')
    def test_4(self):
        print('This is test 4.')


# 类前声明，每个测试函数前都会运行fixture
@pytest.mark.usefixtures('before_1')
class Test2:
    def test_5(self):
        print('This is test 5.')

    def test_6(self):
        print('This is test 6.')


# 方式三
# 每个模块会初始化一次，不管这个.py文件有多少个（除了0个）test，该mod_header函数都只运行一次
@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print('\n-----------------')
    print('module      : %s' % request.module.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------\n')


# 每个test都会先调用该func_header函数，默认是fixture的scope
@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n+++++++++++++++++')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('+++++++++++++++++\n')


def test_one():
    print('in test_one()')


def test_two():
    print('in test_two()')


# # 参数化
# # 参数化方式一
# 测试的ID，方便查看哪里出错。由fixture里面的params参数所得。
def idfn(fixture_value):
    if fixture_value[1] >= 3:
        return "eggs"
    else:
        return "pigs"


# 设置参数以及每组参数的ID
@pytest.fixture(params=[([1, 1], 2),
                        ([2, 3], 5),
                        ([3, 4], 6)], ids=idfn)
def add(request):
    return sum(request.param[0]), request.param[1]


def test_add(add):
    print('test_add: %s' % add[0])
    assert add[0] == add[1]


# # 参数化方式二
def add2(a, b):
    return a + b


data = [([1, 1], 2),
        ([2, 3], 5),
        ([3, 4], 8)]


@pytest.mark.parametrize("data, expected_result", data, ids=idfn)
def test_add2(data, expected_result):
    print('\ninput data is: ', data,
          '\nexpected result is: ', expected_result)
    assert expected_result == add2(data[0], data[1])
