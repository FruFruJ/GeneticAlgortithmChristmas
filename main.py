# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
from geneticalgorithm import geneticalgorithm as ga






def mainFunction():
    cena = [1000, 500, 200, 700, 50, 70, 100, 300, 5000, 1500, 200, 600]
    vaznost = [10, 2, 5, 2, 1, 6, 7, 3, 9, 10, 8, 3]
    predmeti = ["jelka za sto", "ukras za vrh jelke", "komplet ukrasa malih", "komplet ukrasa veliki",
                "jedan ukras deda mraz", "jedan ukras irvas", "jedan ukras zvezda", "masna za unutra i spolja",
                "velika jelka", "crevo duzina 8m", "sijalice 3m", "sijalice 8m"];
    print("Dobar dan pomoci cemo vam u vasoj optimalnoj dekoraciji kuce ukrasima")
    budzet=int(input("Unesite vas budzet \n"));
    vaznost=[];
    for x in predmeti:
       vaznost.append(int(input("Na skali od 1-20 nam kazite koliko vam je bitno "+x+" \n")));
    print(vaznost)

    def f(x):
        fit = 0;
        ukCena = 0
        i = 0
        while i in range(0, 12):
            fit += vaznost[i] * x[i]
            ukCena += x[i] * cena[i];
            #print(i)
            i = i + 1
        #print(ukCena)
        if (ukCena > budzet):
            return 0;
        return -fit

    varbound = np.array([[0, 1]] * 12)

    algorithm_param = {'max_num_iteration': 100, \
                       'population_size': 100, \
                       'mutation_probability': 0.1, \
                       'elit_ratio': 0.0, \
                       'crossover_probability': 0.5, \
                       'parents_portion': 0.2, \
                       'crossover_type': 'one_point', \
                       'max_iteration_without_improv': None}

    model = ga(function=f, \
               dimension=12, \
               variable_type='int', \
               variable_boundaries=varbound, \
               algorithm_parameters=algorithm_param)

    model.run()
    print(model.output_dict)
    return

if __name__ == '__main__':
    mainFunction();



