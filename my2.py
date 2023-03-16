
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(66, 115)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 37)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1_Click
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(229, 215)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 1
		self._checkBox1.Text = "checkBox1"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(42, 214)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 2
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "radioButton1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(90, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(332, 291)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._button1)
		self.ForeColor = System.Drawing.SystemColors.ControlDark
		self.Name = "Form1"
		self.Text = "Form_my"
		self.ResumeLayout(False)


	def Button1_Click(self, sender, e):
		print("command")