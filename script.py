import pandas as pd
import tensorflow as tf
import json
from sklearn.preprocessing import StandardScaler

def predict(mq7, mq135):
  model = tf.keras.models.load_model('gas_new.h5')
  df = pd.read_csv('Gas_Sensors_Measurements_value.csv')
  data = df.drop(['Serial Number','MQ2', 'MQ3', 'MQ5', 'MQ6', 'MQ8', 'Corresponding Image Name'], axis=1)

  scaler = StandardScaler()
  scaler.fit(data.drop('Gas', axis=1))

  df_test = pd.DataFrame([[mq7,mq135]], columns=['mq7', 'mq135'])

  data_test = scaler.transform(df_test)
  data_test = pd.DataFrame(data_test, columns=df_test.columns)

  pred = model.predict(data_test)
  kelas = ['No Gas', 'Smoke' ,'Mixture']

  return json.dumps({"hasil": str(kelas[pred.argmax()])})

  