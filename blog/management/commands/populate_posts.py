from typing import Any

from django.core.management.base import BaseCommand

from blog.models import Post,Category

import random 

class Command(BaseCommand):
    help="this command helps to  populate data"

    def handle(self, *args: Any, **options: Any):
        #delete the posts
        
        Post.objects.all().delete()

        posts=[
    "Mastering Flask: A Beginner's Guide to Building Web Applications",
    "Optimizing MongoDB Clusters for High Traffic: Best Practices and Strategies",
    "Exploring Flask vs. Django: Which Framework Suits Your Project?",
    "MongoDB Change Streams: Real-Time Data Synchronization Across Clusters",
    "A Deep Dive into Flask Development with VS Code",
    "Building Scalable Web Applications with Flask and MongoDB",
    "Advanced Git Techniques: Resolving and Understanding Merge Conflicts",
    "Streamlining CI/CD Pipelines with Jenkins and Ansible",
    "MongoDB Atlas on AWS: Setting Up and Managing Multi-Cluster Deployments",
    "From Design to Deployment: My Journey in Graphic Design",
    "Using Flask for RESTful APIs: A Complete Step-by-Step Guide",
    "Harnessing the Power of SonarQube for Code Quality and Security",
    "Scaling with MongoDB: Effective Horizontal Sharding Techniques",
    "Deploying Flask Applications with Docker: A Complete Tutorial",
    "MongoDB Connection Pooling: Maximizing Performance and Efficiency",
    "Mastering Flask Authentication: Secure Your Web Applications",
    "Flask + MongoDB: Building a Dynamic Web Platform",
    "Unveiling the Power of MongoDB Replica Sets for Data Redundancy",
    "Crafting Elegant Web Interfaces with Flask and Jinja2",
    "Advanced Flask Patterns: Blueprints and Modular Application Design"
]
        content=[
    "Understanding Flask Routing: A Comprehensive Guide",
    "Efficient Data Handling with MongoDB Aggregation Framework",
    "Deploying Flask Applications on AWS Using Docker",
    "Mastering Flask Forms with WTForms for User Input",
    "MongoDB Schema Design Best Practices for Scalable Applications",
    "Building Secure Flask Applications with JWT Authentication",
    "Optimizing Flask Performance with Caching Techniques",
    "Implementing Role-Based Access Control in Flask",
    "Managing MongoDB Backups and Restores for Data Safety",
    "Flask Blueprint Architecture for Modular Applications",
    "Integrating Flask with Frontend Frameworks like React",
    "Advanced MongoDB Indexing for Faster Query Execution",
    "Monitoring Flask Applications with Prometheus and Grafana",
    "Handling File Uploads Securely in Flask",
    "MongoDB Change Streams for Real-Time Analytics",
    "Creating RESTful APIs with Flask and MongoDB",
    "Flask Logging and Error Handling Best Practices",
    "Scaling Flask Applications with Gunicorn and Nginx",
    "Implementing WebSockets in Flask for Real-Time Communication",
    "Optimizing Flask Query Performance with SQLAlchemy"
]
        img_url=[
    "https://picsum.photos/id/1/300/300",
    "https://picsum.photos/id/2/300/300",
    "https://picsum.photos/id/3/300/300",
    "https://picsum.photos/id/4/300/300",
    "https://picsum.photos/id/5/300/300",
    "https://picsum.photos/id/6/300/300",
    "https://picsum.photos/id/7/300/300",
    "https://picsum.photos/id/8/300/300",
    "https://picsum.photos/id/9/300/300",
    "https://picsum.photos/id/10/300/300",
    "https://picsum.photos/id/11/300/300",
    "https://picsum.photos/id/12/300/300",
    "https://picsum.photos/id/13/300/300",
    "https://picsum.photos/id/14/300/300",
    "https://picsum.photos/id/15/300/300",
    "https://picsum.photos/id/16/300/300",
    "https://picsum.photos/id/17/300/300",
    "https://picsum.photos/id/18/300/300",
    "https://picsum.photos/id/19/300/300",
    "https://picsum.photos/id/20/300/300",
    "https://picsum.photos/id/21/300/300"
]
           
           
        categories= Category.objects.all()
        for posts,content,img_url in zip(posts,content,img_url):
            category=random.choice(categories)
            Post.objects.create(title=posts,content=content,img_url=img_url,category=category)
            
        self.stdout.write(self.style.SUCCESS("Data populated successfully"))

