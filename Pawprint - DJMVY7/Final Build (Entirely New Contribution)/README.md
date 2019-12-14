## Viewing Instructions: 
 *THIS SITE IS MEANT TO BE RUN ON CHROME ON A 1920X1080 DEVICE. IF USING A LAPTOP, PLEASE USE CHROME AND ZOOM OUT UNTIL IT LOOKS APPROPIATE*
- A full, working version of our project is available on www.dmantro.com

***Description***
- The home page gives a description of Augur and has a video speaking about CHAOS. There is a graph that loads in and shows the amount of contributors in each repo group. There is a picture of the Augur logo in the bottom right corner of the page that when clicked, will take you to the login page.
- By defuault, the user will not be logged in. So, the small Augur logo in the top right corner will be RED. When logged in, the Augur logo will be GREEN.
- You can hover over that logo and when logged out, there will be a login button, and when logged in, there will be a log out button.
- The login page displays random data every 5 seconds or so below the login area itself, along with an explanation of the stuff written prior to this.
- The about page describes some of the repo groups within Augur.
- The madeby page just shows the names of the creators (us).
- The contact page just has some made up contact info.
- There are 8 users you can log into. GraphQL, Zephyr-RTOS, MHS, Netflix, Rails, Comcast, CHAOSS, & Apache. GraphQL login info: User: graph Pass: pass | Zephyr login info: User: zephyr Pass: pass | MHS login info: User: mhs Pass: pass | Netflix login info: User: netflix Pass: pass | Rails login info: User: rails Pass: pass | Comcast login info: User: comcast Pass: pass | CHAOSS login info: User: chaoss Pass: pass | Apache login info: User: apache Pass: pass.
- Now logged in, you can view whoevers profile you are logged into. It displays 3 different graphs with info, and the group logo, and there is a button that when clicked, you can view the list of repos within the repo group.

**Tutorial**
1. To use the login system, hover over the Augur logo in the top corner of the site and click login. 
2. Once on the login page, enter the username 'graph' and password 'pass' for GraphQL, or enter the username 'zephyr' and password 'pass' for Zephyr-RTOS, or enter the username 'mhs' and password 'pass' for MHS, and so on and so on for all of the users.
3. You may now access their respective profile pages by clicking the profile button in the Nav!

## Deployment Instructions:

1. Clone repository and use the folder from the Final Build branch titled 'Final Build'.
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
 - FinalBuild: Completed December 11th, 2019

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

## Acceptance Criteria for About, Contact, and Made By Tabs
As a user, should I navigate to the About or Contact tab on the navbar, to view more information about the augur system.

As a user, should I click on the settings button on the navbar, I will be redirected to a site where I can see the creators of the site.
