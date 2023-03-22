# Scrapy框架实现b站搜索结果爬取
## 说明
### 1.这是一个半死的爬虫
### 2.上面那句话是开玩笑的
### 3.使用说明

#### a.获取Cookies
- 程序内已内置Cookies
- 若Cookies失效（如返回412）请前往`/finaltask/Spider/Spider/setting.py`中的`DEFAULT_REQUEST_HEADERS`粘贴你的Cookies

#### b.设定搜索关键词和搜索页码范围
- 默认搜索关键词为ikun（滑稽），搜索范围为1-34页
- 关键词请前往`/finaltask/Spider/Spider/Spiders/bili.py`中的`start_urls`->`keywords=`中修改
- 搜索范围请在相同文件的相同位置中的`range()`修改，参数为`('起始页码','终止页码+1')`
- 更多选项：注意到api链接后面的params参数有很多值可以选择，可以自行添加搜索类别，排序方式等等
#### c.设定筛选结果参数
- 参数筛选在文件`/finaltask/Spider/Spider/Spiders/bili.py`中，默认筛选播放量大于`1000000`的视频
- 我定义了若干量描述一个视频的属性（类型均为`String`）：
    - `bvid`：BV号
    - `title`：视频标题
    - `author`：作者
    - `play`：播放量
    - `like`：点赞数
    - `favorites`：收藏数
    - `tag`：标签
    - `duration`：时长
- 你可以在我的`if()`中自定义筛选参数
#### d.在命令行中运行
- 在命令行中前往`/finaltask/Spider`
- 运行`$ scrapy crawl bili -o results.csv`，会在目录里生成`results.csv`文件
- 你也可以自行决定参数让爬虫干别的事情
#### e.Enjoy! 🚀