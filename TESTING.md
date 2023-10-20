

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

![]()

* Also an error received indicating “form” element cannot be a child of “strong” element. I changed the “strong” to “div”. The error is no longer received.

![]()

![]()

* Search result page – pass
  
* Articles by product families page – pass
  
* Login page – pass

* Register page – errors were received regarding the allauth signup template. This code was not visible in the signup/register template and could not be rectified.
  
![]()

![]()

* Edit comment page – pass
  
* Delete comment page – pass

* Logout page – pass
  
* 404,500,403 error pages - pass

### CSS

The style.css file successfully passed through the [Jigsaw](https://jigsaw.w3.org/css-validator/) official validator without any errors being detected. Only one warning displayed regarding the imported google fonts. 

![]()

![]()

### Javascript

No errors were found for modal.js when passing through the official jshin validator  https://jshint.com/

### Python

All python files were successfully passed through the [PEP8]( https://pep8ci.herokuapp.com/#) official validator without any errors being detected.