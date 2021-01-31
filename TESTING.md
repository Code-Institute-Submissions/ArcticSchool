# Testing

- [Testing](#testing)
  - [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Navigation](#navigation)
    - [Home Page](#home-page)
    - [Lessons Page](#lessons-page)
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
      - [User Form not updated while payment is proccessed](#user-form-not-updated-while-payment-is-proccessed)
      - [Sass compiler stopped working main.scss file update stopped](#sass-compiler-stopped-working-mainscss-file-update-stopped)
      - [Adding or Editing Lessons, Instructor Profiles, Resorts](#adding-or-editing-lessons-instructor-profiles-resorts)

## Manual Testing

### Responsiveness

- **User story being tested**:
*As a User, I want to be able to access the website from my phone as I'm using it most often, also from desktop and tablet.*
- **Owner story being tested**:
*To have a good design, with easy to use interface so the custmoer/s will not feel frustrated when using they're using the website.*
- **Test**:
  - each page of the website was created based on mobile-first responsive web design approach, next on tablets and desktop devices
  - more information about responsiveness testing can be found in [Compatibility and Responsiveness](#compatibility-and-responsiveness) section
- **Results**: Few examples from lots of different minor issues: wrong size of images displayed, style of Lesson Cards buttons different across all devices.
- **Verdict**: The issues were fixed, the test passed.

### Navigation

- **User story being tested**:
*As a User, I expect nice and clean website navigation so I can easily move around all pages.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Home Page

- **User stories being tested**:
*As a User, I want to find more information about the company, to understand more about what they are doing, where lesson/s take place, how flexible they are with providing lesson/s.*
*As a User, I want to be able to access company social media links, so I can read more about events, new lesson/s, sales, or promo codes.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Lessons Page

- **User stories being tested**:
*As a User, I want to be able to search from all the lesson/s, filter, and adjust price value to fina a specific to pick one I can afford.*
*As a User, I want to be able to view all lesson/s and make a safe purchase.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

#### Lesson Page

- **User story being tested**:
*As a User, I want to be able to view all lesson/s details such as image (if there is one), description, time, who will be my instructor, skills level, time, and price, so that I can choose the best lesson type.*
- **Owner story being tested**:
*To provide creative, safe, and interactive lessons for customer/s.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Booking Page

- **User story being tested**:
*As a User, I want to be able to view my chosen lesson/s, total price in the cart before purchasing, so I can make my last changes if needed.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Checkout Page

- **User stories being tested**:
*As a User, I expect to purchase lesson/s in a safe and secure way by using card method payments.*
*As a User, I want to be able to make quick purchases for lesson/s by using previously saved personal information.*
- **Owner story being tested**:
*To be able to provide a secure payment method for my clients/website users*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Checkout Success Page

- **User story being tested**:
*As a User, I want to receive email confirmations after I successfully purchased my lesson/s.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Contact Page

- **User story being tested**:
*As a User, I want to be able to contact the owner/lesson/s provider, so I can ask questions or write an additional query about their services.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### My Bookings

#### Active / Archived Booking Pages - Booking Review Page

- **User story being tested**:
*As a User, I want to be able to view my ordering history.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Account Page

- **User stories being tested**:
*As a User, I want to be able to login back anytime.*
*As a User, I want to be able to fully changed my personal details, home address, name (in case I'm married now), phone number, e-mail address, etc.*

### Authentication pages (Allauth)

- **User storie being tested**:
*As a User, I want to be notified when I successfully finished the registration process.*
*As a User, I want to be able to create my own account, which will give me the possibility to store, view, and edit my profile information.*
*As a User, I want to be able to change my password from my profile account, in case my account was hacked, to protect my personal details.*
- **Test**:
- **Results**:
- **Verdict**: Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

### Management/Administration (CRUD)

- **Admin & Owner stories being tested**:
*To have the possibility to Add, Edit, and Delete lesson/s.*
*To have a secure admin interface, easy to use. Important thing is, this interface must be available only for admins.*
- **Test**:
  * Remove instance from database
- **Results**:
  * Instance removed successfuly. Unfortunatelly when instance has a image, image wasn't removed.
- **Verdict**: Added if statment to modules `if instance.image - exists` than `instance.image.delete()` ,bug was fixed. 
  Tests passed, works as expected, no bugs were found during the testing. Functionality covered.

---

## Validators

### HTML

All the HTML files were validated by using online code validator [W3C HTML Validation Service](https://validator.w3.org).
Errors found were about IMG 'hegiht, width' attributes missing. Wrong code scope by using UL and DIV's, also duplicated ID's were found.
Code was checked and all errors and warning were corrected, code is valid with no errors and warnings on all pages.

### CSS

All the SCSS and Main.min.css file were validated by using online code validator [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator).
There were several errors and warning found. There are warnings for colors contrast according to background that can be ignored.
Also there are warnings about -webkit- as validator is catching it as 'an unknown vendor extension'.

### JavaScript

All the Java Script files were validated by using online code validator [Beautifytools.com](http://beautifytools.com/javascript-validator.php).
Missing semicolons were added at the end of functions. 'Const' and 'Let' warning can be ingored.
Validator is showing message 'is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).' all Const's and Let's will be converted to Var's by browser.
Code is syntactically valid.
For more information about Const, Let and Future JS you can use [BabelJS](https://babeljs.io)

### Python

All Python files were validated by using online code validator [Pep8](http://pep8online.com).
File changes were made to make the code PEP8 compliant where possible.

### Debug = True

While developing app, local debugger: `debug=True` was on.
Everytime when application has an error, debugger was displaying error message page.
Thanks to that I could catch all errors and fix them staright away.

---

## Compatibility and Responsiveness

This website had been being tested during the development on Safari Browser by Web Development Tools.

Mostly I've used Web Inspector and Responsive Design Mode to preview different webpages across various screen sizes, orientations, and resolutions, as well as custom viewports and user agents.

It also been tested on different browsers such as: Google Chrome or Mozzila FireFox.

I have used powerfull online screen resizer and resposnivness tester [BlueTree Screenfly](https://bluetree.ai/screenfly/) Strongly recommended for everyone who want's easly test responsivity

---

## Bugs

### Bugs During Development

During development of this project I've faced my lack of knowledge and lots of challenging issues that makes my life 10000 times harder then it actually was.. Most of the solutions were so simply that I couldn't believe in it.

Verdict? Don't waist your time trying re-invent the wheel. Take a small break and try to release all the stress and bad thinking. Ask for advice, don't be afriad to do it. There is plenty of people with bigger knowledge and great, great solutions!

#### Django-responsive

- **Bug** : Issues with setting up django-responsive2, show different navigation bar on different device size.
- **Fix**: Removed all `django-responsive2` code and information. I've asked Code Institute - Tutors section for help/solution, advice given : try to use Bootstrap breakpoints and classes instead of django-responsive2. \
  Display classes applied to index.html header code.
- **Verdict**: Result as expected. Different navigation bars presented on different device size.

#### Navigation Hamburger Button

- **Bug**: Navigation hamburger button not working on medium devices.
- **Fix**: Different ID selector added to medium size / tablet nav bar, script.js function extended.
- **Verdict**: Hamburger button anmiation working as expected.

#### Social Media Icons

- **Bug**: Social media style seems to be incorect after moving social media icons code snippet to speparate html file/includes.
- **Fix**: CSS classes adapted to match previous stlye.
- **Verdict**: Social media icons section presented in the same way, as before moving code to outside html file. Social-media-set.html file can be used as includes when building homepnage.

#### Fixture and migrations issue

- **Bug**: `./manage.py loaddata file-name.json` command not working and showin the error message. I couldn't make a migrations properly.
- **Fix**: Command found on [https://stackoverflow.com](https://stackoverflow.com) `./manage.py migrate --run-syn`
- **Verdict**: Database synchronized, all unmigrated migrations applied. Fixtures loaded. Working as expected. Beautifully !

#### Team cards - read more button

- **Bug**: When button is clicked on random card, description on all cards is shoew.
- **Fix**: Forloop iterate number added to ID and target `ID -  '{{ forloop.counter }}`'
- **Verdict**: Dropdown description field shows only on card where button was clicked. Work as expected!

#### Relation does not exist error in Django when deployed

- **Bug**: When trying to access login page, website shows relation error page.
- **Fix**: Data base url changed in settings. Migrations have been updated. Database url changed to Development database.
- **Verdict**: Deployed website works as expected.

#### User Form not updated while payment is proccessed

- **Bug**: While making payment user form details form should be updated
- **Fix**: I have added two print statement when form suppoused to be validated. I've received message for `'else' = not` valid. To get more info I have searched in Django dosc., I've used `{{ form.error }}` in as messages to see what is creating my issue when form is validated. Solution! Required newsletter field changed to not be required anymore.
- **Verdict**: Form validation = passed! User details form updated.

#### Sass compiler stopped working main.scss file update stopped

- **Bug**: When editing other files than main.scss while using sass compiler is working on file, save is not updating.
- **Fix**: Import files names have been chagned from example.scss to `_example.scss` .
- **Verdict**: This will inform compiler these files are partials for main.scss file and they will be import corretly. Main.scss file updated as expected. Css.map  file is not created anymore based on compiler settings.

#### Adding or Editing Lessons, Instructor Profiles, Resorts

- **Bug**: When adding/editing Lesson, Instructor Profile Card or Resorts on Management Pages images weren't uploading to Database.
- **Fix**: HTML `<form>` enctype attribute  `enctype="multipart/form-data"` added to Add/Edit Management Forms
- **Verdict**: Images uploading and changing correctly.

---

<div align="right">
    <b><a href="#testing">Back To Top</a></b>
</div>