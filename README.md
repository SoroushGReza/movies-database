# <span style="color:aqua">[Movie Base](https://movie-base-application-c1658d190bfd.herokuapp.com/)</span> <br>
<img src="images/moviebase.gif" alt="Moviebase logo" width="250" height="250"> <br><br>


## Project Overview
This project is a simple movie database web application that is built using Django, and  It allows users to signup and view a list popular movies for the current year, see detailed information about each movie, and access to trailers. 

Users can also leave reviews about movies after signing up, and also rate them. Users can manage their account, by being able to edit/delete their approved reviews. And also having the possibility to delete their account.

Users can search for movies using the [**TMDB**](https://developer.themoviedb.org/docs) API.

There is also admin functionality on this app, where the admin can manage users and reviews written by users. Posted User reviews is sent to the admin panel for approval, before presented on the site. <br><br>

## Responsive Design
This application was designed to be fully responsive, using [**Bootstrap**](https://getbootstrap.com/docs/5.3) classes along with custom Media Queries. Real time testing was performed using [**Google Dev Tools**](https://developer.chrome.com/docs/devtools/open/). And as a final check I used [**Am I Responsive**](https://ui.dev/amiresponsive) that also provided us with this beautiful Image below. 

![Am I Responsive screen-shot](/movies/static/media/responsiveness-image.png)


## Installation
To install and run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/SoroushGReza/movies-database.git`
2. Navigate to the project directory: `cd movies-database`
3. Install the required packages: `pip3 install -r requirements.txt`
4. Run the server: `python3 manage.py runserver` <br><br>


## How to use
### Legend Explaining Instruction icons.  <br><br>
![Legend](/movies/static/media/How%20To%20Use/0%20Legend.png) <br><br>

### If you already have an account you can signin, by typing your **Username** and **Password** and then pressing the **Login** button. <br>
![Login](/movies/static/media/How%20To%20Use/1%20Login.png) <br><br>

### If you don't have an account and press **Register**, you will be navigated to the registration page. Her you need to fill out all the form fields before pressing **Register** button. <br>
![Register](/movies/static/media/How%20To%20Use/2%20Register.png) <br><br>

### Look at the image below to see how to navigate to your **Profile**. <br>
![Profile](/movies/static/media/How%20To%20Use/3%20Profile.png) <br><br>

### In the **Profile** page you can **Edit Profile**, Navigate to **My Reviews** and you can also **Delete Account**. <br>
* After Pressing the **Edit Profile** button you will se the edit form. <br>
* It is optional if you want to **Update Email** or **Change Password**, however if you fill in the **Old Password** field then **New Password** and **Confirm New Password** fields will be required. <br>
* After filling out the form you can press **Update Profile** button. <br>
* You can also **Delete Account** as a registered user by pressing the **Delete Account** button. 
 <br>

![Edit Profile](/movies/static/media/How%20To%20Use/4%20Edit%20Profile.png) <br><br>

### When pressing the **Delete Account** button a confirmation modal with pop up. <br>
* If you pressed the button by mistake you can close the modal by pressing **Close** or **X** in the top right of the modal. 
* If you want to delete your account, you got to fill in your current password and then press **Delete Account** button. <br><br>

* <span style="color:orange">WARNING</span>: If you delete your account, all your data will be deleted, including your posted reviews. <br>

![Delete Account](/movies/static/media/How%20To%20Use/5%20Delete%20Account.png) <br><br>

### You can also search for movies in the top right of the navbar.
* Type your search and press **Search** or **Enter**.  <br>

![Movie Search](/movies/static/media/How%20To%20Use/6%20Movie%20Search.png) <br><br>

### If you need to contact the page owner follow this steps : 
* Press on the **Contact** link in the navbar. 
* Type your **Name** followed by you **Email** and your **Message** and then press **Send**. <br>

![Contact](/movies/static/media/How%20To%20Use/7%20Contact.png) <br><br>

### You can post reviews **ONLY** as a signed in member in Movie Base application. 
* You can write a review that is up to 1000 characters long. 
* Note that, if you don't choose a rating, the form will rate **Three <span style="color:yellow">★★★</span>** per default. 
* Before you reviews is presented on the page, they need to get approval from the admin. Once they are approved you can find them on the specific movie overview page and **My Reeviews** page.
<br> 

![Post Review](/movies/static/media/How%20To%20Use/8%20Post%20Review.png) <br><br>

### When navigating to **My Reviews** page, you can se alla of your approved reviews inthe page. <br>

#### Now you can: <br>
* Edit your reviews, byr pressing the **Edit** button and adjusting the text and rating.
(Note that your updated review will be removed from the **My Reviews** page and will need admin approval once again before presented on the site.) <br>

* Delete  your reviews by pressing the **Delete** button and confirming deletion. 

* You can also press **Overview** link to navigate to the specific movie overview, where you can see trailer for the movie and see all reviews posted for the movie by all users. <br>

![Edit/Delete Reviews](/movies/static/media/How%20To%20Use/9%20Edit%20Delete%20review.png) <br><br>

### If you don't know what you are looking you you can navigate to **Recomendations** page where popular movies from the current year is presented. <br>

![Reccomendations](/movies/static/media/How%20To%20Use/10%20Recommendations.png) <br><br>



## Deployment
To set up and deploy this APP to heroku you can use [this teps](https://docs.google.com/document/d/1CncA1F2JClME2S_K0w4XoV3edMjOl_HrOQoEs3h9LOo/edit?pli=1#heading=h.hvy9tw74f1o0) provided by Code Institue. <br><br>

## Features
- **Movie List**: Users can view a list of movies in the database.
- **Movie Detail**: Users can click on a movie to see more detailed information.
- **Reviews**: Users kan post reviews and rate movies after signing up.
- **Review Managment**: Users can edit and delete their posted reviews.
- **Send Email**: Users can send email directly to the site owner for contact.
- **Profile Managment**: Users can manage their profile, such as changing email address and password
- **Movie Search**: Users can search for movies, through the [**TMDB**](https://developer.themoviedb.org/docs) API.
- **Account Deletion**: Users can delete their acount from the profile page.<br><br>

## Colour Themes
This is the colors used in this application. I've tried to make different parts of the app have slightly different colors, but without to big of a contrast between them. Overall I've gone for a dark look, which is why the footer and navigation bar is the same darkgrey color on all pages. <br>

![Color Theme](/movies/static/media/Application%20Colour%20Theme.png)

## Technologies Used

- [**Django**](https://docs.djangoproject.com/en/4.2/): For backend development
- [**Bootstrap**](https://getbootstrap.com/docs/5.3/getting-started/introduction/): To make the application responsive
- [**Google Fonts**](https://fonts.google.com/): For typography
- [**FontAwesome**](https://fontawesome.com/icons): For icons
- [**TMDB API**](https://developer.themoviedb.org/docs): For fetching movie data
- [**EmailJS**](https://www.emailjs.com/): For sending emails
- [**Cloudinary**](https://console.cloudinary.com/): <span style="color:orange">NOTE</span>: Not currently is use, but linked for future improvements.
- [**Canva**]([Canva](https://www.canva.com/)): For creating images and gifs. 
- [**ElephantSQL**](https://www.elephantsql.com/): For managing PostgresSQL database service.
- [**Google Dev Tools**](https://developer.chrome.com/docs/devtools/open/): Used for debugging, testing styles and checking responsiveness.
<br><br>

## Languages Used
![**Languages Used Image**](/movies/static/media/languages-used.png) <br><br>

## Validators used
- [**Jigsaw W3**](https://jigsaw.w3.org/css-validator/) - To validate CSS code.
- [**JSHint**](https://jshint.com/) - To validate JavaScript code.
- [**Markup W3**](https://validator.w3.org/) - To validate HTML code.
- [**CI Python Linter**](https://pep8ci.herokuapp.com/) - To validtae Python code. 
<br><br>



## &#x1F4CB; User Stories - [**GitHub Project**](https://github.com/users/SoroushGReza/projects/11/views/1)


&#x1f7e2; As a **Developer**, I can **set up the workspace**, so that I can **start writing the code**.
### &#x2699; Tasks:
<input type="checkbox" checked="checked" /> - Set up workspace with [Code-Institute-template](https://github.com/Code-Institute-Org/gitpod-full-template). <br>
<input type="checkbox" checked="checked" /> - Install required packages.<br>
<input type="checkbox" checked="checked" /> - Add the workspace structure.<br><br>

&#x1f7e2; As a **User**, I can **Register, Login and Logout**, so that I can **access my personal info and manage my account**.
### &#x2699; Tasks:
<input type="checkbox" checked="checked" /> - Implement user login functionality. <br>
<input type="checkbox" checked="checked" /> - Implement user registration functionality.<br>
<input type="checkbox" checked="checked" /> - Implement user logout functionality.<br><br>

&#x1f7e2; As a **User**, I can **View and Edit my Profile**, so that **I can manage my personal information**.
### &#x2699; Tasks:  

<input type="checkbox" checked="checked" /> - Create a profile view page. <br>
<input type="checkbox" checked="checked" /> - Display user's current information on the profile page. <br>
<input type="checkbox" checked="checked" /> - Implement edit button on the profile page. <br>
<input type="checkbox" checked="checked" /> - Create a form for editing user profile information. <br>
<input type="checkbox" checked="checked" /> - Add validation to ensure proper data input. <br>
<input type="checkbox" checked="checked"/> - Provide feedback to the user after successful editing.
<br> <br>

&#x1f7e2; As a **User**, I can **search for movie titles**, so that **I can quickly find the movies I'm looking for**.
### &#x2699; Tasks:  

<input type="checkbox" checked="checked"/> - Implement search functionality in the movie list. <br>
<input type="checkbox" checked="checked"/> - Display search results in a user-friendly manner. <br>
<input type="checkbox" checked="checked"/> - Provide an option to clear the search. <br>
<input type="checkbox" checked="checked"/> - Present "No results found" header when a searched movie does not exist in the database (TMDB). 
<br><br>

&#x1f7e2; As a **User**, I can **view movie information and trailers**, so that **I can learn more about the movies**.
### &#x2699; Tasks: 

<input type="checkbox" checked="checked"/> - Display information about the film and an image of the film's cover. <br>
<input type="checkbox" checked="checked"/> - Implement a link to click to see a trailer. <br> <br>

&#x1f7e2; As a **User**, I can **initiate contact with the admin via email, or through social networks**, so that **I can provide feedback and address any issues that may arise**.
### &#x2699; Tasks: 

<input type="checkbox" checked="checked"/> - Create a contact form for users to be able to send email directly from the app.<br>
<input type="checkbox" checked="checked"/> - Create social media links for Movie Base in the footer.
<br><br>

&#x1f7e1; As a **User**, I can **Leave reviews and Rate movies**, so that **I can share my opinion about the movies with others**.

### &#x2699; Tasks:

<input type="checkbox" checked="checked"/> - Write test cases to ensure user can write reviews. <br>
<input type="checkbox" checked="checked"/> - Implement functionality for users to submit reviews. <br>
<input type="checkbox" checked="checked"/> - Write test to ensure users can rate movies. <br>
<input type="checkbox" checked="checked"/> - Implementfunctionality for users to rate movies. <br>
<input type="checkbox" checked="checked"/> - Develop admin panel to to manage pending reviews by approving, rejecting or deleting them. <br>
<input type="checkbox" checked="checked"/> - Write test case to confirm that approved reviews is being presented in the app. <br>
<input type="checkbox" checked="checked"/> - Implement functionality to display approved reviews.
<br><br>

&#x1f7e2; As a **Developer** I can **test the app and all it's functions to make sure that everything works as it should**, and **make sure it follows the criteria**.

### &#x2699; Tasks: 

<input type="checkbox" checked="checked"/> - Validate all HTML files <br>
<input type="checkbox" checked="checked"/> - Validate all CSS files<br>
<input type="checkbox" checked="checked"/> - Validate all Python files<br>
<input type="checkbox" checked="checked"/> - Validate all JavaScript files<br>
<input type="checkbox" checked="checked"/> - Make sure everything is documented in README.md<br>
<input type="checkbox" checked="checked"/> - Resolve all workspace warnings and errors.<br>
<input type="checkbox" checked="checked"/> - Compress all project images, when design decisions are finalised. <br><br>

## Testing

### Automated TDD Tests
During the development phase, I implemented TDD tests to validate the functionality of the application. All these tests passed successfully and helped to shape the application robustnes.

<span style="color:orange">Note on Automated Testing</span> <br>
Unfortunately, due to time constraints and technical issues with setting up the test environment toward the end of the project, I was unable to run the automated tests again to confirm their status. However, it should be noted that these tests were functional and passed during the development phase. <br><br>

### Manual Testing 
In addition to the TDD tests, manual testing was also performed to ensure the application runs as expected. This involve real-time test usage of application, navigating through its functionalities to identify and fix any bugs. <br><br>


## Future Improvements (USER STORIES):

&#x1f7e0; As a **User**, I can **receive email confirmations**, so that I **can be notified of important account activities**.
### &#x2699; Tasks: 

<input type="checkbox"/> - Send a welcome email when registering. <br>
<input type="checkbox"/> - Send confirmation when the password has been changed. <br>
<input type="checkbox"/> - Send confirmation when the account has been deleted. <br> <br>

&#x1f7e0; As a **User**, I can **make a list of my favorite movies**, so that I can **share my list with others**.
### &#x2699; Tasks: 
<input type="checkbox"/> - Implement functionality to make a list of favorite movies. <br>
<input type="checkbox"/> - Implement functionality to share the movie list social media, copy link, email, etc. <br><br>


### Suggestions for future improvements also include: <br>
<input type="checkbox"/> - Implement auto suggestions when searching, based on search query in a user frinedly dropdown layout. <br>
<input type="checkbox"/> - Implement friend system, to send / get friend requests to connect with others. <br>
<input type="checkbox"/> - Implement posibility for users to accpet / ignore friend requests sent by others. <br>
<input type="checkbox"/> - Implement DM future for registered users (after accepted friend request)<br>
 <input type="checkbox"/>- Implement functionality for user to upload / change / delete profile image. <br>
 <input type="checkbox"/>- Add default profile image as a dark shadow image to be shown if user doesnt have a profile image.<br><br>


## Credits
### Specials thanks to those who made this project possible by providing essential knowledge and guidance. 
* [**Stack Overflow**](https://stackoverflow.com/) members who guided me when I wa stuck.
* [**Slack**](https://slack.com/) community that also provided guidance when needed. 
* [**Code Institute**](https://codeinstitute.net/global/)'s tutor support.
* [**ChatGPT**](https://chat.openai.com/) by OpenAI for providing valuable insights through out the development process.
* [**Canva**](https://www.canva.com/) - Where I could create the images / gifs presented in the app. 
* **Antonio Rodriguez** - My mentor
* [**Free Front End**](https://freefrontend.com/css-star-ratings/) - For the beautiful rating stars used for user ratings in the app.
* [**CompressJPG**](https://compressjpeg.com/) - Where I compressed all images for the application.