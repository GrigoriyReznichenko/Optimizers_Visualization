import numpy as np
from numpy.linalg import norm


class Derivatives:
    """
    Class containing lambda functions used to calculate gradients. These functions are partial derivatives/
    METHODS:
    _______
    get_grad: returns lambda function
        Method which plays the role of a switch with input "adrress bits" represented as names
    """

    def get_grad(self, surface):
        if surface == "Himmelblau's function":  # Min locations : (3, 3), (-2.8, 3.13), (-3.78, -3.28), (-3.58, -1.84)
            return self.Himmelblaus_grad(), surface
        elif surface == "Beale function":  # Min location: (3, 0.5)
            return self.Beale_grad(), surface
        elif surface == "Booth function":  # Min location: (1, 3)
            return self.booth_grad(), surface
        elif surface == "Bukin function":  # Min location: (-10, 1)
            return self.Bukin_n6_grad(), surface
        elif surface == "Matyas function":  # Min location: (0, 0)
            return self.Matyas_grad(), surface
        elif surface == "McCormick function":  # Min location: (-0.55, -1.55)
            return self.McCormick_grad(), surface
        elif surface == "Sphere function":  # Min location: (0, 0)
            return self.sphere_grad(), surface

    def Himmelblaus_grad(self):
        grad = lambda x, y: [2 * (pow(x, 2) + 2 * y * (x + pow(y, 2) - 7) + y - 11),
                             2 * (pow(y, 2) + 2 * x * (y + pow(x, 2) - 11) + x - 7)]
        return grad

    def Beale_grad(self):
        grad = lambda x, y: [2 * x * (pow(y, 6) + pow(y, 4) - 2 * pow(y, 3) - pow(y, 2) - 2 * y + 3) + \
                             5.25 * pow(y, 3) + 4.5 * pow(y, 2) + 3 * y - 12.75,
                             6 * x * (x * (pow(y, 5) + 2 / 3 * pow(y, 3) - pow(y, 2) - 1 / 3) + \
                                      2.625 * pow(y, 2) + 1.5 * y + 0.5)]
        return grad

    def booth_grad(self):
        grad = lambda x, y: [10 * x + 8 * y - 34, 8 * x + 10 * y - 38]
        return grad

    def Bukin_n6_grad(self):
        grad = lambda x, y: [0.01 * np.sign(x + 10) + (x * (y - 0.01 * pow(x, 2))) \
                             / pow(np.abs(y - 0.01 * pow(x, 2)), 3 / 2),
                             (50 * (y - 0.01 * pow(x, 2))) / pow(np.abs(y - 0.01 * pow(x, 2)), 3 / 2)]
        return grad

    def Matyas_grad(self):
        grad = lambda x, y: [0.52 * x - 0.48 * y, 0.52 * y - 0.48 * x]
        return grad

    def McCormick_grad(self):
        grad = lambda x, y: [np.cos(x + y) + 2 * x - 2 * y - 1.5, np.cos(x + y) - 2 * x + 2 * y + 2.5]
        return grad

    def sphere_grad(self):
        grad = lambda x, y: [2 * x, 2 * y]
        return grad


