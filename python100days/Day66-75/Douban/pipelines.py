

class DoubanPipeline(object):
    # def __init__(self, server, port):
    #     pass

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(crawler.settings['MONGO_SERVER'],
    #                crawler.settings['MONGO_PORT'])
    def process_item(self, item, spider):
        return item