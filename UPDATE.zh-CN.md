# UPDATE

[Click here to open the English UPDATE](./UPDATE.md)

## 2020.01.27

- 版本号更新为 2.01
- 添加了更改输出图像模式的功能
- 优化了当缩小倍数为1时的逻辑

## 2018.10.09

- 版本号更新为 2.0
- 添加了中文 README 和中文 UPDATE
- 添加了进度条

## 2018.10.08

在 ImageConverter.py 中:

- 添加了 ```pool.close()```
- 移动了 ```Image.MAX_IMAGE_PIXELS = None```
- 将方法 ```getQueue()``` 更名为 ```getGlobalVariables()```
- 删除全局变量 ```g_logTextCtrl```, 并将其作为 ```convertImage()``` 和 ```convertImages()``` 方法的一个参数
- 删除方法 ```init()```

在 MianFrame.py 中:

- 根据 ImageConverter.py 中的变化修改对应的方法

在 the LogTextCtrl.py 中:

- 更新方法 ```AppendLogAuto()```

其它:

- 将程序的入口改为 Start.pyw
