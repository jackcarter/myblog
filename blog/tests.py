from django.test import TestCase
from blog.models import Post


class PostMethodTest(TestCase):

    def test_slug_collisions_get_resolved(self):
        """
        Titles don't have to be unique, but slugs do. The unique_slugify() function
        should always ensure that we have unique slugs, behind the scenes
        """
        first_post = Post(title="slug?")
        second_post = Post(title="slug!")
        first_post.save()
        second_post.save()
        self.assertNotEquals(first_post.slug, second_post.slug)
