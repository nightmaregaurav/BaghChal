"""
	BaghChal
"""


import math
import os
import sys
from datetime import datetime
from platform import system

from PyQt5.QtCore import QRect, Qt, QTimer
from PyQt5.QtGui import QPen, QPainter, QMouseEvent
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QVBoxLayout, QHBoxLayout, QFrame, QLCDNumber, \
	QApplication, QGridLayout, QPushButton, QFileDialog, QMessageBox

__author__ = "NightmareGaurav"
__version__ = 1.0


# noinspection PyUnusedLocal
class Window(QWidget):
	# noinspection PyUnresolvedReferences
	def __init__(self):
		# Variables Or Constants
		self.selection = (None, 9, 9, "")
		self.game_buffer = list()
		self.init_game_struct = {
			"G_S": 20,
			"G_F": 0,
			"D_G": 0,
			"TIM": 0,
			"MOV": 0,
			"TUR": "Goat's",
			"STA": "Saved",
			"POS": [["*", ".", ".", ".", "*"], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], ["*", ".", ".", ".", "*"]]
		}
		self.game_struct = {
			"G_S": 20,
			"G_F": 0,
			"D_G": 0,
			"TIM": 0,
			"MOV": 0,
			"TUR": "Goat's",
			"STA": "Saved",
			"POS": [["*", ".", ".", ".", "*"], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", ".", ".", ".", "."], ["*", ".", ".", ".", "*"]]
		}
		self.graph = [[[15, 15], [182.5, 15], [350, 15], [517.5, 15], [685, 15]], [[15, 182.5], [182.5, 182.5], [350, 182.5], [517.5, 182.5], [685, 182.5]], [[15, 350], [182.5, 350], [350, 350], [517.5, 350], [685, 350]], [[15, 517.5], [182.5, 517.5], [350, 517.5], [517.5, 517.5], [685, 517.5]], [[15, 685], [182.5, 685.5], [350, 685], [517.5, 685], [685, 685]]]

		# Main Window Attributes
		QWidget.__init__(self)
		self.setFixedSize(1000, 720)
		self.setWindowTitle("BaghChal")
		screen_size = QDesktopWidget().screenGeometry(-1)
		self.move(int((screen_size.width() - self.width()) / 2), int((screen_size.height() - self.height()) / 2))

		# Score & Status Frame
		frame1 = QFrame(self)
		temp_x = 260
		temp_y = 430
		temp_t = (self.height() - temp_y) / 2
		frame1.setGeometry(QRect(730, int(temp_t), temp_x, temp_y))
		frame1.setContextMenuPolicy(Qt.NoContextMenu)
		frame1.setFrameShape(QFrame.StyledPanel)
		frame1.setFrameShadow(QFrame.Sunken)

		vertical_layout1 = QVBoxLayout(frame1)

		horizontal_layout1 = QHBoxLayout()
		label1 = QLabel()
		label1.setText("Goats in Stock:")
		horizontal_layout1.addWidget(label1)
		horizontal_layout1.addStretch(0)
		self.lcdNumber1 = QLCDNumber()
		self.lcdNumber1.setMode(QLCDNumber.Dec)
		self.lcdNumber1.setStyleSheet("background-color: green;")
		horizontal_layout1.addWidget(self.lcdNumber1)
		vertical_layout1.addLayout(horizontal_layout1)

		line1 = QFrame()
		line1.setFrameShape(QFrame.HLine)
		line1.setFrameShadow(QFrame.Sunken)
		vertical_layout1.addWidget(line1)

		horizontal_layout2 = QHBoxLayout()
		label2 = QLabel()
		label2.setText("Goats In Field:")
		horizontal_layout2.addWidget(label2)
		horizontal_layout2.addStretch(0)
		self.lcdNumber2 = QLCDNumber()
		self.lcdNumber2.setMode(QLCDNumber.Dec)
		self.lcdNumber2.setStyleSheet("background-color: yellow;")
		horizontal_layout2.addWidget(self.lcdNumber2)
		vertical_layout1.addLayout(horizontal_layout2)

		line2 = QFrame()
		line2.setFrameShape(QFrame.HLine)
		line2.setFrameShadow(QFrame.Sunken)
		vertical_layout1.addWidget(line2)

		horizontal_layout3 = QHBoxLayout()
		label3 = QLabel()
		label3.setText("Dead Goats:")
		horizontal_layout3.addWidget(label3)
		horizontal_layout3.addStretch(0)
		self.lcdNumber3 = QLCDNumber()
		self.lcdNumber3.setMode(QLCDNumber.Dec)
		self.lcdNumber3.setStyleSheet("background-color: red;")
		horizontal_layout3.addWidget(self.lcdNumber3)
		vertical_layout1.addLayout(horizontal_layout3)

		line3 = QFrame()
		line3.setFrameShape(QFrame.HLine)
		line3.setFrameShadow(QFrame.Sunken)
		vertical_layout1.addWidget(line3)

		vertical_layout1.addStretch(0)
		grid_layout = QGridLayout()
		button1 = QPushButton()
		button1.setText("Save")
		button1.clicked.connect(self.save)
		grid_layout.addWidget(button1, 0, 0)
		self.button2 = QPushButton()
		self.button2.setText("Undo")
		self.button2.clicked.connect(self.undo)
		grid_layout.addWidget(self.button2, 1, 0)
		button3 = QPushButton()
		button3.setText("Load")
		button3.clicked.connect(self.load)
		grid_layout.addWidget(button3, 0, 1)
		button4 = QPushButton()
		button4.setText("Restart")
		button4.clicked.connect(self.restart)
		grid_layout.addWidget(button4, 1, 1)
		vertical_layout1.addLayout(grid_layout)
		vertical_layout1.addStretch(0)

		line4 = QFrame()
		line4.setFrameShape(QFrame.HLine)
		line4.setFrameShadow(QFrame.Sunken)
		vertical_layout1.addWidget(line4)

		horizontal_layout4 = QHBoxLayout()
		label4 = QLabel()
		label4.setText("Time:")
		horizontal_layout4.addWidget(label4)
		horizontal_layout4.addStretch(0)
		self.lcdNumber4 = QLCDNumber()
		self.lcdNumber4.setMode(QLCDNumber.Dec)
		self.lcdNumber4.setStyleSheet("background-color: black;")
		horizontal_layout4.addWidget(self.lcdNumber4)
		vertical_layout1.addLayout(horizontal_layout4)

		line5 = QFrame()
		line5.setFrameShape(QFrame.HLine)
		line5.setFrameShadow(QFrame.Sunken)
		vertical_layout1.addWidget(line5)

		horizontal_layout5 = QHBoxLayout()
		label5 = QLabel()
		label5.setText("Moves:")
		horizontal_layout5.addWidget(label5)
		horizontal_layout5.addStretch(0)
		self.lcdNumber5 = QLCDNumber()
		self.lcdNumber5.setMode(QLCDNumber.Dec)
		self.lcdNumber5.setStyleSheet("background-color: black;")
		horizontal_layout5.addWidget(self.lcdNumber5)
		vertical_layout1.addLayout(horizontal_layout5)

		line6 = QFrame()
		line6.setFrameShape(QFrame.HLine)
		line6.setFrameShadow(QFrame.Sunken)
		vertical_layout1.addWidget(line6)

		horizontal_layout6 = QHBoxLayout()
		label6 = QLabel()
		label6.setText("Turn & Status:")
		horizontal_layout6.addWidget(label6)
		horizontal_layout6.addStretch(0)
		self.label7 = QLabel()
		self.label7.setText("Goat's")
		horizontal_layout6.addWidget(self.label7)
		self.label8 = QLabel()
		self.label8.setText("Saved")
		horizontal_layout6.addWidget(self.label8)
		vertical_layout1.addLayout(horizontal_layout6)

		# Playground
		self.frame2 = QFrame(self)
		temp_x = 700
		temp_y = 700
		temp_t = (self.height() - temp_y) / 2
		self.frame2.setGeometry(QRect(10, int(temp_t), temp_x, temp_y))
		self.frame2.setContextMenuPolicy(Qt.NoContextMenu)
		self.frame2.setFrameShape(QFrame.StyledPanel)
		self.frame2.setFrameShadow(QFrame.Sunken)
		self.frame2_def_paintEvent = self.frame2.paintEvent
		self.frame2.paintEvent = self.frame2_paintEvent
		self.positions = list()
		j = 0
		for item in self.graph:
			k = 0
			temp_list = list()
			for i in item:
				position = QLabel(self.frame2)
				position.setGeometry(QRect(int(i[0] - 12.4), int(i[1] - 12.4), 25, 25))
				position.setObjectName(str(j)+" "+str(k))
				position.mousePressEvent = self.position_clicked
				temp_list.append(position)
				k += 1
			self.positions.append(temp_list)
			j += 1
		self.paint_game()
		self.timer = QTimer()
		self.timer.timeout.connect(self.time)
		self.timer.start(1000)

	def paint_game(self, stat_only=False):
		self.lcdNumber1.display(self.game_struct.get("G_S"))
		self.lcdNumber2.display(self.game_struct.get("G_F"))
		self.lcdNumber3.display(self.game_struct.get("D_G"))
		self.lcdNumber4.display(self.game_struct.get("TIM"))
		self.lcdNumber5.display(self.game_struct.get("MOV"))
		self.label7.setText(self.game_struct.get("TUR"))
		self.label8.setText(self.game_struct.get("STA"))
		if len(self.game_buffer) <= 1:
			self.button2.setDisabled(True)
		else:
			self.button2.setDisabled(False)
		if stat_only:
			return
		i = 0
		for rows in self.game_struct.get("POS"):
			j = 0
			for item in rows:
				if item == "*":
					self.positions[i][j].setStyleSheet("border-radius:12.4; background-color: rgb(255, 0, 0);")
				elif item == "@":
					self.positions[i][j].setStyleSheet("border-radius:12.4; background-color: rgb(255, 255, 0);")
				else:
					self.positions[i][j].setStyleSheet("")
				j += 1
			i += 1

	# noinspection PyMethodMayBeStatic
	def position_clicked(self, event: QMouseEvent):
		if event.buttons().__int__() == 1:
			cx, cy = self.detect_click(event.windowPos().x()-10, event.windowPos().y()-12)
			if cx > 4 or cy > 4:
				return
			label = self.positions[cx][cy]
			if self.game_struct.get("G_S") > 0 and self.game_struct.get("TUR") == "Goat's" and label.styleSheet() != "":
				self.err_box("Place All Goats From Stock In Field First.")
				return
			elif self.game_struct.get("G_S") > 0 and self.game_struct.get("TUR") == "Goat's" and label.styleSheet() == "":
				ret = self.moved(0, 0, cx, cy)
				if not ret[0]:
					self.err_box(ret[1])
				return
			if self.game_struct.get("TUR") == "Goat's" and label.styleSheet() == "border-radius:12.4; background-color: rgb(255, 0, 0);":
				return
			if self.game_struct.get("TUR") == "Tiger's" and label.styleSheet() == "border-radius:12.4; background-color: rgb(255, 255, 0);":
				return
			elif label.styleSheet() != "":
				if self.selection[0]:
					self.selection[0].setStyleSheet(self.selection[3])
				self.selection = (label, cx, cy, label.styleSheet())
				label.setStyleSheet("border-radius:12.4; background-color: rgb(255, 255, 255);")
			elif label.styleSheet() == "" and self.selection[0] is not None:
				ret = self.moved(self.selection[1], self.selection[2], cx, cy)
				if not ret[0]:
					self.err_box(ret[1])
					return
				self.selection = (None, 9, 9, "")

	# noinspection PyMethodMayBeStatic
	def err_box(self, string):
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Critical)
		msg.setText("Error!")
		msg.setInformativeText(string)
		msg.setWindowTitle("Error")
		msg.setStandardButtons(QMessageBox.Ok)
		msg.exec_()

	def add(self, i, j, item):
		old = self.game_struct.get("POS")
		old[i][j] = item
		self.game_struct["POS"] = old
		self.paint_game()

	def remove(self, i, j):
		old = self.game_struct.get("POS")
		old[i][j] = "."
		self.game_struct["POS"] = old
		self.paint_game()

	def save(self, e):
		if system() == r"Windows":
			ps = '\\'
		else:
			ps = '/'
		path = r"BaghChal_Saved" + ps
		if not os.path.exists(path):
			os.mkdir(path)
		filename = datetime.now().strftime("%Y%m%d%H%M%S%f") + ".BaghChal_Saved"
		pos = ""
		for i in self.game_struct.get("POS"):
			for j in i:
				pos += j
		txt = "G_S\t" + str(self.game_struct.get("G_S")) + "\nG_F\t" + str(self.game_struct.get("G_F")) + "\nD_G\t" + str(self.game_struct.get("D_G")) + "\nTIM\t" + str(self.game_struct.get("TIM")) + "\nMOV\t" + str(self.game_struct.get("MOV")) + "\nTUR\t" + str(self.game_struct.get("TUR")) + "\nSTA\tNONE" + "\nPOS\t" + pos
		if e == "auto":
			return txt
		with open(r"{0}{2}{1}".format(path, filename, ps), "w") as file:
			file.write(txt)
			file.close()
		self.game_struct["STA"] = "Saved"
		self.paint_game()

	def load(self, e):
		if system() == r"Windows":
			ps = '\\'
		else:
			ps = '/'

		dlg = QFileDialog()
		dlg.setFileMode(QFileDialog.AnyFile)
		if dlg.exec_():
			file = dlg.selectedFiles()[0]
			if not os.path.exists(file):
				return
			# noinspection PyBroadException
			try:
				with open(file) as file:
					val = file.read()
					file.close()
					self.parse_struct(val)
					self.game_struct["STA"] = "Saved"
					self.paint_game()
			except Exception:
				pass

	def parse_struct(self, val):
		val = list(map(lambda x: x.split("\t"), val.split("\n")))
		temp = list()
		for items in val:
			temp.append(items[0])
		if temp == list(self.game_struct.keys()):
			for items in val:
				if items[0] == 'POS':
					a = list(items[1][:5])
					b = list(items[1][5:10])
					c = list(items[1][10:15])
					d = list(items[1][15:20])
					e = list(items[1][20:25])
					self.game_struct[items[0]] = [a, b, c, d, e]
				elif items[0] not in ['TUR', 'STA']:
					self.game_struct[items[0]] = int(items[1])
				else:
					self.game_struct[items[0]] = items[1]

	def restart(self, e):
		self.game_struct = self.init_game_struct
		self.paint_game()

	def moved(self, sx, sy, dx, dy):
		s_pos = sx * 10 + sy
		d_pos = dx * 10 + dy
		if self.positions[dx][dy].styleSheet() != "":
			return [False, "Destination Field Is Not Empty."]
		if self.game_struct.get("TUR") == "Goat's" and self.game_struct.get("G_S") == 0:
			if (sx+sy) % 2 != 0:
				if d_pos not in [s_pos-1, s_pos+1, s_pos-10, s_pos+10]:
					return [False, "Destination Field Has Invalid Path."]
			else:
				if d_pos not in [s_pos-1, s_pos+1, s_pos-10, s_pos+10, s_pos-11, s_pos-9, s_pos+11, s_pos+9]:
					return [False, "Destination Field Has Invalid Path."]
			self.add(dx, dy, "@")
			self.remove(sx, sy)
			self.game_struct["MOV"] += 1
		elif self.game_struct.get("TUR") == "Goat's" and self.game_struct.get("G_S") != 0:
			self.add(dx, dy, "@")
			self.game_struct["MOV"] += 1
			self.game_struct["G_F"] += 1
			self.game_struct["G_S"] -= 1
		else:
			if (sx+sy) % 2 != 0:
				if d_pos not in [s_pos-1, s_pos+1, s_pos-10, s_pos+10, s_pos+2, s_pos-2, s_pos+20, s_pos-20]:
					return [False, "Destination Field Has Invalid Path."]
			else:
				if d_pos not in [s_pos-1, s_pos+1, s_pos-10, s_pos+10, s_pos-11, s_pos-9, s_pos+11, s_pos+9, s_pos+2, s_pos-2, s_pos+20, s_pos-20, s_pos+18, s_pos-18, s_pos+22, s_pos-22]:
					return [False, "Destination Field Has Invalid Path."]
			if d_pos not in [s_pos+2, s_pos-2, s_pos+20, s_pos-20, s_pos+18, s_pos-18, s_pos+22, s_pos-22]:
				self.add(dx, dy, "*")
				self.remove(sx, sy)
				self.game_struct["MOV"] += 1
			else:
				n = int((s_pos + d_pos)/2)
				nx = n // 10
				ny = n % 10
				if self.positions[nx][ny].styleSheet() != "border-radius:12.4; background-color: rgb(255, 255, 0);":
					return [False, "Can't Jump, No Goat To Eat For Energy."]
				else:
					self.add(dx, dy, "*")
					self.remove(nx, ny)
					self.remove(sx, sy)
					self.game_struct["MOV"] += 1
					self.game_struct["D_G"] += 1
					self.game_struct["G_F"] -= 1
		if self.game_struct.get("TUR") == "Goat's":
			self.game_struct["TUR"] = "Tiger's"
		else:
			self.game_struct["TUR"] = "Goat's"
		self.game_struct["STA"] = "Unsaved"
		self.paint_game()
		self.game_buffer.insert(0, self.save("auto"))
		return [True, ]

	def time(self):
		self.lcdNumber5.display(self.lcdNumber5.value() + 1)
		self.game_struct["TIM"] += 1
		self.game_struct["STA"] = "Unsaved"
		self.paint_game(True)

	def detect_click(self, x, y):
		i = 0
		for rows in self.graph:
			j = 0
			for cord in rows:
				if math.sqrt(math.pow(cord[0]-x, 2) + math.pow(cord[1]-y, 2)) <= 12.4:
					return i, j
				j += 1
			i += 1
		return 9, 9

	# noinspection PyPep8Naming
	def frame2_paintEvent(self, event):
		self.frame2_def_paintEvent(event)
		painter = QPainter(self.frame2)
		pen = QPen()
		pen.setColor(Qt.black)
		pen.setWidth(3)
		painter.setPen(pen)
		# Outer Rect
		painter.drawRect(14, 14, 671, 671)
		# Main Diamond
		painter.drawLine(350, 15, 685, 350)
		painter.drawLine(685, 350, 350, 685)
		painter.drawLine(350, 685, 15, 350)
		painter.drawLine(15, 350, 350, 15)
		# Main Diagonals
		painter.drawLine(15, 15, 685, 685)
		painter.drawLine(15, 685, 685, 15)
		# For Dividing Outer Rect
		painter.drawLine(350, 15, 350, 685)
		painter.drawLine(685, 350, 15, 350)
		# For Cols
		painter.drawLine(int(182.5), 15, int(182.5), 685)
		painter.drawLine(int(517.5), 15, int(517.5), 685)
		# For Rows
		painter.drawLine(15, int(182.5), 685, int(182.5))
		painter.drawLine(15, int(517.5), 685, int(517.5))

	def undo(self):
		if len(self.game_buffer) > 1:
			self.parse_struct(self.game_buffer.pop(1))
		self.paint_game()
		self.button2.setDisabled(True)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
