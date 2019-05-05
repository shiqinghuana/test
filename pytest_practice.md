pytest初体验
2019-5-1
下午安装了pytest，跑了几个case,感觉不错
与untitest相比，pytest更灵活，更轻便，同时对个人掌握能力要求更高

untitest-- 创建一个类，继承Testcase,码到底就能run,或者用HTMLTestRunner 生产测试报告，
            提供setup,teardown(class)作为初始化方法与结尾方法，比较笨重，拓展性较差，
            优点在于简单，上手快，几乎不需要去考虑其他东西专注于撸代码
pytest  -- 基于untitest的拓展，几乎能完美实现所有untitest的功能，支持多元化生成测试报告
            如xml,极大的亲和CI集成工具，如jenkins
            更加灵活，提供fixture方法能自由组装需要的东西，及maker自由选择执行的case与跳过的case
            不需要组装suite,同时对文件，类，函数命名要求更高
            开源拓展性好，目前支持300多款插件
            对使用者要求更高
后续更新~~~

执行测试用例，，
cmd --  pytest  XXX(路径或指定任务)  --后面加各种参数（--junitxml='文件路径’//--HTML='文件路径’
                需安装pytest-html）
pycharm --  pytest.main(['','','','','',']) 列表形式，值跟cmd一样，放入列表中‘
            '--self-contained-html’ 保存css样式
文件会自动创建
运行后目录下会创建一堆文件，描述是缓存文件  pytest_cache md中有一句
    **Do not** commit this to version control. 
--目前来看，pytest比unittest好用太多，好好研究一下！
    
2019-5-2

fixture 四个等级  session  module  class function 级别从大到小
        分别表示作用域，整个测试，某个模块（.py） 某个类，某个函数      
        举例 ： 
        @fixture(scorp = 'class')
        def A（）
            return XX
            pass
        作用于某个类，需要用到的测试类把A 当做参数加入 ~~~好像不太方便
~~ 带参数的fixture\
几中方法，举个例子
一：
data = [{'a':"5"}]   需要传的参数

@pytest.fixture(scope='class')
def haha(request):  加入request
    print('开始测试') 
    #a = '5'
    a = request.param['a']   request.param【键】 获取参数中的值
    yield a   返回值
    print('测试结束')



class Test_Case(object):
    @pytest.mark.parametrize('haha', data, indirect=True)  三个参数’函数‘，数据，indirect=true
    def test_case(self,haha):
       # print(self.a,)
        #time.sleep(1)
        assert haha =='5','不是5'
其他正常写
此方法只能返回单个值，所以尽量让参数在fixture中使用，返回一个实例
如果要用fixture的函数，及值、、、？？有这个必要么
分开写fixture,并叠加pytest.mark.parametrize
这种方法会叠加测试用例数
如 A['a','b']
  B['11','22']
  我们想测a--11 b-22两组数据，但实际中会生成 a-11 a-22 b-11 b-22四组（A*B)
  

2019-5-3
pytets 参数化
写法同上，只是把fixtrue函数放入conflist.py ，fixtrue加parma参数，值=需要放入的参数列表

conflist.py
fixtrue中不加参数 parma参数
希望 A数据执行 case1  B数据执行case2
用标记数据传入参数
@pytest.mark.parametrize('haha', A, indirect=True)
def case(fixtrue)
    pass
方法同上，

传入多数据
data =[(a1,b1,c1),(a2,b2,c2),(a3,b3,c3)]
@pytest.mark.parametrize('A,B,C',data )
def case(fixtrue)
    pass
 参数以列表形式传入，此方法跟上面叠加装饰器相似，测试用例数 =数据数之积
 
 跳过某个测试用例
 @pytest.mark.skip 
 @ytest.mark.skipif(条件跳过)
 
 2019-5-5
 关于参数化几个理解错误的地方
 两种方法实现
 1：@pytest.fixture(params =params )  fixture中自带parmas 关键字
    def A(request):
        return request.param   --用request.param 接收参数，返回测试用例中
    --  
    def test(A):
        assert A == true  
    //或者
    def B（param）:
        return param       
    def test(A)
        assert B(A) ==true
2: 标记处理
    @pytest.mark.parametrize('args',parma)  参数 - 值，如果是多个，要按顺序一一对应
    def test()：
        assert B(args)==true
3：叠加装饰器--太麻烦，不琢磨了
 两种方法都各有用处吧！
 
 
 main 常用参数  -q  -v  --junitxml=path  --html=path 
 
 基础知识，到这儿应该差不多了吧？？