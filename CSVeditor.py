

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget,QFileDialog, QVBoxLayout)
import ressource, sys, csv
from string import ascii_uppercase



class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 698)
        MainWindow.setWindowModality(Qt.ApplicationModal)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.triggered.connect(self.load_csv)
        icon = QIcon()
        icon.addFile(u":/icons/icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as.setIcon(icon2)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.triggered.connect(self.add_table_page)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon3)
        self.actionCreate_table = QAction(MainWindow)
        self.actionCreate_table.setObjectName(u"actionCreate_table")
        self.actionCreate_table.setIcon(icon3)
        self.actionGithub_repo = QAction(MainWindow)
        self.actionGithub_repo.setObjectName(u"actionGithub_repo")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/terminal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGithub_repo.setIcon(icon4)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(7, 580, 792, 41))
        font = QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.tabWidget.addTab(self.tab2, "")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 30, 799, 551))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.table1 = QTableWidget(self.page)
        self.table1.setObjectName(u"table1")
        self.table1.setGeometry(QRect(0, 0, 799, 581))
        self.table1.setRowCount(100)
        self.table1.setColumnCount(100)

        cols = [chr(i) for i in range(ord('A'), ord('Z')+1)]

        # Add second set of column labels (AA to AZ)
        for i in range(ord('A'), ord('Z')+1):
            cols.append('A' + chr(i))

        # Set row labels (numbers 1 to 100)
        rows = [str(i+1) for i in range(100)]

        # Set up table with row and column labels
        self.table1.setColumnCount(len(cols))
        self.table1.setRowCount(len(rows))
        self.table1.setHorizontalHeaderLabels(cols)
        self.table1.setVerticalHeaderLabels(rows)

        # Set each cell to an empty QTableWidgetItem
        for i in range(len(rows)):
            for j in range(len(cols)):
                self.table1.setItem(i, j, QTableWidgetItem(""))

        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.table2 = QTableWidget(self.page2)
        self.table2.setObjectName(u"table2")
        self.table2.setGeometry(QRect(0, 0, 799, 581))
        self.stackedWidget.addWidget(self.page)
        self.stackedWidget.addWidget(self.page2)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, -21, 799, 71))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.header)
        self.gridLayout.setObjectName(u"gridLayout")
        self.italic_button = QPushButton(self.header)
        self.italic_button.setObjectName(u"italic_button")
        font1 = QFont()
        font1.setFamilies([u"NSimSun"])
        font1.setPointSize(13)
        font1.setItalic(True)
        self.italic_button.setFont(font1)
        self.italic_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.italic_button, 0, 0, 1, 1)

        self.bold_button = QPushButton(self.header)
        self.bold_button.setObjectName(u"bold_button")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.bold_button.setFont(font2)
        self.bold_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.bold_button, 0, 1, 1, 1)

        self.normal_button = QPushButton(self.header)
        self.normal_button.setObjectName(u"normal_button")
        self.normal_button.setFont(font)
        self.normal_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.normal_button, 0, 2, 1, 1)

        self.font_size = QSpinBox(self.header)
        self.font_size.setObjectName(u"font_size")
        self.font_size.setFont(font)
        self.font_size.setCursor(QCursor(Qt.SizeVerCursor))
        self.font_size.setValue(9)

        self.gridLayout.addWidget(self.font_size, 0, 3, 1, 1)

        self.color_button = QPushButton(self.header)
        self.color_button.setObjectName(u"color_button")
        self.color_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/droplet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.color_button.setIcon(icon6)

        self.gridLayout.addWidget(self.color_button, 0, 4, 1, 1)

        self.search_input = QLineEdit(self.centralwidget)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setGeometry(QRect(63, 620, 218, 22))
        self.search_input.setFont(font)
        self.search_input.setFrame(False)
        self.search_input.setClearButtonEnabled(False)
        self.search_label = QLabel(self.centralwidget)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(7, 620, 64, 21))
        self.search_label.setFont(font)
        self.occurence_label = QLabel(self.centralwidget)
        self.occurence_label.setObjectName(u"occurence_label")
        self.occurence_label.setGeometry(QRect(294, 620, 43, 21))
        self.occurence_label.setFont(font)
        self.replace_label = QLabel(self.centralwidget)
        self.replace_label.setObjectName(u"replace_label")
        self.replace_label.setGeometry(QRect(371, 620, 85, 21))
        self.replace_label.setFont(font)
        self.replace_input = QLineEdit(self.centralwidget)
        self.replace_input.setObjectName(u"replace_input")
        self.replace_input.setGeometry(QRect(462, 620, 232, 21))
        self.replace_input.setFont(font)
        self.replace_input.setFrame(False)
        self.replace_button = QPushButton(self.centralwidget)
        self.replace_button.setObjectName(u"replace_button")
        self.replace_button.setGeometry(QRect(704, 620, 85, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.replace_button.setFont(font3)
        self.replace_button.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        sizePolicy.setHeightForWidth(self.menuHelp.sizePolicy().hasHeightForWidth())
        self.menuHelp.setSizePolicy(sizePolicy)
        self.menuHelp.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuHelp.addAction(self.actionGithub_repo)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)
        self.tabWidget.tabBarClicked.connect(self.stackedWidget.setCurrentIndex)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.tab_counter = 1

    def load_csv(self):
        options = QFileDialog.Options()
        options |= QFileDialog.Option.ReadOnly  # Allow read-only access
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV file", "", "CSV files (*.csv)", options=options)
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            num_rows = len(data)
            num_cols = len(data[0])
            current_index = self.tabWidget.currentIndex()
            current_table_widget = self.tabWidget.widget(current_index).findChild(QTableWidget)
            current_table_widget.setRowCount(num_rows)
            current_table_widget.setColumnCount(num_cols)
            for i, row in enumerate(data):
                for j, item in enumerate(row):
                    current_table_widget.setItem(i, j, QTableWidgetItem(item))
    
    def add_table_page(self):
        self.tab_counter += 1
        new_page = QWidget()
        self.tabWidget.addTab(new_page, f"Table {self.tab_counter}")

        # Create the QTableWidget and add it to the new QWidget
        table_widget = QTableWidget(new_page)
        table_widget.setRowCount(100)
        table_widget.setColumnCount(100)
        
        # Set the horizontal header labels to letters
        for i in range(100):
            label = chr(ord('A') + i)
            table_widget.setHorizontalHeaderItem(i, QTableWidgetItem(label))

        # Set the vertical header labels to numbers
        for i in range(100):
            label = str(i+1)
            table_widget.setVerticalHeaderItem(i, QTableWidgetItem(label))

        layout = QVBoxLayout(new_page)
        layout.addWidget(table_widget)

        self.stackedWidget.setCurrentIndex(self.tab_counter)

        
        print(self.stackedWidget.currentIndex())

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CSVeditor by Kais and Adam", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreate_table.setText(QCoreApplication.translate("MainWindow", u"Create table", None))
#if QT_CONFIG(shortcut)
        self.actionCreate_table.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionGithub_repo.setText(QCoreApplication.translate("MainWindow", u"Github repo", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Table 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Table 2", None))
        self.italic_button.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.bold_button.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.normal_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.color_button.setText("")
        self.search_label.setText(QCoreApplication.translate("MainWindow", u"Search:", None))
        self.occurence_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.replace_label.setText(QCoreApplication.translate("MainWindow", u"Replace by:", None))
        self.replace_input.setText("")
        self.replace_button.setText(QCoreApplication.translate("MainWindow", u"Replace all", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())