from tortoise import Model, fields

class Scam(Model):
    user_id = fields.IntField(max_length=255)
    reason = fields.TextField()
    count_scamming = fields.IntField()
    date = fields.TextField()

class Admins(Model):
    user_id = fields.IntField(max_length=255)
    rank = fields.IntField()
    count_added = fields.IntField()

class Garant(Model):
    user_id = fields.IntField(max_length=255)
    count = fields.IntField()

class User(Model):
    user_id = fields.IntField(max_length=255)