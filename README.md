# Licensing Capsule

**Welcome to Licensing Capsule!**

**A Microsoft Licensing News site**

Licensing Capsule addresses to any Microsoft licensing enthusiast, whether to a small business owner, an IT administrator, or an individual user. It aims to be their comprehensive guide to understanding the latest license terms and leveraging Microsoft to drive productivity and collaboration within their businesses.

This site is beneficial for both new customers and those who have been long-time customers.

Visit deployed site here : https://licensing-capsule-55f92c8ddd11.herokuapp.com/

## User Experience (UX)

### The goal of the site owner

* Keep the audience and potential users up to date with the latest Microsoft license terms.  Clarify the world of Microsoft licensing, providing valuable insights and updates.

### The goal of the external user

* Users’ scope is to stay informed about the latest Microsoft licensing developments and license terms. To be able to engage with the content and provide valuable feedback and comments. Users want to benefit from valuable insights and updates to enhance their understanding of Microsoft licensing.

### User stories:

* There were created 9 EPICs which were developed into 23 User stories:

#### EPIC: Site administration

1. As an admin, I can access an admin panel where I can view users, comments, and posts and filter in the sections so that I can efficiently oversee and maintain the website and its content.
2. As an admin I can create, read, update, and delete articles, so that I can manage my articles
3. As an admin I can approve or disapprove comments so that I can filter out inappropriate comments

#### EPIC: Site content management

4. As an admin, I can add a title, slug, author, image, content, select status of an article so that I can efficiently create the articles for the website.
5. As an admin, I can create draft articles so that I can complete the content at a later time

#### EPIC: User administration

6. As an admin, I can view and manage registered users so that I can monitor the user base

#### EPIC: Article accessibility and navigation

7. As a user on the site, I can view articles by clicking on their title so that I can read the full content
8. As a site user, I can view the article’s author and publication date and time so that I stay informed about contributors and remain up to date with the latest developments in specific licensing news and updates.
9. As a site user, I can read comments of an article so that I can view other readers feedback and insights on the article.
10. As a site user, I can view the most liked and commented articles so that I can stay informed about licensing trends and most discussed topics within the community.

#### EPIC: Article categorization and search

12. As a user on the site I can search the articles on the site so that I can easily locate the relevant content.
13. As a user on the site, I can access the articles by Product family so that I can save time and efficiently access the topics I am interested in.

#### EPIC: User Profile

14. As a frequent site user, I can register on the site so that I can provide feedback on the content and to the content creator and engage with other readers
15. As a registered user I can login and see my login status so that that I know when login was successful.
17. As a registered user, I can edit and delete comments so that I can manage my contributions, edit, and remove mistakes or inaccurate information.

#### EPIC: User feedback on articles

18. As a registered site user I can add a comment on an article so that I can engage with the content, ask questions, offer suggestions to the author, participate in discussions with other readers.
19. As a registered site User, I can like an article so that I can show appreciation and support to the content creator.
20. As a site user I can view number of likes and comments of an article so that I can gain valuable insights and perspectives from other readers regarding the topic.

#### EPIC: Site development documentation

23. As a developer I can access a detailed README so that I can understand the process of the site development.

### Future Features:

The user stories below were not implemented in the project due to time constraints and were labelled as “Won’t Have” on the Kanban board on Github. These user stories and last EPIC will be implemented in the future:

**EPIC: Article accessibility and navigation**

11. As a User on the site I can click on a “Read More” button on the Most Liked and commented posts on home page so that I can easily access the article without having to click on the title.

**EPIC: User Profile**

16. As a registered user I can access my user profile page so that I can manage my comments and see their status (approved or pending).

#### EPIC: User Profile Enhancement

21. As a user on the site I can save articles in my profile so that I can easily access them at any time.
22. As a registered user on the site I can share articles on social media directly from the site so that I can easily share insights with other users, promote the site and support the content creator.

### Design, colors and typography

Throughout the site, there were illustrations picturing cloud computing, software, corporations and various technology elements.

The colour palette chosen was mainly shades of blue, grey and orange. Blue was the dominant color choice, which aligns with the conventions of technology-related websites and gives users a sense of familiarity:

