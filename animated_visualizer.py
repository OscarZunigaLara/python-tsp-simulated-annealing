import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def animateTSP(history, points):
    ''' animate the solution over time

        Parameters
        ----------
        hisotry : list
            history of the solutions chosen by the algorith
        points: array_like
            points with the coordinates
    '''

    ''' approx 1500 frames for animation '''

    key_frames_mult = len(history) // 200

    fig, ax = plt.subplots()

    ''' path is a line coming through all the nodes '''
    line, = plt.plot([], [], lw=2)

    def init():
        ''' initialize node dots on graph '''
        x = [points[i][0] for i in history[0]]
        y = [points[i][1] for i in history[0]]
        plt.plot(x, y, 'co')
        ##ADDING NAMES TO THE NODES

        dictCapital = {-99.12766: "Ciudad de México ", -98.20193: "Puebla de Zaragoza ", -103.39182: "Guadalajara", -100.31847:"Monterrey",
                       -106.08889: "Chihuahua", -89.61696: "Mérida", -101.0053: "Saltillo", -102.28259: "Aguascalientes",
                       -110.97732: "Hermosillo", -115.45446: "Mexicali", -100.9855: "San Luis Potosí", -107.7321500: "Culiacán Rosales",
                      -100.38806: "Santiago de Querétaro", -101.18443: "Morelia",  -104.65756: "Durango", -93.11308: "Tuxtla Gutiérrez",
                      -96.91589: "Xalapa-Enríquez", -104.89569: "Tepic", -99.23075: "Cuernavaca", -92.93028: "Villahermosa",
                       -99.14599: "Ciudad Victoria", -98.73329: "Pachuca de Soto", -96.72365: "Oaxaca de Juárez", -110.3005: "La Paz",
                      -90.52554: "San Francisco de Campeche", -99.50578: "Chilpancingo de los Bravo", -99.65324: "Toluca de Lerdo", -88.30381: "Chetumal",
                      -103.72714: "Colima", -102.58141: "Zacatecas", -101.2591: "Guanajuato", -98.19982: "Tlaxcala de Xicohténcatl"}

        for i in range(32):
            plt.annotate(dictCapital[x[i]], (x[i], y[i]))

        #Mapa Pais

        img = plt.imread("mapaMexico.jpg")
        ax.imshow(img, extent=[-117, -89, 15, 33])

        ''' draw axes slighty bigger  '''
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

        '''initialize solution to be empty '''
        line.set_data([], [])
        return line,

    def update(frame):
        ''' for every frame update the solution on the graph '''
        x = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        y = [points[i, 1] for i in history[frame] + [history[frame][0]]]
        line.set_data(x, y)
        return line

    ''' animate precalulated solutions '''

    ani = FuncAnimation(fig, update, frames=range(0, len(history), key_frames_mult),
                        init_func=init, interval=3, repeat=False)

    plt.show()
