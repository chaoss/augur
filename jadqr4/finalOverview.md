#Beginning NavBar Code
<!DOCTYPE html>
 <html>
     <head>
         <title>Profile Page</title>
         <meta charset="utf-8">
         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
     </head>
     <style>
     ul {
           list-style-type: none;
           margin: 0;
           padding: 0;
           overflow: hidden;
           background-color: #333;
         }

         li {
           float: left;
         }

         li a {
           display: block;
           color: white;
           text-align: center;
           padding: 14px 16px;
           text-decoration: none;
         }

         li a:hover {
           background-color: #111;
         }
          .dropdown {
           float: left;
           overflow: hidden;
         }

         .dropdown .dropbutton {
           font-size: 16px;  
           border: none;
           outline: none;
           color: white;
           padding: 14px 16px;
           background-color: inherit;
           font-family: inherit;
           margin: 0;
         }

         .navbar a:hover, .dropdown:hover .dropbutton {
           background-color: red;
         }

         .dropdown-content {
           display: none;
           position: absolute;
           background-color: #f9f9f9;
           min-width: 160px;
           box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
           z-index: 1;
         }

         .dropdown-content a {
           float: none;
           color: black;
           padding: 12px 16px;
           text-decoration: none;
           display: block;
           text-align: left;
         }

         .dropdown-content a:hover {
           background-color: #ddd;
         }

         .dropdown:hover .dropdown-content {
           display: block;
         }
         
     </style>
     <body>

         <ul>
           <li><a href="#home">Home</a></li>
           <li><a href="#news">News</a></li>
           <li><a href="#contact">Contact</a></li>
           <li><a href="#about">About</a></li>
         </ul>
             <div class="dropdown">
                 <button class="dropbuttton"><i class="fa fa-caret-down"></i></button>
                 <div class="dropdown-content">
                     <a href="#setting">Settings</a>
                     <a href="#logout">Logout</a>
                 </div>
             </div>
         <h1>Welcome User!</h1>
     </body>
 </html> 

#Updated NavBar,CSS, and Routing

 <nav class="navbar navbar-default">
     <div class="container-fluid" id="container">

     <div class="collapse navbar-collapse">
       <ul class="nav navbar-nav">
         <li class="buttons">
             <div class="navbar-form">
                 <div class="btn-group">
                     <a class="btn btn-default"  href="#home">Home</a>
                     <a class="btn btn-default"  href="#about">About</a>
                     <a class="btn btn-default"  href="#contact">Contact</a>
                     <a class="btn btn-default"  href="#profile">Profile</a>
                     <a class="btn btn-default dropdown-toggle" data-toggle="dropdown" href="#">Settings<span class="caret"></span></a>
                   <ul class="dropdown-menu">
                     <li><a href="#sort">Sort Data</a></li>
                     <li><a href="#logout">Logout</a></li>
                   </ul>
                 </div>
             </div>
         </li> 
       </ul>
      </div>
     </div>
 </nav>

         <h1>Welcome User!</h1>

         <script>
 //            functions in javascript
 //            routing
             
             import { HomeComponent } from './home/home.component';
             import { AboutComponent } from './about/about.component';
             import { PrivacyComponent } from './privacy/privacy.component';
             import { TermsComponent } from './terms/terms.component';
             
             const routes: Routes = [
               { path: 'home', component: HomeComponent },
               { path: 'about', component: AboutComponent },
               { path: 'contact', component: ContactComponent },
               { path: 'profile', component: ProfileComponent },
               { path: '', redirectTo: '/home', pathMatch: 'full' }
             ];
         </script>

#Media Queries Created but not pushed for lack of testing 
@media only screen and (min-device-width: 768px) and (max-device-width: 1024px) and (-webkit-min-device-pixel-ratio: 1) {
   /* ipad device width */
    #textWrapper{
        overflow: wrap;
        text-align: left;
        font-size: 1em;
        /* slightly smaller font */
    }
    #secondaryWrapper{
        float: left;
        font-size: 1em;
    }
    #logoWrapper{
        float: left;
        height: 157.5px;
        width: 337.5px;
    }
    #imagesWrapper{
        float: left;
        height: 502.5px;
        width: 390px;
        /* 75 percent of original size */
    }
}

@media only screen and (min-device-width: 320px)  and (max-device-width: 480px) and (-webkit-min-device-pixel-ratio: 2) {
    /* iphone device width */
    #textWrapper{
        overflow: wrap;
        text-align: left;
        font-size: .5em;
        /* reducing font by around half */
    }
    #secondaryWrapper{
        float: left;
        font-size: .5em; 
    }
    #logoWrapper{
        float: left;
        height: 105px;
        width: 225px;
    }
    #imagesWrapper{
        float: left;
        height: 335px;
        width: 260px;
        /* 50 percent of original size */
    }
}

#Documentation 
## Viewing Instructions: 
 *THIS SITE IS MEANT TO BE RUN ON CHROME ON A 1920X1080 DEVICE. IF USING A LAPTOP, PLEASE USE CHROME AND ZOOM OUT UNTIL IT LOOKS APPROPIATE*
- A full, working version of our project is available on www.dmantro.com

