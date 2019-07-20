class VKPost:
    def __init__(self):
        self.title = None
        self.text = None
        self.likes = None
        self.comments = []
        self.num_comments = None
        self.poll = None

    def fill_from_vk_object(self, vk_post, vk_comments):
        instance = vk_post['items'][0]
        self.title = instance['text'].split('\n')[0]
        self.text = '\n'.join(instance['text'].split('\n')[1:])
        self.likes = instance['likes']['count']
        self.num_comments = instance['comments']['count']
        self.fill_from_vk_comments(vk_comments)
        self.fill_from_vk_poll(instance['attachments'][0]['poll'])

    def fill_from_vk_comments(self, vk_comments):
        self.comments = [VKComment(i) for i in vk_comments['items']]

    def fill_from_vk_poll(self, vk_poll):
        self.poll = VKPoll(vk_poll)


class VKComment:
    def __init__(self, vk_comment):
        self.text = None
        self.likes = None
        self.fill_from_vk_object(vk_comment)

    def fill_from_vk_object(self, instance):
        self.text = instance['text']
        self.likes = instance['likes']['count']


class VKPoll:
    def __init__(self, vk_poll):
        self.answers = []
        self.question = None
        self.votes = None
        self.fill_from_vk_object(vk_poll)

    def fill_from_vk_object(self, vk_poll):
        self.answers = [VKAnswer(i) for i in vk_poll['answers']]
        self.question = vk_poll['question']
        self.votes = vk_poll['votes']


class VKAnswer:
    def __init__(self, vk_answer):
        self.rate = None
        self.text = None
        self.votes = None
        self.fill_from_vk_object(vk_answer)

    def fill_from_vk_object(self, vk_answer):
        self.rate = vk_answer['rate']
        self.text = vk_answer['text']
        self.votes = vk_answer['votes']
