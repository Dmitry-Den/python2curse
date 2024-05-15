import pickle

def save_as_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
