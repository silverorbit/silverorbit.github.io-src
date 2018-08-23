Title: Containerized Flask API using AWS Fargate and Mongo Atlas 
Date: 2018-08-22 01:40
Category: aws, fargate, mongodb, microservices

Microservices: Building a containerized Flask API using AWS Fargate with  MongoAtlas. 

![Yay] (/images/mongo-atlas/diagram.jpg)

The project idea is to get a stream of data going into MongoDB from a separate app, in this case using a script to insert new records.
Mongo Atlas provides a hosted mongodb, which was setup with VPC Peering with AWS in the same US East region. 

![Yay] (/images/mongo-atlas/mongo-atlas.jpg)

On the API service side, setup ECS and create a Docker repository, i.e  Using Flask-Resful and PyMongo to access the MongoDB. 
Uploading the API image to Docker repository using AWS CLI, seems good.

![Yay](/images/mongo-atlas/docker_push.jpg)

The API serves request from the mobile app and backoffice for reports and new updates. 
Mobile app post request to group results per week.  

![Yay](/images/mongo-atlas/mobileapp.jpg)


The Results

- API is containerized using Docker and image were pushed to  ECR.
- Saves time in managing EC2 instances, Fargate handles them.
- We did not need to manage MongoDB cluster as it is hosted on the same region, with read replica and secured with peering.

In the future, we will continue upgrading the setup, with more details and best practices in deploying this project. 


Do you need help in setup like this? Feel free to reach to TeamSilverOrbit on [Twitter](https://twitter.com/TeamSilverOrbit) or via email.