class Algorithms:
    """Class with algorithms used to Neural Network optimization. The main idea is ot start calculating as soon as possible.
    And than, using drawPoint QPainter PyQt5 class method start paining current value

    ATTRIBUTES:
    __________
    self.stop_flag: bool
        This is the flag which turns off algorithms on interaction with interface
    self.params: dict
        It's a dict which contains init algorithms parameters
    self.grad: lambda function
        function used to calculate dx dy vector of partial derivatives
    self.init: np.array
        inital weigths
    self.init: list
        List which contain weigths of algorithms
    minimas: dict
        It contains minima points according to surface name
    self.location: dict
        It's an auxiliary dict used for stopping criterion as norm of difference between minima coords and current weigths = current coords

    METHODS:
        sgd(): Calculates Stohastic Gradient Descent weights https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Implicit_updates_(ISGD)
        momentum(): Calculates Momentum weights https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Momentum
        adagrad(): Calculates Adagrad weights  https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad
        rmsprop(): Calculates RMSProp weights  https://en.wikipedia.org/wiki/Stochastic_gradient_descent#RMSProp
        adam(): Calculates Adam weights  https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam
        Adadelta(): Calculates Adadelta weights  https://d2l.ai/chapter_optimization/adadelta.html
        rho params devided into beta and gamma params.
        beta is used to calculate exponential moving average for square gradient vector:
        gamma is used to calculate exponential moving average for scaled square gradient vector:
        https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average


    """

    def __init__(self, grad_func, params, init_vals):
        self.stop_flag = False
        self.params = params
        self.grad, surface = grad_func
        self.init = np.array(init_vals)
        self.weights = []

        minimas = {"Himmelblau's function": ((3, 3), (-2.8, 3.13), (-3.78, -3.28), (-3.58, -1.84)),
                   "Beale function": (3, 0.5), "Booth function": (1, 3), "Sphere function": (0.0, 0.0),
                   "Bukin function": (-10, 1), "Matyas function": (0, 0), "McCormick function": (-0.55, -1.55)}
        self.location = minimas[surface]

    def sgd(self):
        mu = self.params['SGD']['mu']
        w = self.init.copy()
        it = 0
        while norm(w - self.location) > 1e-7:
            it += 1
            w -= mu * np.array(self.grad(w[0], w[1]))
            self.weights.append([w[0], w[1]])
            if self.stop_flag is True or it == 5000:
                break

    def momentum(self):
        mu, beta = self.params['Momentum']['mu'], self.params['Momentum']['beta']
        w, v = self.init.copy(), np.array((0.0, 0.0))
        it = 0
        while norm(w - self.location) > 1e-7:
            it += 1
            v = beta * v + (1 - beta) * np.array(self.grad(w[0], w[1]))
            w -= mu * v
            self.weights.append([w[0], w[1]])
            if self.stop_flag is True or it == 5000:
                break

    def adagrad(self):
        mu, eps = self.params['Adagrad']['mu'], self.params['Adagrad']['eps']
        w, s = self.init.copy(), np.array((0.0, 0.0))
        it = 0
        while norm(w - self.location) > 1e-7:
            it += 1
            grad = np.array(self.grad(w[0], w[1]))
            s += grad ** 2
            w -= mu / np.sqrt(s + eps) * grad
            self.weights.append([w[0], w[1]])
            if self.stop_flag is True or it == 5000:
                break

    def rmsprop(self):
        mu, beta, eps = self.params['RMSProp']['mu'], self.params['RMSProp']['beta'], self.params['RMSProp']['eps']
        w, s = self.init, np.array((0.0, 0.0))
        it = 0
        while norm(w - self.location) > 1e-7:
            it += 1
            grad = np.array(self.grad(w[0], w[1]))
            s = beta * s + (1 - beta) * grad ** 2
            w -= mu / np.sqrt(s + eps) * grad
            self.weights.append([w[0], w[1]])
            if self.stop_flag is True or it == 5000:
                break

    def adadelta(self):
        params = self.params['Adadelta']
        mu, beta, gamma, eps = params['mu'], params['beta'], params['gamma'], params['eps']
        w, s, v = self.init.copy(), np.array((0.0, 0.0)), np.array((0.0, 0.0))
        it = 0
        while norm(w - self.location) > 1e-7:
            it += 1
            grad = np.array(self.grad(w[0], w[1]))
            v = beta * v + (1 - beta) * np.square(grad)
            dx = np.sqrt(s + eps) / np.sqrt(v + eps) * grad
            w -= mu * dx
            s = gamma * s + (1 - gamma) * np.square(dx)
            self.weights.append([w[0], w[1]])
            if self.stop_flag is True or it == 5000:
                break

    def adam(self):
        params = self.params['Adam']
        mu, beta, gamma, eps = params['mu'], params['beta'], params['gamma'], params['eps']
        w, v, s = self.init.copy(), np.array((0.0, 0.0)), np.array((0.0, 0.0))
        it = 0
        while norm(w - self.location) > 1e-7:
            it += 1
            grad = np.array(self.grad(w[0], w[1]))
            v = beta * v + (1 - beta) * grad
            s = gamma * s + (1 - gamma) * np.square(grad)
            v_scaled = v / (1 - beta ** it)
            s_scaled = s / (1 - gamma ** it)
            w -= mu / (np.sqrt(s_scaled) + eps) * v_scaled
            self.weights.append(np.array([w[0], w[1]]))
            if self.stop_flag is True or it == 5000:
                break