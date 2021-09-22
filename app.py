import numpy as np
import pickle

model=pickle.load(open('model.pkl','rb'))
N = int(input("Enter nitrogen: "))
P = int(input("Enter Phosphorous: "))
K = int(input("Enter Potassium"))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
ph = float(input("Enter pH value: "))
rainfall = float(input("Enter Rainfall in mm: "))


sample = [N, P, K, temperature, humidity, ph, rainfall]
single_sample = np.array(sample).reshape(1,-1)
pred = model.predict(single_sample)
print(pred.item().title())
