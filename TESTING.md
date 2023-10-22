
# Testing

## Table of contents

- [Testing](#testing)
  - [Table of contents](#table-of-contents)
  - [Browser Compatibility](#browser-compatibility)
  - [Lighthouse](#lighthouse)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)
  - [Manual Testing](#manual-testing)
  - [User Story Testing](#user-story-testing)
  - [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
  - [Testing Responsiveness](#testing-responsiveness)
    - [Responsiveness on devices](#responsiveness-on-devices)
    - [iPad Mini](#ipad-mini)
      - [Home Page](#home-page)
      - [Search bar function](#search-bar-function)
      - [Articles by product families page](#articles-by-product-families-page)
      - [News Page](#news-page)
      - [Login Page](#login-page)
      - [Register Page](#register-page)
      - [Logout Page](#logout-page)
      - [Single article page](#single-article-page)
        - [Unauthenticated user](#unauthenticated-user)
        - [Authenticated user - Comment and like section](#authenticated-user---comment-and-like-section)
    - [iPhone 12 Pro](#iphone-12-pro)
      - [Home Page](#home-page-1)
      - [Search bar function](#search-bar-function-1)
      - [Articles by product families page](#articles-by-product-families-page-1)
      - [News Page](#news-page-1)
      - [Login Page](#login-page-1)
      - [Register Page](#register-page-1)
      - [Logout Page](#logout-page-1)
      - [Single article page](#single-article-page-1)
        - [Unauthenticated user](#unauthenticated-user-1)
        - [Authenticated user - Comment and like section](#authenticated-user---comment-and-like-section-1)

## Browser Compatibility

I tested the site on different browsers Google Chrome, Edge and Mozilla.

The layout, the features as buttons, search bars, like, comment form, alerts are displayed correctly and are all working correctly. The site features are functioning as intended.  Images are displayed correctly.

| Browser       | Layout rendered as expected | Features and buttons work as expected | Images work as expected |
| ------------- | --------------------------- | -------------------- | ------------------ |
| Google Chrome | Yes                         | Yes                  | Yes                |
| Edge          | Yes                         | Yes                  | Yes                |
| Mozilla       | Yes                         | Yes                  | Yes                |

## Lighthouse

I tested performance, accessibility, best practice, and SEO using Lighthouse accessed via DevTools and here are the results:

![Lighthouse report](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse_licensing_capsule.png)

<details>
<summary>Lighthouse Results by page</summary>

![Lighthouse report home](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse_licensing_capsule.png)

![Lighthouse report news](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse-licensing-capsule-news.png)

![Lighthouse report single article page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse_singlearticle.png)

![Lighthouse report login](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse_login_page.png)

![Lighthouse report logout](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse_logout_page.png)

![Lighthouse report register](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/lighthouse_register_page.png)

</details>

[Back to table of contents](#table-of-contents)

## Code Validation

### HTML

I passed all html pages through the [W3C](https://validator.w3.org/) official validator. Most of the files passed without any errors and warnings. These are the results:

* Home page – pass

* News page -pass

* Single article page - warnings and errors received on elements caused by the Summernote library used to write the articles. These errors cannot be rectified as they come from the library.

    ![Screenshot html code validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/html_code_validation_summernote_error.png)

    ![Screenshot html code validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/singlearticle_error_summernote_code.png)

  * Also under this page an error was received indicating that a “form” element may not be a child of “strong” element.

    ![Screenshot error html code validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/singlearticle_error_code_validation.png)

  * I replaced the “strong” tag with a “div” and the error is no longer appearing.

* Search result page – pass
  
* Articles by product families page – pass
  
* Login page – pass

* Register page – errors were received regarding the allauth signup html template. This code is not visible in the signup/register template and could not be rectified.
  
![Screenshot error html code validator for register page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/register_allauth_html_code_validation_error.png)

![Screenshot html code validator for register page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/register_code_error_validation.png)

* Edit comment page – pass
  
* Delete comment page – pass

* Logout page – pass
  
* 404,500,403 error pages - pass

### CSS

The style.css file successfully passed through the [Jigsaw](https://jigsaw.w3.org/css-validator/) official validator without any errors being detected.

![Screenshot CSS code validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/css_code_validation.png)

Only one warning displayed regarding the imported Google fonts, as per below:

![Screenshot CSS code validator-warning](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/css_code_validation_warning.png)

### Javascript

No errors were found for modal.js when passing through the official [Jshin](https://jshint.com/) validator.  

### Python

All python files were successfully passed through the [PEP8]( https://pep8ci.herokuapp.com/#) official validator. Long lines were present in both "urls.py" and "views.py" files. These lines were shorttened and resubmitted to the validator without any errors being detected.

The only file containing a message is the "settings.py" for the "AUTH_PASSWORD_VALIDATORS".

![Screenshot PEP8CI validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/pepci_settingspy.png)

[Back to table of contents](#table-of-contents)

## Manual Testing

* I have thoroughly tested all functions and features, confirming their proper functionality as expected.

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
| Logo name (upper left corner)| When clicked should bring back to Home page.| Click | When clicked it leads to Home page. ![Navbar](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_navbar_logo.png)|
|Home navigation link (upper right corner) |When hovering over it should be light blue and when clicked should bring back to Home page. | Hover over and click | When hovering Home nav link is light blue; When clicked it leads to Home page.|
|News navigation link (upper right corner) |When hovering over it should be light blue and when clicked should bring to "News" page which lists all articles. | Hover over and click | When hovering the "News" nav link is light blue; When clicked it leads to "News" page and displays all articles. |
|Login page | When clicked it should lead to the Login page. | Click | When clicked it leads to Login page. ![Login Page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/login_page.png)|
| | After entering their valid credentials and clicking the Login button, the user should be logged in. They should see a green alert message at the top of the page. Their username should be displayed in the top-right  corner | Click |  After entering their credentials and clicking the “Login” button, the user is logged in. The green alert is displayed. The username is displayed in the top-right  corner. ![User logged in](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/navbar_user_logged_in.png) |
| | If user enters wrong username or password, they should be prompted with the message” The username and/or password you specified are not correct.” | Type valid data|  If user enters wrong username or password, they are prompted with the message ”The username and/or password you specified are not correct.”![Incorrect credentials](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/login_incorrect_password.png)|
|Register navigation link (upper right corner) |When clicked it should lead to the “Register” page. | Click and redirection to "Register" page | When clicked it leads to “Register” page. ![Register page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/register_page.png)|
| |To register the user should have “Username” and “Password” as mandatory fields.  | Enter data | “Username” and “Password are mandatory fields.|
| |Email should be an optional field.  | Enter data | Email is an optional field|
| |The conditions indicated must be met to create a password. | Enter data | If the conditions are not met the account is not created, the user ![Register-Enter valid data](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/register_enter_valid_password.png)|
| |Once registered, the user should be signed in and see their username displayed in the top right corner. | Authentication and redirection to Home page | Once registered, the user signs in and see their username displayed in the top right corner. They are directed to the “Home” page ![Register and log in](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/register_successful_logged_in.png)|
|Logout navigation link (upper right corner) | To logout, the user should click on “Logout”. They should be redirected to the “Log Out” page. When clicking on “Log Out” they should be redirected to the “Home” page| Click and redirection to Home page | When clicking on Logout, the user is redirected to the “Log Out” page. When clicking on “Log Out”  to confirm the action, they are redirected to the “Home” page. ![Logout](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/logout_page.png)|
| Search bar function| When entering Microsoft product names or entering a word that is included in the articles, the user should be redirected to an “Article results” page.If no articles are found, there should be a message stating “No articles found”| Enter query | When the user enters Microsoft product names, or enters a word that is included in the articles, the user is directed to an “Article results” page. If no articles are found, there is a message stating “No articles found”.![Search results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/search_results.png) ![Search no results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/search_no_articles.png)|
|Latest news on Home Page |The Latest news section should only include three most recent articles on the site that are dynamically displayed and automatically updated when a new article is published.  | Display data | The Latest news section includes the three most recent articles on the site, and they are dynamically displayed and automatically updated when a new article is published.|
| Product Families |The user should see the Product families listed on the “Home Page”.When a user clicks on a product name, they should be redirected to a page that displays all the articles related to that corresponding family name. On the article results by product family page, there should be a “Back to Home” button to allow users to easily return to the main page. | Click and Redirect to relevant articles | On the right-hand side, there is a list of all available Product Families. When a user clicks on a product name, they are redirected to a page that displays all the articles related to that corresponding family name. On the article results by product family page, there is a “Back to Home” button. This button allows users to easily return to the main page. ![Articles by product family](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/articles_by_product_family.png)|
| Most liked and commented articles|On the “Home page” the user should find three cards: the first and second cards should display the two most liked articles and the third card should highlight the most commented article. The articles should be accessed by clicking on the article title. | Display most liked and commented articles | On the “Home page” the user can find the three cards: the first and second cards display the two most liked articles and the third card highlights the most commented article.The articles can be accessed by clicking on the article title.![Most Liked and Commented articles](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/home_most_liked_and_commented.png)|
|News page |Under the news page the user should be able to view a list of all articles. At the bottom of the page, there should be pagination links that enable users to navigate to the “next” or “last” page.  | Pagination link | Under the news page the user can view a list of all articles. At the bottom of the page, there are pagination links that enable users to navigate to the “next” or “last” page. ![News - pagination](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/news_all_articles_and_pagination.png)|
| Single article page and access| Articles should be accessed by clicking on their title on any of the page on the site where they are listed: “Latest News” section, “Most liked and commented articles” section, “Search results” page, “Articles by product family” page.| Click | Articles can be accessed by clicking on their title on any page across the website where they are listed: “Latest News” section, “Most liked and commented articles” section, “Search results” page, “Articles by product family” page.|
| |When accessing an article, unauthenticated users should be able to view the article’s content, see the number of likes and comments it has received, and read existing comments. | View data | When accessing an article, unauthenticated users can view the article’s content, see the number of likes and comments it has received, and read existing comments.![Article body and icons](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_body_and_icons.png)|
|Like an article – unauthenticated user |Unauthenticated users should not be able to like an article. When clicking on the like icon, they should be prompted with a popup window stating “You must be logged in to like and leave a comment.” | Click on Like icon | Unauthenticated users are not able to like an article. When clicking on the like icon, they are prompted with a popup window stating, “You must be logged in to like and leave a comment.” When the user clicks on “Ok” the window closes and they return to the article. ![Modal popup window](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_modal_message.png)|
|Like – logged in user | Authenticated user should be able to like and unlike an article by clicking on the “like” icon, that is provided on the article’s page. | Click on like icon | Authenticated user are able to like and unlike an article by clicking on the “like” icon, that is provided on the article’s page. |
|Add comment – logged in user |When a user is logged in, they should have the option to submit a comment using a comment form. After sending a comment, they should be prompted with the message “Your message is waiting approval.”| Submit comment | When a user is logged in, they have the option to submit a comment using a comment form. After sending a comment, they will be prompted with the message “Your message is waiting approval.” Once approved it appears in the comment section.![Leave comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_leave_comment.png)![Pending approval](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/comment_waiting_approval.png)|
| |If the user attempts to refresh immediately after submitting the comment that is pending for approval, a pop-up message should appear as a warning. This message should indicate that refreshing at this point, might result in the duplication of their action, which leads to the resubmission of the same comment twice if they proceed. |Refresh page  | If the user attempts to refresh the article page immediately after submitting the comment that is pending for approval, a pop-up message will appear as a warning. This message indicates that refreshing at this point, might result in the duplication of their action, which leads to the resubmission of the same comment twice if they proceed. ![Confirm form resubmission](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/comment_resubmission_message.png)|
|Edit comment – logged in user |Logged in users should be able to edit their own comments. When editing the comment, the user is redirected to a new page where they can make the necessary changes. After editing, they are redirected to the previous page and they are be prompted with a success message alert that automatically dismisses after 5 seconds.  | Click on Edit  button | Logged in users can edit their own comments. When editing the comment, the user is redirected to a new page where they can make the necessary changes. After editing, they are redirected to the previous page, and they are be prompted with a success message alert that automatically dismisses after 5 seconds.  ![Edit comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_edit_comment.png) ![Confirmation edit](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_successful_edit_comment.png)|
|Delete comment – logged in user| Logged in users should be able to delete their own comments. When deleting a comment, the user should be prompted with a confirmation message to confirm the deletion. After confirming, the comment should be deleted. They are redirected to the previous page and they are prompted with a success message alert that automatically dismisses after 5 seconds. | Click on Delete button | Logged in users can delete their own comments. When deleting a comment, the user is prompted with a confirmation message to confirm the deletion. After confirming, the comment will be deleted. They are redirected to the previous page and they are prompted with a success message alert that automatically dismisses after 5 seconds. ![Confirm deletion](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_deletion_confirmation_page.png) ![Comment deleted](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/singlearticle_successul_message_comment_deletion.png)|
|Error pages: 403,404,500 Error |These pages should have a “Back to Home” button which should redirect to the “Home” page | Click | When displayed, these error pages have a “Back to Home” buttons which when clicked redirects to the “Home” page. ![404 error](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagesreadme/404_error_page.png)|
| Footer| When clicking on Facebook, Linkedin and Twitter pages, they should redirect to the corresponding site by opening in a new tab. | Click | When clicking on Facebook, Linkedin and Twitter pages, they redirect to the corresponding site by opening in a new tab.|

[Back to table of contents](#table-of-contents)

## User Story Testing

|                User Story                            |   Testing                                                         |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
|As an admin, I can access an admin panel where I can view users, comments, and posts and filter in the sections so that I can efficiently oversee and maintain the website and its content.| <ul><li>You can access the admin panel in the backend. In the Admin panel, you can view users, comments, and articles. You can filter each section accordingly.</li></ul>|
|As an admin I can create, read, update, and delete articles, so that I can manage my articles.   | <ul><li>You can create an article in the admin panel. There is an article section where you can view the existing articles, edit, and delete them. </li></ul>|
| As an admin I can approve or disapprove comments so that I can filter out inappropriate comments. | <ul><li>You can approve and disapprove the comments from the Comments section in the Admin panel.</li></ul>|
| As an admin, I can add a title, slug, author, image, content, select status of an article so that I can efficiently create the articles for the website.  | <ul><li>You can create an article and add all the fields, title, slug, author, image, content and select status of an article.</li></ul>|
| As an admin, I can create draft articles so that I can complete the content at a later time.  | <ul><li>When creating the article there is a dropdown menu which allows you to select “published” or “draft”. </li></ul>|
| As an admin, I can view and manage registered users so that I can monitor the user base.  | <ul><li> The users can be managed from the Admin panel under the “Users” section. </li></ul>|
| As a user on the site, I can view articles by clicking on their title so that I can read the full content.  | <ul><li>The site is accessible to all users, allowing them to view and read all listed articles.  The articles can be accessed by clicking on their title.</li></ul>|
|As a site user, I can view the article’s author and publication date and time so that I stay informed about contributors and remain up to date with the latest developments in specific licensing news and updates. | <ul><li> Under the title of each article, you will find the publication date, time, and the author’s name.  </li></ul>|
| As a site user, I can read comments of an article so that I can view other readers feedback and insights on the article.  | <ul><li> All users can access and read the comments on any article. </li></ul>|
| As a site user, I can view the most liked and commented articles so that I can stay informed about licensing trends and most discussed topics within the community. | <ul><li> The most liked and commented articles can be found at the bottom of the home page.These articles are dynamically updated based on the number of likes and comments they receive. </li></ul>|
| As a user on the site I can search the articles on the site so that I can easily locate the relevant content. | <ul><li>The search bar function is accessible on every page, located in the top-right corner just beneath the navigation bar.</li></ul>|
| As a user on the site, I can access the articles by Product family so that I can save time and efficiently access the topics I am interested in.  | <ul><li> You can find the Product Family category on the home page, situated to the right of the “Latest articles” section. You can access the relevant articles by clicking on the Product name. </li></ul>|
| As a frequent site user, I can register on the site so that I can provide feedback on the content and to the content creator and engage with other readers.  | <ul><li>You can register as a user, by clicking on “Register”, located in the top right corner.</li></ul>|
| As a registered user I can login and see my login status so that that I know when login was successful.  | <ul><li> You can login by selecting “Login” in the top right corner. Once logged in, you are prompted with a message indicating successful login. Furthermore, as long as you are logged in, your username will be displayed in the top-right corner. </li></ul>|
| As a registered site user I can add a comment on an article so that I can engage with the content, ask questions, offer suggestions to the author, participate in discussions with other readers. | <ul><li> Registered users can submit a comment, through the comment form available at the bottom of each article. This comment form becomes accessible when you log in to your account. </li></ul>|
| As a registered user, I can edit and delete comments so that I can manage my contributions, edit, and remove mistakes or inaccurate information. | <ul><li> Registered users can edit and delete their comments once they have been approved. You will see the “Edit” and “Delete” buttons under your comment.</li></ul>|
| As a registered site User, I can like an article so that I can show appreciation and support to the content creator. | <ul><li>Registered users can like and unlike articles. The “Like” option can be found at the bottom of each article.</li></ul>|
| As a site user I can view number of likes and comments of an article so that I can gain valuable insights and perspectives from other readers regarding the topic. | <ul><li>All users can view the number of likes and comments on an article, which is available at the bottom of each article. Additionally, on the home page, users can see the articles with the highest number of likes and comments.</li></ul>|

[Back to table of contents](#table-of-contents)

## Bugs

### Fixed Bugs

**Incorrect display of articles when clicking on Product Family name  from Home page**

When clicking on a Product Family name from the Home page, all articles were displayed instead of the ones relevant to the selected Product Family.

* I created a Product Families section to allow users to easily access the articles by Product Family name without having to search in search bar or to manually go through all articles in “News” page.

* Initially, I encountered an issue in class "ArticlesByProductFamily" in the "views.py" file, where clicking on a product name on the page, resulted in displaying all articles. The issue was due to the use of an incorrect filter based on "Status", which listed all the Published articles.

![Bug articles by product](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/bug_articles_by_product.png)

* I resolved this problem by checking in the Admin panel how the articles were filtered when grouped by Product Family.
* I used 'product_name__id__exact' which now correctly displays the relevant articles. Refer to [commit cd69138](https://github.com/AdrianaStoi/Licensing-Capsule/commit/cd69138b6cc3fd6aea13e3637aa263e9035142e7)

![Admin panel](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/bug_solved_articles_by_product_name_usingadminpanel.png)
![Articles by product family](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/bug_solved_articles_by_product.png)

**Pagination display issue resolved for Galaxy Fold with Media Queries**

* The pagination on the last page was not displaying properly on Galaxy Fold. I used dev tools and adjusted the font-size accordingly. I added media queries for max-width 287 devices in the style.css.

![Pagination](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/bug_responsiveness_pagination_galaxyfold.png)

* On the “News” page I noticed that the pagination number on the final page was not rendering correctly when viewed on the Galaxy Fold. To address this issue, I used dev tools to modify the font size.  I added media queries in the style.css file targeting devices with  a max-width 287 devices.

![Pagination solved](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/solved_bug_responsiveness_galaxyfold_pagination.png)

### Unfixed Bugs

* I am not aware of any remaining unresolved bugs.

[Back to table of contents](#table-of-contents)

## Testing Responsiveness

* Chrome DevTools was used for testing responsiveness on desktop, tablets, and smartphones.
  
* The page layout, images, search button, like/unlike, comment form, comment/like count, login, register/logout, modal message popup when user is not logged in and tries to like an article are all displayed correctly, as expected. The testing on various devices has ensured that the site functions properly and provides the desired user experience.

### Responsiveness on devices

| Responsiveness                           | Desktop >1200px | Desktop 1024px | Devices >= 700 iPad Air/Mini, Surface Pro 7 | Devices <699 iPhone SE/ XR/12 Pro/X, Pixel, Samsung Galaxy S8+/ A51/71/Fold |
| ---------------------------------------- | --------------- | -------------- | ------------------------------------------- | --------------------------------------------------------------------------- |
| Links, icons and buttons work                               | Yes             | Yes            | Yes                                         | Yes                                                                         |
| Login,logout, register functions work                              | Yes             | Yes            | Yes                                         | Yes                                                                         |
| Images, Layout and Content displayed as expected | Yes             | Yes            | Yes                                         | Yes|

* I tested on iPad Mini (768x1027) and iPhone 12 Pro (390x844) and these are the results:

### iPad Mini 

* The website displays a consistent layout when accessed on an iPad Mini with a screen resolution of 768x1027, as detailed below:
  
<details>
<summary> iPad Mini </summary>

#### Home Page

![Home page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_home_page.png) ![Home-Latest news and product families section](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_latest_articles_prodfamilies.png) ![Home Page- Most liked and commented articles](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_most_liked_commented_articles.png)

#### Search bar function

![Search results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_search_results.png)

![Search no results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_search_no_results.png)


#### Articles by product families page

![Articles by product families](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/articles_by_product_families.png)

#### News Page

![News-all articles list](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_allarticles.png)

![News-all articles pagination](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_allarticles_pagination.png) ![News-all articles pagination last page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_allarticles_pagination_last.png)

#### Login Page

![Login page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_login.png)

![Login status](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_loggedin_status.png)

#### Register Page

![Register page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_register.png)

#### Logout Page

![Logout page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_loggout.png)

#### Single article page

![Single article body](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_singlearticle.png)

##### Unauthenticated user

* When the user is not logged in, he can see the number of likes and comments. When he clicks on like icon he receives the popup window:

![Comments view and Likes Modal window](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_modal.png)

##### Authenticated user - Comment and like section

* When the user is logged in, the comment form is displayed. They can like, unlike and perform actions as "Edit" and "Delete" their own comments: 

![Authenticated user-comment form and section](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_comment_form_edit_del.png)

* Pending comment approval
  
![Pending comment approval](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_comment_waiting_approval.png)

* Edit comment
  
![Edit comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_edit_comment.png) ![Edit success message](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_successful_edit.png)

* Delete comment

![Delete comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_confirm_deletion.png) ![Deletion comment confirmed](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/ipadmini_comment_deleted.png)

</details>

[Back to table of contents](#table-of-contents)

### iPhone 12 Pro

* I also conducted testing on an iPhone 12 Pro with a screen resolution of (390x844), and all functions are displayed correctly, as shown below:

<details>
<summary> iPhone 12 Pro </summary>
#### Home Page

![Home page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_home_page.png)![Home page navbar](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_home_navbar.png) ![Home- about us and latest news](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_about_us.png)

![Home-Latest news and product families section](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_product_families.png) ![Home Page- Most liked and commented articles](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_most_liked.png)

#### Search bar function

![Search results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_searchresults.png) ![Search no results](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_no_articles_found.png)


#### Articles by product families page

![Articles by product families](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_articles_by_product_family.png)

#### News Page

![News-all articles list](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_allnews_page.png)  ![News-all articles pagination](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_allnews_pagination.png)  ![News-all articles pagination last page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_allnews_second_pagination.png)

#### Login Page

![Login page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_login_page.png)![Successfully logged in](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_loggedin%20user.png)![Login status](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_login_status.png)

#### Register Page

![Register page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_register_page.png)

#### Logout Page

![Logout page](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_logout.png)![Successfull logout](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_successful_logout.png)

#### Single article page

![Single article body](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_singlearticle.png)

##### Unauthenticated user

* When the user is not logged in, he can see the number of likes and comments. When he clicks on like icon he receives the popup window:

![Comments view and Likes Modal window](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_singlearticle_modal.png) ![Comments view unauthenticated user](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_singlearticle_comment.png)

##### Authenticated user - Comment and like section

* When the user is logged in, the comment form is displayed. They can like, unlike and perform actions as "Edit" and "Delete" their own comments: 

![Authenticated user-comment form and section](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_comment_form.png) ![Edit and delete own comment options](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_edit_delete_comment.png)

* Pending comment approval
  
![Pending comment approval](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_comment_waiting_approval.png)

* Edit comment
  
![Edit comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_edit_comment.png) ![Edit success message](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_edit_successully.png)

* Delete comment

![Delete comment](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_confirm_deletion.png) ![Deletion comment confirmed](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/iphone12pro_message_success_deletion.png)

</details>

[Back to table of contents](#table-of-contents)

**Return to the [README.md](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/README.md) file.**