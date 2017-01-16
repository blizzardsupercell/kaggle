import pandas as pd
import numpy as np
import time


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def training(X, Y, alpha):
    startTime = time.time()

    numSamples, numFeatures = np.shape(X)

    theta = np.ones((numFeatures, 1))

    for k in range(count):
        theta = theta - alpha * (X.T * (sigmoid(X * theta) - Y)) / numSamples

    print 'Congratulations, training complete! Took %fs!' % (time.time() - startTime)
    return theta

