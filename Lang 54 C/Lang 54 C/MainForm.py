from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MistyRose
        self._button1.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 381)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(138, 58)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MistyRose
        self._button2.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(156, 381)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(155, 58)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MistyRose
        self._button3.Font = System.Drawing.Font("MS PGothic", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(317, 381)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(138, 58)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MistyRose
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(123, 205)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(318, 34)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MistyRose
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(123, 255)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(318, 34)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MistyRose
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(123, 305)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(318, 34)
        self._label3.TabIndex = 5
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.RosyBrown
        self._label4.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 205)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(95, 34)
        self._label4.TabIndex = 6
        self._label4.Text = "Radius:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.RosyBrown
        self._label5.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 255)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(95, 34)
        self._label5.TabIndex = 7
        self._label5.Text = "Area:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.RosyBrown
        self._label6.Font = System.Drawing.Font("Papyrus", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 306)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(95, 34)
        self._label6.TabIndex = 8
        self._label6.Text = "Circumference:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(100, 42)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(274, 20)
        self._textBox1.TabIndex = 9
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SeaShell
        self.ClientSize = System.Drawing.Size(467, 451)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Lang 54 c"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


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

    def MainFormLoad(self, sender, e):
        pass