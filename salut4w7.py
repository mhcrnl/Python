import  wx
 
class ExampleApp(wx.Frame):
    def __init__(self):
        # Every wx app must create one App object
        # before it does anything else using wx.
        self.app = wx.App()
 
        # Set up the main window
        wx.Frame.__init__(self,
                          parent=None,
                          title='wxPython Example',
                          size=(300, 200))
 
        # The greetings available
        self.greetings = ['hello', 'goodbye', 'heyo']
 
        # Layout panel and hbox
        self.panel = wx.Panel(self, size=(300, 200))
        self.box = wx.BoxSizer(wx.VERTICAL)
 
        # Greeting combobox
        self.greeting = wx.ComboBox(parent=self.panel,
                                    value='hello',
                                    size=(280, -1),
                                    choices=self.greetings)
 
        # Add the greeting combo to the hbox
        self.box.Add(self.greeting, 0, wx.TOP)
        self.box.Add((-1, 10))
 
        # Recipient entry
        self.recipient = wx.TextCtrl(parent=self.panel,
                                     size=(280, -1),
                                     value='world')
 
        # Add the greeting combo to the hbox
        self.box.Add(self.recipient, 0, wx.TOP)
 
        # Add padding to lower the button position
        self.box.Add((-1, 100))
 
        # The go button
        self.go_button = wx.Button(self.panel, 10, '&Go')
 
        # Bind an event for the button
        self.Bind(wx.EVT_BUTTON, self.print_result, self.go_button)
 
        # Make the button the default action for the form
        self.go_button.SetDefault()
 
        # Add the button to the hbox
        self.box.Add(self.go_button, 0, flag=wx.ALIGN_RIGHT|wx.BOTTOM)
 
        # Tell the panel to use the hbox
        self.panel.SetSizer(self.box)
 
    def print_result(self, *args):
        ''' Print a greeting constructed from
            the selections made by the user. '''
        print('%s, %s!' % (self.greeting.GetValue().title(),
                           self.recipient.GetValue()))
 
    def run(self):
        ''' Run the app '''
        self.Show()
        self.app.MainLoop()
 
# Instantiate and run
app = ExampleApp()
app.run()