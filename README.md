# RetroReview
![title](https://github.com/HerFri/RetroReview/blob/main/readmeimages/title.PNG?raw=true)
RetroReview is a Retro videogame review website made with Django, where website users can explore and search for videogames in the game catalogue, read reviews, like them and discuss them by writing comments. To be able to like and write comments, users have to register and log into their account. Once logged in, users are able to write, edit and delete their comments and can like and also unlike reviews again. After submitting a comment, this comment will wait for approval by the administrator of the website. Nonetheless, unauthenticated website visitors are able to view the game catalogue and read the respective reviews. The content of the website, i.e. the presented games and reviews, are managed by the administrator of the website, who can add games and reviews and approve, edit and delete comments. Enjoy a little travel back in time and let the nostalgia flow through you!

![mockup](https://github.com/HerFri/RetroReview/blob/main/readmeimages/mockup.PNG?raw=true)

Visit the live page [here](https://retro-review-a5a97966a295.herokuapp.com/)



 


The mockup image has been generated on [https://ui.dev/amiresponsive](https://ui.dev/amiresponsive)


# User Experience
## User Stories
* As a user, I want 

# Design
## Colors
For the color theme I chose 

![colorpalette]()

The colorpalette above has been generated with [coolors.co]()

For the social network icons in the footer, these colors have been used:
* Facebook: 
* Instagram: 
* YouTube: 
## Fonts
As for the fonts, I imported fonts, namely
* 
The 'Pretendo'-font is being used for 

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