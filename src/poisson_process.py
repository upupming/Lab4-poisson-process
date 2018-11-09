import sys
import numpy
from matplotlib import pyplot

def generate_poisson_process_data(tau, end, lam):
    """
    Generate birth-death process data according o given parameters.

    tau
        a small time interval, see equation (10).
    end
        end time of generated data.
    lam
        lambda parameter for Poisson process
    """

    birth_probability = lam * tau
    def get_next_state(current_state):
        random = numpy.random.random()
        # [0, birth_probability, 1]
        if random < birth_probability:
            return current_state + 1
        elif random < 1:
            return current_state
    
    # X[i] is current state
    # time[i] is current time
    i = 0
    X = numpy.array([0])
    time = numpy.array([0])
    while time[i] < end:
        X = numpy.append(X, get_next_state(X[i]))
        time = numpy.append(time, time[i]+tau)

        i += 1

    grow1In10seconds = 0
    grow2OrMoreIn10seconds = 0
    indeicesBetween10Seconds = int(numpy.ceil(10 / tau))
    for j in range(indeicesBetween10Seconds, i+1):
        if(X[j] - X[j-indeicesBetween10Seconds] == 1):
            grow1In10seconds += 1
        elif(X[j] - X[j-indeicesBetween10Seconds] >= 2):
            grow2OrMoreIn10seconds += 1
    p_grow1In10seconds = grow1In10seconds / (i+1 - indeicesBetween10Seconds)
    p_grow2OrMoreIn10seconds = grow2OrMoreIn10seconds / (i+1 - indeicesBetween10Seconds)

    pyplot.rcParams['font.family'] = 'sans-serif'
    pyplot.rcParams['font.sans-serif'] = ['SimHei', 'Helvetica', 'Calibri']
    pyplot.xlabel('时间 t')
    pyplot.ylabel('状态 X(t)')
    pyplot.title(f'泊松过程模拟 \n $\\tau = {tau}, end\ time = {end}$ \n' f'$\lambda = {lam}$\n' f'10s 内发生 1 次的概率为 {p_grow1In10seconds}\n' f'10s 内发生 2 次及以上的概率为 {p_grow2OrMoreIn10seconds}\n')
    pyplot.plot(time, X)

    # Save to image
    pyplot.savefig(f'../simulation_results/poisson-endtime={end}&lambda={lam}&tau={tau}.png', bbox_inches='tight')
    pyplot.close()

generate_poisson_process_data(1, 1000, 0.05)
generate_poisson_process_data(1, 10000, 0.05)
generate_poisson_process_data(0.1, 10000, 0.05)