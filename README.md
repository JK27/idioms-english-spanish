# IDIOMS ENGLISH - SPANISH

This is an application where the user can find a collection of common Spanish idioms, their equivalent in English, literal translations and meanings on both languages for better understanding of them.

The user can view the different items, add new ones, edit and delete them.

## UX

![Responsive Views of Home Page](/images/idioms-responsive.png)

The application is intended to be a collaborative library of idioms in Spanish and English where users can learn new idioms or share their ones to help others on their learning.

### User stories

1. Students of either language that look to improve their knowledge and learn sayings that normally are not taught in schools or courses.
2. Teachers looking for resources for their lessons can either use the application directly to show the students or use the contents that they require.
3. A person who speaks Spanish or English as a second language that has come across an idiom that they do not know the meaning of, or they do not understand what it means, can use this application to satisfy that need.
4. Native speakers of either language that want to use an idiom on their mother tongue but do not know how to say it on the other language can look it up on the application.

## Features

### Existing Features

- Documentation - README file
- Bootstrap - HTML, CSS framework
    - Grid system
    - Cards
    - Pagination
    - Modal
- Responsive design - mobile first
- UX elements
    - Animations
    - CRUD - Create, Read, Update and Delete elements
- Git - Version Control System
- GitHub - Remote Repository
- Deployed - Hosted on Heroku apps

### Features to be implemented

- Inclusion of other categories of items to expand the variety of contents beyond only idioms. Categories such as:
    - Proverbs
    - Famous quotes
    - Catchphrases
    - Slang
- Addition of search functionality to facilitate users to find a specific item on a much quicker way
- Addition of tags to each item to categorize them into different classes that can be used for filtering searches. Tags could be something like these:
    - Funny
    - Inspirational
    - Animals
    - Food
    - Money
    - Jobs
    - etc.
- Option for users to create an account that will give access to extra functionalities like:
    - Bookmark items and add to favourites
    - Create own lists
    - Share items on social media/email/WhatsApp

## Technologies used

- HTML for the structure of the application.
- CSS for styling.
- Google Chrome for browser and dev tools (https://www.google.com/chrome/).
- Mozilla Firefox for browser and dev tools (https://www.mozilla.org/en-US/firefox/new).
- Bootstrap framework for responsiveness and structure of the application (https://getbootstrap.com/).
- Font Awesome icons for buttons (https://fontawesome.com/).
- Werkzeug Web Server Gateway Interface for debugging and structured error logs.
- Git for version control (https://git-scm.com/).
- GitHub for hosting the repository (https://github.com/).
- Heroku App for hosting and deployment (https://idioms-english-spanish.herokuapp.com/).
- Am I responsive for testing responsiveness (http://ami.responsivedesign.is).

## Testing

All functionalities of the application have been regularly tested during the building process using the python console to check the results and then write the functionalities to pass the tests. After each function was written, and after adding every piece of code, this was tested again on the browser using Google Chrome Developer tools and Werkzeug Web Server Gateway Interface for debugging.

The application has also been regularly tested on different browsers (Google Chrome, Mozilla Firefox and Internet Explorer/Microsoft Edge) and also on different devices (computer, laptop and mobile phones).


## Deployment

The application is hosted as an app in Heroku, sourced via GitHub repository. It can be seen using the following link on the web browser of your preference: https://idioms-english-spanish.herokuapp.com/

The deployment process was as follows:

- Host a git repository on GitHub
- Create an app in Heroku
- On the app settings in Heroku, connect the app to the GitHub repository and enable the automatic deploys from the chosen branch so all commits pushed to GitHub will automatically feed through to the Heroku app.
- Once everything is connected to the app, use the domain URL given or click on the "Open app" button to see the app on the browser.

## Credits

Inspiration for this application was taken from one of the project ideas given by the Code Institute, suggesting to create a jargon dictionary.

The database of idioms, although created by myself, has been put together using the following websites as reference:
- https://www.phrases.org.uk
- https://www.ef.co.uk/english-resources/english-idioms/
- http://www.sonferrer.com/refranes/
- https://listas.20minutos.es/lista/100-grandes-refranes-espanoles-371175/

### Acknoledgements

I would like to thank my mentor Seun Owonikoko and the team of tutors at the Code Institute for their inspiration, support and patience provided to help put this project together.
