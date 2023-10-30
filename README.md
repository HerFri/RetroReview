# RetroReview
![title](https://github.com/HerFri/RetroReview/blob/main/readmeimages/title.PNG?raw=true)

RetroReview is a Retro videogame review website made with Django, where website users can explore and search for videogames in the game catalogue, read reviews, like them and discuss them by writing comments. To be able to like and write comments, users have to register and log into their account. Once logged in, users are able to write, edit and delete their comments and can like and also unlike reviews again. After submitting a comment, this comment will wait for approval by the administrator of the website. Nonetheless, unauthenticated website visitors are able to view the game catalogue and read the respective reviews. The content of the website, i.e. the presented games and reviews, are managed by the administrator of the website, who can add games and reviews and approve, edit and delete comments. Enjoy a little travel back in time and let the nostalgia flow through you!

![mockup](https://github.com/HerFri/RetroReview/blob/main/readmeimages/mockup.PNG?raw=true)
The mockup image has been generated on [https://ui.dev/amiresponsive](https://ui.dev/amiresponsive)
Visit the live page [here](https://retro-review-a5a97966a295.herokuapp.com/)

# Agile Approach
This project was designed and built using the agile approach, beginning from the initial planning until final deployment. For visualizing the different project elements I created a GitHub project and used the provided [Kanban board](https://github.com/users/HerFri/projects/11) to monitor my work progress. The project elements are assigned to different User Stories that can be opened to view the Acceptance Criteria and Tasks to be fulfilled. Moreover, every User Story has been tagged with a label to signify the priority and cruciality of the respective features to the overall workings and functionality of the website.

To view all User Stories including their required Acceptance Criterias and Tasks, please refer to the Kanban board linked above. 


# UI/UX
The overall design of the website is kept minimalistic and intuitive, so that site visitors don't get distracted or overwhelmed by unnecessary features. 

By opening the website, visitors are greeted by a welcome text that informs them about the basic functionalities of the website. Without much searching, visitors will observe 
a selection of featured games of the game catalogue on the homepage that are ready to be clicked on to be lead to the game detail page, where reviews, if any are created, can be found and read.

On top of all pages users will find the navigation bar to find the crucial pages for Signing Up or Logging in or to find a way to the homepage.

## Site Goals
The goal of this website is to provide a venue for people who like retro videogames or videogames in general. Website users can search for their favourite videogames, read reviews about them and show their approval or dispproval or impressions and opinions about videogames by commenting and liking. Every website user is welcomed to sign up and speak his or her mind about videogames or retro gaming by writting comments and to interact with other users. However, offensive language or inappropriate topics are not welcome, which is why every comment has to be approved by the website administrator after submission. 
Beside the goal of social interaction and having a place of discourse, this website intends to convey information and facts about a variety of different videogames.

## 5 Planes of UX
### Strategy
Strategy addresses user's needs and product objectives. This website's purpose is not to advertise any product or specific videogame or to meet any other commercial agenda. It's purpose is rather to bring together games and people, and the stories that those bring. As the games presented on this website are rather old in comparison no modern games, it is most certain that many games have been played by many users in their childhood, which most likely brings up a lot of nostalgia and memories that are encouraged to be shared on this webpage. Shared memories and good times playing certain games gives great opportunity of telling wholesome stories that other people can read and by any chance can make their day.

### Scope
Scope addresses what functions and features are within the scope of this project. In this project, it was aimed at providing a Minimal Viable Product (MVP) that fulfills basic requirements for CRUD functionality, such as user sign up and login and the ability to write comments and like reviews for authenticated users. Based on this MVP, improvements and additional features, such as the ability for authenticated users to write their own reviews, can be implemented in the future for additional functionality (See Section [Future Features](#future features)).

### Structure
Structure defines how the functions and features of a website fit together to provide a positive UX. The structure and features of this website are very simple and intuitive and is based on a simple blog website, which serves its purpose for presenting different games and reviews and the resulting discussions in form of comments very well.The need for authentification of new users and the obligatory approval of new comments ensures that RetroReview stays a venue solely for discussing video games and stories that are connected to retro gaming.

### Skeleton
Skeleton deals with the more abstract structure of the website like the design of different interface elements and the arrangement of these to provide positive UX. A typical representation for the skeleton of a website are [Wireframes](#wireframes), which shall be presented for this website at a later time. For intuitive navigation through the website, both the navigation bar and the presentation of the main content follow a well known standard layout pattern, so even not every day internet users will have no problems in finding the right sections of the website. The navigation bar provides links for Signing Up and Logging and a Home button that lead users back to the homepage.
Beside the just mentioned Home button, the brand logo serves also as a button that leads users to the homepage. On medium and small devices the navigation bar is replaced by a burger menu to provide clarity. The main content is presented in a list view of game cards which link to the game details page where the reviews are displayed. On this page, users can choose a review they want to read. On the review detail page, authenticated users will observe the actual review, a comment form, a like button and comments, if any were written. Buttons and links are appropriately named. Moreover, a footer with social media icons, which link to the homepages of respective social media sites (except the YouTube icon, which leads to the YouTube channel of the builder of the website), is present on every page of the website. 

### Surface
Surface deals with the superficial aspects of the website such as visual design and the overall look to create specific emotional reactions or trigger specific behaviours. For more details about the surface layer planning of this website see [Visual Design](#visual-design). 

## Wireframes
For the planning of the website skeleton I created some wireframes using the wireframe software [Balsamiq](https://balsamiq.com/). These wireframes are an overly simplified sketch of the final website and merely served the purtpose of displaying most of the website's essential features:

<details>
    <summary>
        Wireframe Images
    </summary>
    <img src="https://github.com/HerFri/RetroReview/blob/main/readmeimages/wireframe1.png?raw=true" alt="Index">
    <img src="https://github.com/HerFri/RetroReview/blob/main/readmeimages/wireframe2.png?raw=true" alt="Game Detail">
    <img src="https://github.com/HerFri/RetroReview/blob/main/readmeimages/wireframe3.png?raw=true" alt="Review Detail">
    <img src="https://github.com/HerFri/RetroReview/blob/main/readmeimages/wireframe4.png?raw=true" alt="Sign In">
    <img src="https://github.com/HerFri/RetroReview/blob/main/readmeimages/wireframe5.png?raw=true" alt="Sign Out">
</details>

# Visual Design
## Color Scheme
The visual design of the website is kept minimalistic so the games and reviews are in the main focus. The main theme for the colors of the website is white/light-grey, red and orange:
![colorpalette](https://github.com/HerFri/RetroReview/blob/main/readmeimages/coolors.PNG?raw=true)


The gradient used for the header and footer sections is made on [cssgradient.io/](https://cssgradient.io/) and begins with a red color (#f00303) which leads to a white/light-grey color (#fcf9f9), which is also the main background color:
![gradient](https://github.com/HerFri/RetroReview/blob/main/readmeimages/gradient.PNG?raw=true)

The main color for the body font is black (#000000). The font color for highlighted text is (#f00303). The color for the like button and when hovering over the game links is (#E84610). The subtitles for the review detail page have lightgrey(#d3d3d3) color. The sign in and sign out buttons have a red color (#f00303).

The filling of the website logo consists of red color (#E84610) and black(#000000) outline. The same style is applied to some elements of the comment section:
![title](https://github.com/HerFri/RetroReview/blob/main/readmeimages/title.PNG?raw=true)
![comment](https://github.com/HerFri/RetroReview/blob/main/readmeimages/comment.PNG?raw=true)

The social media icons are from [Fontawesome](https://fontawesome.com/) and have white(#ffffff) filling and black(#000000) outline. All of the social media icons, except the YouTube icon, have a small blue (#0d6efd) minus-element in the right corner , that signifies that these social media icons only lead to the homepage of these websites and to no actual social media site. 

## Further Visual Effects
While hovering over on of the Navigation Link elements, this element will light up in black, while the rest stays transparent behind the gradient:
![hover](https://github.com/HerFri/RetroReview/blob/main/readmeimages/hover.png?raw=true)

## Fonts
For the website logo, the navigation bar elements, the footer text and some text of the comment section, a font called 'Pretendo' that was downloaded from [this page](https://fontmeme.com/schriftarten/pretendo-schriftart/), was used. It is similar to the font of the logo that the gaming company 'Nintendo' uses and hints to it to provide a feeling of nostalgia and familiarity:
![title](https://github.com/HerFri/RetroReview/blob/main/readmeimages/title.PNG?raw=true)
![comment](https://github.com/HerFri/RetroReview/blob/main/readmeimages/comment.PNG?raw=true)
![footer](https://github.com/HerFri/RetroReview/blob/main/readmeimages/footer.PNG?raw=true)

The rest of the body uses the familiar font Arial.

## Favicon 
A custom favicon was generated on [this page]() that depicts the two beginning R characters form the logo of 'RetroReview':
![favicon](https://github.com/HerFri/RetroReview/blob/main/readmeimages/favicon.png?raw=true)

# Features

## Implemented Features

### All pages

### Navigation

- Navbar with clickable website logo, leading to the homepage, and links to the different pages
![navbar](https://github.com/HerFri/RetroReview/blob/main/readmeimages/hover.png?raw=true)
- Different links visible for authenticated and unauthenticated users
- Textfield that states that user is logged in
![difflinks](https://github.com/HerFri/RetroReview/blob/main/readmeimages/difflinks.PNG?raw=true)

- Collapsible burger menu with drop-down on small to medium screens
![burgermenu](https://github.com/HerFri/RetroReview/blob/main/readmeimages/burgermenu.PNG?raw=true)

### Footer
- Footer with info about the author of the website and clickable social media icons that are linked to the homepages of social media websites and YouTube Channel of the author
![footer](https://github.com/HerFri/RetroReview/blob/main/readmeimages/footer.PNG?raw=true)

### Home Page

### Welcome Text
- Welcome text at the top of home page that greets site visitors
- Explains what it is about and informs about the opportunity to sign up to use all functionalities of the website 

- Welcome text varies if user is logged in or not
Not logged in:
![welcomenolog](https://github.com/HerFri/RetroReview/blob/main/readmeimages/welcomenolog.PNG?raw=true)
Logged in:
![welcomelog](https://github.com/HerFri/RetroReview/blob/main/readmeimages/welcomelog.PNG?raw=true)

### Dropdown Filter Lists (Search for Games)
- Users can use the dropdown filter lists to filter games by platform and year and click on the search button to be lead to the filtered games page
![dropdownfilter](https://github.com/HerFri/RetroReview/blob/main/readmeimages/dropdownfilter.png?raw=true)

### Featured Games
- A selection of featured games is displayed, every game has its own card
- Users can click on the game image or description to be lead to the game details page
![gameselection](https://github.com/HerFri/RetroReview/blob/main/readmeimages/gameselection.PNG?raw=true)

### Next Page Button
Since the home page is paginated by 6, the button leads to the next page, showing the rest of the games
![nextpage](https://github.com/HerFri/RetroReview/blob/main/readmeimages/nextpage.PNG?raw=true)

### Filtered Games Page
- When users used the dropdown filter lists to filter the games by a specific platform or/and year and clicked the search button, they will be redirected to the Filtered Game Page, where the search criteria is highlighted in red:
![filterresults](https://github.com/HerFri/RetroReview/blob/main/readmeimages/filterresults.PNG?raw=true)

### Game Detail Page
- By clicking on a game image or the game info text, users will be directed to the Game Detail Page
- In the header area, users will find a banner with information about the game and a picture of the cover
- Beneath the banner, users will find for each written review a review card, that shows the cover of the reviewed game, the likes, rating, title and author of the review and the date and time the review was written
![gamedetailpage](https://github.com/HerFri/RetroReview/blob/main/readmeimages/gamedetail.PNG?raw=true)

### Review Detail Page
- By clicking on the image or title of a review card, users will be directed to the Review Detail Page, were, similar to the Game Detail Page, a banner can be found on the top of the page, showing the title, author, date, time and rating of the review, such as some information about the game.
![reviewdetailbanner](https://github.com/HerFri/RetroReview/blob/main/readmeimages/reviewdetailbanner.PNG?raw=true)
- Under the banner, the actual review is displayed, with a thumbs up icon on the bottom depicting the number of likes other authenticated users gave this review.
![review](https://github.com/HerFri/RetroReview/blob/main/readmeimages/review.PNG?raw=true)

### Comment Section
Depending, whether the user is logged in or not, he or she will have a different view of the comment section.
- Not logged in users view:
![commentsnotlog](https://github.com/HerFri/RetroReview/blob/main/readmeimages/commentsnolog.PNG?raw=true)
- Logged in users view:
![commentlog](https://github.com/HerFri/RetroReview/blob/main/readmeimages/commentlog.PNG?raw=true)
- Logged in users will find a comment form which informs them as which user they are commenting. Moreover, users who already wrote a comment will find an edit and delete button that can be clicked to be directed to a different page, were they can edit or delete their comment
- Logged in users are able to like the review, whereas not logged in users can not. By clicking the thumbs up like button, the page reloads, the thumbs up icon is filled completely orange and the number of likes increments. Logged in users can also unlike that button again:
![nolike](https://github.com/HerFri/RetroReview/blob/main/readmeimages/nolike.PNG?raw=true)
![liked](https://github.com/HerFri/RetroReview/blob/main/readmeimages/liked.PNG?raw=true)

### Edit Comment
When clicked on the edit button, logged in users can edit and modify their comments and submit the changes by clicking the submit button:
![editcomment](https://github.com/HerFri/RetroReview/blob/main/readmeimages/editcomment.PNG?raw=true)

### Delete Comment
When clicked on the delete button, logged in users can delete their comments by clicking the delete button:
![deletecomment](https://github.com/HerFri/RetroReview/blob/main/readmeimages/deletecomment.PNG?raw=true)

### Sign Up Page
By clicking the "Sign Up" element in the nav bar, users can sign up by creating an account. Users have to provide a username 

### Login Page 
By clicking the 'Login' element in the navbar, users can sign in by clicking the 'sign in' button. Users that have not created an account yet are informed that they can do that by clicking the 'here' word that is highlighted in red, which directs them to the Sign Up page.
![signin]()

### Logout Page
By clicking the 'Logout' element in the navbar, logged in users can sign out by clicking the 'sign out' button


### Alerts

 





# Structure
## Wireframes
For the structural planning of my website, I created some wireframes using the wireframe software [Balsamiq](https://balsamiq.com/).


* [Desktop wireframe of index page]()
* [Desktop wireframe of  page]()
* [Mobile view wireframe of index page]()
* [Mobile view wireframe of ]()


# Features

## Navigation Bar
The navigation bar is located under the hero image and allows by clicking on one of the navigation elements navigation to the desired section of the website. 
![navbar1]()

## Landing Page
The Landing Page consists of 
![landingpage]()


## Footer
The footer comprises four clickable icons for the social networks Facebook, Instagram, Twitter and YouTube. By clicking the icons, a new tab is opened which leads the user to the respective social network.
The icon designs are imported from [Font Awesome](https://fontawesome.com/).

![footer]()


# Future features


# Accessibility ?
For good accessibility `<aria-label>` and `alt`-attributes have been added to elements like links and images that do not provide sufficient information to support assistive technologies like screenreaders.

# Technologies Used
Following technologies have been used for building my website:

* HTML
* CSS
* Python
* GitHub
* GitHub Pages
* Visual Studio Code

# Testing
## Code Validation
The website has been tested with the W3C Validator and Jigsaw Validator 
* The W3C Validator test passed with no errors. [Test here]()
* The Jigsaw Validator test passed with no errors. [Test here]()

## Performance Test
To test the performance of the website the Google Lighthouse test was used and showed good results:
![googlelighthouseresult]()

## Responsiveness
To test responsiveness, I used the website [AmIresponsive]() that generated the [mockup image]() and showed that my website was responsive on different devices.
Moreover, I used Chrome (Version ) Developer Tools to simulate viewports of different devices, which showed that my website was fully responsive:
![galaxyfoldvw]()
![iphone6vw]()
![ipadairvw]()

## Browser Testing

I tested the layout and appearance of my website for consistency on different browsers.
Moreover, I tested if the navigation, all links, form submission and video works on different browser. 

Tested browser: Chrome (Version 114.0.5735.199), Firefox, Safari, Edge

Result: Layout and all functions work throughout the tested browsers.

## Manual Testing

| Feature         | Expect                                                          | Action                    | Result                                          |   
|-----------------|-----------------------------------------------------------------|---------------------------|-------------------------------------------------|
| 


## Testing User Stories

| Expectation                                                                                        | Result                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a user, I want                                                                                       |
| As a user, I want | 

## Fixed Bugs

When an authenticated site user would click the like button on a review page, the browser would throw a HTTP ERROR 405.
![bug]()

The reason for this issue was that not sufficient arguments have been passed to and inside the
`like`-function of the `ReviewLike`-class. More precisely, the `slug`-arguments were not correct and some were missing, so
I added the correct arguments `slug=review`, `slug=game` and `args=[game.slug, review.slug]`.

![fixclass]()
![fixcode]()

# Deployment

# Credits

## Contents


## Media
Images:
[]()


All media was used for educational purposes only.

## Code 


# Acknowledgements
I want to thank the Slack community and the tutors of Code Institute for their very helpful support and valuable criticism!