unittest +HTMLTestRunner 几个常见的坑
1:测试用例正常运行，不生产测试报告，看网络上普遍说的是系统自动运行的是unit，而不是源文件，如果用
    if name = main  运行，直接跳过main 下的内容   
网络上的几个普遍的几个办法，
    1：手动添加文件到右上角运行，这个可以
    至于右键点不同地方运行不同代码的，我的pycharm没有实现
    2：修改  if name = '文件名'
        -- 亲测，并没卵用
    3 ： 快捷键运行 ALT+SHIFT +F10
        -- 这个办法可以，太麻烦
    个人觉得这几个办法都太麻烦，我推测是由于 类继承了unit.testcase后，编译器自动认为这是
        测试用例，用unittest.TextTestRunner.run方法运行
    所以，简单一点的解决办法就是把 main 函数单独建一个文件
        用discover去组装测试用例，这样比较简单
2：继承 unittest.testcase的几个init方法
    1 setup   每个测试用例开始/结束前运行一遍
    2 teardown
    3 setupclasss   务必加@classmethod装饰器
    4 teardownclass 每组测试用例（一个class里所有test）开始/结束前运行一遍
            -- selenium 初始化驱动，关闭驱动贼好用
            -- @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
            -- @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
                                                -- 这个。。真没用到过，为啥不单独写一个函数？？
3：用例跳过问题
    提供一个装饰器@skip
    skip装饰器一共有四个
    @unittest.skip(reason)    
    翻译：无条件跳过用例，reason是说明原因
    @unittest.skipIf(condition, reason)   
    翻译：condition为true的时候跳过
    @unittest.skipUnless(condition, reason)  
    翻译：condition为False的时候跳过
    @unittest.expectedFailure
    翻译：断言的时候跳过(暂时不知道有啥用，没看懂，貌似断言失败，也变成用例pass了。)
4:用例执行顺序问题
    这个目前还没找到好办法，总结网上的资料，如果是discover组装suite 默认assic码顺序运行test
    若要指定顺序，用suite.add 添加（好麻烦）  后续再找资料
5： 关于失败用例重复执行问题
          直接上链接了
           https://blog.csdn.net/a_1060584570/article/details/78821194                                
          综合网上说法，
            1：添加装饰器，麻烦，不灵活
            2：就是修改源码，一劳永逸
            3：用插件 pytest -没试过 目前来看这个比较合适