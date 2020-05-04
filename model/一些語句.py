from model.chat import Chat




def create_index(table_name, field_name, index_name, unique=False, order=False):
    """创建索引"""
    if unique == False:
        if order == 'desc' or order == 'asc':
            Chat.raw("CREATE INDEX {index_name} ON {table_name}({field_name} {order})".format(
                **{"index_name": index_name,
                   "table_name": table_name,
                   "field_name": field_name,
                   "order": order})).execute()
        else:
            Chat.raw("CREATE INDEX {index_name} ON {table_name}({field_name})".format(
                **{"index_name": index_name,
                   "table_name": table_name,
                   "field_name": field_name})).execute()
    else:
        if order == 'desc' or order == 'asc':
            Chat.raw("CREATE UNIQUE INDEX {index_name} ON {table_name}({field_name} {order})".format(
                **{"index_name": index_name,
                   "table_name": table_name,
                   "field_name": field_name,
                   "order": order})).execute()
        else:
            Chat.raw("CREATE UNIQUE INDEX {index_name} ON {table_name}({field_name})".format(
                **{"index_name": index_name,
                   "table_name": table_name,
                   "field_name": field_name})).execute()
