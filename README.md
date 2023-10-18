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

* Throughout the site, there were illustrations picturing cloud computing, software, corporations and various technology elements.

* The colour palette chosen was mainly shades of blue, grey and orange. Blue was the dominant color choice, which aligns with the conventions of technology-related websites and gives users a sense of familiarity.

  * Color used for the body-background: #ececec
  * The text color scheme was black for the paragraph text and shade of blue #00008b, for heading and the nvaigation menu. This particular shade of blue was selected to align with the color of the logo. Additionally, it was applied to certain containers like the one used for Product Family and the landing container on the "News" page.
  * The color choice for the nvagation bar, Login, Register was #aaebef, selected to harmonize with the color of the static landing image on the homepage, ensuring a cohesive visual theme.

* Google fonts "Alegreya Sans" and "Exo" were used. Specifically, "Exo" was employed for headings, navbar and buttons and "Alegreya Sans" was chosen for paragraphs.

* The reason "Exo" font was chosen for the headings is because it is also the font used in the site’s logo. According to the site [Appypie](https://www.appypie.com/blog/font-pairings#:~:text=Two%20fonts%20that%20look%20absolutely,tech%2C%20aerospace%2C%20and%20) such the font pairing "EXO" font and "Alegreya Sans" is considered to be a particularly good fitting for technology oriented websites, which conveys with the site’s design strategy.

* Sans Serif font was used as alternative font.

## Wireframes and Database schema

### Wireframe

* I used Balsamiq Wireframes to create the wireframes for site layout. The wireframe can be found here: [Licensing Capsule-Wireframes]() 
* The layout of the site has changed throughout the project development due to time constraints. As a result, some of the features originally outlined in the wireframe as the User Profile page are to be implemented in the future.


### Database schema

* In order to create and plan the databse structure, I used [Lucidchart](https://www.lucidchart.com/pages/) to create a Database ER diagram. The diagram is available [here - Licensing Capsule - Database Diagram]().

* I applied Object-Oriented Programming principles in the project, along with Django’s Class-based generic views. I created three custom models Article, Product Family and Comment and I used Allauth library for the user authentication system.

* For the author/admin to create an article the custom model "Article" was required.  In this model, the article author is represented as a Foreign Key, which means that each article is associated with a single author.
  
* The "Comment" model enables logged in users to comment on articles. In this case, the "Article" custom model is linked as a Foreign Key ensuring that each comment is associated with a specific article.  Also, the "User" built in model serves as a Foreign Key, as each comment is attributed to a single user.
  
* A third "Product Family" custom model was created to classify articles in specific groups. This custom model is established as a Many-to-Many relationship with the Article model, allowing multiple articles to be associated with a single Product Family.

## Agile Methodology

* Github Project was utilized to manage the development process using an agile methodology. The link to the Project Kanban board can be accessed [here-Licensing Capsule User Stories](https://github.com/users/AdrianaStoi/projects/2/views/1).
* For each user story I created a Github Issue which includes the EPIC, Acceptance Criteria and Tasks.
* Each User Story comes with defined acceptance criteria, ensuring a clear understanding of when the User Story can be considered completed. These acceptance criteria are subdivided into tasks, making it easier to execute the User Story.
* The User stories were categorized according to the MoSCoW prioritization technique from highest to lowest: "Must Have", "Should Have", "Could Have" and "Won't Have". They were assigned to Milestones that corresponded to the Sprints cycles of the project.
