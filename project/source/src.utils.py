
def train_test_split(data, test_size_weeks=3):

    data.columns = [col.lower() for col in data.columns]
    data.rename(columns={'household_key': 'user_id',
                         'product_id': 'item_id'},
                inplace=True)

    test_size_weeks = 3

    data_train = data[data['week_no'] < data['week_no'].max() - test_size_weeks]
    data_test = data[data['week_no'] >= data['week_no'].max() - test_size_weeks]

    return data_test, data_train



def prefilter_items(data):
    # Уберем самые популярные товары (их и так купят)
    popularity = data_train.groupby('item_id')['user_id'].nunique().reset_index() / data_train['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)

    top_popular = popularity[popularity['share_unique_users'] > 0.5].item_id.tolist()
    data = data[~data['item_id'].isin(top_popular)]

    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.01].item_id.tolist()
    data = data[~data['item_id'].isin(top_notpopular)]

    # Уберем товары, которые не продавались за последние 12 месяцев

    # Уберем не интересные для рекоммендаций категории (department)

    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.

    # Уберем слишком дорогие товарыs

    # ...


def postfilter_items(user_id, recommednations):
    pass