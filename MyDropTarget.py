import wx

from ConstantsVariables import C


class MyDropTarget(wx.FileDropTarget):
    def __init__(self, textCtrl, logTextCtrl):
        super().__init__()
        self.textCtrl = textCtrl
        self.logTextCtrl = logTextCtrl

    def OnDropFiles(self, _, __, fileNames):
        if len(fileNames) == 1:
            self.textCtrl.SetValue(fileNames[0])
            return True
        else:
            self.logTextCtrl.AppendError(C.E_INPUT_PATH_MULTIPLE)
            return False
