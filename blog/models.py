from django.db import models

class User(models.Model):
  name = models.CharField(max_length=32)
  mail = models.EmailField()

  # Authorの選択肢を key : usernameで出力する
  def __str__(self):
    return "{}: {}".format(self.pk, self.name)

class Entry(models.Model):
  STATUS_DRAFT = 'draft'
  STATUS_PUBLIC = 'public'
  STATUS_SET = (
    (STATUS_DRAFT, '下書き中'),
    (STATUS_PUBLIC, '公開中'),
  )
  title = models.CharField(max_length=128)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
  author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)