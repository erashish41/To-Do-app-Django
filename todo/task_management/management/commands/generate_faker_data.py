from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from task_management.models import (
    Category, Tag, Task, SubTask, Comment
)
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = "Seed large fake data for task management app"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(" Seeding fake data started..."))



        users = []
        for i in range(1, 21):
            user, created = User.objects.get_or_create(
                username=f"user{i}",
                defaults={"email": f"user{i}@test.com"}
            )
            if created:
                user.set_password("test1234")
                user.save()
            users.append(user)

        self.stdout.write(" 20 users created")


        category_names = [

            ("Work", "Office related work"),
            ("Personal", "Personal tasks"),
            ("Mobile", "Mobile related tasks"),
            ("Entertainment", "Movies, games, fun"),
            ("Learning", "Study and skill building"),
            ("Health", "Fitness and health"),
            ("Finance", "Money and bills"),
            ("Travel", "Trips and planning"),
        ]

        categories = []
        for user in users:
            for name, desc in category_names:
                category, _ = Category.objects.get_or_create(
                    name=f"{name}-{user.username}",
                    created_by=user,
                    defaults={"description": desc}
                )
                categories.append(category)

        self.stdout.write(" Categories created")


        tag_names = [
            "urgent", "low-priority", "backend", "frontend",

            "django", "bug", "feature", "review", "api",
            "design", "testing", "refactor", "database",
            "devops", "research", "meeting", "home",
            "office", "mobile", "fun"
        ]

        tags = []
        for user in users:
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(
                    name=f"{name}-{user.username}",
                    created_by=user
                )
                tags.append(tag)

        self.stdout.write(" 20 tags per user created")


        tasks = []
        for i in range(1, 21):
            user = random.choice(users)

            user_categories = Category.objects.filter(created_by=user)
            user_tags = Tag.objects.filter(created_by=user)

            task = Task.objects.create(
                title=f"Task {i} for {user.username}",
                priority=random.choice(["low", "medium", "high"]),
                description=f"This is task {i} description",
                status=random.choice(["pending", "in_progress", "completed"]),
                due_date=date.today() + timedelta(days=random.randint(1, 30)),
                created_by=user,
                category=random.choice(list(user_categories)),
            )

            task.tags.set(random.sample(list(user_tags), k=3))
            tasks.append(task)

        self.stdout.write(" 20 tasks created")


        for task in tasks:
            for i in range(1, random.randint(2, 5)):
                SubTask.objects.create(
                    task=task,

                    title=f"Subtask {i} for {task.title}",
                    is_completed=random.choice([True, False])
                )

        self.stdout.write(" Subtasks created")


        for task in tasks:
            Comment.objects.create(
                task=task,
                comment=f"This is a comment for {task.title}",
                commented_by=task.created_by

            )

        self.stdout.write(self.style.SUCCESS(" Fake data seeding completed!"))
