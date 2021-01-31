# Testing

## Manual Testing

---

## Validators

---

## Compatibility and Responsiveness

---

## Bugs

### Bugs During Development

During development of this project I've faced my lack of knowledge and lots of challenging issues that makes my life 10000 times harder then it actually was.. Most of the solutions were so simply that I couldn't believe in it.

Verdict? Don't waist your time trying re-invent the wheel. Take a small break and try to release all the stress and bad thinking. Ask for advice, don't be afriad to do it. There is plenty of people with bigger knowledge and great, great solutions!

<strong>Django-responsive2</strong>

- <strong>Bug</strong>: Issues with setting up django-responsive2, show different navigation bar on different device size.
- <strong>Fix</strong>: Removed all django-responsive2 code and information. I've asked Code Institute - Tutors section for help/solution, advice given : try to use Bootstrap breakpoints and classes instead of django-responsive2. \
  Display classes applied to index.html header code.
- <strong>Verdict</strong>: Result as expected. Different navigation bars presented on different device size.

<strong>Navigation Hamburger Button</strong>

- <strong>Bug</strong>: Navigation hamburger button not working on medium devices.
- <strong>Fix</strong>: Different ID selector added to medium size / tablet nav bar, script.js function extended.
- <strong>Verdict</strong>: Hamburger button anmiation working as expected.

<strong>Social Media Icons</strong>

- <strong>Bug</strong>: Social media style seems to be incorect after moving social media icons code snippet to speparate html file/includes.
- <strong>Fix</strong>: CSS classes adapted to match previous stlye.
- <strong>Verdict</strong>: Social media icons section presented in the same way, as before moving code to outside html file. Social-media-set.html file can be used as includes when building homepnage.

<strong>Fixture and migrations issue</strong>

- <strong>Bug</strong>: Python3 manage.py loaddata fiel.json command not working and showin the error message. I couldn't make a migrations properly.
- <strong>Fix</strong>: Command found on []() \
    python manage.py migrate --run-syn
- <strong>Verdict</strong>: Database synchronized, all unmigrated migrations applied. Fixtures loaded. Working as expected. Beautifully !

<strong>Team cards - read more button</strong>

- <strong>Bug</strong>: When button is clicked on random card, description on all cards is shoew.
- <strong>Fix</strong>: Forloop iterate number added to ID and target ID -  '{{ forloop.counter }}'
- <strong>Verdict</strong>: Dropdown description field shows only on card where button was clicked. Work as expected!

<strong>Relation does not exist error in Django when deployed</strong>

- <strong>Bug</strong>: When trying to access login page, website shows relation error page.
- <strong>Fix</strong>: Data base url changed in settings. Migrations have been updated. Database url changed to Development database.
- <strong>Verdict</strong>: Deployed website works as expected.

<strong>User Form not updated while payment is proccessed</strong>

- <strong>Bug</strong>: While making payment user form details form should be updated
- <strong>Fix</strong>: I have added two print statement when form suppoused to be validated. I've received message for 'else' = not valid. To get more info I have searched in Django dosc., I've used {{ form.error }} in as messages to see what is creating my issue when form is validated. Solution! Required newsletter field changed to not be required anymore.
- <strong>Verdict</strong>: Form validation = passed! User details form updated.

<strong>Sass compiler stopped working main.scss file update stopped</strong>

- <strong>Bug</strong>: When editing other files than main.scss while using sass compiler is working on file, save is not updating.
- <strong>Fix</strong>: Import files names have been chagned from example.scss to _example.scss . 
- <strong>Verdict</strong>: This will inform compiler these files are partials for main.scss file and they will be import corretly. Main.scss file updated as expected. Css.map  file is not created anymore based on compiler settings.

---

<div align="right">
    <b><a href="#arctic-school-">Back To Top</a></b>
</div>