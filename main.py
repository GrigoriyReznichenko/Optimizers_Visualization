import sys
from time import sleep
from PyQt5.QtGui import QPen, QPixmap, QPainter, QColor
from PyQt5 import QtCore
from interactive import ParamsSetter
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
from optimizers import Derivatives, Algorithms


class App(ParamsSetter, QtWidgets.QWidget):
    """class which get coord from mouse left button click, starts optimization and draw it current surface

    ATRIBUTES:
    _________
    self.app: PyQt5.QtWidgets.QApplication used for update event setting graph

    METHODS:
    _______
    paint_event(x, y) this method draws point on current surface using drawPoint
    on_mouse_click: calculates optimizer weights ad start paint_event method to draw

    """

    def __init__(self, app):
        super(App, self).__init__()
        self.app = app
        self.surface_img.mousePressEvent = self.on_mouse_click  # event starts computing and drawing on mouse button click

    def paintEvent(self, event):
        self.surface_img.setPixmap(QPixmap(self.comboBox.currentText()))
        if self.draw is True:
            sleep(0.01)  # used to slow down drawing. draws every 10ms
            pen = QPen()
            pen.setWidth(18)
            pen.setCapStyle(QtCore.Qt.RoundCap)
            pen.setColor(QColor(36, 67, 157, 220))
            painter = QPainter(self.surface_img.pixmap())
            painter.setPen(pen)
            painter.drawPoint(int(self.x), int(self.y))

    def on_mouse_click(self, event):
        """auxiliary_dict contains graph ((x range, y range), (smallest x, smallest y)) on surfaces availabale to test/
        It is used to convert screen linear space to surface linear space by flipping scaling and translate affine transforms"""
        self.draw = False  # stop drawing and calculating instances
        x_coord, y_coord = event.x(), event.y()

        auxiliary_dict = {"Himmelblau's function": ((10, 10), (-5, -5)),
                          "Beale function": ((5, 2.4), (-1, -1.2)),
                          "Booth function": ((8, 8), (-4, -4)),
                          "Bukin function": ((4, 8), (-12, -4)),
                          "Matyas function": ((10, 10), (-5, -5)),
                          "McCormick function": ((10, 10), (-5, -5)),
                          "Sphere function": ((6, 6), (-3, -3))}
        if 140 <= x_coord <= 820 and 95 <= y_coord <= 685:  # if clicked mouse is inside displayed image
            (dx, dy), (x0, y0) = auxiliary_dict[self.comboBox.currentText()]  # get auxilary values
            x_max, y_max = x0 + dx, y0 + dy  # create img max coords
            x_init = (x_coord - 140) * dx / 680 + x0  # make linear transforms to x and y display coord
            y_init = -(y_coord - 95) * dy / 590 - y0
            init_val = x_init, y_init  # pack into tuple
            grad_func = Derivatives().get_grad(self.comboBox.currentText())  # get dervative lambda function
            optimization = Algorithms(grad_func, self.params, init_val)  # init optimizer
            self.draw = True  # start draw
            if self.radio_sgd.isChecked():  # choose optimizer based on radio button
                optimization.sgd()
            elif self.radio_momentum.isChecked():
                optimization.momentum()
            elif self.radio_rmsprop.isChecked():
                optimization.rmsprop()
            elif self.radio_adagrad.isChecked():
                optimization.adagrad()
            elif self.radio_adadelta.isChecked():
                optimization.adadelta()
            elif self.radio_adam.isChecked():
                optimization.adam()

            while optimization.weights != []:  # if weights list is not empty
                x, y = optimization.weights.pop(0)  # pop from class array
                if x < x0 or x > x_max or y < y0 or y > y_max:  # stop calclulating and drawing if algorithm weights are outside image
                    optimization.stop_flag = True
                    self.draw = False
                    break
                # convert weigths to screen coords
                self.x, self.y = round((x - x0) * 680 / dx + 140), round(-(y + y0) * 590 / dy + 95)
                self.app.processEvents()  # force drawing event
                if self.draw is False:  # stop calculation and drawing on mouse click or interation with application
                    optimization.stop_flag = True
                    break




def main():
    app = QtWidgets.QApplication(sys.argv)
    extra = {'font_size': 22}  # set fontsize
    apply_stylesheet(app, theme='dark_red.xml', extra=extra)  # use qt_material application style
    application = App(app)  # update all events
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()