'''from pymongo import MongoClient

client = MongoClient('localhost', 27017)'''

from elasticsearch import Elasticsearch
client=Elasticsearch([{'host':'localhost','port':9200,'scheme':'http'}])

