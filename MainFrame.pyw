import os

import wx

import ImageConverter
from ConstantsVariables import C
from LogTextCtrl import LogTextCtrl
from MyDropTarget import MyDropTarget


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        kw["title"] = C.T_MAIN_FRAME
        kw["size"] = C.SI_MAIN_FRAME
        kw["style"] = C.ST_FRAME
        super().__init__(*args, **kw)

        self.panel = wx.Panel(self)

        self.bS_Root = wx.BoxSizer(wx.VERTICAL)
        self.bS_Input = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_Output = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_SET = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_WEBP = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_PNG = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_JPEG = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_LOG = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_Button = wx.BoxSizer(wx.HORIZONTAL)
        self.bS_Root.Add(self.bS_Input)
        self.bS_Root.Add(self.bS_Output)
        self.bS_Root.Add(self.bS_SET)
        self.bS_Root.Add(self.bS_WEBP)
        self.bS_Root.Add(self.bS_PNG)
        self.bS_Root.Add(self.bS_JPEG)
        self.bS_Root.Add(self.bS_LOG)
        self.bS_Root.Add(self.bS_Button)

        self.sT_Input = wx.StaticText(self.panel, label=C.LST_INPUT, size=C.SI_DEFAULT)
        self.tC_Input = wx.TextCtrl(self.panel, size=C.SI_MAX)
        self.tC_Input.SetHint(C.HTC_INPUT)
        self.bS_Input.Add(self.sT_Input, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_Input.Add(self.tC_Input, flag=wx.ALL, border=C.B_DEFAULT)
        self.tC_Input.Bind(wx.EVT_TEXT, self.optionChanged)

        self.sT_Output = wx.StaticText(self.panel, label=C.LST_OUTPUT, size=C.SI_DEFAULT)
        self.tC_Output = wx.TextCtrl(self.panel, size=C.SI_MAX)
        self.tC_Output.SetHint(C.HTC_OUTPUT)
        self.bS_Output.Add(self.sT_Output, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_Output.Add(self.tC_Output, flag=wx.ALL, border=C.B_DEFAULT)

        self.sT_Multiple = wx.StaticText(self.panel, label=C.LST_MULTIPLE, size=C.SI_DEFAULT)
        self.tC_Multiple = wx.TextCtrl(self.panel, size=(40, C.SI_DEFAULT[1]))
        self.sT_Process = wx.StaticText(self.panel, label=C.LST_PROCESS, size=C.SI_DEFAULT)
        self.tC_Process = wx.TextCtrl(self.panel, size=(40, C.SI_DEFAULT[1]))
        self.c_Filters = wx.Choice(self.panel, size=(130, C.SI_DEFAULT[1]), choices=list(C.FILTERS.keys()))
        self.cB_RGB = wx.CheckBox(self.panel, label=C.LCB_RGB, size=C.SI_DEFAULT)
        self.bS_SET.Add(self.sT_Multiple, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_SET.Add(self.tC_Multiple, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_SET.Add(self.sT_Process, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_SET.Add(self.tC_Process, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_SET.Add(self.c_Filters, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_SET.Add(self.cB_RGB, flag=wx.ALL, border=C.B_DEFAULT)

        self.rB_WEBP = wx.RadioButton(self.panel, label=C.LRB_WEBP, size=(50, C.SI_DEFAULT[1]), style=wx.RB_GROUP)
        self.cB_W_lossless = wx.CheckBox(self.panel, label=C.LCB_W_LOSSLESS, size=(70, C.SI_DEFAULT[1]))
        self.c_W_quality = wx.Choice(self.panel, size=(100, C.SI_DEFAULT[1]), choices=C.CC_W_QUALITY)
        self.c_W_method = wx.Choice(self.panel, size=(100, C.SI_DEFAULT[1]), choices=C.CC_W_METHOD)
        self.bS_WEBP.Add(self.rB_WEBP, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_WEBP.Add(self.cB_W_lossless, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_WEBP.Add(self.c_W_quality, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_WEBP.Add(self.c_W_method, flag=wx.ALL, border=C.B_DEFAULT)
        self.rB_WEBP.Bind(wx.EVT_RADIOBUTTON, self.optionChanged)

        self.rB_PNG = wx.RadioButton(self.panel, label=C.LRB_PNG, size=(50, C.SI_DEFAULT[1]))
        self.cB_P_optimize = wx.CheckBox(self.panel, label=C.LCB_P_OPTIMIZE, size=(70, C.SI_DEFAULT[1]))
        self.bS_PNG.Add(self.rB_PNG, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_PNG.Add(self.cB_P_optimize, flag=wx.ALL, border=C.B_DEFAULT)
        self.rB_PNG.Bind(wx.EVT_RADIOBUTTON, self.optionChanged)

        self.rB_JPEG = wx.RadioButton(self.panel, label=C.LRB_JPEG, size=(50, C.SI_DEFAULT[1]))
        self.cB_J_optimize = wx.CheckBox(self.panel, label=C.LCB_J_OPTIMIZE, size=(70, C.SI_DEFAULT[1]))
        self.c_J_quality = wx.Choice(self.panel, size=(100, C.SI_DEFAULT[1]), choices=C.CC_J_QUALITY)
        self.cB_J_progressive = wx.CheckBox(self.panel, label=C.LCB_J_PROGRESSIVE, size=C.SI_DEFAULT)
        self.bS_JPEG.Add(self.rB_JPEG, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_JPEG.Add(self.cB_J_optimize, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_JPEG.Add(self.c_J_quality, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_JPEG.Add(self.cB_J_progressive, flag=wx.ALL, border=C.B_DEFAULT)
        self.rB_JPEG.Bind(wx.EVT_RADIOBUTTON, self.optionChanged)

        self.lTC_LOG = LogTextCtrl(self.panel, size=(C.SI_MAX[0], C.SI_MAX[1] * 14), )
        self.bS_LOG.Add(self.lTC_LOG, flag=wx.ALL, border=C.B_DEFAULT)

        self.b_Clear = wx.Button(self.panel, label=C.LB_CLEAR, size=C.SI_DEFAULT)
        self.b_Help = wx.Button(self.panel, label=C.LB_HELP, size=C.SI_DEFAULT)
        self.b_Start = wx.Button(self.panel, label=C.LB_START, size=C.SI_DEFAULT)
        self.bS_Button.Add(self.b_Clear, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_Button.Add(self.b_Help, flag=wx.ALL, border=C.B_DEFAULT)
        self.bS_Button.Add(self.b_Start, flag=wx.ALL, border=C.B_DEFAULT)
        self.b_Clear.Bind(wx.EVT_BUTTON, self.buttonClicked)
        self.b_Help.Bind(wx.EVT_BUTTON, self.buttonClicked)
        self.b_Start.Bind(wx.EVT_BUTTON, self.buttonClicked)

        self.tC_Input.SetDropTarget(MyDropTarget(self.tC_Input, self.lTC_LOG))
        self.initSet()
        self.panel.SetSizer(self.bS_Root)
        self.Center()
        ImageConverter.init(self.lTC_LOG)

    def initSet(self):
        #SET
        self.tC_Multiple.SetValue(C.IVTC_MULTIPLE)
        self.tC_Process.SetValue(C.IVTC_PROCESS)
        self.c_Filters.SetSelection(C.ISC_FILTERS)
        self.cB_RGB.SetValue(C.IVCB_RGB)
        #WEBP
        self.rB_WEBP.SetValue(C.IVRB_WEBP)
        self.cB_W_lossless.SetValue(C.IVCB_W_LOSSLESS)
        self.c_W_quality.SetSelection(C.ISC_W_QUALITY)
        self.c_W_method.SetSelection(C.ISC_W_METHOD)
        #PNG
        self.rB_PNG.SetValue(C.IVRB_PNG)
        self.cB_P_optimize.SetValue(C.IVCB_P_OPTIMIZE)
        #JPG
        self.rB_JPEG.SetValue(C.IVRB_JPG)
        self.cB_J_optimize.SetValue(C.IVCB_J_OPTIMIZE)
        self.c_J_quality.SetSelection(C.ISC_J_QUALITY)
        self.cB_J_progressive.SetValue(C.IVCB_J_PROGRESSIVE)

    def optionChanged(self, _):
        pathInput = self.tC_Input.GetValue().strip(" \\\"")
        pathAppend = C.PATH_SUFFIX
        if os.path.isfile(pathInput):
            if self.rB_WEBP.GetValue():
                pathAppend = pathAppend + "." + self.rB_WEBP.GetLabel().lower()
            elif self.rB_PNG.GetValue():
                pathAppend = pathAppend + "." + self.rB_PNG.GetLabel().lower()
            elif self.rB_JPEG.GetValue():
                pathAppend = pathAppend + "." + self.rB_JPEG.GetLabel().lower()
            pathOutput = os.path.splitext(pathInput)[0] + pathAppend
            self.tC_Output.SetValue(pathOutput)
        elif os.path.isdir(pathInput):
            pathOutput = pathInput + pathAppend
            self.tC_Output.SetValue(pathOutput)
        else:
            self.tC_Output.Clear()

    def buttonClicked(self, event):
        if event.GetId() == self.b_Clear.GetId():
            self.lTC_LOG.Clear()
        elif event.GetId() == self.b_Help.GetId():
            self.lTC_LOG.AppendWarning("TODO: 快写帮助页面!\n")
        elif event.GetId() == self.b_Start.GetId():
            pathInput = self.tC_Input.GetValue()
            pathOutput = self.tC_Output.GetValue()

            if os.path.exists(pathOutput):
                self.lTC_LOG.AppendWarning(C.W_OUTPUT_PATH_ALREADY_EXISTS)
                self.lTC_LOG.AppendWarning("TODO: 快改逻辑!\n")
                return

            multiple = float(self.tC_Multiple.GetValue())
            processNum = int(self.tC_Process.GetValue())
            filters = C.FILTERS[self.c_Filters.GetStringSelection()]
            toRGB = self.cB_RGB.GetValue()
            if self.rB_WEBP.GetValue():
                imageFormat = self.rB_WEBP.GetLabel()
                lossless = self.cB_W_lossless.GetValue()
                quality = self.c_W_quality.GetSelection() + 1
                method = self.c_W_method.GetSelection() + 1
                if os.path.isfile(pathInput):
                    ImageConverter.convertImage(
                        imageFormat, pathInput, pathOutput, multiple, filters,
                        toRGB, lossless=lossless, quality=quality, method=method
                    )
                elif os.path.isdir(pathInput):
                    ImageConverter.convertImages(
                        imageFormat, pathInput, pathOutput, multiple, filters,
                        toRGB, processNum, lossless=lossless, quality=quality, method=method
                    )
                else:
                    self.lTC_LOG.AppendError(C.E_INPUT_PATH_NOT_EXIST)
            elif self.rB_PNG.GetValue():
                imageFormat = self.rB_PNG.GetLabel()
                optimize = self.cB_P_optimize.GetValue()
                if os.path.isfile(pathInput):
                    ImageConverter.convertImage(
                        imageFormat, pathInput, pathOutput, multiple, filters,
                        toRGB, optimize=optimize
                    )
                elif os.path.isdir(pathInput):
                    ImageConverter.convertImages(
                        imageFormat, pathInput, pathOutput, multiple, filters,
                        toRGB, processNum, optimize=optimize
                    )
                else:
                    self.lTC_LOG.AppendError(C.E_INPUT_PATH_NOT_EXIST)
            else:
                imageFormat = self.rB_JPEG.GetLabel()
                optimize = self.cB_J_optimize.GetValue()
                quality = self.c_J_quality.GetSelection() + 1
                progressive = self.cB_J_progressive.GetValue()
                if os.path.isfile(pathInput):
                    ImageConverter.convertImage(
                        imageFormat, pathInput, pathOutput, multiple, filters,
                        toRGB, optimize=optimize, quality=quality, progressive=progressive
                    )
                elif os.path.isdir(pathInput):
                    ImageConverter.convertImages(
                        imageFormat, pathInput, pathOutput, multiple, filters,
                        toRGB, processNum, optimize=optimize, quality=quality, progressive=progressive
                    )
                else:
                    self.lTC_LOG.AppendError(C.E_INPUT_PATH_NOT_EXIST)


def main():
    app = wx.App()
    mainFrame = MainFrame(None)
    mainFrame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
