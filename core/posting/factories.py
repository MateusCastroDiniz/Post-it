from .models import *
import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda x: "%s@exemple.com" % x.first_name)
    birthday = factory.Faker('date_of_birth')

    class Meta:
        model = User

    def __str__(self):
        return self.email


class ProfileFactory(factory.django.DjangoModelFactory):
    email = factory.SubFactory(UserFactory)
    username = factory.Faker('name')
    # birthday = factory.Faker('date_of_birth')

    class Meta:
        model = Profile


class PostFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(ProfileFactory)
    text_content = factory.Faker('text')

    class Meta:
        model = Post


class CommentFactory(factory.django.DjangoModelFactory):
    content = factory.Faker('text')
    post = factory.SubFactory(PostFactory)
    created_by = factory.SubFactory(ProfileFactory)

    class Meta:
        model = Comment