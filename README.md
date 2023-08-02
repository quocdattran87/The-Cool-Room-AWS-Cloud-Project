## Third Year University Assignment
By Quoc Tran (s3827826)

This project was fully operational and funded by a $100 coupon provided by the university.
This infrastructure has since been torn down as it will incur extra costs to keep it up and running.

- 'deployment/lambda_function' should be zipped up and uploaded into the lambda. It is left unzipped to see inside.
- 'scripts' contain basic test scripts for API calls from API Gateway.
- 'source/TheCoolRoom_django' contains the main Django project that is ran inside the Elastic Beanstalk. This directory should be git enabled so the CodeCommit can trigger the CodePipeline build process whenever commits are made.

### The Cool Room – System Architecture
<img width="915" alt="Screenshot 2023-08-02 at 8 49 13 pm" src="https://github.com/quocdattran87/The-Cool-Room-AWS-Cloud-Project/assets/63576134/47794fe5-d844-4850-9de2-b06155672629">

‘TheCoolRoom’ is a Django project that was adapted from a Traversy Media YouTube tutorial for their application called ‘Study Buddy’. I followed the tutorial to learn Django in my own time. The original project was a standalone Django application that used an inbuilt database. I have adapted the project to be fitting with the AWS tools and environment.
Such changes include changing the database to an RDS instance, including calls to API gateway to query the RDS database, changing the static files to point to S3, adding a Dockerfile to build a docker image and a buildspec.yml for AWS CodePipeline, enabling git so I can push the code base into AWS CodeCommit.

### References
    [1] Traversy Media. 2021. Python Django 7 hours Course. [online] Available at: <https://www.youtube.com/watch?v=PtQiiknWUcI&t=21975s> [Accessed 12 January 2022].
    [2] AWS Documentation. 2022. Tutorial: Create a pipeline with an Amazon ECR source and ECS-to-CodeDeploy deployment. [online] Available at: <https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-ecs-ecr- codedeploy.html> [Accessed 14 April 2022].
    [3] Nik Tomazic. 2022. Deploying a Django Application to Elastic Beanstalk. [online] Available at: https://testdriven.io/blog/django-elastic-beanstalk [Accessed 14 April 2022].
    [4] Be A Better Dev. 2020. How to Deploy a Docker App to AWS using Elastic Container Service (ECS). [online] Available at: <https://www.youtube.com/watch?v=zs3tyVgiBQQ> [Accessed 21 April 2022].

When users type ‘thecoolroom.link’ on their browsers, Route 53 will direct them to the Elastic Load Balancer that is maintained by Elastic Beanstalk. The Elastic Load Balancer re- routes any http traffic to https with the use of an ACM certificate in Certificate Manager to provide a secure SSL connection. The load balancer finally sends the user to an EC2 instance in the auto scaling group. The auto scaling group is configured to have 1 to 4 instances depending on current traffic. The load balancer spreads incoming traffic evenly onto the active EC2 instances.


When users create an account, chat room, or message, the API gateway is called by it’s invoke URL. The routes in the API gateway are integrated to a lambda function which contains code to connect to and query the RDS. Any request is returned, processed, and displayed on the website for users to see. RDS stores tables containing user, chat room, and message information. The S3 is used to store profile pictures and static files for the web application to use.


An auto deployment pipeline has been integrated for ease of development. The Django code base can be worked on locally. Any changes can then be git committed and pushed to the repository on Code Commit. Any changes are picked up automatically via cloudwatch and triggers the Code Pipeline to run. It first builds the Django project into a Docker image. Then it pushes this image into the Elastic Container Registry and then runs a new task with the latest image container that was just updated. The previous running task is automatically cancelled, and the changes are run in a EC2 instance.

   
The project is elastic beanstalk enabled and has the RDS, S3, Elastic Load Balancer, and Auto Scaling group contained within it. I also created an ECS cluster to run the docker image which comes with its own Auto Scaling group and Load Balancer. I detached the EC2 container from the ECS Auto Scaling group and added it to the Elastic Beanstalk Auto Scaling group. I then detached the provisioned EC2 instance that comes with Elastic Beanstalk from the Auto Scaling group. Now we have an EC2 instance linked to ECS and Elastic Beanstalk. I then delete the Auto Scaling group and Elastic Load Balancer that was made by the ECS cluster.
