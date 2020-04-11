import Data

# @return data_test data to test
def first_training():
    quantyty_training = int(0.5 * 4520 * 0.8)
   # quantyty_training = 100
    data_training = Data.data[:quantyty_training]
    quantyty_test = int(0.5 * 4520 * 0.2)
    #quantyty_test = 10
    data_test = Data.data[quantyty_training:quantyty_test + quantyty_training]
    return data_training.values.tolist(), data_test.values.tolist()


##data for secound trainnig
# @return data_training data to training
# @return data_test data to test
def secound_training():
    quantyty_firs = int(0.5 * 4520)
    quantyty_training = quantyty_firs + int(0.25 * 4520 * 0.8)
    data_training = Data.data[quantyty_firs:quantyty_training]
    quantyty_test = int(0.25 * 4520 * 0.2)
    data_test = Data.data[quantyty_training:quantyty_test + quantyty_training]
    return data_training.values.tolist(), data_test.values.tolist()


##data for third trainnig
# @return data_training data to training
# @return data_test data to test
def third_training():
    print("first Data")
    quantyty_firs = int(0.75 * 4520)
    quantyty_training = quantyty_firs + int(0.25 * 4520 * 0.8)
    data_training = Data.data[quantyty_firs:quantyty_training]
    quantyty_test = int(0.25 * 4520 * 0.2)
    data_test = Data.data[quantyty_training:quantyty_test + quantyty_training]
    return data_training.values.tolist(), data_test.values.tolist()