* Color used for the body-background: #ececec
* The text color scheme was black for the paragraph text and shade of blue #00008b, for heading and the nvaigation menu. This particular shade of blue was selected to align with the color of the logo. Additionally, it was applied to certain containers like the one used for Product Family and the landing container on the "News" page.
* The color choice for the nvagation bar, Login, Register was #aaebef, selected to harmonize with the color of the static landing image on the homepage, ensuring a cohesive visual theme.

Google fonts "Alegreya Sans" and "Exo" were used. Specifically, "Exo" was employed for headings, navbar and buttons and "Alegreya Sans" was chosen for paragraphs.

The reason "Exo" font was chosen for the headings is because it is also the font used in the site’s logo. According to the site [Appypie](https://www.appypie.com/blog/font-pairings#:~:text=Two%20fonts%20that%20look%20absolutely,tech%2C%20aerospace%2C%20and%20) such the font pairing "EXO" font and "Alegreya Sans" is considered to be a particularly good fitting for technology oriented websites, which conveys with the site’s design strategy.

Sans Serif font was used as alternative font.

## Wireframes and Database schema

### Wireframe

* I used Balsamiq Wireframes to create the wireframes for the site layout. The wireframe can be found here: [Licensing Capsule-Wireframes](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/licensing_capsule_wireframes.pdf) 
* The layout of the site has changed throughout the project development due to time constraints. As a result, some of the features originally outlined in the wireframe as the User Profile page are to be implemented in the future.

### Database schema

* In order to create and plan the databse structure, I used [Lucidchart](https://www.lucidchart.com/pages/) to create a Database ER diagram. The diagram is available [here - Licensing Capsule - Database Diagram](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/licensing_capsule_database_er_diagram.pdf).

* I applied Object-Oriented Programming principles in the project, along with Django’s Class-based generic views. I created three custom models Article, Product Family and Comment and I used Allauth library for the user authentication system.

* For the author/admin to create an article the custom model "Article" was required.  In this model, the article author is represented as a Foreign Key, which means that each article is associated with a single author.
  
* The "Comment" model enables logged in users to comment on articles. In this case, the "Article" custom model is linked as a Foreign Key ensuring that each comment is associated with a specific article.  Also, the "User" built in model serves as a Foreign Key, as each comment is attributed to a single user.
  
* A third "Product Family" custom model was created to classify articles in specific groups. This custom model is established as a Many-to-Many relationship with the Article model, allowing multiple articles to be associated with a single Product Family.

 ![Licensing Capsule - Database Diagram](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/licensing_capsule_lucid_diagram.png)

## Agile Methodology

* Github Project was utilized to manage the development process using an agile methodology. The link to the Project Kanban board can be accessed [here-Licensing Capsule User Stories](https://github.com/users/AdrianaStoi/projects/2/views/1).
* For each user story I created a Github Issue which includes the EPIC, Acceptance Criteria and Tasks.
* Each User Story comes with defined acceptance criteria, ensuring a clear understanding of when the User Story can be considered completed. These acceptance criteria are subdivided into tasks, making it easier to execute the User Story.
* The User stories were categorized according to the MoSCoW prioritization technique from highest to lowest: "Must Have", "Should Have", "Could Have" and "Won't Have". They were assigned to Milestones that corresponded to the Sprints cycles of the project.

## Existing Features

### Home page

#### Navigation Bar

* The navigation Bar is present on all site pages. It is a fully responsive navigation bar which includes the links for easy user navigation to the “Home”, “News”, “Login” and “Register” page. When users click on the “Licensing Capsule” logo they will be directed to the “Home” page.

* With this feature the user can navigate from page to page and does not have to use back to revert to the previous page. The navigation bar can be used on all device types: desktop, tablet, and smartphones.

![Navigation bar](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_navbar_logo.png)

#### Search Bar

* Under the navigation bar the user can access a search bar, which remains accessible across all pages. This feature enables the user to search for articles. If no articles are found, a message is displayed stating “No articled found.”

* On the article results page, there is a “Back to Home” button to improve the user experience. This button allows users to easily return to the main page.  

![Search bar](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_search_bar.png)

![Search results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/search_results.png)

![Search no articles found](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/search_no_articles.png)

#### Landing Page image

* The home page includes an illustration picturing individuals collaborating on the transmission of company data to cloud which conveys the site’s purpose. Additionally, a welcoming message is displayed on the homepage. 

![Landing image - home](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_landing_page.png)

#### About us

* This section provides information about the site owner’s scope. Reassuring the user that they are at the right place for getting their latest Microsoft licensing insights and news.
  
![About us section](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_about_us_section.png)

#### Latest News

* Beneath the “About us” section, on the left side the user will find the “Latest News” section, where the three most recent articles on the site are dynamically displayed and automatically updated when a new article is published.
  
* Each listing includes the article title, date, and time when it was published, the author’s name, and a brief excerpt from the article. The user can access the article when clicking on the title.

![Latest News](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_latest_news.png)

#### Product Families

* On the right-hand side, there is a list of all available Product Families. When a user clicks on a product name, they are redirected to a page that displays all the articles related to that corresponding family name.

* On the article results by product family page, there is a “Back to Home” button to improve the user experience. This button allows users to easily return to the main page.

![Product Families](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_product_families.png)

#### Most liked and commented articles:

* In the final section on the home page the user can find the “Most liked and commented articles”. Three cards are presented: the first and second cards display the two most liked articles and the third card highlights the most commented article. These articles dynamically change based on the number of likes and comments they receive.

![Most liked and commented articles section](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_most_liked_and_commented.png)

#### Footer

* The footer section displays the site name and the three social media font awesome icons for Facebook, LinkedIn, and Twitter. The links open in a new tab.

![Footer image](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_footer.png)

### News page

#### Landing image

* On the news page, the user will encounter a new corporate illustration with a blue background, aligning with the site’s color palette.
Under this image all articles are listed, but only three articles are visible at a time.

![Landing image - news page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/news_landing_page.png)

#### All articles

* Below the list of the three articles, there is the pagination feature that displays the total number of available pages and provides users with the option to navigate to the next or last page. This allows users to easily access and browse through the entire site collection.  

![All articles -news page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/news_all_articles_and_pagination.png)

### Single article page

* On each article page, the user finds a different illustration by product family type.

![Illustration single article for Microsoft 365 articles](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_dynamic_image.png)

* Under the image the title of the article is displayed. Following the title, users will find the date and time of publication, along with the author’s name and the article’s content.

* At the bottom of the article, there are two icons. One icon represents likes and number of likes. The other icon represents comments showing the corresponding number of comments.

![Article title and publication details](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_article_details.png)

![Article body and like-comment icons](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_body_and_icons.png)

* If the user is not logged in and clicks on the like button, they will be prompted with a modal window which states “You must be logged in to like and leave a comment. “ This prompts users to log in before they interact with the article in these ways.

![Modal-Login or Register to like](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_modal_message.png)

#### Comments section

* In the Comments section,  users who are not logged in will have read access to view the comments.

* There is also a message displayed “Login or Register to like and leave a comment.” This message encourages users to engage with the community by providing feedback.

![Comments section - user not logged in](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_comments_section_user_not_loggedin.png)

* If no comments are available, there is stated “No comments yet.”

![Comments section -no comments yet](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_no_comments_yet.png)

* When a user is logged in, they have the option to submit a comment using a comment form. After sending a comment, they will be prompted with the message “Your message is waiting approval.” Comments submitted by users need to be approved by the admin before they are displayed in the comment section.

![Comment form](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_leave_comment.png)

![Comment submitted waiting for approval](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/comment_waiting_approval.png)

* If the user attempty to refresh the article page immediately after submitting the comment that is pending for approval, a pop=up message will appear as a warning. This message indicates that refresing at this point, might result in the duplication of their action, which leads to the resubmission of the same comment twice if they proceed.

![Confirm Form Resubmission](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/comment_resubmission_message.png)
  
* Once the comment is approved, it will appear in the comment section, and the logged-in user will have the ability to “Edit” or “Delete” their comment.

![Edit-Delete comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_comments_edit_delete.png)

* When editing the comment, the user is redirected to a new page where they can make the necessary changes. After editing, they are redirected to the previous page and they are be prompted with a success message alert that automatically dismisses after 5 seconds.

![Edit comment page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_edit_comment.png)

![Edit comment successfully](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_successful_edit_comment.png)

* When deleting a comment, the user is prompted with a confirmation message to confirm the deletion. After confirming, the comment will be deleted. They are redirected to the previous page and they are prompted with a success message alert that automatically dismisses after 5 seconds.

![Delete comment page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_deletion_confirmation_page.png)

![Delete comment successfully](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_successul_message_comment_deletion.png)

### Login page

* On the login page the user is asked to enter their username and password. If the user is not registered yet, they can click on “Register”.
* When user enters a wrong username or password, they are prompted with the message “The username and/or password you specified are not correct.”

![Login page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/login_page.png)

![Password incorrect](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/login_incorrect_password.png)

### Logged in user

* When users are logged in, at the top right corner their user name is displayed and they have the Logout button.

![Login navbar](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/navbar_user_logged_in.png)

### Logout page

* When clicking on logout, users are redirected to a page that asks them to confirm their intention to  log out. This step helps ensure that users do not accidentally log out and asks for them to confirm this action before proceeding.

![Logout page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/logout_page.png)

### Register Page

* On the register page, users are asked to enter their name, email (optional field) and create a password:
Once they are registered, they are logged in. They are prompted with a success message alert.

![Register page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/register_page.png)
![Successfully signed in after registration](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/register_successful_logged_in.png)

### Error pages

* Custom error pages were created to provide additional error details and give guidance to the user to return to the site. 

* 404 Page not Found – “The page you are looking for does not exist.”
* 403 Forbidden – “You are not authorized to perform the requested action.”
* 500 Server Error – “Licensing Capsule is currently unable to handle this request.”

![404 Page not Found](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/404_error_page.png)
![500 Server Error](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/500_error_page.png)

## Technology

### Languages

* Skillset used for the project was HTML, CSS, JavaScript and Python.

### Frameworks, Libraries and Programs used

* [Codeanywhere](https://app.codeanywhere.com/) was used as the editor for developing the site.
* Django was used as Python framework in the development of the project.
* [ElephantSQL](https://www.elephantsql.com/) was used as a database for the project.
* [Django Allauth library](https://docs.allauth.org/en/latest/ ) was utilized for user authentication system.
* [Cloudinary](https://cloudinary.com/) was used as storage for dynamic images.
* [Whitenoise library](https://whitenoise.readthedocs.io/en/latest/index.html) was installed and used for the static files and images.
* Psycopg2 and gunicorn were installed as supporting libraries.
* [Summernote](https://summernote.org/ )library was used to enable the admin to create the articles.
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) was used for Django Forms.
* [Bootstrap 5.1.3](https://getbootstrap.com/docs/5.1/getting-started/introduction/) was used for general layout, spacing and buttons.
* [Heroku](https://dashboard.heroku.com/apps) was used as the cloud based hosting platform to deploy the site.
* [GitHub](https://github.com/AdrianaStoi) - The project's deployment history was tracked using Git commit messages on Github. GitHub also served as agile project management tool.
* [Lucidchart](https://www.lucidchart.com/pages/) was used to create and plan the databse structure. The diagram is available [here - Licensing Capsule - Database Diagram](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/licensing_capsule_database_er_diagram.pdf).
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/?gad_source=1&gclid=CjwKCAjwp8OpBhAFEiwAG7NaEgqiAxWUYgb9TgMNO1yffgUGLUJ1sDE3PpAl5Xf2bSoMCE1me-MSKhoCOOoQAvD_BwE) was used to create the wireframes for site layout. The wireframe can be found [here:Licensing Capsule-Wireframes](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/licensing_capsule_wireframes.pdf)

## Testing
Testing and results can be found in the [TESTING.md](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/TESTING.md) file [here](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/TESTING.md).

## Deployment

### Codeanywhere

* I used Codeanywhere to develop the project. Here are the steps to create the workspace and run the project:
* Log in to [Codeanywhere](https://app.codeanywhere.com/) using GitHub account
* On the Dashboard, click on “New Workspace” which can be found under “Workspaces” section
* Copy and paste the Repository URL created in GitHub by using the [Code Institute p4-template](https://github.com/Code-Institute-Org/ci-full-template) into the designated field
* Click on Create.
* New Workspace is created in Codeanywhere.
* To run and view the project written in Codeanywhere, click on “Terminal” in the upper bar, then select “New Terminal”.
* The New terminal will open at the bottom part of the page.
* Install **Django** by using the command “pip3 install 'django<4' gunicorn”
* Install supporting libraries: “pip3 install dj_database_url==0.5.0 psycopg2”
* Install **Cloudinary Libraries** by running in the terminal : “pip3 install dj3-cloudinary-storage”and 
“pip3 install urllib3==1.26.15”
* Then create the Create requirements file by running the code “pip3 freeze --local > requirements.txt”
* Create Project by running “django-admin startproject project name (e.g. licensing capsule) .”
* Create App by using the code “python3 manage.py startapp app name (e.g. news)”
* In settings.py file add the app to installed apps and save.
* Migrate the changes in the terminal by using “python3 manage.py migrate”
* Run the server “python3 manage.py runserver”
* An error message will appear, copy the host name and add it to “ALLOWED_HOSTS” in the settings.py folder. "e.g. ALLOWED_HOSTS = []"

### Database

I created a Database on [ElephantSQL](https://www.elephantsql.com/) as follows:

* Log in to ElephantSQL account
* Click on “Create New Instance”
* Set up the plan:
  * Give the plan a Name (e.g. project name)
  * Select the "Tiny Turtle (Free) plan"
  * Leave the "Tags" field blank
* Select “Select Region” and then select a data center near
* Click on “Review”
* Check that details are correct and then click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name
* Under the URL section, the database URL is available. Click on the copy icon to copy the URL.

#### Attach the Database

In Codeanywhere terminal:

* Create "env.py" file on top level directory
* In "env.py" file import os library
* Set environment variables : “os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
* Add in secret key : “os.environ["SECRET_KEY"] = "Make up own randomSecretKey"

### Set up the environment and settings.py file

In "settings.py" file in Codeanywhere:

* Reference env.py
* Create a Remove the insecure secret key and replace it with: “os.environ.get('SECRET_KEY') and add the secret key to env.py”
* Comment out the old DataBases Section and replace it with the new Database
* In the Codeanywhere terminal, save all files and Make Migrations using “python3 manage.py migrate”

### Store images to Cloudinary

* Create [Cloudinary account](https://cloudinary.com/)
* Once logged in go to  Cloudinary Dashboard and copy the CLOUDINARY_URL, e.g. API Environment Variable
* Add Cloudinary URL to "env.py" file in Codeanywhere

### Create app in Heroku

I deployed the project on Heroku at the beginning of the project and the steps below were followed:

* Log into [Heroku]( https://heroku.com/) account or create new account.
* From the Heroku dashboard click on “New” on the upper right corner and then click on “Create new app”.
* Add app name (app name must be unique on Heroku).
* Then select the appropriate region e.g. “Europe” and then click on “Create app”.
* Then go to “Settings tab”.
* Add three config vars:
  * DATABASE_URL, and add the database URL from ElephantSQL as the value
  * SECRET_KEY containing the secret key
  * CLOUDINARY_URL as key and the link as value.

In settings.py file in Codeanywhere:

* Add Cloudinary Libraries to installed apps.
* Add Cloudinary to be used as store media and static files.
* Link file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR.
* Add Heroku Hostname to ALLOWED_HOSTS.

In Codenaywhere terminal:

* Create media, static, templates folders on top level directory.
* Create a Procfile on the top level diectory.
* In Procfile add “web: gunicorn PROJ_NAME.wsgi”.
* Add, commit and push changes to GitHub.

### Deploy to Heroku:

* Go to [Heroku account](https://heroku.com/).
* Go to “Deploy” tab located at the top of the page.
* Under “Deployment method” section, select Github here, and then confirm connection to Github.  
* Search for the corresponding Github repository name, e.g. Licensing Capsule and click “Search”.
* Click on “Connect” to link up the Heroku app to the GitHub repository code.
* Scroll down on the page, and there are two deployment options in this section: “Automatic deploys” and “Manual deploy”.
* Under “Manual deploy”, click on “Deploy Branch”.
* Once is deployed there is a message displayed “Your app was successfully deployed.” And a button “View”.
* Click on “View” and you are directed to the app deployed and the link.

Visit deployed site [here:Licensing Capsule](https://licensing-capsule-55f92c8ddd11.herokuapp.com/)

## Credits

* I used [Code Institute - Template](https://github.com/Code-Institute-Org/ci-full-template) for the deployable application.
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Font Pairing suggestion was taken from [Appypie](https://www.appypie.com/blog/font-pairings#:~:text=Two%20fonts%20that%20look%20absolutely,tech%2C%20aerospace%2C%20and%20such)
* The icons in the footer were sourced from [Font Awesome](https://fontawesome.com/)
* To create diagram for custom modelI used [Lucidchart](https://www.lucidchart.com/pages/)
* To create the wireframes I used [Balsamiq Wireframes](https://balsamiq.com/wireframes/?gad_source=1&gclid=CjwKCAjwp8OpBhAFEiwAG7NaEgqiAxWUYgb9TgMNO1yffgUGLUJ1sDE3PpAl5Xf2bSoMCE1me-MSKhoCOOoQAvD_BwE)
* For logo creation I used the site [Logo](https://logo.com/)

### Tutorials

* The [Code Institute Django Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) walkthrough served as a foundation and I adapted and customized it accordingly
* To edit and delete comments I used as source the [Todo CI walkthrough](https://github.com/ckz8780/ci-fsf-hello-django/blob/c13b414fd2e87a54b4f2788ceffec55be4ade925/todo/views.py)
* To add pagination I used the code for pagination from [Django Project site](https://docs.djangoproject.com/en/4.2/topics/pagination/).
* In order to created the function and display the 3 latest articles on the home page, I used as guidance the [Stackflow thread](https://stackoverflow.com/questions/23928866/only-show-the-latest-3-posts-in-django) 
* To create the Search view I used as source and inspiration the project blog created by [Rathan Kumar](https://github.com/dev-rathankumar/django-blog/blob/main/blogs/views.py) and customized accordingly.
* For creating query for most likes and most commented articles and display them, I used the [Stackflow thread](https://stackoverflow.com/questions/68575418/django-sort-posts-by-comments-count?rq=3) and I customized it accordingly.

### Images and content

#### Content

* Articles were written based on official information from Microsoft Product Terms licensing sites and blogs: 

* [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/product/changes/EAEAS)
* [New subscription structure for Microsoft 365 in Europe](https://www.microsoft.com/en-us/licensing/news/Microsoft365-Teams-EEA)
* [Microsoft announces changes to Microsoft 365 and Office 365 to address European competition concerns](https://blogs.microsoft.com/eupolicy/2023/08/31/european-competition-teams-office-microsoft-365/ )
* [Dynamics 365 Customer Insights FAQs](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/ci-faq)
* [Microsoft launches Power Automate Process Mining and next-generation AI](https://cloudblogs.microsoft.com/powerplatform/2023/07/18/microsoft-launches-power-automate-process-mining-and-next-generation-ai/)
* [Microsoft Dev Box is now generally available](https://azure.microsoft.com/en-us/updates/microsoft-dev-box-is-now-generally-available/)

#### Images

* Illustrations were taken from [Shutterstock](https://www.shutterstock.com/) and [Istockphoto](https://www.istockphoto.com/de):

* [Photo credits:Sorbetto](https://www.istockphoto.com/de/vektor/gesch%C3%A4ftsleute-arbeiten-online-zusammen-gm1421764550-467289983)
* [Illustration by Graphic farm](https://www.shutterstock.com/image-vector/business-technology-storage-cloud-computing-service-1715236615)
* [Illustration by MPetrovskaya](https://www.shutterstock.com/image-vector/set-vector-illustrations-flat-cartoon-characters-1892882557)
* [Illustration by AlisaRut](https://www.shutterstock.com/image-illustration/call-center-custome-support-technical-service-1910982568)
* [Illustration by TuGuDesign](https://www.shutterstock.com/image-vector/top-view-office-workplace-2122215641)
* [Illustration by Designsells](https://www.shutterstock.com/image-illustration/violet-concept-marketing-people-scene-flat-2256240047)
