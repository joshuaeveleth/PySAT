# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicholas\Documents\GitHub\PYSAT\src\New PYSAT_Gui\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class CreateModels(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(581, 841)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_9.setMargin(11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 561, 768))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaWidgetContents_2.setFont(font)
        self.scrollAreaWidgetContents_2.setStyleSheet(_fromUtf8("QGroupBox {\n"
"  border: 2px solid gray;\n"
"  border-radius: 6px;\n"
"  margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"  padding-top: -14px;\n"
"  padding-left: 8px;\n"
"}\n"
""))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setMargin(11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.CreateModels = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CreateModels.setFont(font)
        self.CreateModels.setObjectName(_fromUtf8("CreateModels"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.CreateModels)
        self.verticalLayout_17.setMargin(11)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setMargin(11)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setMargin(11)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.label_70 = QtGui.QLabel(self.CreateModels)
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.verticalLayout_18.addWidget(self.label_70)
        self.label_71 = QtGui.QLabel(self.CreateModels)
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.verticalLayout_18.addWidget(self.label_71)
        self.label_72 = QtGui.QLabel(self.CreateModels)
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.verticalLayout_18.addWidget(self.label_72)
        self.label_73 = QtGui.QLabel(self.CreateModels)
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.verticalLayout_18.addWidget(self.label_73)
        self.horizontalLayout_14.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setMargin(11)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.create_model_spin = QtGui.QSpinBox(self.CreateModels)
        self.create_model_spin.setMaximum(20)
        self.create_model_spin.setObjectName(_fromUtf8("create_model_spin"))
        self.verticalLayout_19.addWidget(self.create_model_spin)
        self.create_model_spin_2 = QtGui.QSpinBox(self.CreateModels)
        self.create_model_spin_2.setMaximum(20)
        self.create_model_spin_2.setObjectName(_fromUtf8("create_model_spin_2"))
        self.verticalLayout_19.addWidget(self.create_model_spin_2)
        self.create_model_spin_3 = QtGui.QSpinBox(self.CreateModels)
        self.create_model_spin_3.setMaximum(20)
        self.create_model_spin_3.setObjectName(_fromUtf8("create_model_spin_3"))
        self.verticalLayout_19.addWidget(self.create_model_spin_3)
        self.create_model_spin_4 = QtGui.QSpinBox(self.CreateModels)
        self.create_model_spin_4.setMaximum(20)
        self.create_model_spin_4.setObjectName(_fromUtf8("create_model_spin_4"))
        self.verticalLayout_19.addWidget(self.create_model_spin_4)
        self.horizontalLayout_14.addLayout(self.verticalLayout_19)
        self.verticalLayout_17.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setMargin(11)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_74 = QtGui.QLabel(self.CreateModels)
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.horizontalLayout_15.addWidget(self.label_74)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setMargin(11)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_75 = QtGui.QLabel(self.CreateModels)
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.horizontalLayout_16.addWidget(self.label_75)
        self.label_76 = QtGui.QLabel(self.CreateModels)
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.horizontalLayout_16.addWidget(self.label_76)
        self.label_77 = QtGui.QLabel(self.CreateModels)
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.horizontalLayout_16.addWidget(self.label_77)
        self.label_78 = QtGui.QLabel(self.CreateModels)
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.horizontalLayout_16.addWidget(self.label_78)
        self.label_79 = QtGui.QLabel(self.CreateModels)
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.horizontalLayout_16.addWidget(self.label_79)
        self.label_83 = QtGui.QLabel(self.CreateModels)
        self.label_83.setObjectName(_fromUtf8("label_83"))
        self.horizontalLayout_16.addWidget(self.label_83)
        self.label_84 = QtGui.QLabel(self.CreateModels)
        self.label_84.setObjectName(_fromUtf8("label_84"))
        self.horizontalLayout_16.addWidget(self.label_84)
        self.label_88 = QtGui.QLabel(self.CreateModels)
        self.label_88.setObjectName(_fromUtf8("label_88"))
        self.horizontalLayout_16.addWidget(self.label_88)
        self.label_89 = QtGui.QLabel(self.CreateModels)
        self.label_89.setObjectName(_fromUtf8("label_89"))
        self.horizontalLayout_16.addWidget(self.label_89)
        self.label_90 = QtGui.QLabel(self.CreateModels)
        self.label_90.setObjectName(_fromUtf8("label_90"))
        self.horizontalLayout_16.addWidget(self.label_90)
        self.label_91 = QtGui.QLabel(self.CreateModels)
        self.label_91.setObjectName(_fromUtf8("label_91"))
        self.horizontalLayout_16.addWidget(self.label_91)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)
        self.verticalLayout_17.addLayout(self.horizontalLayout_15)
        self.verticalLayout_8.addWidget(self.CreateModels)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuPreprocessing = QtGui.QMenu(self.menuBar)
        self.menuPreprocessing.setObjectName(_fromUtf8("menuPreprocessing"))
        self.menuBaseline_Removal = QtGui.QMenu(self.menuPreprocessing)
        self.menuBaseline_Removal.setObjectName(_fromUtf8("menuBaseline_Removal"))
        self.menuCalibration_Transfer = QtGui.QMenu(self.menuPreprocessing)
        self.menuCalibration_Transfer.setObjectName(_fromUtf8("menuCalibration_Transfer"))
        self.menuVisualization = QtGui.QMenu(self.menuBar)
        self.menuVisualization.setObjectName(_fromUtf8("menuVisualization"))
        self.menuClustering = QtGui.QMenu(self.menuVisualization)
        self.menuClustering.setObjectName(_fromUtf8("menuClustering"))
        self.menuRegression = QtGui.QMenu(self.menuBar)
        self.menuRegression.setObjectName(_fromUtf8("menuRegression"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionLoad_Refence_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Refence_Data.setObjectName(_fromUtf8("actionLoad_Refence_Data"))
        self.actionLoad_Unknown_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Unknown_Data.setObjectName(_fromUtf8("actionLoad_Unknown_Data"))
        self.actionSave_Current_Workflow = QtGui.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName(_fromUtf8("actionSave_Current_Workflow"))
        self.actionSave_Current_Plots = QtGui.QAction(MainWindow)
        self.actionSave_Current_Plots.setObjectName(_fromUtf8("actionSave_Current_Plots"))
        self.actionSave_Current_Data = QtGui.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName(_fromUtf8("actionSave_Current_Data"))
        self.actionCreate_New_Workflow = QtGui.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName(_fromUtf8("actionCreate_New_Workflow"))
        self.actionNoise_Reduction = QtGui.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName(_fromUtf8("actionNoise_Reduction"))
        self.actionApply_Mask = QtGui.QAction(MainWindow)
        self.actionApply_Mask.setObjectName(_fromUtf8("actionApply_Mask"))
        self.actionInterpolate = QtGui.QAction(MainWindow)
        self.actionInterpolate.setObjectName(_fromUtf8("actionInterpolate"))
        self.actionInstrument_Response = QtGui.QAction(MainWindow)
        self.actionInstrument_Response.setObjectName(_fromUtf8("actionInstrument_Response"))
        self.actionALS = QtGui.QAction(MainWindow)
        self.actionALS.setObjectName(_fromUtf8("actionALS"))
        self.actionDietrich = QtGui.QAction(MainWindow)
        self.actionDietrich.setObjectName(_fromUtf8("actionDietrich"))
        self.actionPolyFit = QtGui.QAction(MainWindow)
        self.actionPolyFit.setObjectName(_fromUtf8("actionPolyFit"))
        self.actionAirPLS = QtGui.QAction(MainWindow)
        self.actionAirPLS.setObjectName(_fromUtf8("actionAirPLS"))
        self.actionFABC = QtGui.QAction(MainWindow)
        self.actionFABC.setObjectName(_fromUtf8("actionFABC"))
        self.actionKK = QtGui.QAction(MainWindow)
        self.actionKK.setObjectName(_fromUtf8("actionKK"))
        self.actionMario = QtGui.QAction(MainWindow)
        self.actionMario.setObjectName(_fromUtf8("actionMario"))
        self.actionMedian = QtGui.QAction(MainWindow)
        self.actionMedian.setObjectName(_fromUtf8("actionMedian"))
        self.actionRubberband = QtGui.QAction(MainWindow)
        self.actionRubberband.setObjectName(_fromUtf8("actionRubberband"))
        self.actionUndecimated_Wavelet = QtGui.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName(_fromUtf8("actionUndecimated_Wavelet"))
        self.actionRatio = QtGui.QAction(MainWindow)
        self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
        self.actionTommy_s_Methgod = QtGui.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName(_fromUtf8("actionTommy_s_Methgod"))
        self.actionPiecewise_Direct_Standardization = QtGui.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName(_fromUtf8("actionPiecewise_Direct_Standardization"))
        self.actionPCA = QtGui.QAction(MainWindow)
        self.actionPCA.setObjectName(_fromUtf8("actionPCA"))
        self.actionICA = QtGui.QAction(MainWindow)
        self.actionICA.setObjectName(_fromUtf8("actionICA"))
        self.actionK_Means = QtGui.QAction(MainWindow)
        self.actionK_Means.setObjectName(_fromUtf8("actionK_Means"))
        self.actionHierarchical = QtGui.QAction(MainWindow)
        self.actionHierarchical.setObjectName(_fromUtf8("actionHierarchical"))
        self.actionOthers = QtGui.QAction(MainWindow)
        self.actionOthers.setObjectName(_fromUtf8("actionOthers"))
        self.actionOthers_2 = QtGui.QAction(MainWindow)
        self.actionOthers_2.setObjectName(_fromUtf8("actionOthers_2"))
        self.actionOthers_3 = QtGui.QAction(MainWindow)
        self.actionOthers_3.setObjectName(_fromUtf8("actionOthers_3"))
        self.actionPLS = QtGui.QAction(MainWindow)
        self.actionPLS.setObjectName(_fromUtf8("actionPLS"))
        self.actionSM_PLS = QtGui.QAction(MainWindow)
        self.actionSM_PLS.setObjectName(_fromUtf8("actionSM_PLS"))
        self.actionICA_Regression = QtGui.QAction(MainWindow)
        self.actionICA_Regression.setObjectName(_fromUtf8("actionICA_Regression"))
        self.actionGaussian_Process = QtGui.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName(_fromUtf8("actionGaussian_Process"))
        self.actionMLP = QtGui.QAction(MainWindow)
        self.actionMLP.setObjectName(_fromUtf8("actionMLP"))
        self.actionSVM = QtGui.QAction(MainWindow)
        self.actionSVM.setObjectName(_fromUtf8("actionSVM"))
        self.actionOthers_4 = QtGui.QAction(MainWindow)
        self.actionOthers_4.setObjectName(_fromUtf8("actionOthers_4"))
        self.actionOthers_5 = QtGui.QAction(MainWindow)
        self.actionOthers_5.setObjectName(_fromUtf8("actionOthers_5"))
        self.actionIndex = QtGui.QAction(MainWindow)
        self.actionIndex.setObjectName(_fromUtf8("actionIndex"))
        self.actionContent_2 = QtGui.QAction(MainWindow)
        self.actionContent_2.setObjectName(_fromUtf8("actionContent_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_QtCreator = QtGui.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName(_fromUtf8("actionAbout_QtCreator"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNormalization = QtGui.QAction(MainWindow)
        self.actionNormalization.setObjectName(_fromUtf8("actionNormalization"))
        self.menuFile.addAction(self.actionLoad_Refence_Data)
        self.menuFile.addAction(self.actionLoad_Unknown_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Current_Plots)
        self.menuFile.addAction(self.actionSave_Current_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCreate_New_Workflow)
        self.menuFile.addAction(self.actionSave_Current_Workflow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBaseline_Removal.addAction(self.actionALS)
        self.menuBaseline_Removal.addAction(self.actionDietrich)
        self.menuBaseline_Removal.addAction(self.actionPolyFit)
        self.menuBaseline_Removal.addAction(self.actionAirPLS)
        self.menuBaseline_Removal.addAction(self.actionFABC)
        self.menuBaseline_Removal.addAction(self.actionKK)
        self.menuBaseline_Removal.addAction(self.actionMario)
        self.menuBaseline_Removal.addAction(self.actionMedian)
        self.menuBaseline_Removal.addAction(self.actionRubberband)
        self.menuBaseline_Removal.addAction(self.actionUndecimated_Wavelet)
        self.menuCalibration_Transfer.addAction(self.actionRatio)
        self.menuCalibration_Transfer.addAction(self.actionTommy_s_Methgod)
        self.menuCalibration_Transfer.addAction(self.actionPiecewise_Direct_Standardization)
        self.menuCalibration_Transfer.addAction(self.actionOthers_3)
        self.menuPreprocessing.addAction(self.actionNormalization)
        self.menuPreprocessing.addAction(self.actionNoise_Reduction)
        self.menuPreprocessing.addAction(self.actionApply_Mask)
        self.menuPreprocessing.addAction(self.actionInterpolate)
        self.menuPreprocessing.addAction(self.actionInstrument_Response)
        self.menuPreprocessing.addAction(self.menuCalibration_Transfer.menuAction())
        self.menuPreprocessing.addAction(self.menuBaseline_Removal.menuAction())
        self.menuClustering.addAction(self.actionK_Means)
        self.menuClustering.addAction(self.actionHierarchical)
        self.menuClustering.addAction(self.actionOthers)
        self.menuClustering.addAction(self.actionOthers_2)
        self.menuVisualization.addAction(self.actionPCA)
        self.menuVisualization.addAction(self.actionICA)
        self.menuVisualization.addAction(self.menuClustering.menuAction())
        self.menuRegression.addAction(self.actionPLS)
        self.menuRegression.addAction(self.actionSM_PLS)
        self.menuRegression.addAction(self.actionICA_Regression)
        self.menuRegression.addAction(self.actionGaussian_Process)
        self.menuRegression.addAction(self.actionMLP)
        self.menuRegression.addAction(self.actionSVM)
        self.menuRegression.addAction(self.actionOthers_4)
        self.menuRegression.addAction(self.actionOthers_5)
        self.menuHelp.addAction(self.actionIndex)
        self.menuHelp.addAction(self.actionContent_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_QtCreator)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPreprocessing.menuAction())
        self.menuBar.addAction(self.menuVisualization.menuAction())
        self.menuBar.addAction(self.menuRegression.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT", None))
        self.CreateModels.setTitle(_translate("MainWindow", "Create Models", None))
        self.label_70.setText(_translate("MainWindow", "Value 1", None))
        self.label_71.setText(_translate("MainWindow", "Value 2", None))
        self.label_72.setText(_translate("MainWindow", "Value 3", None))
        self.label_73.setText(_translate("MainWindow", "Value 4", None))
        self.label_74.setText(_translate("MainWindow", "ncs", None))
        self.label_75.setText(_translate("MainWindow", "[", None))
        self.label_76.setText(_translate("MainWindow", "(", None))
        self.label_77.setText(_translate("MainWindow", "0", None))
        self.label_78.setText(_translate("MainWindow", ",", None))
        self.label_79.setText(_translate("MainWindow", "0", None))
        self.label_83.setText(_translate("MainWindow", ",", None))
        self.label_84.setText(_translate("MainWindow", "0", None))
        self.label_88.setText(_translate("MainWindow", ",", None))
        self.label_89.setText(_translate("MainWindow", "0", None))
        self.label_90.setText(_translate("MainWindow", ")", None))
        self.label_91.setText(_translate("MainWindow", "]", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuPreprocessing.setTitle(_translate("MainWindow", "Preprocessing", None))
        self.menuBaseline_Removal.setTitle(_translate("MainWindow", "Baseline Removal", None))
        self.menuCalibration_Transfer.setTitle(_translate("MainWindow", "Calibration Transfer", None))
        self.menuVisualization.setTitle(_translate("MainWindow", "Visualization", None))
        self.menuClustering.setTitle(_translate("MainWindow", "Clustering", None))
        self.menuRegression.setTitle(_translate("MainWindow", "Regression", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data", None))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data", None))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow", None))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots", None))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data", None))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow", None))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction", None))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask", None))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate", None))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response", None))
        self.actionALS.setText(_translate("MainWindow", "ALS", None))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich", None))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit", None))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS", None))
        self.actionFABC.setText(_translate("MainWindow", "FABC", None))
        self.actionKK.setText(_translate("MainWindow", "KK", None))
        self.actionMario.setText(_translate("MainWindow", "Mario", None))
        self.actionMedian.setText(_translate("MainWindow", "Median", None))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband", None))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet", None))
        self.actionRatio.setText(_translate("MainWindow", "Ratio", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))
        self.actionPiecewise_Direct_Standardization.setText(_translate("MainWindow", "Piecewise Direct Standardization", None))
        self.actionPCA.setText(_translate("MainWindow", "PCA", None))
        self.actionICA.setText(_translate("MainWindow", "ICA", None))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means", None))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionOthers.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_2.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_3.setText(_translate("MainWindow", "Others...", None))
        self.actionPLS.setText(_translate("MainWindow", "PLS", None))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS", None))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression", None))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process", None))
        self.actionMLP.setText(_translate("MainWindow", "MLP", None))
        self.actionSVM.setText(_translate("MainWindow", "SVM", None))
        self.actionOthers_4.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_5.setText(_translate("MainWindow", "Others...", None))
        self.actionIndex.setText(_translate("MainWindow", "Index", None))
        self.actionContent_2.setText(_translate("MainWindow", "Content", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About QtCreator...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization", None))


        QtCore.QObject.connect(self.create_model_spin_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_79.setNum)
        QtCore.QObject.connect(self.create_model_spin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_77.setNum)
        QtCore.QObject.connect(self.create_model_spin_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_84.setNum)
        QtCore.QObject.connect(self.create_model_spin_4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_89.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

