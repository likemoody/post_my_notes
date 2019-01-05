# Database Querying
class QueryPosts:
    @staticmethod
    def query_posts(model, sort_by='desc', order_by='date_posted', **kwargs):
        sort = '-' + str(order_by)
        if sort_by == 'asc':
            sort = str(order_by)
        return model.objects.filter(**kwargs).order_by(sort)
