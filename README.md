# Optimizers_Visualization
During the training of neural networks, each of us faced such problems as the termination of loss minimization because of vallyes or surface saddle points, etc. 
Here is an application that will help you draw some conclusions based on which you can improve the training of your neural networks. It shows most popular optimization algorithms in process for low dimension surface case. It visualizes problems like getting stuck at saddle points and how Adam sometimes failures for strongly convex optimization case.

The application demonstrates some of optimization surfaces I've got from here: https://en.wikipedia.org/wiki/Test_functions_for_optimization

The optimization algorithms are:

1) Stohastic gradient descent:

	$w_{k+1}=w_{k}-\mu\nabla J(w_{k+1})$
	
2) Momentum Optimizer:

	$v_{k+1}=\beta v_{k}-\mu\nabla J(w_{k+1})$
	
	$w_{k+1}=w_{k}+v_{k+1}$
	
3) Adagrad Optimizer:

	$s_{k+1}=s_{k}+\nabla^{2}J(w_{k+1})$
	
	$w_{k+1}=w_{k}-\frac{\mu}{\sqrt{s_{k+1}+\varepsilon}}\bigodot\nabla J(w_{k+1}))$
4) RMSProp Otimizer:

	$s_{k+1}=\beta s_{k}+\left(1-\beta\right)\nabla^{2}J(w_{k+1})$
	
	$w_{k+1}=w_{k}-\frac{\mu}{\sqrt{s_{k+1}+\varepsilon}}\bigodot\nabla J(w_{k+1})$

5) Adadelta Optimizer:
	
	$v_{k+1}=\beta v_{k}+\left(1-\beta\right)\nabla^{2}J(w_{k+1})$
	
	$\triangle w=\frac{\sqrt{s_{k+1}+\varepsilon}}{\sqrt{v_{k+1}+\varepsilon}}\bigodot\nabla J(w_{k+1})$
	
	$w_{k+1}=w_{k}-\triangle w$
	
	$s_{k+1}=\gamma s_{k}+\left(1-\gamma\right)\nabla^{2}J(w_{k+1})$
	
For truly based Adadelta it is used to $\gamma = \beta$. In my case there are different hyperparameters for more space of experience.

6) Adam Optimizer:


	while stop criterion coditions are not met:

	$s_{k+1}=\gamma s_{k}+\left(1-\gamma\right)\nabla^{2}J(w_{k+1})$

	$v_{k+1}=\beta v_{k}+\left(1-\beta\right)\nabla J(w_{k+1})$
	
	$s_{k+1}^{scaled}=\frac{s_{k+1}}{1-\gamma^{t}}$
	
	$v_{k+1}^{scaled}=\frac{v_{k+1}}{1-\beta^{t}}$
	
	$w_{k+1}=w_{k}-\frac{\mu}{\sqrt{s_{k+1}^{scaled}+\varepsilon}}v_{k+1}^{scaled}$
	
The codition of convegrence of the algorithm is the case when Euclidian distance between optimal point and current point is smaller then threshold.

##How to use:

Choose surface and optimization parameters. 
Click the left mouse button and visualization will start

![Peek 2022-06-01 05-18](https://user-images.githubusercontent.com/99965144/171304169-9e595915-1d2d-4cce-9954-ff1c91951f1a.gif)


	
		
		
	
