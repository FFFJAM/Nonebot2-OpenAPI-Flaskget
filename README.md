# Nonebot2-OpenAPI-Flaskget

**API形式调用OpenAPI进行与chatgpt的交互，适用于Nonebot2机器人框架的插件** 

随着GPT4的发布，OpenAI也禁止了OpenAPI在大陆地区的调用，本项目致力于解决这个问题，使用在境外服务器部署python-flask环境请求调用并转发OpenAPI信息，并结合Nonebot2框架插件实现在qq上的便捷交互

### 配置需要

- 一台地区为非大陆、台湾、香港的服务器，推荐日本或新加坡
- 服务器配置Python3.8+
- 一个已创建的Nonebot2机器人

### 项目结构
```
Nonebot2-OpenAPI-Flaskget
├── plugins
│   ├── available.py
│   └── chat.py
├── README.md
├── requirements.txt
├── server.py
└── test.cfg
```
### 使用教程

> 1.在服务器使用pip安装requirement.txt<br/>
> 2.配置test.cfg,填入你的OpenAPIKEY和记忆次数<br/>
> 3.运行server.py<br/>
> 4.为plugins中的两个文件available.py和chat.py配置服务器ip<br/>
> 5.将plugins放入Nonebot2项目文件的plugins文件夹并启动机器人<br/>
>
> 
### 参考网站
 ##### CSDN **python开发API接口** 作者：默金……<http://t.csdn.cn/ZPJ2X><br/>
 ##### 简书 **OPENAI KEY gpt-3.5-turbo-0301 上下文 python应用举例 import openai** 作者：诸老师 <https://www.jianshu.com/p/6b05c3329870><br/>
 ##### CSDN **Python笔记-从配置读取参数** 作者：DBA大董  <http://t.csdn.cn/4lWjl>


<figure>
  <blockquote>
  这是Stel2ari的第一条Public提交，是一个新的开始
  </blockquote>
  <figcaption>
    
  </figcaption>
</figure>