***Description***
- The home page gives a description of Augur and has a video speaking about CHAOS. There is a graph that loads in and shows the amount of contributors in each repo group. There is a picture of the Augur logo in the bottom right corner of the page that when clicked, will take you to the login page.
- By defuault, the user will not be logged in. So, the small Augur logo in the top right corner will be RED. When logged in, the Augur logo will be GREEN.
- You can hover over that logo and when logged out, there will be a login button, and when logged in, there will be a log out button.
- The login page displays random data every 5 seconds or so below the login area itself, along with an explanation of the stuff written prior to this.
- There are 2 users you can log into (we might implement every single repo group by the final submission on the 14th). GraphQL and Zephyr-RTOS. GraphQL login info: User: graph Pass: pass. Zephyr login info: User: zephyr Pass: pass.
- Now logged in, you can view whoevers profile you are logged into. It displays 3 different graphs with info, and the group logo, and there is a button that when clicked, you can view the list of repos within the repo group.

**Tutorial**
1. To use the login system, hover over the Augur logo in the top corner of the site and click login. 
2. Once on the login page, enter the username 'graph' and password 'pass' for GraphQL. Or enter the username 'zephyr' and password 'pass' for Zephyr-RTOS.
3. You may now access their respective profile pages by clicking the profile button in the Nav!

## Deployment Instructions:

1. Clone repository and use the folder from the Sprint 4 branch titled 'Sprint 4'.
2. Within that folder, use the folder titled 'Site Files' to view the website.
3. Host those files on a server that can run php, as our website pages are .php and not .html.
4. View & Done!

## Modified/Created Code
Changes:
- We scrapped the idea of an admin user logging in. It proved to be too complicated and not really possible.
Branch Descriptions: 
1. Each team member had their own development branch for pushing updates on code they were individually working on
 - DomDevBranch: Dominic Mantro
 - DerekDevBranch: Derek Rechtien
 - JessicaDevBranch: Jessica Dean
 - MartianDevBranch: Martian Lapadatescu
2. Branches were also created for each individual sprint in order to successfully merge and submit code weekly
 - Sprint1: Completed November 4th, 2019
 - Sprint2: Completed November 11th, 2019
 - Sprint3: Completed November 20th, 2019
 - Sprint4: Completed December 5th, 2019

## Testing: 
Used manual testing of website to debug and assess any errors 

## Acceptance Criteria for Nav Bar 
As a user, I want to be able to navigate to different pages, so that I may login, and view other data with a clear navigation system
1. When I click on home in the navbar it will display home page data
2. When I click on profile in the navbar it will display my data based on which profile I have used to login; Data will include 3 graphs, and a list of the repositories
3. If I try to access the profile page without having logged in prior, the page will redirect me to the login page before I can proceed
4. When I hover over the augur logo on the top right corner, a dropdown will appear with the option to logout or login; should I click the button to login it will take me to the login page, should I click the button to logout the page will redirect me to the home page and the augur logo will change from green to red to indicate a change in login status

## Acceptance Criteria for Profile Page
As a user, I want to view my profile, so that I may see a contributions per user in a pie graph, a bar graph of contributors over the last 6 months, a bar graph of weekly pull rate over the last 6 months, and a list of repositories in a dropdown menu
1. To view a full list of the repositories you can click on the dropdown button on the right hand side of the page that will show the full list of repos

## Acceptance Criteria for Home Page
As a user, I want to view the home page when first visiting the website, and when I click on the home tab in the navbar, so that I will see Augur information, a bar graph for contributors in each repo group, a youtube video explaining Augur, with a link to login

## Acceptance Criteria for Login Page
As a user, I want be able to login to my respective repository group, so that I may see data on my profile page after logging in that reflects data pertinent to my work
1. To login on the login page using GraphQL credentials type username “graph” and password “pass”; To login on the login page using Zephyr credentials type username “zephyr” and password “pass”
2. If username or password are incorrectly entered a popup alert will show “Sorry! The username or password you have entered is incorrect, Please try again”
3. If correct username and password are entered the page will redirect the user to the home page, and the augur logo will update from red to green in the top right corner indicating a successful login

## Acceptance Criteria for About, Contact, and Settings Tabs
As a user, should I navigate to the About or Contact tab on the navbar, I will see an image explaining the site is under construction (To be updated later)

As a user, should I click on the settings button on the navbar, the button will be disabled until further testing has taken place to adjust “dark mode” properties
----------------------------------------------------------------------------------------------------------------

#Overview
During this project I worked to create the original drafts of the home page and profiles pages html and css. I worked to create a consist navigation bar and began the process of angular routing. However Dominic had a more advanced navigation bar that we decided to adopt afterwards. I then worked on specific changes on the UI such as  working on the drop down menu, and making crucial decisions for my team for what options and functionality we would have. I worked to create CSS Queries for different screen sizes and sent my verison off to Dominic so he could implement them on his running server. Finally I worked to document our teams project and update the original documentation created in Sprint 1. Besides paticular coded examples I feel I was a valuable member of this team as I helped to lead and faciliate roles, and consistently set up meeting times to keep our group on track.
