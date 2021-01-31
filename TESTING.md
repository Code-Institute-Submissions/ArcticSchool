# Testing

- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validators](#validators)
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

---

<div align="right">
    <b><a href="#testing">Back To Top</a></b>
</div>