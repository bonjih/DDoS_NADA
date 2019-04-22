
# LSTM (memory blocks) with window regression framing i.e. multipule recent time steps can be used to make the prediction for the next time step

#need to look ar tunning the window size to see if gives a better result - under 'look_backs'


#Given a certain time (t-2,t-1,t), predict the when the pps utilisation (%) will go greater than 80%
#Dates can be ignored if each observation is spearated by the same interval e.g. one day. Therefore the x #axis will represent the number of observations

#Problem Statement

# Given the pps utilisation at time (t), in %, what is the pps utilisation at time t+1?



import numpy
import matplotlib.pyplot as plt
import pandas as pd
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


# def custom_parser(s):
#     return pd.datetime.strptime(s, '%d %H:%M')

dataframe = pd.read_csv('data/test_pps_rx_1_week_epoch.csv', index_col='Date')
dataset = dataframe.fillna(method = 'ffill')


# convert an array of values into a dataset matrix - split single column into two, col1 - t and col2 - t+1
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

# fix random seed for reproducibility
numpy.random.seed(7)

# normalize the dataset i.e. rescale - 0 to 1
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)

# split into train and test sets
train_size = int(len(dataset) * 0.67) #67% for training - 33% for testing
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

# reshape into X=t and Y=t+1
look_back = 3 #number of previous steps used as input variables to predict t+1 - increase to find optimal?
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)

# reshape input to be [samples, features]. Normally LSTM requres [samples, time steps, features]
# Remove if dates ar required. Need to add time steps in LSTM network
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# create and fit the LSTM network - One visible, hidden % output layer with 4 LSTM blocks. Default sigmod activation function is used
model = Sequential()
model.add(LSTM(4, input_dim=look_back))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=3, batch_size=1, verbose=2)

# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)

# invert predictions - ensures that performance is reported in CPU % per day
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])

# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))

# shift train predictions for plotting
trainPredictPlot = numpy.empty_like(dataset)
trainPredictPlot[:, :] = numpy.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict

# shift test predictions for plotting
testPredictPlot = numpy.empty_like(dataset)
testPredictPlot[:, :] = numpy.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict

# plot baseline and predictions
plt.plot(scaler.inverse_transform(dataset), label = 'Original Dataset')
plt.plot(trainPredictPlot, label = 'Predicted Trained')
plt.plot(testPredictPlot, label = 'Predicted pps %')
plt.legend(loc='upper right')
plt.xlabel('Day / Time')
plt.ylabel('pps')
plt.show()
