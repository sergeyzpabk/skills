# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(847, 595)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("message.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(167, 194, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(9, 558, 829, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 829, 532))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 9, 231, 111))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonAuth = QtWidgets.QPushButton(self.groupBox)
        self.buttonAuth.setMinimumSize(QtCore.QSize(209, 23))
        self.buttonAuth.setObjectName("buttonAuth")
        self.gridLayout_2.addWidget(self.buttonAuth, 0, 0, 1, 1)
        self.buttonSaveAll = QtWidgets.QPushButton(self.groupBox)
        self.buttonSaveAll.setMinimumSize(QtCore.QSize(209, 23))
        self.buttonSaveAll.setObjectName("buttonSaveAll")
        self.gridLayout_2.addWidget(self.buttonSaveAll, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(243, 9, 231, 109))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonPause = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonPause.setEnabled(False)
        self.buttonPause.setMinimumSize(QtCore.QSize(211, 23))
        self.buttonPause.setObjectName("buttonPause")
        self.gridLayout_3.addWidget(self.buttonPause, 3, 0, 1, 1)
        self.buttonStart = QtWidgets.QPushButton(self.groupBox_4)
        self.buttonStart.setEnabled(False)
        self.buttonStart.setMinimumSize(QtCore.QSize(211, 23))
        self.buttonStart.setObjectName("buttonStart")
        self.gridLayout_3.addWidget(self.buttonStart, 2, 0, 1, 1)
        self.editTime = QtWidgets.QLineEdit(self.groupBox_4)
        self.editTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.editTime.setAlignment(QtCore.Qt.AlignCenter)
        self.editTime.setObjectName("editTime")
        self.gridLayout_3.addWidget(self.editTime, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 126, 478, 64))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.editantigate = QtWidgets.QLineEdit(self.groupBox_5)
        self.editantigate.setObjectName("editantigate")
        self.gridLayout_4.addWidget(self.editantigate, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(486, 9, 321, 244))
        self.groupBox_6.setObjectName("groupBox_6")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget.setEnabled(False)
        self.listWidget.setGeometry(QtCore.QRect(9, 18, 301, 181))
        self.listWidget.setObjectName("listWidget")
        self.buttonLoadAccs = QtWidgets.QPushButton(self.groupBox_6)
        self.buttonLoadAccs.setGeometry(QtCore.QRect(9, 207, 301, 23))
        self.buttonLoadAccs.setMinimumSize(QtCore.QSize(301, 23))
        self.buttonLoadAccs.setObjectName("buttonLoadAccs")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 270, 802, 235))
        self.groupBox_2.setMouseTracking(False)
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.memoLog = QtWidgets.QTextEdit(self.groupBox_2)
        self.memoLog.setGeometry(QtCore.QRect(10, 20, 775, 226))
        self.memoLog.setObjectName("memoLog")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 189, 478, 73))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.editPause2 = QtWidgets.QLineEdit(self.groupBox_9)
        self.editPause2.setObjectName("editPause2")
        self.gridLayout_5.addWidget(self.editPause2, 1, 1, 1, 1)
        self.editPause1 = QtWidgets.QLineEdit(self.groupBox_9)
        self.editPause1.setObjectName("editPause1")
        self.gridLayout_5.addWidget(self.editPause1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_9)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 18, 471, 211))
        self.groupBox_3.setMouseTracking(False)
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.memoText = QtWidgets.QTextEdit(self.groupBox_3)
        self.memoText.setGeometry(QtCore.QRect(10, 20, 451, 181))
        self.memoText.setObjectName("memoText")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(486, 18, 325, 211))
        self.groupBox_7.setMouseTracking(False)
        self.groupBox_7.setAutoFillBackground(True)
        self.groupBox_7.setObjectName("groupBox_7")
        self.memoDict = QtWidgets.QTextEdit(self.groupBox_7)
        self.memoDict.setGeometry(QtCore.QRect(10, 20, 307, 181))
        self.memoDict.setObjectName("memoDict")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(9, 270, 802, 217))
        self.groupBox_8.setMouseTracking(False)
        self.groupBox_8.setAutoFillBackground(True)
        self.groupBox_8.setObjectName("groupBox_8")
        self.memoResult = QtWidgets.QTextEdit(self.groupBox_8)
        self.memoResult.setGeometry(QtCore.QRect(9, 18, 451, 181))
        self.memoResult.setObjectName("memoResult")
        self.buttonRandom = QtWidgets.QPushButton(self.tab_2)
        self.buttonRandom.setGeometry(QtCore.QRect(108, 234, 298, 23))
        self.buttonRandom.setObjectName("buttonRandom")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(9, 9, 802, 487))
        self.groupBox_10.setMouseTracking(False)
        self.groupBox_10.setAutoFillBackground(True)
        self.groupBox_10.setObjectName("groupBox_10")
        self.memoUrl = QtWidgets.QTextEdit(self.groupBox_10)
        self.memoUrl.setGeometry(QtCore.QRect(9, 27, 784, 442))
        self.memoUrl.setObjectName("memoUrl")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расслыка [Ирина Ростова]"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройка"))
        self.buttonAuth.setText(_translate("MainWindow", "Авторизоваться"))
        self.buttonSaveAll.setText(_translate("MainWindow", "Сохранить настройки"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Запуск"))
        self.buttonPause.setText(_translate("MainWindow", "Пауза"))
        self.buttonStart.setText(_translate("MainWindow", "Старт"))
        self.editTime.setText(_translate("MainWindow", "12:00"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Капча AntiGate"))
        self.editantigate.setText(_translate("MainWindow", "26d7985260270f8ea8b4ab36de2839ac"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Аккаунты"))
        self.buttonLoadAccs.setText(_translate("MainWindow", "Загрузить аккаунты"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Log"))
        self.memoLog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Пауза(сек)"))
        self.editPause2.setText(_translate("MainWindow", "120"))
        self.editPause1.setText(_translate("MainWindow", "60"))
        self.label.setText(_translate("MainWindow", "От"))
        self.label_2.setText(_translate("MainWindow", "До"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Отправка сообщений"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Сообщение"))
        self.memoText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">{hello}, {username}{emj1} {buy} был успешно оплачен. {time} вы сможете его забрать. Мы вам {send}.</span></p></body></html>"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Сообщение"))
        self.memoDict.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">hello=Добрый день</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">hello=Здравствуйте</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">hello=Доброго времени суток</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">hello=Приветсвую вас</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">hello=Рада вам сообщить</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Roboto\',\'Open Sans\',\'Helvetica Neue\',\'Noto Sans Armenian\',\'Noto Sans Bengali\',\'Noto Sans Cherokee\',\'Noto Sans Devanagari\',\'Noto Sans Ethiopic\',\'Noto Sans Georgian\',\'Noto Sans Hebrew\',\'Noto Sans Kannada\',\'Noto Sans Khmer\',\'Noto Sans Lao\',\'Noto Sans Osmanya\',\'Noto Sans Tamil\',\'Noto Sans Telugu\',\'Noto Sans Thai\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">&amp;#128522;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Roboto\',\'Open Sans\',\'Helvetica Neue\',\'Noto Sans Armenian\',\'Noto Sans Bengali\',\'Noto Sans Cherokee\',\'Noto Sans Devanagari\',\'Noto Sans Ethiopic\',\'Noto Sans Georgian\',\'Noto Sans Hebrew\',\'Noto Sans Kannada\',\'Noto Sans Khmer\',\'Noto Sans Lao\',\'Noto Sans Osmanya\',\'Noto Sans Tamil\',\'Noto Sans Telugu\',\'Noto Sans Thai\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">&amp;#9786;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Roboto\',\'Open Sans\',\'Helvetica Neue\',\'Noto Sans Armenian\',\'Noto Sans Bengali\',\'Noto Sans Cherokee\',\'Noto Sans Devanagari\',\'Noto Sans Ethiopic\',\'Noto Sans Georgian\',\'Noto Sans Hebrew\',\'Noto Sans Kannada\',\'Noto Sans Khmer\',\'Noto Sans Lao\',\'Noto Sans Osmanya\',\'Noto Sans Tamil\',\'Noto Sans Telugu\',\'Noto Sans Thai\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">&amp;#128513;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">emj1=</span><span style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',\'Roboto\',\'Open Sans\',\'Helvetica Neue\',\'Noto Sans Armenian\',\'Noto Sans Bengali\',\'Noto Sans Cherokee\',\'Noto Sans Devanagari\',\'Noto Sans Ethiopic\',\'Noto Sans Georgian\',\'Noto Sans Hebrew\',\'Noto Sans Kannada\',\'Noto Sans Khmer\',\'Noto Sans Lao\',\'Noto Sans Osmanya\',\'Noto Sans Tamil\',\'Noto Sans Telugu\',\'Noto Sans Thai\',\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">&amp;#9996;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">buy=Ваш заказ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">buy=Ваш товар</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">time=В ближайшее время </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">time=В ближайшие дни </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">time=Через пару дней</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">send=сообщим</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">send=напишем</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">send=напомним</span></p></body></html>"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Проверка рандомности сообщений"))
        self.memoResult.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buttonRandom.setText(_translate("MainWindow", "Сгенирировать рандомное сообщение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Настройка сообщений"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Изображения URL"))
        self.memoUrl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Страница"))
