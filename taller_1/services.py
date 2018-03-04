import pandas as pd, numpy as np, time, os

def get_possible_artists():
    return {'artists': [
		{'id': 1, 'name': 'Artist 1'},
		{'id': 2, 'name': 'Artist 2'}
		]}

def get_recommendation_by_artists(artists):
    return {'id': 2, 'name': 'AC/DC'}