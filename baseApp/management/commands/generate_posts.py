from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from baseApp.models import Post
from faker import Faker
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Generates mock posts for testing'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of posts to generate')

    def handle(self, *args, **options):
        count = options['count']
        users = User.objects.all()
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create users first.'))
            return

        for _ in range(count):
            try:
                title = fake.sentence(nb_words=random.randint(3, 10))
                content = fake.paragraph(nb_sentences=random.randint(3, 7))
                author = random.choice(users)
                
                post = Post.objects.create(
                    title=title,
                    content=content,
                    author=author
                )
                
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created post: "{post.title}" by {post.author.username}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to create post: {str(e)}')
                ) 