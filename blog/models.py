from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته بندی")
    description = models.TextField(verbose_name="توضیحات")
    parent_category = models.CharField(max_length=50, verbose_name="دسته بندی مادر", default="-")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    position = models.IntegerField(verbose_name="جایگاه")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته‌بندی پست"
        verbose_name_plural = "دسته‌بندی پست ها"
        ordering = ["position"]


class Post(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام")
    description = models.TextField(max_length=500, verbose_name="توضیحات") # meta description
    # tags = models.TagsField # meta tags
    slug = models.SlugField(verbose_name="آدرس پست")
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی")
    publish_time = models.DateTimeField(default=timezone.now(), verbose_name="زمان انتشار")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="زمان نوشتن")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="زمان آخرین تغییر")
    is_active = models.BooleanField(default=True, verbose_name="پست نشان داده شود؟")
    content = RichTextField(verbose_name="محتوای صفحه", blank=True, null=True)

    def __str__(self):
        return self.name

    def jpublish(self):
        return jalali_converter(self.publish_time)
    jpublish.short_description = "زمان انتشار"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments', verbose_name="پست")
    author = models.CharField(max_length=200, verbose_name="کاربر")
    text = models.TextField(verbose_name="متن کامنت")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="زمان ثبت کامنت")
    approved_comment = models.BooleanField(default=False, verbose_name="تایید شده")

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"