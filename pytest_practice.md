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
    





