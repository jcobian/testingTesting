import os
print("My awesome git repo")
db_user = os.environ.get('DATABASE_USER')
db_password = os.environ.get('DATABASE_PASSWORD')
if db_user and db_password:
    print "DB User: " + db_user


