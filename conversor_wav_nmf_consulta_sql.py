"""
Programa pessoal para manipular/converter arquivos de áudios da Ura. Fazer consulta no Sql dos caminhos das id's
de ligações.

Arquivo Wav que não roda em qualquer software, para mp3. Arquivos nmf com conversão tanto para wav quanto para mp3.
Prioridade é a conversão e espaço em disco, e não a mais alta qualidade de som do áudio.

A parte do código NMF converter é de autoria do Dmitry Misharov
https://github.com/quarckster/nmf_to_wav

A consulta é feita através de escolha por mês e ano que necessito, utilizando uma planilha externa via pandas.


"""

from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import os
import sys
import struct
import glob
import shutil
import pandas as pd
import pymssql


class Ui_Serial(object):
    def setupUi(self, Serial):
        Serial.setObjectName("Serial")
        Serial.resize(859, 629)
        self.centralwidget = QtWidgets.QWidget(Serial)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(760, 550, 91, 31))
        self.botao_sair.setObjectName("botao_sair")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 540, 181, 41))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 570, 201, 31))
        self.label_7.setObjectName("label_7")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(130, 570, 91, 31))
        self.label_17.setStyleSheet("image: url(:/logos_pasta/logotipo.png);")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 540, 1161, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(230, 570, 131, 51))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1151, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1201, 591))
        self.frame.setStyleSheet("background-color: rgb(134, 134, 134);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_11 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_11.setGeometry(QtCore.QRect(0, 0, 331, 401))
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 301, 81))
        self.groupBox.setObjectName("groupBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 40, 21, 21))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(130, 40, 21, 21))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(230, 40, 21, 16))
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(200, 20, 91, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 100, 301, 91))
        self.groupBox_7.setObjectName("groupBox_7")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_9.setGeometry(QtCore.QRect(110, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setText("")
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_10.setGeometry(QtCore.QRect(40, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setText("")
        self.radioButton_10.setObjectName("radioButton_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_7)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setGeometry(QtCore.QRect(100, 30, 49, 16))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 301, 91))
        font = QtGui.QFont()
        font.setBold(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(40, 50, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.radioButton.setFont(font)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(100, 30, 49, 16))
        self.label_6.setObjectName("label_6")
        self.botaoConverter = QtWidgets.QPushButton(self.groupBox_11)
        self.botaoConverter.setGeometry(QtCore.QRect(120, 360, 81, 31))
        self.botaoConverter.setObjectName("botao")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 280, 301, 80))
        self.groupBox_12.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.groupBox_12.setObjectName("groupBox_12")
        self.origem = QtWidgets.QLineEdit(self.groupBox_12)
        self.origem.setGeometry(QtCore.QRect(10, 40, 281, 21))
        self.origem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.origem.setObjectName("origem")
        self.groupBox_13 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_13.setGeometry(QtCore.QRect(0, 400, 851, 91))
        self.groupBox_13.setObjectName("groupBox_13")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_13)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 281, 61))
        self.textBrowser.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.textBrowser.setObjectName("textBrowser")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_13)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 30, 201, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 63))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setDigitCount(14)
        self.lcdNumber.setObjectName("lcdNumber")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(340, 0, 511, 211))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 20, 201, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_7.setGeometry(QtCore.QRect(80, 30, 21, 16))
        self.radioButton_7.setText("")
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_8.setGeometry(QtCore.QRect(130, 30, 21, 16))
        self.radioButton_8.setText("")
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 31, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(100, 30, 21, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(150, 30, 31, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 90, 361, 101))
        self.groupBox_8.setObjectName("groupBox_8")
        self.origem_2 = QtWidgets.QLineEdit(self.groupBox_8)
        self.origem_2.setGeometry(QtCore.QRect(60, 30, 291, 21))
        self.origem_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.origem_2.setObjectName("origem_2")
        self.origem_3 = QtWidgets.QLineEdit(self.groupBox_8)
        self.origem_3.setGeometry(QtCore.QRect(60, 60, 291, 21))
        self.origem_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.origem_3.setObjectName("origem_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_8)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 49, 16))
        self.label_15.setObjectName("label_15")
        self.label_18 = QtWidgets.QLabel(self.groupBox_8)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 49, 16))
        self.label_18.setObjectName("label_18")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_9.setGeometry(QtCore.QRect(370, 20, 131, 61))
        self.groupBox_9.setObjectName("groupBox_9")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_9)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.radioButton_11.setText("")
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_9)
        self.radioButton_12.setGeometry(QtCore.QRect(60, 30, 21, 16))
        self.radioButton_12.setText("")
        self.radioButton_12.setObjectName("radioButton_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        self.label_13.setGeometry(QtCore.QRect(30, 30, 21, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        self.label_14.setGeometry(QtCore.QRect(80, 30, 31, 16))
        self.label_14.setObjectName("label_14")
        self.pushButtonManipular = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonManipular.setGeometry(QtCore.QRect(410, 130, 71, 31))
        self.pushButtonManipular.setObjectName("pushButton")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_10.setGeometry(QtCore.QRect(220, 20, 141, 61))
        self.groupBox_10.setObjectName("groupBox_10")
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_13.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.radioButton_13.setText("")
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_14.setGeometry(QtCore.QRect(70, 30, 21, 16))
        self.radioButton_14.setText("")
        self.radioButton_14.setObjectName("radioButton_14")
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setGeometry(QtCore.QRect(30, 30, 41, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_10)
        self.label_21.setGeometry(QtCore.QRect(90, 30, 49, 16))
        self.label_21.setObjectName("label_21")
        self.groupBox_14 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_14.setGeometry(QtCore.QRect(340, 220, 511, 181))
        self.groupBox_14.setObjectName("groupBox_14")
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_14)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 20, 221, 61))
        self.groupBox_15.setObjectName("groupBox_15")
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_15)
        self.radioButton_15.setGeometry(QtCore.QRect(10, 30, 21, 16))
        self.radioButton_15.setText("")
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.groupBox_15)
        self.radioButton_16.setGeometry(QtCore.QRect(80, 30, 21, 16))
        self.radioButton_16.setText("")
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_15)
        self.radioButton_17.setGeometry(QtCore.QRect(150, 30, 21, 16))
        self.radioButton_17.setText("")
        self.radioButton_17.setObjectName("radioButton_17")
        self.label_22 = QtWidgets.QLabel(self.groupBox_15)
        self.label_22.setGeometry(QtCore.QRect(30, 30, 49, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_15)
        self.label_23.setGeometry(QtCore.QRect(100, 30, 49, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_15)
        self.label_24.setGeometry(QtCore.QRect(180, 30, 21, 16))
        self.label_24.setObjectName("label_24")
        self.groupBox_16 = QtWidgets.QGroupBox(self.groupBox_14)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 110, 361, 51))
        self.groupBox_16.setObjectName("groupBox_16")
        self.origem_4 = QtWidgets.QLineEdit(self.groupBox_16)
        self.origem_4.setGeometry(QtCore.QRect(10, 20, 341, 21))
        self.origem_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.origem_4.setObjectName("origem_4")
        self.pushButtonRemovendo = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButtonRemovendo.setGeometry(QtCore.QRect(410, 120, 71, 31))
        self.pushButtonRemovendo.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 280, 841, 231))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        self.textBrowser_2.setPalette(palette)
        self.textBrowser_2.setStyleSheet("")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 10, 221, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 30, 81, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 100, 291, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 271, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 891, 561))
        self.frame_2.setStyleSheet("background-color: rgb(134, 134, 134);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButtonConsultando = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonConsultando.setGeometry(QtCore.QRect(560, 230, 91, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.pushButtonConsultando.setPalette(palette)
        self.pushButtonConsultando.setObjectName("pushButtonConsultar_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(560, 200, 91, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 104, 104))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 231))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 104, 104))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        self.comboBox_3.setPalette(palette)
        self.comboBox_3.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.frame_2.raise_()
        self.textBrowser_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.textBrowser_3.raise_()
        self.botao_sair.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_17.raise_()
        self.label_19.raise_()
        self.tabWidget.raise_()
        Serial.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Serial)
        self.statusbar.setObjectName("statusbar")
        Serial.setStatusBar(self.statusbar)
        self.botaoConverter.clicked.connect(self.converter)
        self.pushButtonManipular.clicked.connect(self.manipular)
        self.pushButtonRemovendo.clicked.connect(self.removendo)
        self.pushButtonConsultando.clicked.connect(self.consultando)

        self.retranslateUi(Serial)
        self.tabWidget.setCurrentIndex(0)
        self.botao_sair.clicked.connect(Serial.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Serial)

    def retranslateUi(self, Serial):
        _translate = QtCore.QCoreApplication.translate
        Serial.setWindowTitle(_translate("Serial", "Backup & Restore Conversor"))
        self.botao_sair.setText(_translate("Serial", "Sair"))
        self.label_3.setText(_translate("Serial", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\"></span></p></body></html>"))
        self.label_7.setText(_translate("Serial", "<html><head/><body><p><span style=\" font-weight:700; color:#aa0000;\"></span></p></body></html>"))
        self.tabWidget.setToolTip(_translate("Serial", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox_11.setTitle(_translate("Serial", "Converter"))
        self.groupBox.setTitle(_translate("Serial", "Selecione método"))
        self.label.setText(_translate("Serial", "Arquivo Único"))
        self.label_2.setText(_translate("Serial", "Pasta"))
        self.label_4.setText(_translate("Serial", "Multiplas pastas"))
        self.groupBox_7.setTitle(_translate("Serial", "Formato original"))
        self.label_11.setText(_translate("Serial", "wav"))
        self.label_12.setText(_translate("Serial", "nmf"))
        self.groupBox_2.setTitle(_translate("Serial", "Formato final"))
        self.label_5.setText(_translate("Serial", "wav"))
        self.label_6.setText(_translate("Serial", "mp3"))
        self.botaoConverter.setText(_translate("Serial", "Go"))
        self.groupBox_12.setTitle(_translate("Serial", "Caminho"))
        self.groupBox_13.setTitle(_translate("Serial", "Resultado"))
        self.groupBox_5.setTitle(_translate("Serial", "Manipulação dos arquivos"))
        self.groupBox_6.setTitle(_translate("Serial", "Arquivos"))
        self.label_8.setText(_translate("Serial", "mp3"))
        self.label_9.setText(_translate("Serial", "wav"))
        self.label_10.setText(_translate("Serial", "nmf"))
        self.groupBox_8.setTitle(_translate("Serial", "Origem e Destino"))
        self.label_15.setText(_translate("Serial", "Origem:"))
        self.label_18.setText(_translate("Serial", "Destino:"))
        self.groupBox_9.setTitle(_translate("Serial", "Remover copiados"))
        self.radioButton_11.setToolTip(_translate("Serial", "<html><head/><body><p>Remover arquivo requer permissão na pasta</p></body></html>"))
        self.label_13.setText(_translate("Serial", "Sim"))
        self.label_14.setText(_translate("Serial", "Não"))
        self.pushButtonManipular.setText(_translate("Serial", "Ok"))
        self.groupBox_10.setTitle(_translate("Serial", "Copiar ou Mover"))
        self.label_20.setText(_translate("Serial", "Copiar"))
        self.label_21.setText(_translate("Serial", "Mover"))
        self.groupBox_14.setTitle(_translate("Serial", "Remover arquivos"))
        self.groupBox_15.setTitle(_translate("Serial", "Arquivos para serem removidos"))
        self.label_22.setText(_translate("Serial", "mp3"))
        self.label_23.setText(_translate("Serial", "wav"))
        self.label_24.setText(_translate("Serial", "nmf"))
        self.groupBox_16.setTitle(_translate("Serial", "Caminho dos arquivos:"))
        self.pushButtonRemovendo.setToolTip(_translate("Serial", "<html><head/><body><p>Remover arquivo requer permissão na pasta</p></body></html>"))
        self.pushButtonRemovendo.setText(_translate("Serial", "Remover"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Serial", "Converter"))
        self.groupBox_3.setTitle(_translate("Serial", "Mês e Ano para consulta"))
        self.comboBox.setItemText(0, _translate("Serial", "01"))
        self.comboBox.setItemText(1, _translate("Serial", "02"))
        self.comboBox.setItemText(2, _translate("Serial", "03"))
        self.comboBox.setItemText(3, _translate("Serial", "04"))
        self.comboBox.setItemText(4, _translate("Serial", "05"))
        self.comboBox.setItemText(5, _translate("Serial", "06"))
        self.comboBox.setItemText(6, _translate("Serial", "07"))
        self.comboBox.setItemText(7, _translate("Serial", "08"))
        self.comboBox.setItemText(8, _translate("Serial", "09"))
        self.comboBox.setItemText(9, _translate("Serial", "10"))
        self.comboBox.setItemText(10, _translate("Serial", "11"))
        self.comboBox.setItemText(11, _translate("Serial", "12"))
        self.comboBox_2.setItemText(0, _translate("Serial", "2018"))
        self.comboBox_2.setItemText(1, _translate("Serial", "2019"))
        self.comboBox_2.setItemText(2, _translate("Serial", "2020"))
        self.groupBox_4.setTitle(_translate("Serial", "ID\'s"))
        self.plainTextEdit.setToolTip(_translate("Serial", "<html><head/><body><p>Inserir id\'s. Formato: Sem vírgula, sem aspas simples. Um id por linha</p><p>id</p><p>id2</p><p>etc</p><p>ultimoid</p></body></html>"))
        self.pushButtonConsultando.setText(_translate("Serial", "Consultar"))
        self.comboBox_3.setToolTip(_translate("Serial", "<html><head/><body><p>Selecione o banco para consulta</p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("Serial", "BancoUm"))
        self.comboBox_3.setItemText(1, _translate("Serial", "BancoDois"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Serial", "Consulta"))


    def converter(self):
        #  Check arquivo unico
        if self.radioButton_3.isChecked():
            #  Conversão de arquivo wav para wav/mp3
            if self.radioButton_10.isChecked():
                origem2 = str(self.origem.text())
                opcionado2 = ''
                if self.radioButton.isChecked():
                    opcionado2 = ".wav"
                elif self.radioButton_2.isChecked():
                    opcionado2 = ".mp3"
                subprocess.call(['ffmpeg', '-i', f'{origem2}.wav', f'{origem2}{opcionado2}'])
                contador = 1
                self.lcdNumber.display(contador)
                return
            # Conversão de arquivo NMF para wav/mp3
            elif self.radioButton_9.isChecked():
                if self.radioButton.isChecked():
                    formatado = ".wav"
                elif self.radioButton_2.isChecked():
                    formatado = ".mp3"
                arquivo_nmf = str(self.origem.text())
                path_to_file = arquivo_nmf + '.nmf'
                convert_to_wav(path_to_file, extensao=formatado)
                contador = 1
                self.lcdNumber.display(contador)
                return
        # Check PASTA
        elif self.radioButton_4.isChecked():
            #  Convertendo toda PASTA com WAV para wav/mp3
            if self.radioButton_10.isChecked():
                caminho_pasta = str(self.origem.text())
                os.chdir(caminho_pasta)
                contador = 0
                opcionado2 = ''
                mais_um_cont = 0
                if self.radioButton.isChecked():
                    opcionado2 = ".wav"
                elif self.radioButton_2.isChecked():
                    opcionado2 = ".mp3"
                for file in os.listdir():
                    if file.endswith(".wav"):
                        a = file
                        mais_um_cont += 1
                        subprocess.check_call(['ffmpeg', '-i', f'{a}',
                                               f'{a}{opcionado2}'], shell=True)
                        app.processEvents()
                        self.lcdNumber.display(mais_um_cont)

                for arq in os.listdir():
                    if arq.endswith(f'{opcionado2}'):
                        contador += 1
                        arq_name, arq_ext = os.path.splitext(arq)
                        arq_conjunto, arq_wav = arq_name.split('.wav')
                        #        print(os.path.splitext(arq_conjunto))
                        #        print(f'{arq_conjunto}{arq_ext}')
                        new_name = (f'{arq_conjunto}{arq_ext}')
                        os.rename(arq, new_name)
#                self.lcdNumber.display(contador)
            #  Convertendo toda PASTA com NMF para wav/mp3
            elif self.radioButton_9.isChecked():
                try:
                    abcd = str(self.origem.text())
                    os.chdir(abcd)
                    contador_geral = 0
                    if self.radioButton.isChecked():
                        formatado = ".wav"
                    elif self.radioButton_2.isChecked():
                        formatado = ".mp3"
                    for arquivo in os.listdir():
                        if arquivo.endswith(".nmf"):
                            path_to_file = arquivo
                            convert_to_wav(path_to_file, extensao=formatado)
                            contador_geral += 1
                            app.processEvents()
                            self.lcdNumber.display(contador_geral)
                except IndexError:
                    sys.exit("Please specify path to nmf file")
        # Check MULTIPLAS PLASTAS
        elif self.radioButton_5.isChecked():
            #  Convertendo audios WAV dentro de SUBPASTAS
            if self.radioButton_10.isChecked():
                caminho_wav_todos = str(self.origem.text())
                contador_geral = 0
                opcionado2 = ''
                if self.radioButton.isChecked():
                    opcionado2 = ".wav"
                elif self.radioButton_2.isChecked():
                    opcionado2 = ".mp3"
                for file in glob.glob(caminho_wav_todos + '/**'):
                    if "." not in file:
                        caminho = rf'{file}'
                        os.chdir(caminho)
                        for file2 in os.listdir():
                            contador = 0
                            if file2.endswith(".wav"):
                                contador += 1
                                a = file2
                                subprocess.check_call(['ffmpeg', '-i', f'{a}',
                                                       f'{a}{opcionado2}'], shell=True)
                                contador_geral += 1
                                app.processEvents()
                                self.lcdNumber.display(contador_geral)
                        for arq in os.listdir():
                            if arq.endswith(f'{opcionado2}'):
                                arq_name, arq_ext = os.path.splitext(arq)
                                arq_conjunto, arq_wav = arq_name.split('.wav')
                                new_name = (f'{arq_conjunto}{arq_ext}')
                                os.rename(arq, new_name)
#                self.lcdNumber.display(contador_geral)
            #  Convertendo audios NMF dentro de SUBPASTAS
            elif self.radioButton_9.isChecked():
                try:
                    contador_geral = 0
                    audios_sem_converter = 0
                    origem_sem_sub = str(self.origem.text())
                    if self.radioButton.isChecked():
                        formatado = ".wav"
                    elif self.radioButton_2.isChecked():
                        formatado = ".mp3"
                    for file in glob.glob(origem_sem_sub + '/**'):
                        if "." not in file:
                            caminho = rf'{file}'
                            os.chdir(caminho)
                            contador = 0
                            for arquivo in os.listdir():
                                audios_sem_converter += 1
                                if arquivo.endswith(".nmf"):
                                    contador += 1
                                    path_to_file = arquivo
                                    convert_to_wav(path_to_file, extensao=formatado)
                                    contador_geral += 1
                                    app.processEvents()
                                    self.lcdNumber.display(contador_geral)
                except IndexError:
                    sys.exit("Please specify path to nmf file")


    def manipular(self):
        caminho_para_manipular = (str(self.origem_2.text()))
        lista_arquivos_para_manipular = []
        lista_wav = []
        lista_mp3 = []
        lista_nmf = []
        os.chdir(caminho_para_manipular)
        for file in os.listdir():
            if self.radioButton_6.isChecked():
                if file.endswith(".mp3"):
                    lista_mp3.append(file)
            elif self.radioButton_7.isChecked():
                if file.endswith(".wav"):
                    lista_wav.append(file)
            elif self.radioButton_8.isChecked():
                if file.endswith(".nmf"):
                    lista_nmf.append(file)
            else:
                lista_arquivos_para_manipular.append(file)
        caminho_destino = (str(self.origem_3.text()))
        cont = 0
#        os.chdir(caminho_destino)
        lista_ja_copiados = []
        for arq in os.listdir():
            if self.radioButton_6.isChecked():
                if arq.endswith(".mp3"):
                    if arq in lista_ja_copiados:
                        pass
                    if self.radioButton_13.isChecked():
                        shutil.copy(arq, caminho_destino)
                        lista_ja_copiados.append(arq)
                        if self.radioButton_8.isChecked():
                            os.remove(arq)
                        cont += 1
                        app.processEvents()
                        self.lcdNumber.display(cont)
                    elif self.radioButton_11.isChecked():
                        shutil.move(arq, caminho_destino)
                        lista_ja_copiados.append(arq)
                        cont += 1
                        app.processEvents()
                        self.lcdNumber.display(cont)

            elif self.radioButton_7.isChecked():
                if arq.endswith(".wav"):
                    if arq in lista_ja_copiados:
                        pass
                    elif self.radioButton_13.isChecked():
                        shutil.copy(arq, caminho_destino)
                        lista_ja_copiados.append(arq)
                        if self.radioButton_11.isChecked():
                            os.remove(arq)
                        cont += 1
                        app.processEvents()
                        self.lcdNumber.display(cont)
                    elif self.radioButton_14.isChecked():
                        shutil.move(arq, caminho_destino)
                        lista_ja_copiados.append(arq)
                        cont += 1
                        app.processEvents()
                        self.lcdNumber.display(cont)

            elif self.radioButton_8.isChecked():
                if arq.endswith(".nmf"):
                    if arq in lista_ja_copiados:
                        pass
                    elif self.radioButton_13.isChecked():
                        shutil.copy(arq, caminho_destino)
                        lista_ja_copiados.append(arq)
                        cont += 1
                        app.processEvents()
                        self.lcdNumber.display(cont)
                        if self.radioButton_11.isChecked():
                            os.remove(arq)
                    elif self.radioButton_14.isChecked():
                        shutil.move(arq, caminho_destino)
                        lista_ja_copiados.append(arq)
                        cont += 1
                        app.processEvents()
                        self.lcdNumber.display(cont)

            else:
                pass
            app.processEvents()
            self.lcdNumber.display(cont)


    def removendo(self):
        remover_caminho = (str(self.origem_4.text()))
        os.chdir(remover_caminho)
        contando_removidos = 0
        for arq in os.listdir():
            if self.radioButton_15.isChecked():
                if arq.endswith(".mp3"):
                    os.remove(f'{arq}')
                    contando_removidos += 1
            elif self.radioButton_16.isChecked():
                if arq.endswith(".wav"):
                    os.remove(f'{arq}')
                    contando_removidos += 1
            elif self.radioButton_17.isChecked():
                if arq.endswith(".nmf"):
                    os.remove(f'{arq}')
                    contando_removidos += 1
            self.lcdNumber.display(contando_removidos)


    def consultando(self):
        banco_mes = str(self.comboBox.currentText())  # verifi
        banco_ano = str(self.comboBox_2.currentText())  # ano
        cidade = str(self.comboBox_3.currentText())
#        como_vai_ser = self.plainTextEdit.currentCharFormat()
        self.texto = self.plainTextEdit
        print('Hello')
        varia = self.plainTextEdit
        print('aopa')
        print(varia)
        print(self.texto.toPlainText())  # esse sai elas separado
        print('oi')
        print(self.texto.toPlainText().splitlines())
        minha_lista = self.texto.toPlainText().splitlines()
        print(minha_lista)
        print(f'Oi lindao {minha_lista[0]}')
        quantos_ids = len(self.texto.toPlainText().splitlines())
        print(quantos_ids)
        for ids in minha_lista:
            print(ids)
            if ids in minha_lista[0]:
                n = "'" + ids + "',"
            elif ids not in minha_lista[0] and  ids not in minha_lista[-1]:
                n = n + "'" + ids + "',"
            if ids == minha_lista[-1]:
                n =  n + "'" + ids + "'"
        print(n)
        print(type(banco_mes))
        print(type(banco_ano))
        print(type(cidade))
        mes_e_ano = banco_mes + '-' + banco_ano
        print(mes_e_ano)
        tabela = pd.read_excel("TABELA_DADOS.xlsx")
#        consultando_id = tuple((tabela.loc[tabela['Mes-e-ano']=='BancoUm', mes_e_ano]))
#        print(consultando_id)
#        consultando_id_numero = str(consultando_id[0])
#        print(consultando_id_numero)
        consultando_id2 = tuple((tabela.loc[tabela['Mes-e-ano'] == cidade, mes_e_ano]))
        consultando_id_numero2 = str(consultando_id2[0])
        consultando_id_numero2 = str(consultando_id2[0])
        print('Hellooo')
        print(consultando_id_numero2)
        if len(consultando_id_numero2) < 2:
            consultando_id_numero2 = '0' + consultando_id_numero2
        sql = f"""select tabelaid,archivepath

from storage{consultando_id_numero2}

where tabelaid in ({n})

and MediaTypeId = '2'"""
        print(sql)
        como_vai_ser = self.plainTextEdit.currentCharFormat()
        if cidade == 'BancoUm':
            conn = pymssql.connect(host='bancoum', user='usuario', password='senha',
                               database='database')
            cursor = conn.cursor()
            print('conectado')
            cursor.execute(sql)
            resultado = cursor.fetchall()
            self.textBrowser_2.setText(f'{resultado}')
            print(resultado)
            for row in resultado:
                print(row)
            cursor.close()
            self.textBrowser_2.setText(f'Conectado\n{resultado}\nConexão encerrada')
        elif cidade == 'BancoDois':
            conn = pymssql.connect(host='bancodois', user='usuario', password='senha',
                                   database='database')
            cursor = conn.cursor()
            print('conectado')
            cursor.execute(sql)
            resultado = cursor.fetchall()
            self.textBrowser_2.setText(f'{resultado}')
            print(resultado)
            for row in resultado:
                print(row)
            cursor.close()
            self.textBrowser_2.setText(f'Conectado\n{resultado}\nConexão encerrada')


codecs = {
    0: "g729",
    1: "adpcm_g726",
    2: "adpcm_g726",
    3: "alaw",
    7: "pcm_mulaw",
    8: "g729",
    9: "g723_1",
    10: "g723_1",
    19: "adpcm_g722"
}
def get_packet_header(data):
    "Get required information from packet header."
    return {
        "packet_type": struct.unpack("b", data[0:1])[0],
        "packet_subtype": struct.unpack("h", data[1:3])[0],
        "stream_id": struct.unpack("b", data[3:4])[0],
        "start_time": struct.unpack("d", data[4:12])[0],
        "end_time": struct.unpack("d", data[12:20])[0],
        "packet_size": struct.unpack("I", data[20:24])[0],
        "parameters_size": struct.unpack("I", data[24:28])[0]
    }


def get_compression_type(data):
    "Get compression type of the audio chunk."
    for i in range(0, len(data), 22):
        type_id = struct.unpack("h", data[i:i + 2])[0]
        data_size = struct.unpack("i", data[i + 2:i + 6])[0]
        data = struct.unpack("16s", data[i + 6:i + 22])[0]
        if type_id == 10:
            return get_data_value(data, data_size)


def get_data_value(data, data_size):
    '''The helper function to get value of the data
    field from parameters header.'''
    fmt = "{}s".format(data_size)
    data_value = struct.unpack(fmt, data[0:data_size])
    if data_value == 0:
        data_value = struct.unpack(fmt, data[8:data_size])
    data_value = struct.unpack("b", data_value[0])
    return data_value[0]


def chunks_generator(path_to_file):
    "A python generator of the raw audio data."
    try:
        with open(path_to_file, "rb") as f:
            data = f.read()
    except IOError:
        sys.exit("No such file")
    packet_header_start = 0
    while True:
        packet_header_end = packet_header_start + 28
        headers = get_packet_header(data[packet_header_start:packet_header_end])
        if headers["packet_type"] == 4 and headers["packet_subtype"] == 0:
            chunk_start = packet_header_end + headers["parameters_size"]
            chunk_end = (chunk_start + headers["packet_size"] - headers["parameters_size"])
            chunk_length = chunk_end - chunk_start
            fmt = "{}s".format(chunk_length)
            raw_audio_chunk = struct.unpack(fmt, data[chunk_start:chunk_end])
            yield (get_compression_type(data[packet_header_end:packet_header_end +
                                                               headers["parameters_size"]]),
                   headers["stream_id"],
                   raw_audio_chunk[0])
        packet_header_start += headers["packet_size"] + 28
        if headers["packet_type"] == 7:
            break


def convert_to_wav(path_to_file, extensao):
    "Convert raw audio data using ffmpeg and subprocess."
    previous_stream_id = -1
    processes = {}
    for compression, stream_id, raw_audio_chunk in chunks_generator(path_to_file):
        if stream_id != previous_stream_id and not processes.get(stream_id):
            output_file = os.path.splitext(path_to_file)[0] + "".format(stream_id) + f'{extensao}'
            processes[stream_id] = subprocess.Popen(
                ("ffmpeg",
                 "-hide_banner",
                 "-y",
                 "-f",
                 codecs[compression],
                 "-i",
                 "pipe:0",
                 output_file),
                stdin=subprocess.PIPE
            )
            previous_stream_id = stream_id
        processes[stream_id].stdin.write(raw_audio_chunk)
    for key in processes.keys():
        processes[key].stdin.close()
        processes[key].wait()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Serial = QtWidgets.QMainWindow()
    ui = Ui_Serial()
    ui.setupUi(Serial)
    Serial.show()
    sys.exit(app.exec())