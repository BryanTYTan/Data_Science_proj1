import csv
import numpy as np
from sklearn.svm import SVR
from matplotlib import pyplot as plt

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csv_file_reader = csv.reader(csvfile)
        next(csv_file_reader)
        for row in csv_file_reader:
            dates.append(int(row[0].split('-')[2]))
            prices.append(float(row[1]))
    return 

def predict_price(dates, prices, x):
    dates = np.reshape(dates,(len(dates),1))

    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)


    svr_lin.fit(dates,prices)
    svr_poly.fit(dates,prices)
    svr_rbf.fit(dates,prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_lin.predict(dates), color='blue', label='Liner')
    plt.plot(dates, svr_poly.predict(dates), color='red', label='poly')
    plt.plot(dates, svr_rbf.predict(dates), color='green', label='RBF')
    
    plt.xlabel("Date"), plt.ylabel("Price"), plt.title("Support Vector Regressions"), plt.legend(), plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


def main():
    get_data("Data_sets/AAPL.csv")

    predicted_price = predict_price(dates, prices, 29)

    print(predicted_price)

    return




main()