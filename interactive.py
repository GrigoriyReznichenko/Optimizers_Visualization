from init import Ui_Form
from PyQt5 import QtGui
import imgs

class ParamsSetter(Ui_Form):
    """Сlass that controls user interaction.
    ATRUBUTES:
    self.draw : bool
        It is a flag, which controls animation and also optimization algorithm calculation.
        If self.draw = True, drawing is available. If it is false, drawing and optimization are crushed.
    self.params: dict
        It is a dict, containing initial parameters of optimization algorithms.
    """
    def __init__(self):
        super(ParamsSetter, self).__init__()
        self.draw = False

        self.params = {'SGD': {'mu': float(self.val_sgd_mu.text())},
                       'Momentum': {'mu': float(self.val_momentum_mu.text()),
                                    'beta': float(self.val_momentum_beta.text())},
                       'Adagrad': {'mu': float(self.val_adagrad_mu.text()), 'eps': float(self.val_adagrad_eps.text())},
                       'RMSProp': {'mu': float(self.val_rms_mu.text()), 'beta': float(self.val_rms_beta.text()),
                                   'eps': float(self.val_rms_eps.text())},
                       'Adadelta': {'mu': float(self.val_adadelta_mu.text()),
                                    'beta': float(self.val_adadelta_beta.text()),
                                    'gamma': float(self.val_adadelta_gamma.text()),
                                    'eps': float(self.val_adadelta_eps.text())},
                       'Adam': {'mu': float(self.val_adam_mu.text()), 'beta': float(self.val_adam_beta.text()),
                                'gamma': float(self.val_adam_gamma.text()), 'eps': float(self.val_adam_eps.text())}}


        """Here are constructions which are used to set self.params dict parameters and set self.draw to False"""
        self.comboBox.currentTextChanged.connect(self.set_surface)

        self.dial_sgd_mu.valueChanged.connect(self.set_sgd_mu_dial)
        self.dial_rms_mu.valueChanged.connect(self.set_rms_mu_dial)
        self.dial_rms_beta.valueChanged.connect(self.set_rms_beta_dial)
        self.dial_rms_eps.valueChanged.connect(self.set_rms_eps_dial)
        self.dial_momentum_mu.valueChanged.connect(self.set_momentum_mu_dial)
        self.dial_momentum_beta.valueChanged.connect(self.set_momentum_beta_dial)
        self.dial_adagrad_mu.valueChanged.connect(self.set_adagrad_mu_dial)
        self.dial_adagrad_eps.valueChanged.connect(self.set_adagrad_eps_dial)
        self.dial_adadelta_mu.valueChanged.connect(self.set_adadelta_mu_dial)
        self.dial_adadelta_beta.valueChanged.connect(self.set_adadelta_beta_dial)
        self.dial_adadelta_gamma.valueChanged.connect(self.set_adadelta_gamma_dial)
        self.dial_adadelta_eps.valueChanged.connect(self.set_adadelta_eps_dial)
        self.dial_adam_mu.valueChanged.connect(self.set_adam_mu_dial)
        self.dial_adam_beta.valueChanged.connect(self.set_adam_beta_dial)
        self.dial_adam_gamma.valueChanged.connect(self.set_adam_gamma_dial)
        self.dial_adam_eps.valueChanged.connect(self.set_adam_eps_dial)

        self.val_sgd_mu.textChanged.connect(self.set_sgd_mu_text)
        self.val_rms_mu.textChanged.connect(self.set_rms_mu_text)
        self.val_rms_beta.textChanged.connect(self.set_rms_beta_text)
        self.val_rms_eps.textChanged.connect(self.set_rms_eps_text)
        self.val_momentum_mu.textChanged.connect(self.set_momentum_mu_text)
        self.val_momentum_beta.textChanged.connect(self.set_momentum_beta_text)
        self.val_adagrad_mu.textChanged.connect(self.set_adagrad_mu_text)
        self.val_adagrad_eps.textChanged.connect(self.set_adagrad_eps_text)
        self.val_adadelta_mu.textChanged.connect(self.set_adadelta_mu_text)
        self.val_adadelta_beta.textChanged.connect(self.set_adadelta_beta_text)
        self.val_adadelta_gamma.textChanged.connect(self.set_adadelta_gamma_text)
        self.val_adadelta_eps.textChanged.connect(self.set_adadelta_eps_text)
        self.val_adam_mu.textChanged.connect(self.set_adam_mu_text)
        self.val_adam_beta.textChanged.connect(self.set_adam_beta_text)
        self.val_adam_gamma.textChanged.connect(self.set_adam_gamma_text)
        self.val_adam_eps.textChanged.connect(self.set_adam_eps_text)


        self.radio_sgd.toggled.connect(self.on_radio_button)
        self.radio_rmsprop.toggled.connect(self.on_radio_button)
        self.radio_adagrad.toggled.connect(self.on_radio_button)
        self.radio_momentum.toggled.connect(self.on_radio_button)
        self.radio_adam.toggled.connect(self.on_radio_button)
        self.radio_adadelta.toggled.connect(self.on_radio_button)

    def on_radio_button(self):
        self.draw = False

    def set_surface(self, name):
        """Redraw center label with current surface"""
        self.draw = False
        surfaces = {"Himmelblau's function": "Himmelblau's function.png",
                    "Beale function": "Beale function.png",
                    "Booth function": "Booth function.png",
                    "Bukin function": "Bukin function.png",
                    "Matyas function": "Matyas function.png",
                    "McCormick function": "McCormick function.png",
                    "Sphere function": "Sphere function.png"}
        self.surface_img.setPixmap(QtGui.QPixmap(surfaces[name]))

    def set_sgd_mu_text(self, event):
        """stop drawing and check if current value is inside allowed range.
        If it is true, then set corresponding param to self.dict and update dial value"""
        self.draw = False
        try:
            event = float(event)
            if 0.0001 <= event <= 0.2:
                self.params['SGD']['mu'] = event
                self.dial_sgd_mu.setValue(int(event * 10000))
        except ValueError:
            pass

    def set_rms_mu_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.0001 <= event <= 0.6:
                self.params['RMSProp']['mu'] = event
                self.dial_rms_mu.setValue(int(event * 10000))
        except ValueError:
            pass

    def set_rms_beta_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.001 <= event <= 1:
                self.params['RMSProp']['beta'] = event
                self.dial_rms_beta.setValue(int(event * 1000))
        except ValueError:
            pass

    def set_rms_eps_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.000001 <= event <= 100:
                self.params['RMSProp']['eps'] = event
                self.dial_rms_eps.setValue(int(event * 1000000))
        except ValueError:
            pass

    def set_momentum_mu_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.0001 <= event <= 0.6:
                self.params['Momentum']['mu'] = event
                self.dial_momentum_mu.setValue(int(event * 10000))
        except ValueError:
            pass

    def set_momentum_beta_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.001 <= event <= 1:
                self.params['Momentum']['beta'] = event
                self.dial_momentum_beta.setValue(int(event * 1000))
        except ValueError:
            pass

    def set_adagrad_mu_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.002 <= event <= 2:
                self.params['Adagrad']['mu'] = event
                self.dial_adagrad_mu.setValue(int(event * 500))
        except ValueError:
            pass

    def set_adagrad_eps_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.000001 <= event <= 100:
                self.params['Adagrad']['eps'] = event
                self.dial_adagrad_eps.setValue(int(event * 1000000))
        except ValueError:
            pass

    def set_adadelta_mu_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.0001 <= event <= 1:
                self.params['Adadelta']['mu'] = event
                self.dial_adadelta_mu.setValue(int(event * 10000))
        except ValueError:
            pass

    def set_adadelta_beta_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.001 <= event <= 1:
                self.params['Adadelta']['beta'] = event
                self.dial_adadelta_beta.setValue(int(event * 1000))
        except ValueError:
            pass

    def set_adadelta_gamma_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.001 <= event <= 1:
                self.params['Adadelta']['gamma'] = event
                self.dial_adadelta_gamma.setValue(int(event * 1000))
        except ValueError:
            pass

    def set_adadelta_eps_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.000001 <= event <= 1:
                self.params['Adadelta']['eps'] = event
                self.dial_adadelta_eps.setValue(int(event * 1000000))
        except ValueError:
            pass

    def set_adam_mu_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.0001 <= event <= 0.2:
                self.params['Adam']['mu'] = event
                self.dial_adam_mu.setValue(int(event * 10000))
        except ValueError:
            pass

    def set_adam_beta_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.001 <= event <= 1:
                self.params['Adam']['beta'] = event
                self.dial_adam_beta.setValue(int(event * 1000))
        except ValueError:
            pass

    def set_adam_gamma_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.001 <= event <= 1:
                self.params['Adam']['gamma'] = event
                self.dial_adam_gamma.setValue(int(event * 1000))
        except ValueError:
            pass

    def set_adam_eps_text(self, event):
        self.draw = False
        try:
            event = float(event)
            if 0.000001 <= event <= 1:
                self.params['Adam']['eps'] = event
                self.dial_adam_eps.setValue(int(event * 1000000))
        except ValueError:
            pass

    def set_sgd_mu_dial(self, val):
        """Stop drawing and set param to self.params and set it to corresponding QLineText"""
        self.draw = False
        self.params['SGD']['mu'] = val / 10000
        self.val_sgd_mu.setText(self._translate("Form", f"{val / 10000}"))

    def set_rms_mu_dial(self, val):
        self.draw = False
        self.params['RMSProp']['mu'] = val / 10000
        self.val_rms_mu.setText(self._translate("Form", f"{val / 10000}"))

    def set_rms_beta_dial(self, val):
        self.draw = False
        self.params['RMSProp']['beta'] = val / 1000
        self.val_rms_beta.setText(self._translate("Form", f"{val / 1000}"))

    def set_rms_eps_dial(self, val):
        self.draw = False
        self.params['RMSProp']['eps'] = val / 1000000
        self.val_rms_eps.setText(self._translate("Form", f"{val / 1000000}"))

    def set_momentum_mu_dial(self, val):
        self.draw = False
        self.params['Momentum']['mu'] = val / 10000
        self.val_momentum_mu.setText(self._translate("Form", f"{val / 10000}"))

    def set_momentum_beta_dial(self, val):
        self.draw = False
        self.params['Momentum']['beta'] = val / 1000
        self.val_momentum_beta.setText(self._translate("Form", f"{val / 1000}"))

    def set_adagrad_mu_dial(self, val):
        self.draw = False
        self.params['Adagrad']['mu'] = val / 500
        self.val_adagrad_mu.setText(self._translate("Form", f"{val / 500}"))

    def set_adagrad_eps_dial(self, val):
        self.draw = False
        self.params['Adagrad']['eps'] = val / 1000000
        self.val_adagrad_eps.setText(self._translate("Form", f"{val / 1000000}"))

    def set_adadelta_mu_dial(self, val):
        self.draw = False
        self.params['Adadelta']['mu'] = val / 10000
        self.val_adadelta_mu.setText(self._translate("Form", f"{val / 10000}"))

    def set_adadelta_beta_dial(self, val):
        self.draw = False
        self.params['Adadelta']['beta'] = val / 1000
        self.val_adadelta_beta.setText(self._translate("Form", f"{val / 1000}"))

    def set_adadelta_gamma_dial(self, val):
        self.draw = False
        self.params['Adadelta']['gamma'] = val / 1000
        self.val_adadelta_gamma.setText(self._translate("Form", f"{val / 1000}"))

    def set_adadelta_eps_dial(self, val):
        self.draw = False
        self.params['Adadelta']['eps'] = val / 1000000
        self.val_adadelta_eps.setText(self._translate("Form", f"{val / 1000000}"))

    def set_adam_mu_dial(self, val):
        self.draw = False
        self.params['Adam']['mu'] = val / 10000
        self.val_adam_mu.setText(self._translate("Form", f"{val / 10000}"))

    def set_adam_beta_dial(self, val):
        self.draw = False
        self.params['Adam']['beta'] = val / 1000
        self.val_adam_beta.setText(self._translate("Form", f"{val / 1000}"))

    def set_adam_gamma_dial(self, val):
        self.draw = False
        self.params['Adam']['gamma'] = val / 1000
        self.val_adam_gamma.setText(self._translate("Form", f"{val / 1000}"))

    def set_adam_eps_dial(self, val):
        self.draw = False
        self.params['Adam']['eps'] = val / 1000000
        self.val_adam_eps.setText(self._translate("Form", f"{val / 1000000}"))