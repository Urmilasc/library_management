# Python Django Library Management System

Installed the python

Creating the virtual environment.

Next step is to activate our virual environment 

```jsx
pip install virtualenv

# For Windows:
venv\Scripts\activate

```

![image](https://github.com/user-attachments/assets/eb52f717-c39c-47e9-b540-18882042961e)


Here is our env, an virtual environment is created

![image](https://github.com/user-attachments/assets/701fe495-0f59-4211-a0b1-689f599157c1)


![image](https://github.com/user-attachments/assets/e734d479-c7f2-4e44-b29a-55173996e147)


Now checking if the django is installed or not by using command 

```jsx
python -m django --version
```

![image](https://github.com/user-attachments/assets/03d3eea0-4633-4fdb-a194-eb9c184c877c)


Installing the django and djangorestframework and simplet.jwt token 

![image](https://github.com/user-attachments/assets/a64c8fd3-ca8b-446a-ac64-13cc2ecc4eb5)


While Activating our virtual environment we need to have the administrator permission of Get-ExecutionPolicy, get to know by chat-gpt only 

Go to powershell and type the following commands 

```jsx
Get-ExecutionPolicy

Set-ExecutionPolicy RemoteSigned 

and yess
```

Here in the green bracket env is started showing means our virtaul environment is started

![image](https://github.com/user-attachments/assets/f228decd-7ae6-4536-a475-d08e673fad2e)


![image](https://github.com/user-attachments/assets/5f6d0a05-704d-4ee1-bfe1-e5130549b92c)


Finally django has been setup, after chat-gpt and stckoverflowing each step

![image](https://github.com/user-attachments/assets/4cba98de-0345-4500-b412-b0e9430584ae)


Creating the Custom Model in django, using the AbstractUser , created 2 roles Librarian and Member 

![image](https://github.com/user-attachments/assets/5cdf8307-1061-43d7-973a-75ad3f4b1673)


Migrating the project, why so ?

Because django is providing many dependencies or we could say mainly the database table of auth, admin, contenttypes and sessions. 

Here’s a pro tip - If you want to know which user deleted which entry intable we can check the auth_user table, specailly the contenttypes , because the contenttypes stores the logs of each and every user activity. And all this auth, admin, contenttypes and sessions have the unique Id, we can see them by using the vs code extension.

Migration only can be done one time, we don’t have to do migrate again again

```jsx
pyhton manage.py migrate
```

![image](https://github.com/user-attachments/assets/4bb8500d-1267-4f88-87c1-ba34960a9bec)


Getting the error, because as I new I don’t know hoe to access the api in frontend

![image](https://github.com/user-attachments/assets/5902781f-bc49-48c8-a907-5e5362139352)


Setupped the JWT token which uses the SHA56 algorithm to encrypt our credentials and also provide the access token and refresh token.

![image](https://github.com/user-attachments/assets/d9424d40-f633-4ef1-84a4-3830d8209697)


Here the File structure of our project

![image](https://github.com/user-attachments/assets/29349a7a-d311-44a9-96c9-616c007ac74c)


![image](https://github.com/user-attachments/assets/19228946-3a8c-4841-8d8a-affa10d81fb9)


Troublesooting steps -

Till here, I get to know that this interface is due to becuse I am using the Django Rest Framework, so think to continue in this, but changed he whole aftrwards

To triubleshoot , chnaged the library_system/urls.py file and added the redirecting url package 

Here in Member List provided the username and Password and signing as a librarian

![image](https://github.com/user-attachments/assets/d9b89d28-2fd9-4fbc-8693-e462f4c79ea4)


See the change in ID number field , our username with id  is being seen 

![image](https://github.com/user-attachments/assets/b45a2721-309a-4d63-8cad-97ed6df1bc68)


Here we added 2 members, one as librarian and another one as member, as we can see

![image](https://github.com/user-attachments/assets/5c69ee72-fb61-4b55-a1d1-19fdbe0b46f1)


Here in VS code , we able to see the members are succesfully added with the status code as  200

![image](https://github.com/user-attachments/assets/e90275e5-693e-4b9d-a77d-c9969d6d1ee6)


API Token for authentication. As I get to know about JWT is providing 2 token one is Access token and another one is Refresh token.

Why this 2 seperate token ?

First the access token, is one which is used by our webbrowser for login into particular website. Let say an exmaple , you have the facebook app , and if your friends know the access token as we can see it while debugging in chrome browser developer tools, he can bel to login to your facebook account via thier device, then in case the refresh token is used, which refrehes the token due to which a new access token has been generated and your friend can’t able to access your facebook using the old acess token

![image](https://github.com/user-attachments/assets/47815461-5486-4093-96e6-c76dc192cd91)


Getted the 2 token as we described by JWT one is refresh and another one is access token for the username and password we provided above 

![image](https://github.com/user-attachments/assets/1b149449-aefa-424f-96a9-39478154740d)


After lot of reseaarch and chat gpt , finally came to know that I am using the DRF, a framework to easy manage the fronetend with api. 

But not to use that , I again started building the project from scratch by asking the gemini , chat gpt and finally now it look like this 

Here we have the Signuppage and has descriibed in problem statement user canbe sign as 2 roles either librarian or member with some following activites attached individually to role

```jsx
Username - urmila@sc
Role - Librarian
Password - admin@123

```

![image](https://github.com/user-attachments/assets/8fe656b4-6359-47ba-ba02-fe1ca2370062)


Login using the user credentials we created above and see the api for login has been changed when we clicked the signup button.

![image](https://github.com/user-attachments/assets/57c8cae8-09b8-4ab1-b412-bf81b4892d5d)


Finally dashboard has been opened as this user is login as a member 

![image](https://github.com/user-attachments/assets/c55d1833-4201-4726-8853-4bd25b34b4e1)


User prodeep as librarian role 

![image](https://github.com/user-attachments/assets/64bc47f2-c387-4c7b-905d-f54f5e6ebd75)


Login with pradeep username which has a librarian role

![image](https://github.com/user-attachments/assets/fa20c814-a060-44af-8984-fb8bf7abce49)


![image](https://github.com/user-attachments/assets/37459366-73e5-4be2-af01-3a8f7c4652de)

I acknowledge that this project is far from complete and not well-structured, and I truly apologize for the shortcomings. As someone who is completely new to both Python and Django, this has been a steep learning curve for me. While I did my best to understand and implement each feature, many aspects—especially the specific functionalities tied to librarian and member roles—are still unfinished. Despite these challenges, I’ve tried to push forward, resolving errors step by step. I know there's much more to improve, and I appreciate your understanding as I continue to learn and refine my skills in this tech stack.
