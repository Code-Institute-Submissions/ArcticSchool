# Testing

- [Testing](#testing)
  - [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Navigation](#navigation)
    - [Home Page](#home-page)
    - [Lessons Page](#lessons-page)
      - [Lesson Page](#lesson-page)
    - [Booking Page](#booking-page)
    - [Checkout Page](#checkout-page)
    - [Checkout Success Page](#checkout-success-page)
    - [Contact Page](#contact-page)
    - [My Bookings](#my-bookings)
      - [Active / Archived Booking Pages - Booking Review Page](#active--archived-booking-pages---booking-review-page)
    - [Account Page](#account-page)
    - [Authentication pages (Allauth)](#authentication-pages-allauth)
    - [Management/Administration (CRUD)](#managementadministration-crud)
  - [Validators](#validators)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Debug = True](#debug--true)
  - [Compatibility and Responsiveness](#compatibility-and-responsiveness)
  - [Bugs](#bugs)
    - [Bugs During Development](#bugs-during-development)
      - [Django-responsive](#django-responsive)
      - [Navigation Hamburger Button](#navigation-hamburger-button)
      - [Social Media Icons](#social-media-icons)
      - [Fixture and migrations issue](#fixture-and-migrations-issue)
      - [Team cards - read more button](#team-cards---read-more-button)
      - [Relation does not exist error in Django when deployed](#relation-does-not-exist-error-in-django-when-deployed)
      - [User Form not updated while the payment is processed](#user-form-not-updated-while-the-payment-is-processed)
      - [Sass compiler stopped working main.scss file update stopped](#sass-compiler-stopped-working-mainscss-file-update-stopped)
      - [Adding or Editing Lessons, Instructor Profiles, Resorts](#adding-or-editing-lessons-instructor-profiles-resorts)
      - [Removeing Instance with Image](#removeing-instance-with-image)

## Manual Testing

### Responsiveness

- **User story being tested**:
*As a User, I want to be able to access the website from my phone as I'm using it most often, also from desktop and tablet.*
- **Owner story being tested**:
*To have a good design, with easy to use interface so the custmoer/s will not feel frustrated when using they're using the website.*
- **Test**:
  - Each page of the website was created based on a mobile-first responsive web design approach, next on tablets and desktop devices
  - More information about responsiveness testing can be found in [Compatibility and Responsiveness](#compatibility-and-responsiveness) section
- **Results**: Few examples from lots of different minor issues: the wrong size of images displayed, style of Lesson Cards buttons different across all devices.
- **Verdict**: The issues were fixed, the test passed.

### Navigation

- **User story being tested**:
*As a User, I expect nice and clean website navigation so I can easily move around all pages.*
- **Test**:
  - Click on each link in the navigation to see, if they're pointing the user to the correct page
  - Check if navigation is changing links to the 'hamburger button' on tablets and mobile devices when resizing
  - Hover over navigation links to see if hover style is applied
  - Check if the navigation link has applied hover style when clicked and pointed to a page
  - Check if navigation is fixed/show on the top of the page on each page when scrolled down - all devices
  - Scroll Down to see if the 'Go to Top' button is showing after scrolled X number of pixels
  - Check if the Booking quantity icon is shown when the user add a lesson to the booking cart - Bag
  - Hover over the Account link when the user is not logged in to the user account to see the 'Login', 'Register' buttons on the dropdown menu
  - Hover over the Account link when the user is logged in to see the standard user 'My Bookings' section with Active / Archived Booking button and Logout Button
  - Hover over the Account link when Super User is logged in to see all standard user links plus Management and Home administration links
  - Hover over all links in different dropdown menu's to see, if the hover style works properly
  - Click on the scroll down button to see, if the page will scroll down to the next section
  - Click on the Arctic School logotype - link to see, if the user will be navigated to Home Page
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Home Page

- **User stories being tested**:
*As a User, I want to find more information about the company, to understand more about what they are doing, where lesson/s take place, how flexible they are with providing lesson/s.*
*As a User, I want to be able to access company social media links, so I can read more about events, new lesson/s, sales, or promo codes.*
- **Test**:
  - Scroll down on Home Page to see, if all information is displayed correctly and easy to read.
  - Click on each social media icon to see, if they're not pointing to any page when there is no Social Media Url added
  - Click on each social media icon to see, if they're pointing correctly to outside social media websites when Social Media Url link is provided
  - Click on Booking Promo Baner, 'book now' button to see if a user is navigated to the lessons page
- **Results**:
  - All Company information is provided in nice style and they're very easy to read
  - All Social Media buttons/icons are changing style when hovered and not navigating the user to outside social media website
  - All Social Media buttons/icons are navigating users to outside social media website
  - Booking banner pointing user to Lessons Page
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Lessons Page

- **User stories being tested**:
*As a User, I want to be able to search from all the lesson/s, filter, and adjust price value to find a specific to pick one I can afford.*
*As a User, I want to be able to view all lesson/s and make a safe purchase.*
- **Test**:
  - Click on the Lessons Page link
  - Search icon clicked/enter button pressed when the field is empty
  - Search icon clicked/enter button pressed when the field is not empty
  - Click on All Lessons Buton
  - Click on a Category button
  - Change filtering option
- **Results**:
  - All available lessons displayed
  - When the search field is empty an error message is displayed. 'Nothing was found' text is displayed
  - When the search field isn't empty search term is displayed below search box. Lessons match to the search term are displayed
  - When the All Lessons button is clicked, all lessons are presented on page
  - When Category lin is clicked only lessons matching clicked category are presented
  - When All lessons or Single Category is chosen and filtering option is applied page is showing lessons in the correct order
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

#### Lesson Page

- **User story being tested**:
*As a User, I want to be able to view all lesson/s details such as image (if there is one), description, time, who will be my instructor, skills level, time, and price, so that I can choose the best lesson type.*
- **Owner story being tested**:
*To provide creative, safe, and interactive lessons for customer/s.*
- **Test**:
  - Click on the lesson card 'details' button
- **Results**:
  - Information presented in good looking block and clear structure.
  - All lesson information is easy to find and read
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Booking Page

- **User story being tested**:
*As a User, I want to be able to view my chosen lesson/s, total price in the cart before purchasing, so I can make my last changes if needed.*
- **Test**:
  - No lessons booked
  - Add one lesson to the booking
  - Add more than one lesson to booking
  - Click on the Details button of booked lessons
  - Click on the Remove button of the selected lesson
  - Click on the Clear Booking button
- **Results**:
  - Display Booking Page - no lessons booked
  - Booking summary information displayed such as Booking total, Discount, if applied, Grand Total, promo banner
  - One lesson displayed on Booking Page with all information such as price, lessons name, level, participants
  - Basic information is displayed for each lesson when more than one booked, Booking summary updated
  - When the details button clicked, the user is moved to the selected lesson details page 'Lesson Page'
  - When the Remove button is clicked, the selected lesson is removed from the booking, and the booking summary is updated.
  - When the Clear Booking button is clicked. All lessons are removed from booking 'bag'. Booking - not booked page is displayed.
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Checkout Page

- **User stories being tested**:
*As a User, I expect to purchase lesson/s in a safe and secure way by using card method payments.*
*As a User, I want to be able to make quick purchases for lesson/s by using previously saved personal information.*
- **Owner story being tested**:
*To be able to provide a secure payment method for my clients/website users*
- **Test**:
  - Add lesson to booking
  - Try to click on the 'Make a Payment' button
  - Try to submit the form with incorrect email address (missing @)
  - Try to submit the form without providing a card number
  - Add Stripe Test card information and click the 'Make a Payment' button
- **Results**:
  - Button is blocked until the user will provide all required information
  - Form shows an error with wrong incorrect email address style
  - Error message displayed by Stripe
  - After successful test payment, the Payment Success Page / Checkout Success page is displayed
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Checkout Success Page

- **User story being tested**:
*As a User, I want to receive email confirmations after I successfully purchased my lesson/s.*
- **Test**:
  - Select one lesson to purchase
  - Book/add selected lesson to booking
  - Fulfill information if not logged in to account
  - Provide card details
  - Click the 'Make a Payment' button
- **Results**:
  - After successful payment user is transferred to the Checkout Success page
  - Email is not sent. The view hasn't got a function to send an email to a user after successful payment
- **Verdict**:
  - Email function added to the view
  - Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Contact Page

- **User story being tested**:
*As a User, I want to be able to contact the owner/lesson/s provider, so I can ask questions or write an additional query about their services.*
- **Test**:
  - Try to send an empty contact form
  - Try to enter an incorrect email address, without '@'
  - Try to send the form with all required fields
  - Check the pre-populated fields when the user is authenticated
- **Results**:
  - After trying to send an empty contact form, validation is showing an error message on the required field
  - After trying to send the form with an incorrect email address, validation is showing an error about the wrong email address
  - Form send properly, Success messages displayed
  - When a user is authenticated, the Full name and Email address fields are auto-populated
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### My Bookings

#### Active / Archived Booking Pages - Booking Review Page

- **User story being tested**:
*As a User, I want to be able to view my ordering history.*
- **Test**:
  - Click on the navigation Account link
  - Choose one booking from 10 Recently Booked
  - From the dropdown user menu click on Active in My Bookings menu section
  - From dropdown user menu click on Archived in My Bookings menu section
  - Click on booking user want to display
- **Results**:
  - If the user is logged in Account Page is displayed, otherwise, user is transferred to the login page
  - After logging in user is navigated to the Account Page where 10 latest orders are displayed
  - After clicking on active booking user is transferred to the Order Review page where all booking information is displayed. Including purchased lessons and details button to view lesson details
  - After clicking on the Active link in My Booking, a table with active bookings is presented. If the user booked any lessons. Otherwise, information with button navigating to Lessons Page is displayed
  - After clicking on the Archived link in My Booking, a table with archived bookings is presented. If the user hasn't got any archived bookings, a Page with information and the button 'View Active Booking' is displayed. If there is no Active Booking then information with a button navigating to the Lessons Page is displayed like in the previous case.
  - After clicking any active or archived booking user is transferred to the Order Review page with all important information and lessons booked
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Account Page

- **User stories being tested**:
*As a User, I want to be able to login back anytime.*
*As a User, I want to be able to fully changed my personal details, home address, name (in case I'm married now), phone number, e-mail address, etc.*
- **Test**:
  - Click on the Account link when not logged in
  - Click on the Loggin link
  - Try to Loggin in with empty input fields
  - Try to Loggin in with an incorrect password
  - Try to Loggin in with the wrong email address
  - Try to Loggin with correct credentials
- **Results**:
  - After clicking on the Account link user is transferred to Login Page
  - Loggin form validation system is displaying error messages
  - When all credentials are correct, the user is returned to the page he was currently displaying/viewing.
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Authentication pages (Allauth)

- **User stories being tested**:
*As a User, I want to be notified when I successfully finished the registration process.*
*As a User, I want to be able to create my own account, which will give me the possibility to store, view, and edit my profile information.*
*As a User, I want to be able to change my password from my profile account, in case my account was hacked, to protect my personal details.*
- **Test**:
  - Click on the Register link
  - Click on the Login link
  - Click on Forgot Password link
  - Click on Logout
  - Try to Loggin in with empty input fields
  - Try to Register with empty input fields
  - Try to Loggin in with incorrect credentials
  - Try to Loggin in with an incorrect password
  - Try to register with two different passwords
  - Try to register with the same existing username
  - Try to Loggin in with the wrong email address
  - Try to Register with a wrong email address
- **Results**:
  - Register page with the registration form is displayed
  - Login page with login form is displayed
  - Password reset page with reset form is displayed
  - When the logout link is clicked, the user is transferred to Home Page and a success message is displayed
  - All different combinations of `Try's` created an error with messages displayed in forms and Django-messages.
  - When Successfully logged into account success message is displayed
  - When a user  successfully registered, he is transferred to Account page to fulfill details
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Management/Administration (CRUD)

- **Admin & Owner stories being tested**:
*To have the possibility to Add, Edit, and Delete lesson/s.*
*To have a secure admin interface, easy to use. Important thing is, this interface must be available only for admins.*
- **Test**:
  - Try to access the administration page without login into the account
  - Try to access the administration page with a basic user account
  - Try to access the administration page with superuser account
  - Click on each Management and Home section link from the dropdown menu after the user is logged in (superuser)
  - Click on each Remove Button on the selected Lesson, Instructor Profile, or Resort element
  - Click on each Edit Button on the selected Lesson, Instructor Profile, or Resort element
  - Click on each Add + button on each Administration page
  - Trying to Add/Edit selected element with empty random required fields
  - Trying to Add/Edit selected element with all required fields filled
- **Results**:
  - When a user is not logged in, the Django-allauth decorator is preventing from accessing the page by navigating the user to the Administration Login page
  - When a user is logged in with a standard user account, the Django-allauth decorator is preventing from accessing the page by navigating the user to the Administration Login page
  - When a user is logged in with superuser account, Administration/Management page is displayed
  - All links are pointing superuser to correct Administration/Management page
  - Remove functionality works as expected. By clicking Remove button all instance is removed including images if assigned to.
  - When the Edit button is clicked super user is navigated to the Edit Form Page of the selected instance
  - When Add + button is clicked super user is navigated to Add Form page of the selected instance
  - When Add/Edit form is submitted and required fields are not placed or have incorrect format validation system is showing messages and the form is not submitted until all criteria match.
  - When Add/Edit form is submitted and required fields are correctly filled in form is submitted. The instance is added or edited and updated in the database
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

---

## Validators

### HTML

All the HTML files were validated by using online code validator [W3C HTML Validation Service](https://validator.w3.org).
Errors found were about IMG 'height, width' attributes missing. Wrong code scope by using UL and DIV's, also duplicated ID's were found.
Code was checked and all errors and warning were corrected, code is valid with no errors and warnings on all pages.

### CSS

All the SCSS and Main.min.css files were validated by using an online code validator [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator).
There were several errors and warnings found. There are warnings for color contrast according to the background that can be ignored.
Also, there are warnings about -WebKit- as validator is catching it as 'an unknown vendor extension'.

### JavaScript

All the JavaScript files were validated by using an online code validator [Beautifytools.com](http://beautifytools.com/javascript-validator.php).
Missing semicolons were added at the end of functions. 'Const' and 'Let' warning can be ignored.
Validator is showing the message 'is available in ES6 (use 'version: 6') or Mozilla JS extensions (use Moz).' all Const's and Let's will be converted to Var's my browser.
Code is syntactically valid.
For more information about Const, Let, and Future JS you can use [BabelJS](https://babeljs.io)

### Python

All Python files were validated by using an online code validator [Pep8](http://pep8online.com).
File changes were made to make the code PEP8 compliant where possible.

### Debug = True

While developing an app, the local debugger: `debug=True` was on.
Every time when the application has an error, the debugger was displaying an error message page.
Thanks to that I could catch all errors and fix them straight away.

---

## Compatibility and Responsiveness

This website had been being tested during the development in Safari Browser by Web Development Tools.

Mostly I've used Web Inspector and Responsive Design Mode to preview different webpages across various screen sizes, orientations, and resolutions, as well as custom viewports and user agents.

It has also been tested on different browsers such as Google Chrome or Mozilla Firefox.

I have used a powerful online screen resizer and responsiveness tester [BlueTree Screenfly](https://bluetree.ai/screenfly/) Strongly recommended for everyone who wants's easily test responsivity

---

## Bugs

### Bugs During Development

During the development of this project, I've faced my lack of knowledge and lots of challenging issues that make my life 10000 times harder than it actually was. Most of the solutions were so simple that I couldn't believe in them.

Verdict? Don't waste your time trying to re-invent the wheel. Take a small break and try to release all the stress and bad thinking. Ask for advice, don't be afraid to do it. There is plenty of people with bigger knowledge and great, great solutions!

#### Django-responsive

- **Bug**: Issues with setting up Django-responsive2, show different navigation bar on different device size.
- **Fix**: Removed all `Django-responsive2` code and information. I've asked the Code Institute - Tutors section for help/solution, advice is given: try to use Bootstrap breakpoints and classes instead of Django-responsive2. \
Display classes applied to index.html header code.
- **Verdict**: Result as expected. Different navigation bars presented on different device sizes.

#### Navigation Hamburger Button

- **Bug**: Navigation hamburger button not working on medium devices.
- **Fix**: Different ID selector added to medium size / tablet nav bar, script.js function extended.
- **Verdict**: Hamburger button animation working as expected.

#### Social Media Icons

- **Bug**: Social media style seems to be incorrect after moving social media icons code snippet to separate HTML file/includes.
- **Fix**: CSS classes adapted to match the previous style.
- **Verdict**: Social media icons section presented in the same way, as before moving code to an outside HTML file. Social-media-set.html file can be used as includes when building a homepage.

#### Fixture and migrations issue

- **Bug**: `./manage.py loaddata file-name.json` command not working and showing the error message. I couldn't make migrations properly.
- **Fix**: Command found on [https://stackoverflow.com](https://stackoverflow.com) `./manage.py migrate --run-syn`
- **Verdict**: Database synchronized, all migrations applied. Fixtures loaded. Working as expected. Beautifully!

#### Team cards - read more button

- **Bug**: When the button is clicked on a random card, the description on all cards is shown.
- **Fix**: Forloop iterate number added to ID and target `ID - '{{ forloop.counter }}`'
- **Verdict**: The dropdown description field shows only on the card where the button was clicked. Work as expected!

#### Relation does not exist error in Django when deployed

- **Bug**: When trying to access the login page, the website shows a relation error page.
- **Fix**: Database URL changed in settings. Migrations have been updated. Database URL changed to Development database.
- **Verdict**: Deployed website works as expected.

#### User Form not updated while the payment is processed

- **Bug**: While making payment user form details form should be updated
- **Fix**: I have added two print statements when the form supposed to be validated. I've received message for `'else' = not` valid. To get more info I have searched in Django dosc., I've used `{{ form.error }}` in as messages to see what is creating my issue when the form is validated. Solution! The required newsletter field changed to not be required anymore.
- **Verdict**: Form validation = passed! User details form updated.

#### Sass compiler stopped working main.scss file update stopped

- **Bug**: When editing other files than main.scss while using sass compiler is working on a file, save is not updating.
- **Fix**: Import files names have been chagned from example.scss to `_example.scss` .
- **Verdict**: This will inform the compiler these files are partials for main.scss file and they will be imported correctly. Main.scss file updated as expected. Css.map file is not created anymore based on compiler settings.

#### Adding or Editing Lessons, Instructor Profiles, Resorts

- **Bug**: When adding/editing Lesson, Instructor Profile Card or Resorts on Management Pages images weren't uploading to Database.
- **Fix**: HTML `<form>` enctype attribute `enctype="multipart/form-data"` added to Add/Edit Management Forms
- **Verdict**: Images uploading and changing correctly.

#### Removeing Instance with Image

- **Bug**: Instance removed successfully. Unfortunately, when the instance has an image, the image wasn't removed.
- **Fix**: Added if statement to modules `if instance.image - exists` than `instance.image.delete()` ,bug was fixed.
- **Verdict**: Working as expected, when the instance has an image, it's removed from DB.

---


<div align="right">
    <b><a href="#testing">Back To Top</a></b>
</div>