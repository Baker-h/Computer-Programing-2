import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Transparent
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(144, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Length:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Transparent
		self._label2.Location = System.Drawing.Point(12, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(144, 37)
		self._label2.TabIndex = 1
		self._label2.Text = "Width:"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Brown
		self._label3.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Transparent
		self._label3.Location = System.Drawing.Point(12, 125)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(394, 37)
		self._label3.TabIndex = 2
		self._label3.Text = "Area:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Brown
		self._label4.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Transparent
		self._label4.Location = System.Drawing.Point(12, 172)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(394, 37)
		self._label4.TabIndex = 3
		self._label4.Text = "Perimiter:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DimGray
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(11, 223)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(109, 84)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DimGray
		self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(159, 223)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(109, 84)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DimGray
		self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button3.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(311, 223)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(109, 84)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(99, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(211, 20)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(99, 60)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(211, 20)
		self._textBox2.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(432, 324)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Program54A"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label3.Text = "Area: " + str(area)
		self._label4.Text = "Perimiter " + str(perim)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = "Area:"
		self._label4.Text = "Perimiter:"

	def Button3Click(self, sender, e):
		Application.Exit()