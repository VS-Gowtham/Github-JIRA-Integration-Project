# Github-JIRA-Intergration-Project
Automated Github -JIRA intergration

we have source code in Github and application has been deployed on a EC2 instance.
Written API using FLASK Framework.

The END Goal of this Project is :

>If any Developer writes a comment in the issue tab of the application repository in Github.
>Then immediately ,Github will send the complete information of the particular issue through "Json payload" to my python application.
>A "webhook" has been configured in Github.
>Which informs Github whenever a Developer comments /BUG on a particular issue it will send the information to EC2 instance , where the application is deployed.
>Then the Python application will make an API call to Jira to create a Backlog regarding the issue.



