# Testing

- [Testing](#testing)
  - [Manual Testing](#manual-testing)
    - [Navigation](#navigation)
    - [Home Page](#home-page)
    - [Lessons Page](#lessons-page)
    - [Team Page](#team-page)
    - [Resorts Page](#resorts-page)
    - [Booking Page](#booking-page)
      - [Empty](#empty)
      - [When Booked](#when-booked)
    - [Contact Page](#contact-page)
      - [My Bookings](#my-bookings)
      - [Active Bookings Page](#active-bookings-page)
      - [Archived Bookings Page](#archived-bookings-page)
      - [Booking Review Page](#booking-review-page)
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

### Navigation

### Home Page

### Lessons Page

### Team Page

### Resorts Page

### Booking Page

#### Empty

#### When Booked

### Contact Page

#### My Bookings

#### Active Bookings Page

#### Archived Bookings Page

#### Booking Review Page

### Account Page

### Authentication pages (Allauth)

### Management/Administration (CRUD)

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
- **Fix**: Removed all django-responsive2 code and information. I've asked Code Institute - Tutors section for help/solution, advice given : try to use Bootstrap breakpoints and classes instead of django-responsive2. \
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

- **Bug**: ./manage.py loaddata fiel.json command not working and showin the error message. I couldn't make a migrations properly.
- **Fix**: Command found on [https://stackoverflow.com](https://stackoverflow.com) ./manage.py migrate --run-syn
- **Verdict**: Database synchronized, all unmigrated migrations applied. Fixtures loaded. Working as expected. Beautifully !

#### Team cards - read more button

- **Bug**: When button is clicked on random card, description on all cards is shoew.
- **Fix**: Forloop iterate number added to ID and target ID -  '{{ forloop.counter }}'
- **Verdict**: Dropdown description field shows only on card where button was clicked. Work as expected!

#### Relation does not exist error in Django when deployed

- **Bug**: When trying to access login page, website shows relation error page.
- **Fix**: Data base url changed in settings. Migrations have been updated. Database url changed to Development database.
- **Verdict**: Deployed website works as expected.

#### User Form not updated while payment is proccessed

- **Bug**: While making payment user form details form should be updated
- **Fix**: I have added two print statement when form suppoused to be validated. I've received message for 'else' = not valid. To get more info I have searched in Django dosc., I've used {{ form.error }} in as messages to see what is creating my issue when form is validated. Solution! Required newsletter field changed to not be required anymore.
- **Verdict**: Form validation = passed! User details form updated.

#### Sass compiler stopped working main.scss file update stopped

- **Bug**: When editing other files than main.scss while using sass compiler is working on file, save is not updating.
- **Fix**: Import files names have been chagned from example.scss to _example.scss .
- **Verdict**: This will inform compiler these files are partials for main.scss file and they will be import corretly. Main.scss file updated as expected. Css.map  file is not created anymore based on compiler settings.

#### Adding or Editing Lessons, Instructor Profiles, Resorts

- **Bug**: When adding/editing Lesson, Instructor Profile Card or Resorts on Management Pages images weren't uploading to Database.
- **Fix**: HTML `<form>` enctype attribute  `enctype="multipart/form-data"` added to Add/Edit Management Forms
- **Verdict**: Images uploading and changing correctly.

---

<div align="right">
    <b><a href="#testing">Back To Top</a></b>
</div>