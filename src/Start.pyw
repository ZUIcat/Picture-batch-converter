import wx

from MainFrame import MainFrame


def main():
    app = wx.App()
    mainFrame = MainFrame(None)
    mainFrame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
