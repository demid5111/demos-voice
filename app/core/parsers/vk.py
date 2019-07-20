import vk as vk_api

from app.constants import ACCESS_TOKEN
from app.core.models.vk_post import VKPost
from app.core.parsers.iparser import IParser
from app.core.parsers.utils import get_extended_post_id_from_url, get_group_id_from_url, \
    get_post_id_from_url


class VKParser(IParser):
    def parse(self, url):
        session = vk_api.Session(access_token=ACCESS_TOKEN)
        vk = vk_api.API(session, v='5.84')
        post_id = get_extended_post_id_from_url(url)
        post = vk.wall.getById(posts=post_id, extended=1, copy_history_depth=200)
        group_id = get_group_id_from_url(url)
        # TODO: check for comments > 100
        num_comments = 100
        post_comments = vk.wall.getComments(owner_id=group_id,
                                            post_id=int(get_post_id_from_url(url)),
                                            need_likes=1,
                                            count=num_comments,
                                            offset=0)
        result_post = VKPost()
        result_post.fill_from_vk_object(post, post_comments)
        return result_post
