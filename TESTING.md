
# Testing

## Testing Responsiveness

* Chrome DevTools was used for testing responsiveness on desktop, tablets, and smartphones.
  
* The page layout, images, search button, like/unlike, comment form, comment/like count, login, register/logout, modal message popup when user is not logged in and tries to like an article are all displayed correctly, as expected. The testing on various devices has ensured that the site functions properly and provides the desired user experience.

* I tested on iPad Mini (768x1027) and iPhone 12 Pro (390x844) and these are the results:

### iPad Mini

* The website displays a consistent layout when accessed on an iPad Mini with a screen resolution of 768x1027, as detailed below:

#### Home Page

![ ]()

#### News Page

#### Login Page

#### Register Page

#### Logout Page

#### Single article page



### Responsiveness on devices

| Responsiveness                           | Desktop >1200px | Desktop 1024px | Devices >= 700 iPad Air/Mini, Surface Pro 7 | Devices <699 iPhone SE/ XR/12 Pro/X, Pixel, Samsung Galaxy S8+/ A51/71/Fold |
| ---------------------------------------- | --------------- | -------------- | ------------------------------------------- | --------------------------------------------------------------------------- |
| Links, icons and buttons work                               | Yes             | Yes            | Yes                                         | Yes                                                                         |
| Login,logout, register functions work                              | Yes             | Yes            | Yes                                         | Yes                                                                         |
| Images, Layout and Content displayed as expected | Yes             | Yes            | Yes                                         | Yes|

## Browser Compatibility

I tested the site on different browsers Google Chrome, Edge and Mozilla.

The layout, the features as buttons, search bars, like, comment form, alerts are displayed correctly and are all working correctly. The site features are functioning as intended.  Images are displayed correctly.

| Browser       | Layout rendered as expected | Features and buttons work as expected | Images work as expected |
| ------------- | --------------------------- | -------------------- | ------------------ |
| Google Chrome | Yes                         | Yes                  | Yes                |
| Edge          | Yes                         | Yes                  | Yes                |
| Mozilla       | Yes                         | Yes                  | Yes                |


## Code Validation

### HTML

I passed all html pages through the [W3C](https://validator.w3.org/) official validator. Most of the files passed without any errors and warnings. These are the results:

* Home page – pass

* News page -pass

* Single article page - warnings and errors received on elements caused by the Summernote library used to write the articles. These errors cannot be rectified as they come from the library.

    ![Screenshot html code validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/html_code_validation_summernote_error.png)

    ![Screenshot html code validator](https://github.com/AdrianaStoi/Licensing-Capsule/blob/main/documentation/imagestesting/singlearticle_error_summernote_code.png)

  * Also under this page an error was received indicating that a “form” element cannot be a child of “strong” element.

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

All python files were successfully passed through the [PEP8]( https://pep8ci.herokuapp.com/#) official validator without any errors being detected.