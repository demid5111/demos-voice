def get_extended_post_id_from_url(url):
    # Example: https://vk.com/moneysecrets?w=wall-184648030_2
    return '-{}'.format(url.split('-')[-1])


def get_post_id_from_url(url):
    # Example: https://vk.com/moneysecrets?w=wall-184648030_2
    return url.split('_')[-1]


def get_group_id_from_url(url):
    # Example: https://vk.com/moneysecrets?w=wall-184648030_2
    return '-{}'.format(url.split('-')[-1].split('_')[0])