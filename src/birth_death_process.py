import sys
import numpy
from matplotlib import pyplot

def generate_birth_death_process_data(tau, end, lam, mu):
    """
    Generate birth-death process data according o given parameters.

    tau
        a small time interval, see equation (10).
    end
        end time of generated data.
    lam
        birth rates for all states.
    mu
        death rates for all states.
    """

    def get_next_state(current_state):
        birth_probability = 0
        death_probability = 0

        # Special: state 0 can only birth
        if(current_state == 0):
            birth_probability = lam * tau
            death_probability = 0
        else:
            birth_probability = lam * tau
            death_probability = mu * tau
        
        random = numpy.random.random()
        # [0, birth_probability, 1-death_probability, 1]
        if random < birth_probability:
            return current_state + 1
        elif random < 1 - death_probability:
            return current_state
        else:
            return current_state - 1
    
    # X[i] is current state
    # time[i] is current time
    i = 0
    X = numpy.array([0])
    time = numpy.array([0])
    while time[i] < end:
        X = numpy.append(X, get_next_state(X[i]))
        time = numpy.append(time, time[i]+tau)

        i += 1

    pyplot.rcParams['font.family'] = 'sans-serif'
    pyplot.rcParams['font.sans-serif'] = ['SimHei', 'Helvetica', 'Calibri']
    pyplot.xlabel('时间 t')
    pyplot.ylabel('状态 X(t)')
    pyplot.title(f'生灭过程模拟 \n $\\tau = {tau}, end\ time = {end}$ \n' f'$\lambda = {lam}, \mu = {mu}$')
    pyplot.plot(time, X)

    # Save to image
    pyplot.savefig(f'../simulation_results/birth-death-lambda={lam}&mu={mu}&tau={tau}.png', bbox_inches='tight')
    pyplot.close()

generate_birth_death_process_data(1, 1000, 0.05, 0.03)
generate_birth_death_process_data(0.1, 1000, 0.05, 0.03)
generate_birth_death_process_data(0.01, 1000, 0.05, 0.03)