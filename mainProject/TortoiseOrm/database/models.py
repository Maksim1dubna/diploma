from tortoise import fields, models

class Task(models.Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField(max_length=500)
    date_created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "tasks"