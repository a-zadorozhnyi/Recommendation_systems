#здесь содержатся метрики для использования в проекте

import numpy as np


def hit_rate(recommended_list, bought_list):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def hit_rate_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    top_k = recommended_list[:k]

    flags = np.isin(bought_list, top_k)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def precision(recommended_list, bought_list):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    # flags по спискам товаров
    bought_in_recommended = np.isin(bought_list, recommended_list)
    recommended_in_bought = np.isin(recommended_list, bought_list[bought_in_recommended])

    precision = np.sum(prices_recommended[recommended_in_bought])/np.sum(prices_recommended)

    return precision


def recall(recommended_list, bought_list):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    # flags по спискам товаров
    bought_in_recommended = np.isin(bought_list, recommended_list)
    recommended_in_bought = np.isin(recommended_list, bought_list[bought_in_recommended])

    # меняем только знаменатель
    recall = np.sum(prices_recommended[recommended_in_bought])/np.sum(prices_bought)

    return recall


def ap_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    sum_ = 0
    for i in range(1, k + 1):

        if flags[i] == True:
            p_k = precision_at_k(recommended_list, bought_list, k=i)
            sum_ += p_k

    result = sum_ / k

    return result


import ml_metrics as metrics


def map_k(bought_list, recommended_list, k=5):
    apk = 0
    apk_list = []

    for items in bought_list:
        apk = ap_k(recommended_list, bought_list, k)
        apk_list.append(apk)

    map_k = sum(apk_list) / len(apk_list)

    return map_k


def reciprocal_rank(recommended_list, bought_list, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    inter = list(set(recommended_list[:k]) & set(bought_list))

    index_sum = []
    for i in inter:
        index_sum.append(1 / (list(bought_list).index(i) + 1))
    index = sum(index_sum) / len(index_sum)

    return round(index, 2)

if __name__ == '__main__':
    pass