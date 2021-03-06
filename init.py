
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    """Сгенерировано на основе Qt Designer. Класс инициализации интерфейса"""

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Optimizers Visualization")
        Form.resize(1851, 805)
        font = QtGui.QFont()
        font.setPointSize(13)
        Form.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radio_rmsprop = QtWidgets.QRadioButton(Form)
        self.radio_rmsprop.setObjectName("radio_rmsprop")
        self.gridLayout.addWidget(self.radio_rmsprop, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 17, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 14, 0, 1, 1)
        self.val_sgd_mu = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_sgd_mu.setFont(font)
        self.val_sgd_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.val_sgd_mu.setObjectName("val_sgd_mu")
        self.gridLayout.addWidget(self.val_sgd_mu, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 13, 0, 1, 1)
        self.dial_adagrad_eps = QtWidgets.QDial(Form)
        self.dial_adagrad_eps.setMinimum(1)
        self.dial_adagrad_eps.setMaximum(100000000)
        self.dial_adagrad_eps.setPageStep(1)
        self.dial_adagrad_eps.setProperty("value", 10)
        self.dial_adagrad_eps.setObjectName("dial_adagrad_eps")
        self.gridLayout.addWidget(self.dial_adagrad_eps, 6, 5, 2, 1)
        self.label_adadelta_eps = QtWidgets.QLabel(Form)
        self.label_adadelta_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adadelta_eps.setObjectName("label_adadelta_eps")
        self.gridLayout.addWidget(self.label_adadelta_eps, 13, 5, 1, 1)
        self.val_adam_beta = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adam_beta.setFont(font)
        self.val_adam_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adam_beta.setObjectName("val_adam_beta")
        self.gridLayout.addWidget(self.val_adam_beta, 19, 3, 1, 1)
        self.label_adam_eps = QtWidgets.QLabel(Form)
        self.label_adam_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adam_eps.setObjectName("label_adam_eps")
        self.gridLayout.addWidget(self.label_adam_eps, 18, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 10, 0, 1, 1)
        self.val_adadelta_mu = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adadelta_mu.setFont(font)
        self.val_adadelta_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adadelta_mu.setObjectName("val_adadelta_mu")
        self.gridLayout.addWidget(self.val_adadelta_mu, 14, 2, 1, 1)
        self.dial_adadelta_eps = QtWidgets.QDial(Form)
        self.dial_adadelta_eps.setMinimum(1)
        self.dial_adadelta_eps.setMaximum(100000000)
        self.dial_adadelta_eps.setPageStep(1)
        self.dial_adadelta_eps.setProperty("value", 10)
        self.dial_adadelta_eps.setObjectName("dial_adadelta_eps")
        self.gridLayout.addWidget(self.dial_adadelta_eps, 11, 5, 2, 1)
        self.val_rms_eps = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_rms_eps.setFont(font)
        self.val_rms_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.val_rms_eps.setObjectName("val_rms_eps")
        self.gridLayout.addWidget(self.val_rms_eps, 4, 5, 1, 1)
        self.val_adam_mu = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adam_mu.setFont(font)
        self.val_adam_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adam_mu.setObjectName("val_adam_mu")
        self.gridLayout.addWidget(self.val_adam_mu, 19, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 18, 0, 1, 1)
        self.label_adadelta_gamma = QtWidgets.QLabel(Form)
        self.label_adadelta_gamma.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adadelta_gamma.setObjectName("label_adadelta_gamma")
        self.gridLayout.addWidget(self.label_adadelta_gamma, 13, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 8, 0, 1, 1)
        self.val_adam_eps = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adam_eps.setFont(font)
        self.val_adam_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adam_eps.setObjectName("val_adam_eps")
        self.gridLayout.addWidget(self.val_adam_eps, 19, 5, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 11, 0, 1, 1)
        self.dial_adam_mu = QtWidgets.QDial(Form)
        self.dial_adam_mu.setMinimum(1)
        self.dial_adam_mu.setMaximum(2000)
        self.dial_adam_mu.setPageStep(1)
        self.dial_adam_mu.setProperty("value", 100)
        self.dial_adam_mu.setObjectName("dial_adam_mu")
        self.gridLayout.addWidget(self.dial_adam_mu, 16, 2, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 16, 0, 1, 1)
        self.label_momentum_beta = QtWidgets.QLabel(Form)
        self.label_momentum_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_momentum_beta.setObjectName("label_momentum_beta")
        self.gridLayout.addWidget(self.label_momentum_beta, 8, 3, 1, 1)
        self.dial_rms_eps = QtWidgets.QDial(Form)
        self.dial_rms_eps.setMinimum(1)
        self.dial_rms_eps.setMaximum(100000000)
        self.dial_rms_eps.setPageStep(1)
        self.dial_rms_eps.setProperty("value", 10)
        self.dial_rms_eps.setObjectName("dial_rms_eps")
        self.gridLayout.addWidget(self.dial_rms_eps, 1, 5, 2, 1)
        self.label_adagrad = QtWidgets.QLabel(Form)
        self.label_adagrad.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adagrad.setObjectName("label_adagrad")
        self.gridLayout.addWidget(self.label_adagrad, 5, 4, 1, 2)
        self.dial_momentum_mu = QtWidgets.QDial(Form)
        self.dial_momentum_mu.setMinimum(1)
        self.dial_momentum_mu.setMaximum(6000)
        self.dial_momentum_mu.setPageStep(1)
        self.dial_momentum_mu.setProperty("value", 100)
        self.dial_momentum_mu.setObjectName("dial_momentum_mu")
        self.gridLayout.addWidget(self.dial_momentum_mu, 6, 2, 2, 1)
        self.val_adagrad_mu = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adagrad_mu.setFont(font)
        self.val_adagrad_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adagrad_mu.setObjectName("val_adagrad_mu")
        self.gridLayout.addWidget(self.val_adagrad_mu, 9, 4, 1, 1)
        self.val_adadelta_eps = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adadelta_eps.setFont(font)
        self.val_adadelta_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adadelta_eps.setObjectName("val_adadelta_eps")
        self.gridLayout.addWidget(self.val_adadelta_eps, 14, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 19, 0, 1, 1)
        self.val_momentum_mu = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_momentum_mu.setFont(font)
        self.val_momentum_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.val_momentum_mu.setObjectName("val_momentum_mu")
        self.gridLayout.addWidget(self.val_momentum_mu, 9, 2, 1, 1)
        self.label_momentum_mu = QtWidgets.QLabel(Form)
        self.label_momentum_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_momentum_mu.setObjectName("label_momentum_mu")
        self.gridLayout.addWidget(self.label_momentum_mu, 8, 2, 1, 1)
        self.val_rms_mu = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_rms_mu.setFont(font)
        self.val_rms_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.val_rms_mu.setObjectName("val_rms_mu")
        self.gridLayout.addWidget(self.val_rms_mu, 4, 3, 1, 1)
        self.label_adam_beta = QtWidgets.QLabel(Form)
        self.label_adam_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adam_beta.setObjectName("label_adam_beta")
        self.gridLayout.addWidget(self.label_adam_beta, 18, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 12, 0, 1, 1)
        self.surface_img = QtWidgets.QLabel(Form)
        self.surface_img.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surface_img.sizePolicy().hasHeightForWidth())
        self.surface_img.setSizePolicy(sizePolicy)
        self.surface_img.setMaximumSize(QtCore.QSize(1100, 768))
        self.surface_img.setMouseTracking(False)
        self.surface_img.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.surface_img.setAcceptDrops(False)
        self.surface_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.surface_img.setFrameShadow(QtWidgets.QFrame.Plain)
        self.surface_img.setLineWidth(1)
        self.surface_img.setMidLineWidth(-4)
        self.surface_img.setText("")
        self.surface_img.setPixmap(QtGui.QPixmap("Himmelblau's function.png"))
        self.surface_img.setScaledContents(True)
        self.surface_img.setAlignment(QtCore.Qt.AlignCenter)
        self.surface_img.setOpenExternalLinks(True)
        self.surface_img.setObjectName("surface_img")
        self.gridLayout.addWidget(self.surface_img, 0, 1, 20, 1)
        self.dial_adadelta_gamma = QtWidgets.QDial(Form)
        self.dial_adadelta_gamma.setMinimum(1)
        self.dial_adadelta_gamma.setMaximum(1000)
        self.dial_adadelta_gamma.setPageStep(1)
        self.dial_adadelta_gamma.setProperty("value", 100)
        self.dial_adadelta_gamma.setObjectName("dial_adadelta_gamma")
        self.gridLayout.addWidget(self.dial_adadelta_gamma, 11, 4, 2, 1)
        self.dial_momentum_beta = QtWidgets.QDial(Form)
        self.dial_momentum_beta.setMinimum(1)
        self.dial_momentum_beta.setMaximum(1000)
        self.dial_momentum_beta.setPageStep(1)
        self.dial_momentum_beta.setProperty("value", 900)
        self.dial_momentum_beta.setObjectName("dial_momentum_beta")
        self.gridLayout.addWidget(self.dial_momentum_beta, 6, 3, 2, 1)
        self.radio_momentum = QtWidgets.QRadioButton(Form)
        self.radio_momentum.setObjectName("radio_momentum")
        self.gridLayout.addWidget(self.radio_momentum, 3, 0, 1, 1)
        self.val_adadelta_beta = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adadelta_beta.setFont(font)
        self.val_adadelta_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adadelta_beta.setObjectName("val_adadelta_beta")
        self.gridLayout.addWidget(self.val_adadelta_beta, 14, 3, 1, 1)
        self.label_rms_mu = QtWidgets.QLabel(Form)
        self.label_rms_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rms_mu.setObjectName("label_rms_mu")
        self.gridLayout.addWidget(self.label_rms_mu, 3, 3, 1, 1)
        self.label_adagrad_eps = QtWidgets.QLabel(Form)
        self.label_adagrad_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adagrad_eps.setObjectName("label_adagrad_eps")
        self.gridLayout.addWidget(self.label_adagrad_eps, 8, 5, 1, 1)
        self.label_sgd_mu = QtWidgets.QLabel(Form)
        self.label_sgd_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sgd_mu.setObjectName("label_sgd_mu")
        self.gridLayout.addWidget(self.label_sgd_mu, 3, 2, 1, 1)
        self.dial_adadelta_beta = QtWidgets.QDial(Form)
        self.dial_adadelta_beta.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dial_adadelta_beta.setMouseTracking(False)
        self.dial_adadelta_beta.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dial_adadelta_beta.setMinimum(1)
        self.dial_adadelta_beta.setMaximum(1000)
        self.dial_adadelta_beta.setPageStep(1)
        self.dial_adadelta_beta.setProperty("value", 100)
        self.dial_adadelta_beta.setObjectName("dial_adadelta_beta")
        self.gridLayout.addWidget(self.dial_adadelta_beta, 11, 3, 2, 1)
        self.label_rms_eps = QtWidgets.QLabel(Form)
        self.label_rms_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rms_eps.setObjectName("label_rms_eps")
        self.gridLayout.addWidget(self.label_rms_eps, 3, 5, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 7, 0, 1, 1)
        self.label_sgd = QtWidgets.QLabel(Form)
        self.label_sgd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sgd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_sgd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sgd.setObjectName("label_sgd")
        self.gridLayout.addWidget(self.label_sgd, 0, 2, 1, 1)
        self.label_adagrad_mu = QtWidgets.QLabel(Form)
        self.label_adagrad_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adagrad_mu.setObjectName("label_adagrad_mu")
        self.gridLayout.addWidget(self.label_adagrad_mu, 8, 4, 1, 1)
        self.dial_rms_beta = QtWidgets.QDial(Form)
        self.dial_rms_beta.setMinimum(1)
        self.dial_rms_beta.setMaximum(1000)
        self.dial_rms_beta.setPageStep(1)
        self.dial_rms_beta.setProperty("value", 900)
        self.dial_rms_beta.setObjectName("dial_rms_beta")
        self.gridLayout.addWidget(self.dial_rms_beta, 1, 4, 2, 1)
        self.label_rms = QtWidgets.QLabel(Form)
        self.label_rms.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rms.setObjectName("label_rms")
        self.gridLayout.addWidget(self.label_rms, 0, 3, 1, 3)
        self.val_momentum_beta = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_momentum_beta.setFont(font)
        self.val_momentum_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.val_momentum_beta.setObjectName("val_momentum_beta")
        self.gridLayout.addWidget(self.val_momentum_beta, 9, 3, 1, 1)
        self.dial_adam_beta = QtWidgets.QDial(Form)
        self.dial_adam_beta.setMinimum(1)
        self.dial_adam_beta.setMaximum(1000)
        self.dial_adam_beta.setPageStep(1)
        self.dial_adam_beta.setProperty("value", 900)
        self.dial_adam_beta.setObjectName("dial_adam_beta")
        self.gridLayout.addWidget(self.dial_adam_beta, 16, 3, 2, 1)
        self.radio_adagrad = QtWidgets.QRadioButton(Form)
        self.radio_adagrad.setObjectName("radio_adagrad")
        self.gridLayout.addWidget(self.radio_adagrad, 4, 0, 1, 1)
        self.label_adadelta_beta = QtWidgets.QLabel(Form)
        self.label_adadelta_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adadelta_beta.setObjectName("label_adadelta_beta")
        self.gridLayout.addWidget(self.label_adadelta_beta, 13, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem11, 9, 0, 1, 1)
        self.dial_adadelta_mu = QtWidgets.QDial(Form)
        self.dial_adadelta_mu.setMinimum(1)
        self.dial_adadelta_mu.setMaximum(10000)
        self.dial_adadelta_mu.setPageStep(1)
        self.dial_adadelta_mu.setProperty("value", 100)
        self.dial_adadelta_mu.setObjectName("dial_adadelta_mu")
        self.gridLayout.addWidget(self.dial_adadelta_mu, 11, 2, 2, 1)
        self.val_adam_gamma = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adam_gamma.setFont(font)
        self.val_adam_gamma.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adam_gamma.setObjectName("val_adam_gamma")
        self.gridLayout.addWidget(self.val_adam_gamma, 19, 4, 1, 1)
        self.val_adadelta_gamma = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adadelta_gamma.setFont(font)
        self.val_adadelta_gamma.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adadelta_gamma.setObjectName("val_adadelta_gamma")
        self.gridLayout.addWidget(self.val_adadelta_gamma, 14, 4, 1, 1)
        self.dial_adagrad_mu = QtWidgets.QDial(Form)
        self.dial_adagrad_mu.setMinimum(1)
        self.dial_adagrad_mu.setMaximum(1000)
        self.dial_adagrad_mu.setPageStep(1)
        self.dial_adagrad_mu.setProperty("value", 400)
        self.dial_adagrad_mu.setObjectName("dial_adagrad_mu")
        self.gridLayout.addWidget(self.dial_adagrad_mu, 6, 4, 2, 1)
        self.label_adadelta = QtWidgets.QLabel(Form)
        self.label_adadelta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adadelta.setObjectName("label_adadelta")
        self.gridLayout.addWidget(self.label_adadelta, 10, 2, 1, 4)
        self.dial_rms_mu = QtWidgets.QDial(Form)
        self.dial_rms_mu.setMinimum(1)
        self.dial_rms_mu.setMaximum(6000)
        self.dial_rms_mu.setPageStep(1)
        self.dial_rms_mu.setProperty("value", 100)
        self.dial_rms_mu.setOrientation(QtCore.Qt.Horizontal)
        self.dial_rms_mu.setInvertedAppearance(False)
        self.dial_rms_mu.setInvertedControls(False)
        self.dial_rms_mu.setWrapping(False)
        self.dial_rms_mu.setNotchesVisible(False)
        self.dial_rms_mu.setObjectName("dial_rms_mu")
        self.gridLayout.addWidget(self.dial_rms_mu, 1, 3, 2, 1)
        self.label_adam = QtWidgets.QLabel(Form)
        self.label_adam.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adam.setObjectName("label_adam")
        self.gridLayout.addWidget(self.label_adam, 15, 2, 1, 4)
        self.dial_sgd_mu = QtWidgets.QDial(Form)
        self.dial_sgd_mu.setEnabled(True)
        self.dial_sgd_mu.setMinimumSize(QtCore.QSize(0, 0))
        self.dial_sgd_mu.setMinimum(1)
        self.dial_sgd_mu.setMaximum(2000)
        self.dial_sgd_mu.setPageStep(1)
        self.dial_sgd_mu.setProperty("value", 100)
        self.dial_sgd_mu.setObjectName("dial_sgd_mu")
        self.gridLayout.addWidget(self.dial_sgd_mu, 1, 2, 2, 1)
        self.radio_adadelta = QtWidgets.QRadioButton(Form)
        self.radio_adadelta.setObjectName("radio_adadelta")
        self.gridLayout.addWidget(self.radio_adadelta, 5, 0, 1, 1)
        self.label_adadelta_mu = QtWidgets.QLabel(Form)
        self.label_adadelta_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adadelta_mu.setObjectName("label_adadelta_mu")
        self.gridLayout.addWidget(self.label_adadelta_mu, 13, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem12, 15, 0, 1, 1)
        self.dial_adam_gamma = QtWidgets.QDial(Form)
        self.dial_adam_gamma.setAcceptDrops(False)
        self.dial_adam_gamma.setAutoFillBackground(False)
        self.dial_adam_gamma.setMinimum(1)
        self.dial_adam_gamma.setMaximum(1000)
        self.dial_adam_gamma.setPageStep(1)
        self.dial_adam_gamma.setProperty("value", 900)
        self.dial_adam_gamma.setOrientation(QtCore.Qt.Vertical)
        self.dial_adam_gamma.setObjectName("dial_adam_gamma")
        self.gridLayout.addWidget(self.dial_adam_gamma, 16, 4, 2, 1)
        self.label_adam_gamma = QtWidgets.QLabel(Form)
        self.label_adam_gamma.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adam_gamma.setObjectName("label_adam_gamma")
        self.gridLayout.addWidget(self.label_adam_gamma, 18, 4, 1, 1)
        self.radio_adam = QtWidgets.QRadioButton(Form)
        self.radio_adam.setObjectName("radio_adam")
        self.gridLayout.addWidget(self.radio_adam, 6, 0, 1, 1)
        self.label_momentum = QtWidgets.QLabel(Form)
        self.label_momentum.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_momentum.setAlignment(QtCore.Qt.AlignCenter)
        self.label_momentum.setObjectName("label_momentum")
        self.gridLayout.addWidget(self.label_momentum, 5, 2, 1, 2)
        self.val_rms_beta = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_rms_beta.setFont(font)
        self.val_rms_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.val_rms_beta.setObjectName("val_rms_beta")
        self.gridLayout.addWidget(self.val_rms_beta, 4, 4, 1, 1)
        self.val_adagrad_eps = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.val_adagrad_eps.setFont(font)
        self.val_adagrad_eps.setAlignment(QtCore.Qt.AlignCenter)
        self.val_adagrad_eps.setObjectName("val_adagrad_eps")
        self.gridLayout.addWidget(self.val_adagrad_eps, 9, 5, 1, 1)
        self.label_rms_beta = QtWidgets.QLabel(Form)
        self.label_rms_beta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rms_beta.setObjectName("label_rms_beta")
        self.gridLayout.addWidget(self.label_rms_beta, 3, 4, 1, 1)
        self.label_adam_mu = QtWidgets.QLabel(Form)
        self.label_adam_mu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_adam_mu.setObjectName("label_adam_mu")
        self.gridLayout.addWidget(self.label_adam_mu, 18, 2, 1, 1)
        self.dial_adam_eps = QtWidgets.QDial(Form)
        self.dial_adam_eps.setMinimum(1)
        self.dial_adam_eps.setMaximum(100000000)
        self.dial_adam_eps.setPageStep(1)
        self.dial_adam_eps.setProperty("value", 10)
        self.dial_adam_eps.setObjectName("dial_adam_eps")
        self.gridLayout.addWidget(self.dial_adam_eps, 16, 5, 2, 1)
        self.radio_sgd = QtWidgets.QRadioButton(Form)
        self.radio_sgd.setObjectName("radio_sgd")
        self.radio_sgd.setChecked(True)
        self.gridLayout.addWidget(self.radio_sgd, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(self._translate("Optimizers Visualization", "Optimizers Visualization"))
        self.radio_rmsprop.setText(self._translate("Optimizers Visualization", "RMSProp optimizer"))
        self.val_sgd_mu.setText(self._translate("Optimizers Visualization", "0.01"))
        self.label_adadelta_eps.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&epsilon;</p></body></html>"))
        self.val_adam_beta.setText(self._translate("Optimizers Visualization", "0.9"))
        self.label_adam_eps.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&epsilon;</p></body></html>"))
        self.val_adadelta_mu.setText(self._translate("Optimizers Visualization", "0.01"))
        self.val_rms_eps.setText(self._translate("Optimizers Visualization", "0.000001"))
        self.val_adam_mu.setText(self._translate("Optimizers Visualization", "0.01"))
        self.label_adadelta_gamma.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&gamma;</p></body></html>"))
        self.val_adam_eps.setText(self._translate("Optimizers Visualization", "0.000001"))
        self.comboBox.setItemText(0, self._translate("Optimizers Visualization", "Himmelblau's function"))
        self.comboBox.setItemText(1, self._translate("Optimizers Visualization", "Beale function"))
        self.comboBox.setItemText(2, self._translate("Optimizers Visualization", "Booth function"))
        self.comboBox.setItemText(3, self._translate("Optimizers Visualization", "Bukin function"))
        self.comboBox.setItemText(4, self._translate("Optimizers Visualization", "Matyas function"))
        self.comboBox.setItemText(5, self._translate("Optimizers Visualization", "McCormick function"))
        self.comboBox.setItemText(6, self._translate("Optimizers Visualization", "Sphere function"))
        self.label_momentum_beta.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&beta;</p></body></html>"))
        self.label_adagrad.setText(self._translate("Optimizers Visualization", "Adagrad"))
        self.val_adagrad_mu.setText(self._translate("Optimizers Visualization", "0.4"))
        self.val_adadelta_eps.setText(self._translate("Optimizers Visualization", "0.000001"))
        self.val_momentum_mu.setText(self._translate("Optimizers Visualization", "0.01"))
        self.label_momentum_mu.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&mu;</p></body></html>"))
        self.val_rms_mu.setText(self._translate("Optimizers Visualization", "0.01"))
        self.label_adam_beta.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&beta;</p></body></html>"))
        self.radio_momentum.setText(self._translate("Optimizers Visualization", "Momentum optimizer"))
        self.val_adadelta_beta.setText(self._translate("Optimizers Visualization", "0.9"))
        self.label_rms_mu.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&mu;</p></body></html>"))
        self.label_adagrad_eps.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&epsilon;</p></body></html>"))
        self.label_sgd_mu.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&mu;</p></body></html>"))
        self.label_rms_eps.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&epsilon;</p></body></html>"))
        self.label_sgd.setText(self._translate("Optimizers Visualization", "SGD"))
        self.label_adagrad_mu.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&mu;</p></body></html>"))
        self.label_rms.setText(self._translate("Optimizers Visualization", "RMSProp"))
        self.val_momentum_beta.setText(self._translate("Optimizers Visualization", "0.9"))
        self.radio_adagrad.setText(self._translate("Optimizers Visualization", "Adagrad optimizer"))
        self.label_adadelta_beta.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&beta;</p></body></html>"))
        self.val_adam_gamma.setText(self._translate("Optimizers Visualization", "0.9"))
        self.val_adadelta_gamma.setText(self._translate("Optimizers Visualization", "0.9"))
        self.label_adadelta.setText(self._translate("Optimizers Visualization", "Adadelta"))
        self.label_adam.setText(self._translate("Optimizers Visualization", "Adam"))
        self.label_adam.setText(self._translate("Optimizers Visualization", "Adam"))
        self.radio_adadelta.setText(self._translate("Optimizers Visualization", "Adadelta optimizer"))
        self.label_adadelta_mu.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&mu;</p></body></html>"))
        self.label_adam_gamma.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&gamma;</p></body></html>"))
        self.radio_adam.setText(self._translate("Optimizers Visualization", "Adam optimizer"))
        self.label_momentum.setText(self._translate("Optimizers Visualization", "Momentum"))
        self.val_rms_beta.setText(self._translate("Optimizers Visualization", "0.9"))
        self.val_adagrad_eps.setText(self._translate("Optimizers Visualization", "0.000001"))
        self.label_rms_beta.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&beta;</p></body></html>"))
        self.label_adam_mu.setText(self._translate("Optimizers Visualization", "<html><head/><body><p>&mu;</p></body></html>"))
        self.radio_sgd.setText(self._translate("Optimizers Visualization", "Stohastic Gradient Descent"))