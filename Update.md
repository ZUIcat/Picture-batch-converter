# 2018.10.08
In the ImageConverter.py:
+ Add pool.close()
+ Move Image.MAX_IMAGE_PIXELS = None
+ Rename method getQueue() to getGlobalVariables()
+ Delete global variable g_logTextCtrl, and use it as a parameter of the method convertImage() and convertImages()
+ Delete method init()

In the MianFrame.py:
+ According to ImageConverter.py modified the corresponding method

In the LogTextCtrl.py:
+ Update method AppendLogAuto()

Others:
+ Change the program entry to Start.pyw.
