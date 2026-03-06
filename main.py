import numpy as np
import matplotlib.pyplot as plt
import sys
import functions as fn

#generate x
x = np.linspace(-10, 10, 1000)

#function for saving graphs
def save_plot(x, y, title, filename):
    plt.figure()
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/" + filename)
    plt.close()

def plot_all():
    #linear function
    save_plot(
        x,
        fn.linear(x, 2, 1),
        "Linear Function f(x) = 2x + 1",
        "linear.png"
    )
    #quadratic function
    save_plot(
        x,
        fn.quadratic(x, 1, -2, 1),
        "Quadratic Function f(x) = x^2 - 2x + 1",
        "quadratic.png"
    )
    #sine function
    save_plot(
        x,
        fn.sine(x),
        "Sine Function f(x) = sin(x)",
        "sine.png"
    )
    #exponential function
    save_plot(
        x,
        fn.exponential(x),
        "Exponential Function f(x) = e^x",
        "exponential.png"
    )
    #cubic function
    save_plot(
        x,
        fn.cubic(x),
        "Cubic Function f(x) = x^3",
        "cubic.png"
    )

def plot_multiple():
    plt.figure()
    plt.plot(x, fn.linear(x, 2, 1), label="Linear")
    plt.plot(x, fn.quadratic(x, 1, -2, 1), label="Quadratic")
    plt.plot(x, fn.sine(x), label="Sine")
    plt.title("Multiple Functions")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.savefig("images/multiple_functions.png")
    plt.close()


# point 8
def experiment():
    x_exp = np.linspace(-20, 20, 1000)
    y_exp = fn.sine(x_exp, 3)
    save_plot(
        x_exp,
        y_exp,
        "Experiment: Sine Function f(x) = sin(3x) on interval [-20,20]",
        "experiment_sine.png"
    )

def plot_selected(function_name):
    if function_name == "linear":
        save_plot(x, fn.linear(x, 2, 1),
                  "Linear Function f(x)=2x+1",
                  "linear.png")
    elif function_name == "quadratic":
        save_plot(x, fn.quadratic(x, 1, -2, 1),
                  "Quadratic Function f(x)=x^2-2x+1",
                  "quadratic.png")
    elif function_name == "sin":
        save_plot(x, fn.sine(x),
                  "Sine Function f(x)=sin(x)",
                  "sine.png")
    elif function_name == "exp":
        save_plot(x, fn.exponential(x),
                  "Exponential Function f(x)=e^x",
                  "exponential.png")
    elif function_name == "cubic":
        save_plot(x, fn.cubic(x),
                  "Cubic Function f(x)=x^3",
                  "cubic.png")
    elif function_name == "experiment":
        experiment()
    else:
        print("Unknown function.")
        print("Available options: linear, quadratic, sin, exp, cubic, experiment")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        plot_selected(sys.argv[1])
    else:
        plot_all()
        plot_multiple()
        experiment()
        print("All graphs were generated and saved in the images folder.")