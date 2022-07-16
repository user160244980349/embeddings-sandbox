import fasttext
import os

from pprint import pprint

from opp.reader import read_opp, prepare_data
from kmeans.kmeans import clusterize, get_optimal_k
from config import resources


def main():
    # policies = read_opp()

    # model = fasttext.train_unsupervised(
        # os.path.join(resources, "opp_sample.data"), "cbow", minn=2, maxn=5, dim=300)
    # model.save_model(os.path.join(resources, "opp_fasttext_model.bin"))
    model = fasttext.load_model(os.path.join(resources, "opp_fasttext_model.bin"))

    data = [model.get_word_vector(x) for x in model.words]
    get_optimal_k(data, 10, 1500, 3)
    # pprint(clusterize(data, k=400))



if __name__ == "__main__":
    main()
    # prepare_data()

