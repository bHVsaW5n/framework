class BaseService:
    def __init__(self):
        pass

    def check_data_frame(self, data):
        """
        校验格式
        :param data:
        :return:
        """
        defined_data_struct = {
            "name": "名称",
            "code": "编码",
            "lines": [{
                "color": "red",
                "size": "S",
                "stock": 1
            }],
            "tree": {
                "node": "节点",
            }
        }
        assert type(defined_data_struct) == type(data)
        if isinstance(defined_data_struct, dict):
            for (k1, v1), (k2, v2) in zip(defined_data_struct.items(), data.items()):
                if type(k1) in [dict, type, list]:
                    pass
                else:
                    assert type(k1) == type(k2)

data = {}
base_service = BaseService()
base_service.check_data_frame(data)
print("sdf")