import pandas as pd, numpy as np, time, os
from surprise.model_selection import cross_validate, train_test_split, KFold
from surprise import Dataset, Reader, SVD, NormalPredictor, accuracy, evaluate
from surprise.prediction_algorithms.knns import *
from collections import defaultdict

def load_dataset():
    dataset_4 = pd.read_pickle('matriz_final.pickle')
    return dataset_4

def get_possible_artists():
    dataset = load_dataset()
    a_list = dataset['ARTIST_NAME'].drop_duplicates().tolist() 
    a_list.sort()
    return a_list

def get_recommendation_by_artists(artists):
    dataset = load_dataset()

    dataset_4_test = dataset.copy(deep = True)
    data = {
            'USERID': ['user_001001' for x in artists],
            'ARTIST_NAME': artists,
            'VALOR': [5 for x in artists]}
    x = pd.DataFrame(data = data)
    dataset_4_test = dataset_4_test.append(x, ignore_index = True)


    kf = KFold(n_splits = 2)
    reader = Reader(rating_scale = (1, 5))
    data = Dataset.load_from_df(dataset_4_test[['USERID', 'ARTIST_NAME', 'VALOR']], reader)

    for trainset, testset in kf.split(data):
        sim_options = {'name': 'pearson', 'user_based': False}#'min_k': 1, 'k': 1000, 
        algo = KNNBasic(sim_options = sim_options)
        algo.fit(trainset)
        
        test_set = trainset.build_anti_testset()
        
        test = [x for x in test_set if x[0] is "user_001001"]

        predictions = algo.test(test)

    def get_top_n(predictions, n = 10):
        # First map the predictions to each user.
        top_n = defaultdict(list)
        for uid, iid, true_r, est, _ in predictions:
            top_n[uid].append((iid, est))

        # Then sort the predictions for each user and retrieve the k highest ones.
        for uid, user_ratings in top_n.items():
            user_ratings.sort(key = lambda x: x[1], reverse=True)
            top_n[uid] = user_ratings[:n]

        return top_n
    
    def get_top_n(predictions, n = 10):
        # First map the predictions to each user.
        top_n = defaultdict(list)
        for uid, iid, true_r, est, _ in predictions:
            top_n[uid].append((iid, est))

        # Then sort the predictions for each user and retrieve the k highest ones.
        for uid, user_ratings in top_n.items():
            user_ratings.sort(key = lambda x: x[1], reverse=True)
            top_n[uid] = user_ratings[:n]

        return top_n

    top_n = get_top_n(predictions, n = 10)
    top_n = dict(top_n)
    return top_n['user_001001']
