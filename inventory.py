from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
import threading, mysql.connector, time

#Global List
topmain=[]
stkgroup=[]
category=[]
brand=[]

#Main Class
class Ui_MainWindow(QtCore.QObject):

	#Signal Variables [6 Variables]
	stock_signal = pyqtSignal(str,int)
	category_signal = pyqtSignal(str,int)
	item_signal = pyqtSignal(str,int)
	godown_signal = pyqtSignal(str,int)
	unitmeasure_signal = pyqtSignal(str,int)
	brand_signal = pyqtSignal(str,int)

	def __init__(self):
		super().__init__()
		self.cid = 100 #use for testing purpose [get value from main window]

	#Data Fetch From Server & Add to Respective comboBox's [4 Functions] - Thread Functions
	def stkgrpheadcombo(self):
		global topmain
		prelist = ["Electronics", "Jewellery", "Stationary", "IT", "Tourism", "Other"]
		flag = 0
		self.comboBox.clear()
		self.comboBox.addItems(prelist)
		self.comboBox.setCurrentIndex(0)
		while flag<5 and self.threadexitflag:
			try:
				dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
				if dbcon.is_connected():
					query = dbcon.cursor()
					query.execute("SELECT group_under_custom FROM stkgroup WHERE company_id = '%d' and group_under = 'Other';" % (self.cid))
					record = query.fetchall()
					for i in range(len(record)):
						if record[i][0] not in topmain:
							topmain.append(record[i][0])
					self.comboBox.addItems(topmain)
					query.close()
					dbcon.close()
					flag = 5
			except:
				time.sleep(15)
				flag += 1
				continue


	def stkcatcombo3(self):
		global stkgroup
		flag = 0
		self.comboBox_3.addItem("No Data Loaded")
		self.comboBox_5.addItem("No Data Loaded")
		while flag<5 and self.threadexitflag:
			try:
				dbcon = mysql.connector.connect(host = "localhost", database = "profit_plug", user = "root", password = "", port = 3306)
				if dbcon.is_connected():
					query = dbcon.cursor()
					query.execute("SELECT group_name FROM stkgroup WHERE company_id = '%d' ;" % (self.cid))
					record = query.fetchall()
					for i in range(len(record)):
						if record[i][0] not in stkgroup:
							stkgroup.append(record[i][0])
					self.comboBox_3.clear()
					self.comboBox_5.clear()
					self.comboBox_3.addItems(stkgroup)
					self.comboBox_5.addItems(stkgroup)
					query.close()
					dbcon.close()
					flag = 5
			except:
				time.sleep(15)
				flag += 1
				continue


	def brandcombo(self):
		global brand
		flag = 0
		self.comboBox_7.insertItem(0 , "No Data Loaded")
		while flag<5 and self.threadexitflag:
			try:
				dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
				if dbcon.is_connected():
					query = dbcon.cursor()
					query.execute("SELECT brand_name FROM brands WHERE company_id = '%d' ;" % (self.cid))
					record = query.fetchall()
					for i in range(len(record)):
						if record[i][0] not in brand:
							brand.append(record[i][0])
					self.comboBox_7.clear()
					self.comboBox_7.addItems(brand)
					query.close()
					dbcon.close()
					flag = 5
			except:
				time.sleep(15)
				flag += 1
				continue


	def categorycombo(self):
		global category
		flag = 0
		self.comboBox_6.insertItem(0 , "No Data Loaded")
		while flag<5 and self.threadexitflag:
			try:
				dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
				if dbcon.is_connected():
					query = dbcon.cursor()
					query.execute("SELECT category_name FROM stkcategory WHERE company_id = '%d' ;" % (self.cid))
					record = query.fetchall()
					for i in range(len(record)):
						if record[i][0] not in category:
							category.append(record[i][0])
					self.comboBox_6.clear()
					self.comboBox_6.addItems(category)
					query.close()
					dbcon.close()
					flag = 5
			except:
				time.sleep(15)
				flag += 1
				continue


	#Offline ComboBox Management Once Data Loaded [4 Functions] - Thread Functions
	def mainhead(self):
		global topmain
		prelist = ["Electronics" , "Jewellery" , "Stationary" , "IT" , "Tourism" , "Other"]
		self.comboBox.clear()
		self.comboBox.addItems(prelist)
		self.comboBox.addItems(topmain)
		self.comboBox.setCurrentIndex(0)

	def groupcombo(self):
		global stkgroup
		if stkgroup != []:
			self.comboBox_3.clear()
			self.comboBox_5.clear()
			self.comboBox_3.addItems(stkgroup)
			self.comboBox_5.addItems(stkgroup)
		self.comboBox_3.setCurrentIndex(0)
		self.comboBox_5.setCurrentIndex(0)

	def catcombo(self):
		global category
		if category != []:
			self.comboBox_6.clear()
			self.comboBox_6.addItems(category)
		self.comboBox_6.setCurrentIndex(0)

	def brandcom(self):
		global brand
		if brand != []:
			self.comboBox_7.clear()
			self.comboBox_7.addItems(brand)
		self.comboBox_7.setCurrentIndex(0)

	#Cleaning UI Pages - Thread Functions
	def cleanstkgroup(self):
		self.dateEdit.setDate(QtCore.QDate.currentDate())
		self.lineEdit_4.clear()
		self.lineEdit_5.clear()
		self.comboBox_2.setCurrentIndex(0)
		self.lineEdit_5.setDisabled(True)
		self.lineEdit_4.setFocus()

	def cleanstkcategory(self):
		self.dateEdit_2.setDate(QtCore.QDate.currentDate())
		self.lineEdit_2.clear()
		self.comboBox_3.setCurrentIndex(0)
		self.lineEdit_2.setFocus()

	def cleanbrand(self):
		self.lineEdit_22.clear()
		self.lineEdit_23.clear()
		self.lineEdit_23.setFocus()

	def cleanunitmeasure(self):
		self.comboBox_11.setCurrentIndex(0)
		self.comboBox_10.setCurrentIndex(0)
		self.comboBox_9.setCurrentIndex(0)
		self.lineEdit_20.clear()
		self.spinBox_2.setValue(0)

	def cleangodown(self):
		self.dateEdit_4.setDate(QtCore.QDate.currentDate())
		self.lineEdit_18.clear()
		self.lineEdit_18.setFocus()
		self.comboBox_8.setCurrentIndex(0)

	def cleanitems(self):
		self.dateEdit_3.setDate(QtCore.QDate.currentDate())
		self.lineEdit_6.clear()
		self.lineEdit_8.clear()
		self.comboBox_5.setCurrentIndex(0)
		self.comboBox_6.setCurrentIndex(0)
		self.comboBox_7.setCurrentIndex(0)
		self.spinBox.setValue(0)
		self.lineEdit_9.clear()
		self.lineEdit_13.clear()
		self.lineEdit_10.clear()
		self.lineEdit_11.clear()
		self.lineEdit_12.clear()
		self.lineEdit_14.clear()
		self.lineEdit_7.clear()
		self.lineEdit_24.clear()
		self.lineEdit_25.clear()
		self.lineEdit_17.clear()

	#SetupUI Main Functions (4 Thread)
	def setupUi(self, MainWindow):
		self.threadexitflag = True  #Main Variable To Exit Threads Running
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1003, 647)
		MainWindow.setMinimumSize(QtCore.QSize(0, 0))
		MainWindow.setMouseTracking(True)
		MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
		MainWindow.setAutoFillBackground(True)
		MainWindow.setStyleSheet("QFrame{\n"
		                         "background:rgb(248, 255, 185);}\n"
		                         "\n"
		                         "QPushButton{\n"
		                         "background:#03a9f4;\n"
		                         "border-radius:10px;}\n"
		                         "\n"
		                         "\n"
		                         "\n"
		                         "")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 80))
		font = QtGui.QFont()
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.frame.setFont(font)
		self.frame.setStyleSheet("QFrame{\n"
		                         "background:rgb(248, 255, 185);}\n"
		                         "\n"
		                         "QPushButton{\n"
		                         "background:#03a9f4;\n"
		                         "border-radius:10px;}")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label_5 = QtWidgets.QLabel(self.frame)
		self.label_5.setGeometry(QtCore.QRect(270, 10, 490, 61))
		font = QtGui.QFont()
		font.setPointSize(22)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setGeometry(QtCore.QRect(0, 80, 111, 551))
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.Dash_personal_detail = QtWidgets.QPushButton(self.frame_2)
		self.Dash_personal_detail.setGeometry(QtCore.QRect(10, 30, 101, 23))
		self.Dash_personal_detail.setObjectName("Dash_personal_detail")
		self.Dash_com_deatail = QtWidgets.QPushButton(self.frame_2)
		self.Dash_com_deatail.setGeometry(QtCore.QRect(10, 80, 101, 23))
		self.Dash_com_deatail.setObjectName("Dash_com_deatail")
		self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 101, 23))
		self.pushButton_3.setObjectName("pushButton_3")
		self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_4.setGeometry(QtCore.QRect(10, 180, 101, 23))
		self.pushButton_4.setObjectName("pushButton_4")
		self.Dash_setting = QtWidgets.QPushButton(self.frame_2)
		self.Dash_setting.setGeometry(QtCore.QRect(10, 230, 101, 23))
		self.Dash_setting.setObjectName("Dash_setting")
		self.Dash_Log_out = QtWidgets.QPushButton(self.frame_2)
		self.Dash_Log_out.setGeometry(QtCore.QRect(10, 280, 101, 23))
		self.Dash_Log_out.setObjectName("Dash_Log_out")

		#stackedWidget start Here
		self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.stackedWidget.setGeometry(QtCore.QRect(340, 80, 661, 541))
		font = QtGui.QFont()
		font.setUnderline(False)
		self.stackedWidget.setFont(font)
		self.stackedWidget.setAutoFillBackground(False)
		self.stackedWidget.setStyleSheet("QFrame{\n"
		                                 "background:rgb(248, 255, 185);}\n"
		                                 "\n"
		                                 "QPushButton{\n"
		                                 "background:#03a9f4;\n"
		                                 "border-radius:10px;}")
		self.stackedWidget.setObjectName("stackedWidget")


		#Stock Group Page
		self.stockgrppage = QtWidgets.QWidget()
		self.stockgrppage.setObjectName("stockgrppage")
		self.comboBox = QtWidgets.QComboBox(self.stockgrppage)
		self.comboBox.setGeometry(QtCore.QRect(330 , 190 , 211 , 22))
		self.comboBox.setObjectName("comboBox")

		self.headcombo = threading.Thread(target = self.stkgrpheadcombo) #Thread 1
		self.headcombo.start()

		self.label = QtWidgets.QLabel(self.stockgrppage)
		self.label.setGeometry(QtCore.QRect(20 , 80 , 251 , 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.stockgrppage)
		self.label_2.setGeometry(QtCore.QRect(20 , 250 , 251 , 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.comboBox_2 = QtWidgets.QComboBox(self.stockgrppage)
		self.comboBox_2.setGeometry(QtCore.QRect(330 , 310 , 211 , 21))
		self.comboBox_2.setObjectName("comboBox_2")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.label_4 = QtWidgets.QLabel(self.stockgrppage)
		self.label_4.setGeometry(QtCore.QRect(20 , 130 , 251 , 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.stockgrppage)
		self.lineEdit_5.setGeometry(QtCore.QRect(330 , 250 , 211 , 20))
		self.lineEdit_5.setDisabled(True)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_4 = QtWidgets.QLineEdit(self.stockgrppage)
		self.lineEdit_4.setGeometry(QtCore.QRect(330 , 130 , 211 , 20))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.label_3 = QtWidgets.QLabel(self.stockgrppage)
		self.label_3.setGeometry(QtCore.QRect(20 , 190 , 251 , 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label_6 = QtWidgets.QLabel(self.stockgrppage)
		self.label_6.setGeometry(QtCore.QRect(20 , 310 , 301 , 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.dateEdit = QtWidgets.QDateEdit(self.stockgrppage)
		self.dateEdit.setGeometry(QtCore.QRect(330 , 80 , 211 , 22))
		self.dateEdit.setDate(QtCore.QDate.currentDate())
		self.dateEdit.setMaximumDate(QtCore.QDate(7999 , 12 , 31))
		self.dateEdit.setCalendarPopup(True)
		self.dateEdit.setObjectName("dateEdit")
		self.pushButton_9 = QtWidgets.QPushButton(self.stockgrppage)
		self.pushButton_9.setGeometry(QtCore.QRect(440 , 430 , 101 , 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_9.setFont(font)
		self.pushButton_9.setObjectName("pushButton_9")
		self.label_7 = QtWidgets.QLabel(self.stockgrppage)
		self.label_7.setGeometry(QtCore.QRect(270 , 440 , 151 , 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")
		self.stackedWidget.addWidget(self.stockgrppage)


		#Stock Category Page
		self.stockcategorypage = QtWidgets.QWidget()
		self.stockcategorypage.setObjectName("stockcategorypage")
		self.pushButton_10 = QtWidgets.QPushButton(self.stockcategorypage)
		self.pushButton_10.setGeometry(QtCore.QRect(450, 370, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_10.setFont(font)
		self.pushButton_10.setObjectName("pushButton_10")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.stockcategorypage)
		self.lineEdit_2.setGeometry(QtCore.QRect(340, 140, 211, 31))
		self.lineEdit_2.setText("")
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.label_8 = QtWidgets.QLabel(self.stockcategorypage)
		self.label_8.setGeometry(QtCore.QRect(30, 210, 251, 21))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self.stockcategorypage)
		self.label_9.setGeometry(QtCore.QRect(30, 80, 251, 21))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_9.setFont(font)
		self.label_9.setObjectName("label_9")
		self.dateEdit_2 = QtWidgets.QDateEdit(self.stockcategorypage)
		self.dateEdit_2.setGeometry(QtCore.QRect(340, 80, 211, 22))
		self.dateEdit_2.setDate(QtCore.QDate.currentDate())
		self.dateEdit_2.setMaximumDate(QtCore.QDate(7999 , 12 , 31))
		self.dateEdit_2.setCalendarPopup(True)
		self.dateEdit_2.setObjectName("dateEdit_2")
		self.comboBox_3 = QtWidgets.QComboBox(self.stockcategorypage)
		self.comboBox_3.setGeometry(QtCore.QRect(340, 210, 211, 22))
		self.comboBox_3.setObjectName("comboBox_3")
		self.label_11 = QtWidgets.QLabel(self.stockcategorypage)
		self.label_11.setGeometry(QtCore.QRect(30, 140, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_11.setFont(font)
		self.label_11.setObjectName("label_11")
		self.label_21 = QtWidgets.QLabel(self.stockcategorypage)
		self.label_21.setGeometry(QtCore.QRect(270 , 370 , 151 , 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_21.setFont(font)
		self.label_21.setObjectName("label_21")
		self.label_21.setText("Ready -->")
		self.stackedWidget.addWidget(self.stockcategorypage)

		#Stock Item Page 1
		self.stockitem1page = QtWidgets.QWidget()
		self.stockitem1page.setObjectName("stockitem1page")
		self.label_12 = QtWidgets.QLabel(self.stockitem1page)
		self.label_12.setGeometry(QtCore.QRect(50, 140, 250, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_12.setFont(font)
		self.label_12.setObjectName("label_12")
		self.lineEdit_6 = QtWidgets.QLineEdit(self.stockitem1page)
		self.lineEdit_6.setGeometry(QtCore.QRect(360, 140, 211, 20))
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.label_13 = QtWidgets.QLabel(self.stockitem1page)
		self.label_13.setGeometry(QtCore.QRect(50, 260, 250, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_13.setFont(font)
		self.label_13.setObjectName("label_13")
		self.label_14 = QtWidgets.QLabel(self.stockitem1page)
		self.label_14.setGeometry(QtCore.QRect(50, 320, 250, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_14.setFont(font)
		self.label_14.setObjectName("label_14")
		self.comboBox_5 = QtWidgets.QComboBox(self.stockitem1page)
		self.comboBox_5.setGeometry(QtCore.QRect(360, 260, 211, 22))
		self.comboBox_5.setObjectName("comboBox_5")

		self.groupcombothread = threading.Thread(target = self.stkcatcombo3) #Thread 2
		self.groupcombothread.start()

		self.comboBox_6 = QtWidgets.QComboBox(self.stockitem1page)
		self.comboBox_6.setGeometry(QtCore.QRect(360, 320, 211, 22))
		self.comboBox_6.setObjectName("comboBox_6")
		self.label_16 = QtWidgets.QLabel(self.stockitem1page)
		self.label_16.setGeometry(QtCore.QRect(50, 200, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_16.setFont(font)
		self.label_16.setObjectName("label_16")
		self.dateEdit_3 = QtWidgets.QDateEdit(self.stockitem1page)
		self.dateEdit_3.setGeometry(QtCore.QRect(360, 80, 211, 22))
		self.dateEdit_3.setDate(QtCore.QDate.currentDate())
		self.dateEdit_3.setMaximumDate(QtCore.QDate(7999 , 12 , 31))
		self.dateEdit_3.setCalendarPopup(True)
		self.dateEdit_3.setObjectName("dateEdit_3")
		self.label_17 = QtWidgets.QLabel(self.stockitem1page)
		self.label_17.setGeometry(QtCore.QRect(50, 80, 250, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_17.setFont(font)
		self.label_17.setObjectName("label_17")
		self.lineEdit_8 = QtWidgets.QLineEdit(self.stockitem1page)
		self.lineEdit_8.setGeometry(QtCore.QRect(360, 200, 211, 20))
		self.lineEdit_8.setObjectName("lineEdit_8")
		self.label_18 = QtWidgets.QLabel(self.stockitem1page)
		self.label_18.setGeometry(QtCore.QRect(50, 390, 250, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_18.setFont(font)
		self.label_18.setObjectName("label_18")
		self.comboBox_7 = QtWidgets.QComboBox(self.stockitem1page)
		self.comboBox_7.setGeometry(QtCore.QRect(360, 390, 211, 22))
		self.comboBox_7.setObjectName("comboBox_7")

		self.threadcategorycombo = threading.Thread(target = self.categorycombo) #Thread 3
		self.threadcategorycombo.start()

		self.pushButton_11 = QtWidgets.QPushButton(self.stockitem1page)
		self.pushButton_11.setGeometry(QtCore.QRect(470, 470, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_11.setFont(font)
		self.pushButton_11.setObjectName("pushButton_11")
		self.stackedWidget.addWidget(self.stockitem1page)

		#Stock Item Page 2
		self.stockitem2page = QtWidgets.QWidget()
		self.stockitem2page.setObjectName("stockitem2page")
		self.label_19 = QtWidgets.QLabel(self.stockitem2page)
		self.label_19.setGeometry(QtCore.QRect(20, 80, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_19.setFont(font)
		self.label_19.setObjectName("label_19")
		self.label_20 = QtWidgets.QLabel(self.stockitem2page)
		self.label_20.setGeometry(QtCore.QRect(530, 140, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_20.setFont(font)
		self.label_20.setObjectName("label_20")
		self.lineEdit_9 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_9.setGeometry(QtCore.QRect(310, 160, 71, 20))
		self.lineEdit_9.setText("")
		self.lineEdit_9.setObjectName("lineEdit_9")
		self.label_22 = QtWidgets.QLabel(self.stockitem2page)
		self.label_22.setGeometry(QtCore.QRect(20, 140, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_22.setFont(font)
		self.label_22.setAutoFillBackground(False)
		self.label_22.setScaledContents(False)
		self.label_22.setObjectName("label_22")
		self.label_23 = QtWidgets.QLabel(self.stockitem2page)
		self.label_23.setGeometry(QtCore.QRect(530, 210, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_23.setFont(font)
		self.label_23.setObjectName("label_23")
		self.lineEdit_10 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_10.setGeometry(QtCore.QRect(530, 160, 71, 20))
		self.lineEdit_10.setText("")
		self.lineEdit_10.setObjectName("lineEdit_10")
		self.label_24 = QtWidgets.QLabel(self.stockitem2page)
		self.label_24.setGeometry(QtCore.QRect(420, 210, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_24.setFont(font)
		self.label_24.setObjectName("label_24")
		self.label_25 = QtWidgets.QLabel(self.stockitem2page)
		self.label_25.setGeometry(QtCore.QRect(20, 270, 251, 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_25.setFont(font)
		self.label_25.setObjectName("label_25")
		self.lineEdit_11 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_11.setGeometry(QtCore.QRect(530, 230, 71, 20))
		self.lineEdit_11.setText("")
		self.lineEdit_11.setObjectName("lineEdit_11")
		self.label_26 = QtWidgets.QLabel(self.stockitem2page)
		self.label_26.setGeometry(QtCore.QRect(310, 210, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_26.setFont(font)
		self.label_26.setObjectName("label_26")
		self.lineEdit_12 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_12.setGeometry(QtCore.QRect(420, 230, 71, 20))
		self.lineEdit_12.setText("")
		self.lineEdit_12.setObjectName("lineEdit_12")
		self.label_27 = QtWidgets.QLabel(self.stockitem2page)
		self.label_27.setGeometry(QtCore.QRect(310, 140, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_27.setFont(font)
		self.label_27.setObjectName("label_27")
		self.lineEdit_13 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_13.setGeometry(QtCore.QRect(420, 160, 71, 20))
		self.lineEdit_13.setText("")
		self.lineEdit_13.setObjectName("lineEdit_13")
		self.label_28 = QtWidgets.QLabel(self.stockitem2page)
		self.label_28.setGeometry(QtCore.QRect(420, 140, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_28.setFont(font)
		self.label_28.setObjectName("label_28")
		self.lineEdit_14 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_14.setGeometry(QtCore.QRect(310, 230, 71, 20))
		self.lineEdit_14.setText("")
		self.lineEdit_14.setObjectName("lineEdit_14")
		self.label_29 = QtWidgets.QLabel(self.stockitem2page)
		self.label_29.setGeometry(QtCore.QRect(20, 210, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_29.setFont(font)
		self.label_29.setAutoFillBackground(False)
		self.label_29.setScaledContents(False)
		self.label_29.setObjectName("label_29")
		self.lineEdit_17 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_17.setGeometry(QtCore.QRect(310, 340, 291, 20))
		self.lineEdit_17.setObjectName("lineEdit_17")
		self.label_30 = QtWidgets.QLabel(self.stockitem2page)
		self.label_30.setGeometry(QtCore.QRect(20, 340, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_30.setFont(font)
		self.label_30.setObjectName("label_30")
		self.label_10 = QtWidgets.QLabel(self.stockitem2page)
		self.label_10.setGeometry(QtCore.QRect(310, 270, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_10.setFont(font)
		self.label_10.setObjectName("label_10")
		self.label_15 = QtWidgets.QLabel(self.stockitem2page)
		self.label_15.setGeometry(QtCore.QRect(530, 270, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_15.setFont(font)
		self.label_15.setObjectName("label_15")
		self.lineEdit_7 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_7.setGeometry(QtCore.QRect(530, 290, 71, 20))
		self.lineEdit_7.setText("")
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.label_43 = QtWidgets.QLabel(self.stockitem2page)
		self.label_43.setGeometry(QtCore.QRect(420, 270, 61, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_43.setFont(font)
		self.label_43.setObjectName("label_43")
		self.lineEdit_24 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_24.setGeometry(QtCore.QRect(310, 290, 71, 20))
		self.lineEdit_24.setText("")
		self.lineEdit_24.setObjectName("lineEdit_24")
		self.lineEdit_25 = QtWidgets.QLineEdit(self.stockitem2page)
		self.lineEdit_25.setGeometry(QtCore.QRect(420, 290, 71, 20))
		self.lineEdit_25.setText("")
		self.lineEdit_25.setObjectName("lineEdit_25")
		self.spinBox = QtWidgets.QSpinBox(self.stockitem2page)
		self.spinBox.setGeometry(QtCore.QRect(310, 80, 291, 22))
		self.spinBox.setObjectName("spinBox")
		self.pushButton_12 = QtWidgets.QPushButton(self.stockitem2page)
		self.pushButton_12.setGeometry(QtCore.QRect(500, 450, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_12.setFont(font)
		self.pushButton_12.setObjectName("pushButton_12")
		self.label_33 = QtWidgets.QLabel(self.stockitem2page)
		self.label_33.setGeometry(QtCore.QRect(330 , 450 , 151 , 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_33.setFont(font)
		self.label_33.setObjectName("label_33")
		self.label_33.setText("Ready -->")
		self.stackedWidget.addWidget(self.stockitem2page)

		self.threadbrandcombo = threading.Thread(target = self.brandcombo) #Thread 4
		self.threadbrandcombo.start()

		#Godown Page
		self.godownspage = QtWidgets.QWidget()
		self.godownspage.setObjectName("godownspage")
		self.label_31 = QtWidgets.QLabel(self.godownspage)
		self.label_31.setGeometry(QtCore.QRect(40, 150, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_31.setFont(font)
		self.label_31.setObjectName("label_31")
		self.dateEdit_4 = QtWidgets.QDateEdit(self.godownspage)
		self.dateEdit_4.setGeometry(QtCore.QRect(350, 80, 231, 22))
		self.dateEdit_4.setDate(QtCore.QDate.currentDate())
		self.dateEdit_4.setMaximumDate(QtCore.QDate(7999 , 12 , 31))
		self.dateEdit_4.setCalendarPopup(True)
		self.dateEdit_4.setObjectName("dateEdit_4")
		self.comboBox_8 = QtWidgets.QComboBox(self.godownspage)
		self.comboBox_8.setGeometry(QtCore.QRect(350, 210, 231, 22))
		self.comboBox_8.setObjectName("comboBox_8")
		self.comboBox_8.addItem("")
		self.comboBox_8.addItem("")
		self.label_32 = QtWidgets.QLabel(self.godownspage)
		self.label_32.setGeometry(QtCore.QRect(40, 210, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_32.setFont(font)
		self.label_32.setObjectName("label_32")
		self.lineEdit_18 = QtWidgets.QLineEdit(self.godownspage)
		self.lineEdit_18.setGeometry(QtCore.QRect(350, 150, 231, 20))
		self.lineEdit_18.setObjectName("lineEdit_18")
		self.label_34 = QtWidgets.QLabel(self.godownspage)
		self.label_34.setGeometry(QtCore.QRect(40, 81, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_34.setFont(font)
		self.label_34.setObjectName("label_34")
		self.pushButton_13 = QtWidgets.QPushButton(self.godownspage)
		self.pushButton_13.setGeometry(QtCore.QRect(490, 430, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_13.setFont(font)
		self.pushButton_13.setObjectName("pushButton_13")
		self.label_42 = QtWidgets.QLabel(self.godownspage)
		self.label_42.setGeometry(QtCore.QRect(310 , 430 , 161 , 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_42.setFont(font)
		self.label_42.setObjectName("label_42")
		self.label_42.setText("Ready -->")
		self.stackedWidget.addWidget(self.godownspage)

		#Unit Measure Page
		self.unitmeasurepage = QtWidgets.QWidget()
		self.unitmeasurepage.setObjectName("unitmeasurepage")
		self.label_35 = QtWidgets.QLabel(self.unitmeasurepage)
		self.label_35.setGeometry(QtCore.QRect(40, 330, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_35.setFont(font)
		self.label_35.setObjectName("label_35")
		self.label_36 = QtWidgets.QLabel(self.unitmeasurepage)
		self.label_36.setGeometry(QtCore.QRect(40, 220, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_36.setFont(font)
		self.label_36.setObjectName("label_36")
		self.label_37 = QtWidgets.QLabel(self.unitmeasurepage)
		self.label_37.setGeometry(QtCore.QRect(40, 150, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_37.setFont(font)
		self.label_37.setAutoFillBackground(False)
		self.label_37.setScaledContents(False)
		self.label_37.setObjectName("label_37")
		self.comboBox_9 = QtWidgets.QComboBox(self.unitmeasurepage)
		self.comboBox_9.setGeometry(QtCore.QRect(350, 150, 231, 22))
		self.comboBox_9.setObjectName("comboBox_9")
		self.comboBox_9.addItem("")
		self.comboBox_9.addItem("")
		self.comboBox_9.addItem("")
		self.comboBox_9.addItem("")
		self.comboBox_9.addItem("")
		self.comboBox_9.addItem("")
		self.label_38 = QtWidgets.QLabel(self.unitmeasurepage)
		self.label_38.setGeometry(QtCore.QRect(40, 281, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_38.setFont(font)
		self.label_38.setObjectName("label_38")
		self.comboBox_10 = QtWidgets.QComboBox(self.unitmeasurepage)
		self.comboBox_10.setGeometry(QtCore.QRect(350, 220, 231, 22))
		self.comboBox_10.setObjectName("comboBox_10")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_10.addItem("")
		self.comboBox_11 = QtWidgets.QComboBox(self.unitmeasurepage)
		self.comboBox_11.setGeometry(QtCore.QRect(350, 80, 231, 22))
		self.comboBox_11.setObjectName("comboBox_11")
		self.comboBox_11.addItem("")
		self.comboBox_11.addItem("")
		self.lineEdit_20 = QtWidgets.QLineEdit(self.unitmeasurepage)
		self.lineEdit_20.setGeometry(QtCore.QRect(350, 280, 231, 20))
		self.lineEdit_20.setObjectName("lineEdit_20")
		self.label_39 = QtWidgets.QLabel(self.unitmeasurepage)
		self.label_39.setGeometry(QtCore.QRect(40, 80, 251, 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_39.setFont(font)
		self.label_39.setObjectName("label_39")
		self.spinBox_2 = QtWidgets.QSpinBox(self.unitmeasurepage)
		self.spinBox_2.setGeometry(QtCore.QRect(350, 330, 231, 22))
		self.spinBox_2.setObjectName("spinBox_2")
		self.pushButton_14 = QtWidgets.QPushButton(self.unitmeasurepage)
		self.pushButton_14.setGeometry(QtCore.QRect(480, 440, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_14.setFont(font)
		self.pushButton_14.setObjectName("pushButton_14")
		self.label_44 = QtWidgets.QLabel(self.unitmeasurepage)
		self.label_44.setGeometry(QtCore.QRect(310 , 440 , 151 , 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_44.setFont(font)
		self.label_44.setObjectName("label_44")
		self.label_44.setText("Ready -->")
		self.stackedWidget.addWidget(self.unitmeasurepage)

		#Brand Page
		self.brandpage = QtWidgets.QWidget()
		self.brandpage.setObjectName("brandpage")
		self.lineEdit_22 = QtWidgets.QLineEdit(self.brandpage)
		self.lineEdit_22.setGeometry(QtCore.QRect(340, 140, 231, 31))
		self.lineEdit_22.setText("")
		self.lineEdit_22.setObjectName("lineEdit_22")
		self.label_40 = QtWidgets.QLabel(self.brandpage)
		self.label_40.setGeometry(QtCore.QRect(30, 140, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_40.setFont(font)
		self.label_40.setObjectName("label_40")
		self.label_41 = QtWidgets.QLabel(self.brandpage)
		self.label_41.setGeometry(QtCore.QRect(30, 80, 251, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_41.setFont(font)
		self.label_41.setObjectName("label_41")
		self.lineEdit_23 = QtWidgets.QLineEdit(self.brandpage)
		self.lineEdit_23.setGeometry(QtCore.QRect(340, 80, 231, 31))
		self.lineEdit_23.setText("")
		self.lineEdit_23.setObjectName("lineEdit_23")
		self.pushButton_15 = QtWidgets.QPushButton(self.brandpage)
		self.pushButton_15.setGeometry(QtCore.QRect(470, 400, 101, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.pushButton_15.setFont(font)
		self.pushButton_15.setObjectName("pushButton_15")
		self.label_45 = QtWidgets.QLabel(self.brandpage)
		self.label_45.setGeometry(QtCore.QRect(310 , 400 , 151 , 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_45.setFont(font)
		self.label_45.setObjectName("label_45")
		self.label_45.setText("Ready -->")
		self.stackedWidget.addWidget(self.brandpage)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(319, 80, 21, 547))
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.frame_3 = QtWidgets.QFrame(self.centralwidget)
		self.frame_3.setGeometry(QtCore.QRect(109, 79, 211, 551))
		self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_3.setObjectName("frame_3")
		self.stockgrpbtn = QtWidgets.QPushButton(self.frame_3)
		self.stockgrpbtn.setGeometry(QtCore.QRect(40, 80, 161, 31))
		self.stockgrpbtn.setObjectName("stockgrpbtn")
		self.stockcategorybtn = QtWidgets.QPushButton(self.frame_3)
		self.stockcategorybtn.setGeometry(QtCore.QRect(40, 150, 161, 31))
		self.stockcategorybtn.setObjectName("stockcategorybtn")
		self.stockitemsbtn = QtWidgets.QPushButton(self.frame_3)
		self.stockitemsbtn.setGeometry(QtCore.QRect(40, 220, 161, 31))
		self.stockitemsbtn.setObjectName("stockitemsbtn")
		self.godownsbtn = QtWidgets.QPushButton(self.frame_3)
		self.godownsbtn.setGeometry(QtCore.QRect(40, 290, 161, 31))
		self.godownsbtn.setObjectName("godownsbtn")
		self.unitmeasurebtn = QtWidgets.QPushButton(self.frame_3)
		self.unitmeasurebtn.setGeometry(QtCore.QRect(40, 370, 161, 31))
		self.unitmeasurebtn.setObjectName("unitmeasurebtn")
		self.brandbtn = QtWidgets.QPushButton(self.frame_3)
		self.brandbtn.setGeometry(QtCore.QRect(40, 440, 161, 31))
		self.brandbtn.setObjectName("brandbtn")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.showMessage("Inventory-->Stock Group")
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.stackedWidget.setCurrentWidget(self.stockgrppage)
		self.lineEdit_4.setFocus()

		#Input Validation
		double_validator = QtGui.QDoubleValidator()
		self.lineEdit_9.setValidator(double_validator)
		self.lineEdit_13.setValidator(double_validator)
		self.lineEdit_10.setValidator(double_validator)
		self.lineEdit_11.setValidator(double_validator)
		self.lineEdit_12.setValidator(double_validator)
		self.lineEdit_14.setValidator(double_validator)
		self.lineEdit_7.setValidator(double_validator)
		self.lineEdit_24.setValidator(double_validator)
		self.lineEdit_25.setValidator(double_validator)
		self.lineEdit_10.setDisabled(True)
		self.lineEdit_11.setDisabled(True)
		self.lineEdit_7.setDisabled(True)
		reg_ex = QtCore.QRegExp("^[a-zA-Z0-9 ]*$")
		character_validator = QtGui.QRegExpValidator(reg_ex)
		self.lineEdit_4.setValidator(character_validator)
		self.lineEdit_5.setValidator(character_validator)
		self.lineEdit_2.setValidator(character_validator)
		self.lineEdit_6.setValidator(character_validator)
		self.lineEdit_8.setValidator(character_validator)
		self.lineEdit_18.setValidator(character_validator)
		self.lineEdit_22.setValidator(character_validator)
		self.lineEdit_23.setValidator(character_validator)
		self.retranslateUi(MainWindow)

		#Page Change Management
		self.stockgrpbtn.clicked.connect(self.grppage)
		self.stockcategorybtn.clicked.connect(self.categorypage)
		self.stockitemsbtn.clicked.connect(self.itempage)
		self.godownsbtn.clicked.connect(self.godown)
		self.unitmeasurebtn.clicked.connect(self.unitmeasure)
		self.brandbtn.clicked.connect(self.brand)
		self.pushButton_11.clicked.connect(self.itemnextpage)

		#Submission Management
		self.pushButton_9.clicked.connect(self.stockgrpsubmit)
		self.pushButton_10.clicked.connect(self.stockcategorysubmit)
		self.pushButton_13.clicked.connect(self.godownsubmit)
		self.pushButton_14.clicked.connect(self.unitmeasuresubmit)
		self.pushButton_15.clicked.connect(self.brandsubmit)
		self.pushButton_12.clicked.connect(self.itemssubmit)

		#Activation Management
		self.comboBox.activated.connect(self.stock_group_under_head)
		self.lineEdit_9.textEdited.connect(self.op_check)
		self.lineEdit_13.textEdited.connect(self.op_check)
		self.lineEdit_14.textEdited.connect(self.pp_check)
		self.lineEdit_12.textEdited.connect(self.pp_check)
		self.lineEdit_24.textEdited.connect(self.sp_check)
		self.lineEdit_25.textEdited.connect(self.sp_check)

		#pyqtSignal User Signal
		self.stock_signal.connect(self.feedback)
		self.category_signal.connect(self.feedback)
		self.item_signal.connect(self.feedback)
		self.godown_signal.connect(self.feedback)
		self.unitmeasure_signal.connect(self.feedback)
		self.brand_signal.connect(self.feedback)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	#SetupUI Sub-Function
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "DreamXtreme"))
		self.label_5.setText(_translate("MainWindow", "Welcome to DreamXtreme"))
		self.Dash_personal_detail.setText(_translate("MainWindow", "Personal Details"))
		self.Dash_com_deatail.setText(_translate("MainWindow", "Company Details"))
		self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
		self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
		self.Dash_setting.setText(_translate("MainWindow", "Settings "))
		self.Dash_Log_out.setText(_translate("MainWindow", "Log Out"))
		self.label.setText(_translate("MainWindow", "Date of Creation                                    :"))
		self.label_2.setText(_translate("MainWindow", "Under/Head- Custom                              :"))
		self.comboBox_2.setItemText(0, _translate("MainWindow", "Yes"))
		self.comboBox_2.setItemText(1, _translate("MainWindow", "No"))
		self.label_4.setText(_translate("MainWindow", "Stock Group Name                                 :"))
		self.label_3.setText(_translate("MainWindow", "Under/Head- Predefined                         :"))
		self.label_6.setText(_translate("MainWindow", "Should quantities of Items to be added     ?"))
		self.label_7.setText(_translate("MainWindow", "Ready -->"))
		self.pushButton_9.setText(_translate("MainWindow", "Submit"))
		self.pushButton_10.setText(_translate("MainWindow", "Submit"))
		self.label_8.setText(_translate("MainWindow", "Under Stock Group                                                   :"))
		self.label_9.setText(_translate("MainWindow", "Date of Creation                                    :"))
		self.label_11.setText(_translate("MainWindow", "Category Name"))
		self.label_12.setText(_translate("MainWindow", "Name                                                   :"))
		self.label_13.setText(_translate("MainWindow", "Under                                                  :"))
		self.label_14.setText(_translate("MainWindow", "Categories                                           :"))
		self.label_16.setText(_translate("MainWindow", "Code Number                                       :"))
		self.label_17.setText(_translate("MainWindow", "Date of Creation                                    :"))
		self.label_18.setText(_translate("MainWindow", "Brand                                                  :"))
		self.pushButton_11.setText(_translate("MainWindow", "Next"))
		self.label_19.setText(_translate("MainWindow", "Units                                                      :"))
		self.label_20.setText(_translate("MainWindow", "Value :"))
		self.label_22.setText(_translate("MainWindow", "Opening Balance                                    :"))
		self.label_23.setText(_translate("MainWindow", "Value :"))
		self.label_24.setText(_translate("MainWindow", "Price :"))
		self.label_25.setText(_translate("MainWindow", "Selling Price                                           :"))
		self.label_26.setText(_translate("MainWindow", "Quantity :"))
		self.label_27.setText(_translate("MainWindow", "Quantity :"))
		self.label_28.setText(_translate("MainWindow", "Price :"))
		self.label_29.setText(_translate("MainWindow", "Purchase Price                                       :"))
		self.label_30.setText(_translate("MainWindow", "Rate of Duty                                           :"))
		self.label_10.setText(_translate("MainWindow", "Quantity :"))
		self.label_15.setText(_translate("MainWindow", "Value :"))
		self.label_43.setText(_translate("MainWindow", "Price :"))
		self.pushButton_12.setText(_translate("MainWindow", "Submit"))
		self.label_31.setText(_translate("MainWindow", "Name                                                   :"))
		self.comboBox_8.setItemText(0, _translate("MainWindow", "Primary"))
		self.comboBox_8.setItemText(1, _translate("MainWindow", "Main Location"))
		self.label_32.setText(_translate("MainWindow", "Under                                                  :"))
		self.label_34.setText(_translate("MainWindow", "Date of Creation                                    :"))
		self.pushButton_13.setText(_translate("MainWindow", "Submit"))
		self.label_35.setText(_translate("MainWindow", "Number of Decimal Places                      :"))
		self.label_36.setText(_translate("MainWindow", "Units                                                    :"))
		self.label_37.setText(_translate("MainWindow", "Symbol                                                :"))
		self.comboBox_9.setItemText(0, _translate("MainWindow", "cm"))
		self.comboBox_9.setItemText(1, _translate("MainWindow", "ltr"))
		self.comboBox_9.setItemText(2, _translate("MainWindow", "mm"))
		self.comboBox_9.setItemText(3, _translate("MainWindow", "m"))
		self.comboBox_9.setItemText(4, _translate("MainWindow", "kg"))
		self.comboBox_9.setItemText(5, _translate("MainWindow", "inch"))
		self.label_38.setText(_translate("MainWindow", "SKU                                                     :"))
		self.comboBox_10.setItemText(0, _translate("MainWindow", "Centimeter"))
		self.comboBox_10.setItemText(1, _translate("MainWindow", "Litre"))
		self.comboBox_10.setItemText(2, _translate("MainWindow", "Millimeter"))
		self.comboBox_10.setItemText(3, _translate("MainWindow", "Meter"))
		self.comboBox_10.setItemText(4, _translate("MainWindow", "Kilogram"))
		self.comboBox_10.setItemText(5, _translate("MainWindow", "Inches"))
		self.comboBox_11.setItemText(0, _translate("MainWindow", "Simple"))
		self.comboBox_11.setItemText(1, _translate("MainWindow", "Compound"))
		self.label_39.setText(_translate("MainWindow", "Type                                                    :"))
		self.pushButton_14.setText(_translate("MainWindow", "Submit"))
		self.label_40.setText(_translate("MainWindow", "Parent Company                                   :"))
		self.label_41.setText(_translate("MainWindow", "Name                                                   :"))
		self.pushButton_15.setText(_translate("MainWindow", "Submit"))
		self.stockgrpbtn.setText(_translate("MainWindow", "Stock Group"))
		self.stockcategorybtn.setText(_translate("MainWindow", "Stock Category"))
		self.stockitemsbtn.setText(_translate("MainWindow", "Stock Items"))
		self.godownsbtn.setText(_translate("MainWindow", "Godowns"))
		self.unitmeasurebtn.setText(_translate("MainWindow", "Units of Measure"))
		self.brandbtn.setText(_translate("MainWindow", "Brand"))

	#6 Signal Variable Connect to this Function
	def feedback(self,a,b):
		msg = QMessageBox()
		if b:
			msg.setIcon(QMessageBox.Information)
			msg.setText("{0} | Data Added SuccessFully".format(a))
			msg.setWindowTitle("Done")
			msg.exec_()
		else:
			msg.setIcon(QMessageBox.Critical)
			msg.setText("{0} | Server Not Reachable".format(a))
			msg.setWindowTitle("Error")
			msg.exec_()


	#Stock Item Multiply Functions 3
	def op_check(self):
		quantity = self.lineEdit_9.text().strip()
		price = self.lineEdit_13.text().strip()
		if quantity and price:
			quantity = float(quantity)
			price = float(price)
			a = quantity*price
			self.lineEdit_10.setText(str(a))
		else:
			self.lineEdit_10.clear()

	def pp_check(self):
		quantity = self.lineEdit_14.text().strip()
		price = self.lineEdit_12.text().strip()
		if quantity and price:
			quantity = float(quantity)
			price = float(price)
			a = quantity * price
			self.lineEdit_11.setText(str(a))
		else:
			self.lineEdit_11.clear()

	def sp_check(self):
		quantity = self.lineEdit_24.text().strip()
		price = self.lineEdit_25.text().strip()
		if quantity and price:
			quantity = float(quantity)
			price = float(price)
			a = quantity * price
			self.lineEdit_7.setText(str(a))
		else:
			self.lineEdit_7.clear()

	#Main Function Need to Call - If SetupUI Called ****
	def closethreads(self):
		self.threadexitflag = False

	#Stock Group Head Function
	def stock_group_under_head(self):
		oth = self.comboBox.currentText()
		if oth == 'Other':
			self.lineEdit_5.setDisabled(False)
			self.lineEdit_5.setFocus()
		else:
			self.lineEdit_5.setDisabled(True)


	#Page Change Management Functions 7
	def grppage(self):
		self.statusbar.showMessage("Inventory-->Stock Group")
		self.stackedWidget.setCurrentWidget(self.stockgrppage)
		self.lineEdit_4.setFocus()

	def categorypage(self):
		self.statusbar.showMessage("Inventory-->Stock Category")
		self.threadA = threading.Thread(target = self.groupcombo)
		self.threadA.start()
		self.stackedWidget.setCurrentWidget(self.stockcategorypage)
		self.lineEdit_2.setFocus()

	def itempage(self):
		self.statusbar.showMessage("Inventory-->Stock Items")
		self.thstkgroup = threading.Thread(target = self.groupcombo)
		self.thstkgroup.start()
		self.thcategory = threading.Thread(target = self.catcombo)
		self.thcategory.start()
		self.thbrand = threading.Thread(target = self.brandcom)
		self.thbrand.start()
		self.stackedWidget.setCurrentWidget(self.stockitem1page)
		self.lineEdit_6.setFocus()

	def itemnextpage(self):
		self.statusbar.showMessage("Inventory-->Stock Items")
		name = self.lineEdit_6.text().strip().title()
		codenumber = self.lineEdit_8.text().strip().title()
		under = self.comboBox_5.currentText()
		category = self.comboBox_6.currentText()
		brand = self.comboBox_7.currentText()
		if name and codenumber and under!="No Data Loaded" and category!="No Data Loaded" and brand!="No Data Loaded":
			self.stackedWidget.setCurrentWidget(self.stockitem2page)
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Enter Data Correctly!")
			msg.setWindowTitle("Warning")
			msg.exec_()

	def godown(self):
		self.statusbar.showMessage("Inventory-->Godowns")
		self.stackedWidget.setCurrentWidget(self.godownspage)
		self.lineEdit_18.setFocus()

	def unitmeasure(self):
		self.statusbar.showMessage("Inventory-->Units of Measure")
		self.stackedWidget.setCurrentWidget(self.unitmeasurepage)

	def brand(self):
		self.statusbar.showMessage("Inventory-->Brand")
		self.stackedWidget.setCurrentWidget(self.brandpage)
		self.lineEdit_23.setFocus()

	#Stock Group Page Main Functions 3
	def dbgroupsubmit(self,groupname,under1,under2,dofcreation,addsubitem):
		global stkgroup, topmain
		self.stock_group = False
		try:
			dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
			if dbcon.is_connected():
				query = dbcon.cursor()
				if under1 != 'Other':
					query.execute(
						"INSERT INTO stkgroup(company_id,group_name,group_under,date_of_creation,item_add_sub) VALUES ('%d','%s','%s','%s','%s');" % (
							self.cid , groupname , under1 , dofcreation , addsubitem))
					dbcon.commit()
					query.close()
					dbcon.close()
					self.stock_group = True
					stkgroup.append(groupname)
					self.stock_signal.emit("Stock Group",1)
				else:
					query.execute(
						"INSERT INTO stkgroup(company_id,group_name,group_under,group_under_custom,date_of_creation,item_add_sub) VALUES ('%d','%s','%s','%s','%s','%s');" % (
							self.cid , groupname , under1 , under2 , dofcreation , addsubitem))
					dbcon.commit()
					query.close()
					dbcon.close()
					stkgroup.append(groupname)
					topmain.append(under2)
					self.stock_group = True
					self.stock_signal.emit("Stock Group",1)

			else:
				self.stock_group = False
				self.stock_signal.emit("Stock Group",0)
		except:
			self.stock_group = False
			self.stock_signal.emit("Stock Group",0)



	def msgstksubmit(self):
		while self.threaddbgroupsubmit.is_alive()and self.threadexitflag:
			time.sleep(2)
			continue

		else:
			if self.stock_group:
				threadB = threading.Thread(target = self.cleanstkgroup)
				threadB.start()
				threadA = threading.Thread(target = self.mainhead)
				threadA.start()
				self.label_7.setText("Updated | Ready -->")
				threadA.join()
				threadB.join()
				self.pushButton_9.setDisabled(False)

			else:
				self.label_7.setText("Failed | Ready -->")
				self.pushButton_9.setDisabled(False)



	def stockgrpsubmit(self):
		tempvar = self.dateEdit.date()
		dofcreation = tempvar.toPyDate()
		groupname = self.lineEdit_4.text().strip().title()
		under1 = self.comboBox.currentText()
		under2 = self.lineEdit_5.text().strip().title()
		addsubitem = self.comboBox_2.currentText().strip().title()
		self.stock_group = False
		msg = QMessageBox()
		if groupname:
			self.threaddbgroupsubmit = threading.Thread(target = self.dbgroupsubmit, args = (groupname,under1,under2,dofcreation,addsubitem,) , daemon = True)
			self.threaddbgroupsubmit.start()
			self.threadmsggroup = threading.Thread(target = self.msgstksubmit)
			self.threadmsggroup.start()
			self.pushButton_9.setDisabled(True)
			self.label_7.setText("Updating...")

		else:
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Enter Data Correctly!")
			msg.setWindowTitle("Warning")
			msg.exec_()

	#Stock Category Page Main Functions 3
	def dbcategorysubmit(self, categoryname, under, dofcreation):
		global category
		self.stock_category = False
		try:
			dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
			if dbcon.is_connected():
				query = dbcon.cursor()
				query.execute("INSERT INTO stkcategory(company_id,category_name,stk_group_under,date_of_creation) VALUES ('%d','%s','%s','%s');" % (self.cid , categoryname , under , dofcreation))
				dbcon.commit()
				query.close()
				dbcon.close()
				category.append(categoryname)
				self.stock_category = True
				self.category_signal.emit("Stock Category",1)
			else:
				self.stock_category = False
				self.category_signal.emit("Stock Category",0)
		except:
			self.stock_category = False
			self.category_signal.emit("Stock Category",0)

	def msgcatsubmit(self):

		while self.threaddbcatgorysubmit.is_alive()and self.threadexitflag:
			time.sleep(2)
			continue

		else:
			if self.stock_category:
				threadA = threading.Thread(target = self.cleanstkcategory)
				threadA.start()
				self.label_21.setText("Updated | Ready -->")
				self.pushButton_10.setDisabled(False)
				threadA.join()

			else:
				self.label_21.setText("Failed | Ready -->")
				self.pushButton_10.setDisabled(False)

	def stockcategorysubmit(self):
		global category
		tempvar = self.dateEdit_2.date()
		dofcreation = tempvar.toPyDate()
		categoryname = self.lineEdit_2.text().strip().title()
		under = self.comboBox_3.currentText()
		self.stock_category = False
		msg = QMessageBox()
		if categoryname and under!="No Data Loaded":
			self.threaddbcatgorysubmit = threading.Thread(target = self.dbcategorysubmit, args = (categoryname,under,dofcreation,), daemon = True)
			self.threaddbcatgorysubmit.start()
			self.threadmsgcategory = threading.Thread(target = self.msgcatsubmit)
			self.threadmsgcategory.start()
			self.label_21.setText("Updating...")
			self.pushButton_10.setDisabled(True)
		else:
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Enter Data Correctly!")
			msg.setWindowTitle("Warning")
			msg.exec_()

	#Stock Item Main Functions 3
	def dbitemsubmit(self, dofcreation,itemname,codenumber,under,category,brand,units,opquantity,opprice,ppquantity,ppprice,spquantity,spprice,rateofduty):
		self.item_result = False
		try:
			dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
			if dbcon.is_connected():
				query = dbcon.cursor()
				query.execute("INSERT INTO stkitem(company_id,itemname,dofcreation,codenumber,under,category,brand,units,opquantity,opprice,ppquantity,ppprice,spquantity,spprice,rateofduty) VALUES ('%d','%s','%s','%s','%s','%s','%s','%s','%d',,'%d','%d','%d','%d','%d','%d');" % (self.cid ,itemname,dofcreation,codenumber,under,category,brand,units,opquantity,opprice,ppquantity,ppprice,spquantity,spprice,rateofduty))
				dbcon.commit()
				query.close()
				dbcon.close()
				self.item_result = True
				self.item_signal.emit("Stock Item",1)
			else:
				self.item_result = False
				self.item_signal.emit("Stock Item",0)
		except:
			self.item_result = False
			self.item_signal.emit("Stock Item",0)


	def msgitemsubmit(self):
		while self.threaddbitemsubmit.is_alive()and self.threadexitflag:
			time.sleep(2)
			continue

		else:
			if self.item_result:
				threadA = threading.Thread(target = self.cleanitems)
				threadA.start()
				self.label_33.setText("Updated | Ready -->")
				self.pushButton_12.setDisabled(False)
				threadA.join()
			else:
				self.label_33.setText("Failed | Ready -->")
				self.pushButton_12.setDisabled(False)

	def itemssubmit(self):
		tempvar = self.dateEdit_3.date()
		dofcreation = tempvar.toPyDate()
		itemname = self.lineEdit_6.text().strip().title()
		codenumber = self.lineEdit_8.text().strip()
		under = self.comboBox_5.currentText()
		category = self.comboBox_6.currentText()
		brand = self.comboBox_7.currentText()
		units = self.spinBox.value()
		opquantity = self.lineEdit_9.text().strip()
		opprice = self.lineEdit_13.text().strip()
		ppquantity = self.lineEdit_14.text().strip()
		ppprice = self.lineEdit_12.text().strip()
		spquantity = self.lineEdit_24.text().strip()
		spprice = self.lineEdit_25.text().strip()
		rateofduty = self.lineEdit_17.text().strip()
		self.item_result = False
		self.threaddbitemsubmit = threading.Thread(target = self.dbitemsubmit, args = (dofcreation,itemname,codenumber,under,category,brand,units,opquantity,opprice,ppquantity,ppprice,spquantity,spprice,rateofduty,), daemon = True)
		self.threaddbitemsubmit.start()
		self.threadmsgitemsubmit = threading.Thread(target = self.msgitemsubmit)
		self.threadmsgitemsubmit.start()
		self.label_33.setText("Updating...")
		self.pushButton_12.setDisabled(True)

	#Godown Page Main Functions 3
	def dbgodownsubmit(self, name, under, dofcreation):
		self.gocheck = False
		try:
			dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
			if dbcon.is_connected():
				query = dbcon.cursor()
				query.execute(
					"INSERT INTO godown(company_id,name,under,date_of_creation) VALUES ('%d','%s','%s','%s');" % (self.cid , name , under , dofcreation))
				dbcon.commit()
				query.close()
				dbcon.close()
				self.gocheck = True
				self.godown_signal.emit("Godown",1)
			else:
				self.gocheck = False
				self.godown_signal.emit("Godown",0)

		except:
			self.gocheck = False
			self.godown_signal.emit("Godown",0)

	def msggodownsubmit(self):
		while self.threaddbgodownsubmit.is_alive()and self.threadexitflag:
			time.sleep(2)
			continue

		else:
			if self.gocheck:
				threadA = threading.Thread(target = self.cleangodown)
				threadA.start()
				self.label_42.setText("Updated | Ready -->")
				self.pushButton_13.setDisabled(False)
				threadA.join()

			else:
				self.label_42.setText("Failed | Ready -->")
				self.pushButton_13.setDisabled(False)


	def godownsubmit(self):
		tempvar = self.dateEdit_4.date()
		dofcreation = tempvar.toPyDate()
		name = self.lineEdit_18.text().strip().title()
		under = self.comboBox_8.currentText()
		self.gocheck = False
		msg = QMessageBox()
		if name:
			self.threaddbgodownsubmit = threading.Thread(target = self.dbgodownsubmit , args = (name,under,dofcreation,), daemon = True)
			self.threaddbgodownsubmit.start()
			self.threadmsggodown = threading.Thread(target = self.msggodownsubmit)
			self.threadmsggodown.start()
			self.label_42.setText("Updating...")
			self.pushButton_13.setDisabled(True)

		else:
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Enter Data Correctly!")
			msg.setWindowTitle("Warning")
			msg.exec_()

	#Unit Measure Page Main Functions 3
	def dbunitmeasuresubmit(self, typ, symb, unitname, sku, decimalplaces):
		self.unitcheck = False
		try:
			dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
			if dbcon.is_connected():
				query = dbcon.cursor()
				query.execute(
					"INSERT INTO unitmeasure(company_id,type,symbol,unitname,sku,decimal_places) VALUES ('%d','%s','%s','%s','%s','%f');" % (
						self.cid , typ , symb , unitname , sku , decimalplaces))
				dbcon.commit()
				query.close()
				dbcon.close()
				self.unitcheck = True
				self.unitmeasure_signal.emit("Unit",1)

			else:
				self.unitcheck = False
				self.unitmeasure_signal.emit("Unit",0)

		except:
			self.unitcheck = False
			self.unitmeasure_signal.emit("Unit",0)

	def msgunitmeasure(self):

		while self.threaddbunitmeasure.is_alive()and self.threadexitflag:
			time.sleep(2)
			continue

		else:
			if self.unitcheck:
				threadA = threading.Thread(target = self.cleanunitmeasure)
				threadA.start()
				self.label_44.setText("Updated | Ready -->")
				self.pushButton_14.setDisabled(False)
				threadA.join()
			else:
				self.label_44.setText("Failed | Ready -->")
				self.pushButton_14.setDisabled(False)

	def unitmeasuresubmit(self):
		typ = self.comboBox_11.currentText()
		symb = self.comboBox_9.currentText()
		unitname = self.comboBox_10.currentText()
		sku = self.lineEdit_20.text().strip().title()
		decimalplaces = self.spinBox_2.value()
		self.unitcheck = False
		msg = QMessageBox()
		self.threaddbunitmeasure = threading.Thread(target = self.dbunitmeasuresubmit, args = (typ, symb, unitname, sku, decimalplaces,), daemon = True)
		self.threaddbunitmeasure.start()
		self.threadmsgunitmeasure = threading.Thread(target = self.msgunitmeasure)
		self.threadmsgunitmeasure.start()
		self.label_44.setText("Updating...")
		self.pushButton_14.setDisabled(True)

	#Brand Page Main Functions 3
	def dbbrandsubmit(self, name, parentcompany):
		self.brandcheck = False
		global brand
		try:
			dbcon = mysql.connector.connect(host = "localhost" , database = "profit_plug" , user = "root" ,password = "" , port = 3306)
			if dbcon.is_connected():
				query = dbcon.cursor()
				query.execute("INSERT INTO brands(company_id,brand_name,parent_company) VALUES ('%d','%s','%s');" % (self.cid , name , parentcompany))
				dbcon.commit()
				query.close()
				dbcon.close()
				brand.append(name)
				self.brandcheck = True
				self.brand_signal.emit("Brand",1)

			else:
				self.brandcheck = False
				self.brand_signal.emit("Brand",0)

		except:
			self.brandcheck = False
			self.brand_signal.emit("Brand",0)

	def msgbrandsubmit(self):
		while self.threaddbbrand.is_alive() and self.threadexitflag:
			time.sleep(2)
			continue

		else:
			if self.brandcheck:
				threadA = threading.Thread(target = self.cleanbrand)
				threadA.start()
				self.label_45.setText("Updated | Ready -->")
				self.pushButton_15.setDisabled(False)
				threadA.join()

			else:
				self.label_45.setText("Failed | Ready -->")
				self.pushButton_15.setDisabled(False)

	def brandsubmit(self):
		name = self.lineEdit_23.text().strip().title()
		parentcompany = self.lineEdit_22.text().strip().title()
		self.brandcheck = False
		msg = QMessageBox()
		if name and parentcompany:
			self.threaddbbrand = threading.Thread(target = self.dbbrandsubmit ,args = (name, parentcompany,), daemon = True)
			self.threaddbbrand.start()
			self.threadmsgbrand = threading.Thread(target = self.msgbrandsubmit)
			self.threadmsgbrand.start()
			self.label_45.setText("Updating...")
			self.pushButton_15.setDisabled(True)

		else:
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Enter Data Correctly!")
			msg.setWindowTitle("Warning")
			msg.exec_()



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	app.aboutToQuit.connect(ui.closethreads) #****Destruction Of All Thread Necessary to call if SetupUI has been called!
	sys.exit(app.exec_())
