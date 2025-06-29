# offline_chatbot
Works Completely offline

In many places, people still don’t have reliable internet — but they need smart tools like chatbots for learning, support, or help. Most AI chatbots today only work online, which makes them useless when there’s no internet.
Also, keeping these chatbots updated, monitored, and working smoothly usually needs manual work or complex setups. 

We wanted to solve this problem by building a chatbot that:

Works completely offline
 Gets updates from the cloud (like new data or models) when internet is available
 Uses DevOps tools to automate updates, logging, and deployments
 Runs inside Docker so it can work on any machine, even without setup
Has a simple chat interface (console or app) for easy interaction
SOLUTION OVERVIEW : 
We built an offline AI Chatbot that runs without internet using a lightweight NLP model , and auto-updates itself from AWS S3 using Docker + CI/CD + DevOps tools .

It's smart , Portable , and cloud-connected .

KEY FEATURES :

 Offline Functionality – Works without internet after setup
 Lightweight NLP Model – Uses DistilBERT/GPT-2 for fast local responses
 Cloud Sync – Downloads latest model/data from AWS S3 when online
 CI/CD Automation – GitHub → CodePipeline → S3 for smooth updates
 Dockerized App – Portable and easy to run on any machine
 Chat UI – Clean interface built with Electron or console UI
 Logging with CloudWatch – Monitors errors, sync status, and performance
 Secure Cloud Access – IAM roles to protect AWS resources
 Auto Update Script – Checks for model updates automatically
 Modular Architecture – Easily upgradable (model, UI, sync logic)

![image](https://github.com/user-attachments/assets/33ca7906-a543-40ec-9657-26636e5f9eb6)


