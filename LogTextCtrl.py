import wx


class LogTextCtrl(wx.TextCtrl):
    COLOR_BK = (40, 40, 50)
    COLOR_LOG = (100, 185, 245)
    COLOR_ERROR = (225, 60, 60)
    COLOR_WARNING = (245, 245, 70)
    ID_LOG = "<"
    ID_WARNING = ">"
    ID_ERROR = "*"


    def __init__(self, *args, **kw):
        if "style" not in kw.keys():
            kw["style"] = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2
        else:
            kw["style"] = kw.get("style") | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2
        super().__init__(*args, **kw)

        self.c_Bk = kw.get("colorBk", LogTextCtrl.COLOR_BK)
        self.c_Log = kw.get("colorLog", LogTextCtrl.COLOR_LOG)
        self.c_Error = kw.get("colorError", LogTextCtrl.COLOR_ERROR)
        self.c_Warning = kw.get("colorWarning", LogTextCtrl.COLOR_WARNING)

        self.SetBackgroundColour(self.c_Bk)
        self.SetDefaultStyle(wx.TextAttr(wx.NullColour, font=wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, faceName="微软雅黑")))

    def AppendLog(self, logText):
        self.SetDefaultStyle(wx.TextAttr(self.c_Log))
        self.AppendText(logText)

    def AppendError(self, errorText):
        self.SetDefaultStyle(wx.TextAttr(self.c_Error))
        self.AppendText(errorText)

    def AppendWarning(self, warningText):
        self.SetDefaultStyle(wx.TextAttr(self.c_Warning))
        self.AppendText(warningText)

    def AppendLogAuto(self, *autoText):
        for text in autoText:
            if isinstance(text, tuple):
                self.AppendLogAuto(*text)
                return

            if text.startswith(LogTextCtrl.ID_LOG):
                self.AppendLog(text.lstrip(LogTextCtrl.ID_LOG))
            elif text.startswith(LogTextCtrl.ID_WARNING):
                self.AppendWarning(text.lstrip(LogTextCtrl.ID_WARNING))
            elif text.startswith(LogTextCtrl.ID_ERROR):
                self.AppendError(text.lstrip(LogTextCtrl.ID_ERROR))
            else:
                self.AppendText(text)
