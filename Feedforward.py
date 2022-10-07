def get_train_test(url, split_percent=0.8):
    diff = read_csv(url, usecols=[1], engine='python')
    ourdata = num.array(diff.values.astype('float32'))
    ourscaler = MinMaxScaler(feature_range=(0, 1))
    ourdata = ourscaler.fit_transform(ourdata).flatten()
    pn = len(data)
    
    datasplit = int(pn*split_percent)
    ourtrain_data = data[range(datasplit)]
    ourtest_data = data[datasplit:]
    return ourtrain_data, ourtest_data, ourdata

def get_XY(dat, time_steps):
    inputy = num.arange(time_steps, len(dat), time_steps)
    Y = dat[inputy] 
    inputx = len(Y)
    X = dat[range(time_steps*inputx)]
    X = num.reshape(X, (inputx, time_steps, 1)) 
    return X, Y 
def create_RNN(hidden_units, dense_units, input_shape, activation): 
    ourModel = Sequential()
    ourModel.add(SimpleRNN(hidden_units,input_shape=input_shape,activation=activation[0]))
    ourModel.add(Dense(units=dense_units, activation=activation[1]))
    ourModel.compile(loss='mean_squared_error', optimizer='adam')
    return ourModel 

def print_error(trainY, testY, train_predict, test_predict):    
    train_error = math.sqrt(mean_squared_error(trainY, train_predict))
    test_error = math.sqrt(mean_squared_error(testY, test_predict))
    print('Train RMSE: %.3f RMSE' % (train_error))
    print('Test RMSE: %.3f RMSE' %(test_error))   


def plot_result(trainY, testY, train_predict, test_predict):
    actualData = num.append(trainY, testY)
    predictions = num.append(train_predict, test_predict)
    rows = len(actualData)
    mpl.figure(figsize=(15, 6), dpi=80) 
    mpl.plot(range(rows), actualData)
    mpl.plot(range(rows), predictions)
    mpl.axvline(x=len(trainY), color='r')
    mpl.legend(['Actual data', 'Predicted data'])
    mpl.xlabel('Observation number ')
    mpl.ylabel('Dataset scaled')
    mpl.title('Actual and Predicted Values.')

train_data, test_data, data = get_train_test(dataset_url)
trainX, trainY = get_XY(train_data, time_steps)
testX, testY = get_XY(test_data, time_steps)
ourModel = create_RNN(hidden_units=3, dense_units=1, input_shape=(time_steps,1), activation=['tanh', 'tanh'])
ourModel.fit(trainX, trainY, epochs=20, batch_size=1, verbose=2)
tp = ourModel.predict(trainX)
ts = ourModel.predict(testX)
print_error(trainY, testY, tp, ts) 
plot_result(trainY, testY, tp, ts)
