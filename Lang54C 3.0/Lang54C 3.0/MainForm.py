import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.AntiqueWhite
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("PMingLiU-ExtB", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(45, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(162, 28)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.AntiqueWhite
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("PMingLiU-ExtB", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(45, 98)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(162, 28)
		self._label3.TabIndex = 2
		self._label3.Text = "Area:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.AntiqueWhite
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("PMingLiU-ExtB", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(45, 183)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(162, 28)
		self._label4.TabIndex = 3
		self._label4.Text = """Circumfrence:
"""
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# textBox1
		# 
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.Font = System.Drawing.Font("Poor Richard", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(259, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(166, 29)
		self._textBox1.TabIndex = 4
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.BurlyWood
		self._button1.Font = System.Drawing.Font("MS UI Gothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 253)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(133, 59)
		self._button1.TabIndex = 5
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.BurlyWood
		self._button2.Font = System.Drawing.Font("MS UI Gothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(180, 253)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(133, 59)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.BurlyWood
		self._button3.Font = System.Drawing.Font("MS UI Gothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(348, 253)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(133, 59)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Orange
		self.ClientSize = System.Drawing.Size(484, 324)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang54C 3.0"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		pi = 3.14159
        radius = float(self._textBox1.Text)
        area = pi * radius ** 2  # round area to 3 decimal places
        round(radius, 3)
        round(area, 3)
        (area  * radius**2)
        circumference = pi * radius
        
        self._label1.Text = str(radius)
        self._label2.Text = str(area)
        self._label3.Text = str(circumference)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()
