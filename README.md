# Arctic School

Our school name doesn't mean, we are the coldest people on the earth... We are happy, funny and we've got big warm hearts, waiting for you. Our passion is to help you in your new beautiful journey by learning how to snowboarding. Our world's best trainers/teachers are here for you!

_"The attraction of snowboarding is the freedom it gives you. With a snowboard on your feet, the sky is the limit. You can do anything and go anywhere. This is not just for pro riders. It is for everyone."_\
**Jeremy Jones**

![Arctic School Mockup](https://raw.githubusercontent.com/KarolSliwka/ArcticSchool/main/wireframes/mockup.png)

---

## Table Of Contents

- [Arctic School](#arctic-school)
  - [Table Of Contents](#table-of-contents)
  - [UX](#ux)
    - [Project Goals](#project-goals)
      - [Audience](#audience)
      - [Users](#users)
      - [Site Owner/Business](#site-ownerbusiness)
    - [User Stories](#user-stories)
      - [Common User Stories](#common-user-stories)
      - [New Users](#new-users)
      - [Returning Users](#returning-users)
    - [Site Owner Goals](#site-owner-goals)
  - [Design](#design)
    - [Logotype](#logotype)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Framework](#framework)
    - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Modelling](#data-modelling)
      - [Profiles App](#profiles-app)
        - [User Profile](#user-profile)
      - [Leesons App](#leesons-app)
        - [Lesson](#lesson)
        - [Category](#category)
      - [Team App](#team-app)
        - [Instructors](#instructors)
      - [Resorts App](#resorts-app)
        - [Resort](#resort)
      - [Home App](#home-app)
        - [Level Cards](#level-cards)
        - [Lesson Cards (why our lessons)](#lesson-cards-why-our-lessons)
        - [Social Media Icons](#social-media-icons)
        - [Choices](#choices)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Tools](#tools)
    - [Databases](#databases)
  - [Features](#features)
    - [Features Left to Implement](#features-left-to-implement)
      - [Social account login (Google and Facebook)](#social-account-login-google-and-facebook)
      - [Subscribing Newsletter Form](#subscribing-newsletter-form)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
      - [Tools to be installed](#tools-to-be-installed)
      - [Accounts to be created](#accounts-to-be-created)
    - [Deployment on Heroku pages](#deployment-on-heroku-pages)
  - [Credits](#credits)
    - [Code](#code)
    - [Content and Media](#content-and-media)
    - [Acknowledgements](#acknowledgements)
  - [Contact](#contact)
  - [Disclaimer](#disclaimer)

---

## UX

### Project Goals

#### Audience

- People who want to learn snowboarding - Age is not a limit!
- People who want to improve their snowboarding skills.
- People interested in wintertime activities.
- People who want to try something new in their lives.
- People who are passionate about snowboarding.
- People who want to be trained by top-class world instructors.
- People who want to be trained safely, well-motivated, and achieve their goals.
- People who want to have fun.
- People who want to feel a bit of adrenaline while training on the highest level.

#### Users

- Get information about lesson/s provided in offers.
- Purchase selected lesson/s easily and securely.
- Contact website owner/administrator for more information about lesson/s, if needed.
- Get information about COVID-19, all restrictions, and protection information.

#### Site Owner/Business

- Engage people to start learning and discover their new limits.
- Engage people to do outdoor winter sports.
- Help people improve their snowboarding skills.
- Let people know about 'Arctic School' - a real school for everybody, "Age is not a limit!".
- Provide a fully secure, well designed, and easy to use an e-commerce platform to purchase snowboarding lesson/s.
- Make profit from selling/providing lesson/s for customers from the whole world.

### User Stories

#### Common User Stories

- As a User, I want to be able to access the website from my phone as I'm using it most often, also from desktop and tablet.
- As a User, I want to be notified when I successfully finished the registration process.
- As a User, I expect nice and clean website navigation so I can easily move around all pages.
- As a User, I want to find more information about the company, to understand more about what they are doing, where lesson/s take place, how flexible they are with providing lesson/s.
- As a User, I want to be able to access company social media links, so I can read more about events, new lesson/s, sales, or promo codes.
- As a User, I want to be able to contact the owner/lesson/s provider, so I can ask questions or write an additional query about their services.
- As a User, I want to be able to view all lesson/s details such as image (if there is one), description, time, who will be my instructor, skills level, time, and price, so that I can choose the best lesson type.
- As a User, I want to be able to search from all the lesson/s, filter, and adjust price value to fina a specific to pick one I can afford.
- As a User, I want to be able to view my chosen lesson/s, total price in the cart before purchasing, so I can make my last changes if needed.
- As a User, I expect to purchase lesson/s safely and securely by using card method payments.
- As a User, I want to receive email confirmations after I successfully purchased my lesson/s.
- As a User, I want to receive an email reminder of upcoming lesson/s, so I can prepare myself.
- As a User, I want to be able to rent additional snowboard equipment, If it is damaged or I forgot to pack it before attending the lesson/s.

#### New Users

- As a User, I want to be able to view all lesson/s and make a safe purchase.
- As a User, I want to be able to create my own account, which will give me the possibility to store, view, and edit my profile information.

#### Returning Users

- As a User, I want to be able to login back anytime.
- As a User, I want to be able to make quick purchases for lesson/s by using previously saved personal information.
- As a User, I want to be able to change my password from my profile account, in case my account was hacked, to protect my personal details.
- As a User, I want to be able to fully changed my personal details, home address, name (in case I'm married now), phone number, e-mail address, etc.
- As a User, I want to be able to view my ordering history.

### Site Owner Goals

- To provide creative, safe, and interactive lessons for customer/s.
- To have a good design, with easy to use interface so the custmoer/s will not feel frustrated when using they're using the website.
- To receive email from website users/customers when they fill out the online contact form, so I can replay their queries
- To have the possibility to Add, Edit, and Delete lesson/s.
- To be able to provide a secure payment method for my clients/website users.
- To have a secure admin interface, easy to use. Important thing is, this interface must be available only for admins.

---

## Design

### Logotype

I've used [Provicali](https://www.dafont.com/provicali.font) to create a logotype.

### Colors

The whole application coloristic was selected based on the project name and my personal style of design. Name **Arctic** will always remind us of winter and cold climate. That's why I've decided to use two main colors: white and blue. I've also used different additional tones of blue color to accent different elements of the page. To break white and blue colors I've used black and tones of black color.

After testing different coloristic to break out the blues and whites, I've decided to add another color: red.
Red will stand out and notify customers about something important on the page, something they should look at.

To create a color pallet I've used [Coolors.co](https://coolors.co) - super fast color schemes generator!

If you want to copy my color pallet scheme, please use this link [ArcticSchoolColors](https://coolors.co/ffffff-9deefb-00d4f5-31addf-1ca5dc-059cd9-000000) or view locally [ColorPalette](https://github.com/KarolSliwka/ArcticSchool/blob/main/wireframes/colour-palette.png)

![Arctic School Coloristic](https://raw.githubusercontent.com/KarolSliwka/ArcticSchool/main/wireframes/colour-palette.png)

### Fonts

In this project, I've decided to use two different fonts.
Fonts have been selected carefully to separate main titles from the content text. This should help the user read the smaller text on a different type of devices

As the main title and subtitle font, I've used -
[Montserrat](https://fonts.google.com/specimen/Montserrat?thickness=7&preview.text=&preview.text_type=custom&query=Montserrat) font. \
For other text, I've used - [Lato](https://fonts.google.com/specimen/Lato?thickness=7&preview.text=&preview.text_type=custom&query=Lato) font.

### Icons

I've used different types, shapes, and styles of icons in this project to separate important elements from the main content. Part of my icons is static files which you can download by registering on [icons8](https://icons8.com/icons). \
I have also used a [Fontawesome](https://fontawesome.com) for handy and most common icons.

### Framework

From the first time when I've started using [jQuery](https://jquery.com), I just fell in love with this JavaScript library designed to simplify tree traversal and manipulation. By using it I've created lots of different mouse events, CSS animation, and other very nice-looking features. Because of jQuery, I believe user interaction with the page is on the next level. This is making my project more attractive for users and make their experience better.

I have used [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/) to build quickly designed and customized responsive applications with a mobile-first approach. Bootstrap is providing sass variables and mixins, responsive grid system which helped me create a nice page layout and structure. I've used components to create navbar, cards, forms, etc.

### Wireframes

I have been told that everything I have created in [Axure RP9](https://www.axure.com) wasn't a wireframes but prototypes.
To recreate all wireframes I've used [Balsamiq.com](https://balsamiq.com) software.
If you don't want to buy the software, you can use the 30 days free trial version (Exactly like I did).

To view all wireframes for this project please use this link -
[Arctic School Wireframes](https://github.com/KarolSliwka/ArcticSchool/tree/main/wireframes)

__*Note:*__ To create this project I am fighting with myself to decide which style will suit this project the most. That's why, I believe some wireframes may change through the development process and several improvements could be done, such as buttons style, image position, text style, or user small user interface changes.

---

## Information Architecture

### Database choice

During the development, I worked with **sqlite3** databases, installed with Django.
For production, I've used a **PostgreSQL** database which is provided in Heroku as an add-on.

- The **User model** I have used in this project was provided by Django Allauth. It is a part of default `django.contrib.auth.models`.

### Data Modelling

#### Profiles App

##### User Profile

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
User | user | OneToOneField 'User' | on_delete=models.CASCADE
Full Name | full_name | CharField | max_length=200, null=True, blank=True
First Name | first_name | models.CharField | max_length=100, null=True, blank=True
Last Name | last_name | models.CharField | max_length=100, null=True, blank=True
Email Address | email_address | models.EmailField | max_length=254, null=False, blank=True
Phone Number | phone_number | models.CharField | max_length=20, null=True, blank=True
Street Address 1 | street_address1 | models.CharField | max_length=80, null=True, blank=True
Street Address 2 | street_address2 | models.CharField | max_length=80, null=True, blank=True
Postcode | postcode | models.CharField | max_length=20, null=True, blank=True
Town or City | town_or_city | models.CharField | max_length=40, null=True, blank=True
County | county | models.CharField | max_length=80, null=True, blank=True
Country | country | CountryField | blank_label='Select Country', null=True, blank=True
Receiving Newsletter | receiving_newsletter | models.CharField | max_length=3, choices=newsletter_choices, blank=True, null=True

#### Leesons App

##### Lesson

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | models.CharField | max_length=254
Category | category | models.ForeignKey 'Category' | null=True, blank=False, on_delete=models.PROTECT
Level | level | models.ForeignKey 'LevelCard' | null=True, blank=False, on_delete=models.PROTECT
Description | description | models.TextField | null=True, blank=True
Start Date | start_date | models.DateField | null=True, blank=False
End Date | end_date | models.DateField | null=True, blank=False
Start Time | start_time | models.TimeField | auto_now=False, auto_now_add=False
End Time | end_time | models.TimeField | auto_now=False, auto_now_add=False
Participants | participants | models.IntegerField | null=True, blank=False
Resort | resort | models.ForeignKey 'Resort' | null=True, blank=False, on_delete=models.PROTECT
Price | price | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=False
Supper Offer | supper_offer | models.BooleanField | null=True, blank=True, default=False
Image | image | models.ImageField | upload_to="lessons", null=True, blank=True

##### Category

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=False

#### Team App

##### Instructors

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | models.CharField | max_length=254, blank=False
Age | age | models.CharField | max_length=2, null=True, blank=False
About | about | models.TextField | null=True, blank=False
Image | image | models.ImageField | upload_to="instructors",null=True, blank=True

#### Resorts App

##### Resort

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | models.CharField | max_length=120
Country | country | CountryField | max_length=200, blank_label="(Select Country)"
About | about | models.TextField | max_length=500
Open Season | open_season | models.CharField | max_length=120, default="December - April"
Top Altitude | top_altitude | models.IntegerField | default=0
Bottom Altitude | bottom_altitude | models.IntegerField | default=0
Resort Altitude | resort_altitude | models.IntegerField | default=0
Levels | levels | models.TextField
Instrutors | instructors | models.IntegerField | default=0
Image| image | models.ImageField | upload_to="resorts", null=True, blank=True

#### Home App

##### Level Cards

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | models.TextField | max_length=40
Level | level | models.CharField | choices=LevelChoices.choices, default=LevelChoices.Level_1, max_length=1
Description | description | models.TextField | max_length=300

##### Lesson Cards (why our lessons)

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Title | title | models.TextField | max_length=40
Description | description | models.TextField | max_length=300

##### Social Media Icons

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | ---
Name | name | models.TextField | choices=NameChoices.choices, max_length=40, null=False, blank=False, default='Facebook'
Icon | icon | models.CharField | choices=LevelChoices.choices, max_length=30
Url Address | url | models.URLField | max_length=1024, default='', null=True, blank=True

##### Choices

Level Choices for Level Cards

- Level_1 = '1'
- Level_2 = '2'
- Level_3 = '3'
- Level_4 = '4'

Level Choices for Social Media Icons

- Facebook = 'fa-facebook-f'
- YouTube = 'fa-youtube'
- Pintereset = 'fa-pinterest-p'
- Snapchat = 'fa-snapchat-ghost'
- Twitter = 'fa-twitter'
- Instagram = 'fa-instagram'
- TikTok = 'fa-tiktok'
- Vimeo = 'fa-vimeo-v'

Name Choices for Social Media Icons

- Facebook = 'facebook'
- YouTube = 'youtube'
- Pintereset = 'pinterest'
- Snapchat = 'snapchat'
- Twitter = 'twitter'
- Instagram = 'instagram'
- TikTok = 'tiktok'
- Vimeo = 'vimeo'

Newsletter Choices

- ('Yes', 'Yes')
- ('No', 'No')

---

## Technologies Used

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [SCSS](https://sass-lang.co) (CSS extension language)
- [JavaScript](https://www.javascript.com)
- [Python](https://www.python.org)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)

### Libraries and Frameworks

- [Bootstrap](https://getbootstrap.com)
- [Fontawesome](https://fontawesome.com)
- [Google Fonts](https://fonts.google.com)
- [Django](https://www.djangoproject.com)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- [Stripe](https://stripe.com/ie)
- [jQuery](https://jquery.com)

### Tools

To create this web application, I've decided to change my IDE from [AWS Cloud 9](https://aws.amazon.com/cloud9/) to [VS Code](https://code.visualstudio.com).

Also, I've used the tools listed below :

- [Git](https://git-scm.com) - Version Control
- [GitHub](https://github.com) - Store Remote Repository
- [Heroku](https://www.heroku.com) - Project Hosting
- [PIP](https://pypi.org/project/pip/) - Installation of Tools
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS Compatibility
- [Axure RP9](https://www.axure.com) - To Create Wireframes
- [AWS S3 Bucket](https://aws.amazon.com/s3/) - Store Media and Static Files (Production)
- [Adobe Photoshop 2021](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwi1jtO-lYjtAhWRtu0KHVSdBuIYABAMGgJkZw&ae=2&ohost=www.google.com&cid=CAESQeD26XjYo-QzyoB2wcpxICKBRcP9GrB4c8gAn9paIaX33r0xVThzoIuEVAd5W9NMGzIpEnaxYR6rGHmVm3Xs6HqK&sig=AOD64_0qloXz9J7Jl2Hmpb5xL3Ar0APH5w&q&adurl&ved=2ahUKEwiXncq-lYjtAhV-ShUIHTryBD0Q0Qx6BAgSEAE&dct=1) - creating and editing images/logotype/icons.

To create colour pallete and image compressing I've used :

- [Coolors.co](https://coolors.co)
- [TinyPng](https://tinypng.com)

__*All images in the README file is hosted on my private server.*__

### Databases

- [PostgreSQL](https://www.postgresql.org)
- [SQLite3](https://www.sqlite.org/index.html)

---

## Features

Arctic School Web App contains 8 applications `home`, `lessons`(contains lessons to book), `team`, `resorts`, `booking`, `checkout`, `contact` and `profiles`(contains booking active and archived history + Management/Administartion Pages).

### Features Left to Implement

#### Social account login (Google and Facebook)

This feature allows users to log in by using their social accounts. This will change the user experience and make the login process easy and simple.

#### Subscribing Newsletter Form

The newsletter form is only a visual prototype. It hasn't got a real action to sign customers for a newsletter.
All customers have signed automatically to subscribing newsletter when registering.
This will allow users to subscribe without creating an account on a website.

Other small features are going to be implemented in feature, **Filtering Lessons** by Level, **Real-Time Chat**, **Email Remainder - Upcoming Lessons** and **Rent Equipment Page** .also I would like to change **Management/Administration Pages** style and **Forms** usability.

---

## Testing

Testing information can be found in a separate file - [Testing.md](https://github.com/KarolSliwka/ArcticSchool/blob/main/TESTING.md)

---

## Deployment

The Arctic School project was developed [VS Code](https://code.visualstudio.com) and using Git & GitHub for version control
It is hosted on the Heroku Pages, with static files hosted in AWS S3 Basket.

### Local Deployment

To run this project you have to install these tools and create accounts on the platforms listed below if haven't got them.

#### Tools to be installed

- IDE - I've used [VS Code](https://code.visualstudio.com)
- [Git](https://git-scm.com)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [PipEnv](https://pypi.org/project/pipenv/)
- [Python3](https://www.python.org/download/releases/3.0/)

#### Accounts to be created

- [Stripe](https://stripe.com/en-ie)
- [Goole Mail](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)
- [AWS](https://aws.amazon.com)
- [Amazon Simple Storage Service (S3)](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Before cloning the repository make sure you have got installed Python & Pip

```bash
python --version
```

If Pip is not installed then you have to install it

```bash
install pipenv
````

also, you can upgrade your pipenv at any time using the following code

```bash
upgrade pipenv
```

Clone this repository directly into the editor. Paste the following command into your terminal

```bash
git clone https://github.com/KarolSliwka/ArcticSchool.git
```

Next, you have to activate the Pipenv shell by typing it into your terminal

```bash
pipenv shell
```

You have to set up your environmental variables.
You can do it by adding variables to your settings.json file which can be found in the .vscode folder.

```python
"DEVELOPMENT": "",
"AWS_ACCESS_KEY_ID": "YOUR-AWS_ACCESS_KEY_ID",
"AWS_SECRET_ACCESS_KEY": "YOUR-AWS_SECRET_ACCESS_KEY",
"EMAIL_HOST_PASSWORD": "YOUR-EMAIL_HOST_PASSWORD",
"EMAIL_HOST_USER": "YOUR-EMAIL_HOST_USER",
"SECRET_KEY": "YOUR-SECRET_KEY,
"STRIPE_PUBLIC_KEY": "YOUR-DSTRIPE_PUBLIC_KEY",
"STRIPE_SECRET_KEY": "YOUR-STRIPE_SECRET_KEY",
"STRIPE_WH_SECRET": "YOUR-STRIPE_WH_SECRET",
```

The next step is to install all requirements from the rquirements.txt file by using this command

```bash
python -m pip install -r requirements.txt
```

In your IDE terminal migrate the models to create a database by using these commands

```bash
./manage.py makemigrations
./manage.py migrate
```

When migrations are created you have to load data fixtures(categories, levels, resorts, lessons, social-icons, why-lessons, instructors ) in this order to the database

```bash
./manage.py loaddata <fixture_name>
```

When all database is setup and fixtures are loaded. You have to create a superuser to access the administration panel. Use the command below to create superuser and follow the instructions displayed on the screen.

```bash
./manage.py createsuperuser
```

Now when all set up is done you can use

```bash
./manage.py runserver
```

The administration panel has to be accessed by adding /admin into the URL path.
To login to administration use your superuser credentials.


### Deployment on Heroku pages

To deploy your project please use the following steps:

- 1: Create a **requirements.txt** file using command below.

```bash
pipenv lock -r > requirements.txt
```

- 2: Create a **Procfile** file using command below.

```bash
echo web: python3 app.py > Procfile
```

- 3: Push all files to your git repository.
``` git push origin master ``` - your master branch
- 4: Create a new application for this project on the Heroku Pages. Click on 'New App' button and follow steps to create new app.
- 5: Select your deployment method by clicking on the **deployment** method button.
- 7: You can either follow Heroku Git deployment method or GitHub connect (I did it  this time - project is deployed automatically when master branch is pushed to repository)
- 6: Set the following config variables:

**Key**|**Value**
:-----:|:-----:
AWS_ACCESS_KEY_ID|YOUR-AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY|YOUR-AWS_SECRET_ACCESS_KEY
BUCKET_S3|True
DATABASE_URL|YOUR-DATABASE_URL
EMAIL_HOST_PASSWORD|YOUR-EMAIL_HOST_PASSWORD
EMAIL_HOST_USER|YOUR-EMAIL_HOST_USER
SECRET_KEY|YOUR-SECRET_KEY
STRIPE_PUBLIC_KEY|YOUR-STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY|YOUR-STRIPE_SECRET_KEY
STRIPE_WH_SECRET|YOUR-STRIPE_WH_SECRET

- 7: Remember to add an Add-on Heroku Postgres, select Hobby Dev - Free and click Provision button to add it into your heroku app project.
- 8: To setup your DATABASE_URL you have to copy Postgres database URL into your variable key value
- 9: Click the deploy button on the Heroku Pages dashboard.
- 10: The site has been deployed the Heroku Pages, Enjoy!;

---

## Credits

### Code

- Project was developed by following [Code Institute](https://codeinstitute.net/) video course 'Boutique Ado Django Mini-Project'.
- [Stack Overflow](https://stackoverflow.com/) for finding solutions or hints on how to solve issues and how to make it work.
- I referred to the [Django](https://docs.djangoproject.com/en/3.1/) documentation sources during the development.

### Content and Media

- Whole website content was written by the project author.
- Project logo was created by the project author in Photoshop by using [Provicali Font](https://www.dafont.com/provicali.font) and some special layer effects.
- Favicon was created from the existing logotype by the author as a basic icon 64px x 64px via using the [Realfavicongenerator](https://realfavicongenerator.net).
- Images and icons used in this project were taken from :
- [Unsplash.com](https://unsplash.com/s/photos/snowboard)
- [Pexels](https://www.pexels.com)
- [Icons8](https://icons8.com)

- Scroll down button code snippet was taken from [Codepen/nxworld](https://codepen.io/nxworld/pen/OyRrGy)
- Particles library - example used was created by [Mamboleoo](https://codepen.io/Mamboleoo) - [code snippet](https://codepen.io/Mamboleoo/pen/obWGYr), edited to match an author design.
- Navbar links hover style - code used from [Hoover.css](https://ianlunn.github.io/Hover). Code was edited to match an author's design.
- [Hero pattern](https://www.heropatterns.com) was used to create a background pattern in the promo banner section.
- Mountains graphic - [Twentypine](http://www.twentypine.com)
- SVG Background graphics - [SVGBackgrounds](https://www.svgbackgrounds.com/#large-triangles) and [LoadingIO](https://loading.io) - highly recommended.

### Acknowledgements

I would like to say 'Thank You' to everyone who helped me throughout the development of this project:

- [Simen Daehlin](https://github.com/Eventyret) for his support, help, patience and guidance, very useful tips and advice! Also for not only being a Mentor but an amazing Friend!
- [Code Institute](https://codeinstitute.net) Amazing people! For their help, assistance, and support when I had the most challenging times in my life.
- Also I would like to thank my close friends and family who never stopped believing I can finish this course and become a Developer!

---

## Contact

If you've got any questions about this project please contact me via email: *contact@karolsliwka.com*

If you're interested in my other projects please visit

- [Mariocarparts.co.uk](https://mariocarparts.co.uk) - First online store project on Shopify platform.
- [Balticgold.co.uk](https://balticgold.co.uk) - Second online store project on Shopify platform (my personal store).
- [Spsservice.uk](https://spsservice.uk) - First website created at the beginning of the Code Institute course, static only (hosted on the personal server).

---

## Disclaimer

__This web app was made for educational purposes only.__

---

<div align="right">
    <b><a href="#arctic-school-">Back To Top</a></b>
</div>