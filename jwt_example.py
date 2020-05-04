import time
import jwt
# print(time.time())
a = time.time()
b  = a + 1


# payload
token_dict = {
    'iat': time.time(),  # 时间戳
    'name': 'lowman',  # 自定义的参数
    "exp": b
}

# headers
headers = {
    'alg': "HS256",  # 声明所使用的算法
}

"""headers 中一些固定参数名称的意义"""


# 调用jwt库,生成json web token
jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                       "zhananbudanchou1234678",  # 进行加密签名的密钥
                       algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                       headers=headers,  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)

                       ).decode('ascii')  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str

print(jwt_token)

# 个人测试生成结果如下: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6Ijk1MjcifQ.eyJpYXQiOjE1NTkyNzY5NDEuNDIwODgzNywibmFtZSI6Imxvd21hbiJ9.GyQhOJK8FKD_Gd-ggSEDPPP1Avmz3M5NDVnmfOfrEIY




token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODcyODMzMDguMTQ1NTkxMywibmFtZSI6Imxvd21hbiIsImV4cCI6MTU4NzI4MzMwOS4xNDU1ODh9.jKEO0BrBSpUit8fmw8iqaSAtC-WhRAylQ2hdUsxUEEA"
data = None
try:
    #           需要解析的 jwt        密钥                使用和加密时相同的算法
    data = jwt.decode(token, "zhananbudanchou1234678", algorithms=['HS256'])
except Exception as e:
    # 如果 jwt 被篡改过; 或者算法不正确; 如果设置有效时间, 过了有效期; 或者密钥不相同; 都会抛出相应的异常
    print(e)

# 解析出来的就是 payload 内的数据
print(data)

# 输出: {'iat': 1559276941.4208837, 'name': 'lowman'}