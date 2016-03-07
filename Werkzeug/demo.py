# -*- coding: utf-8 -*

# 使用Werkzeug实现密码散列
from werkzeug.security import generate_password_hash, check_password_hash

# password = 'password'
# password_hash = generate_password_hash(password)
#
# print password_hash
#
# verify_password = False
# verify_password = check_password_hash(password_hash, password)
#
# print verify_password

class Encrypt():
    password_hash = 'password'

    # 加密生成code
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 对比
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


e = Encrypt()

e.password('hello')
print e.password_hash

print e.verify_password('hello')
