# UPDATE

[点击此处打开中文版 UPDATE](./UPDATE.zh-CN.md)

## 2020.01.27

- Update version number to 2.01
- Add function to change the output image mode
- Optimize the logic when the multiple factor is 1

## 2018.10.09

- Update version number to 2.0
- Add Chinese README and UPDATE
- Add a progress bar

## 2018.10.08

In the ImageConverter.py:

- Add ```pool.close()```
- Move ```Image.MAX_IMAGE_PIXELS = None```
- Rename method ```getQueue()``` to ```getGlobalVariables()```
- Delete global variable ```g_logTextCtrl```, and use it as a parameter of the method ```convertImage()``` and ```convertImages()```
- Delete method ```init()```

In the MianFrame.py:

- According to ImageConverter.py modify the corresponding method

In the LogTextCtrl.py:

- Update method ```AppendLogAuto()```

Others:

- Change the program entry to Start.pyw.
