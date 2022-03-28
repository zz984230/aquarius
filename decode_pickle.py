import pickle


if __name__ == '__main__':
    with open("data/cookies", 'rb') as f:
        print(pickle.load(f))
