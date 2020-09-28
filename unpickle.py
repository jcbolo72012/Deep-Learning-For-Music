import pickle

pickle_off = open("MuseData.pickle","rb")
emp = pickle.load(pickle_off)
print(emp)