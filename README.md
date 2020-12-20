# Final Sprint
Golden Gophers: Michael Branstetter, Maxwell Loduca, Paul Orton, Simon Welge

## Overview and Discussion
Our team chose to primarily move Augur’s frontend from Vue to React and subsequently look at additional endpoint functionality. We also removed any bad/deprecated endpoints that were being called.

## Working Product
Below is a comparison between what we have running currently and the original Augur interface. As you can see, the end product is pretty similar to the original. Our code is hosted [here](http://goldengophers.sociallycompute.io/).

## Requirements Breakdown
Our requirements haven’t deviated too much from what we originally set. Additionally, our use cases haven’t had to change. It seems we’ve made good progress without compromising functionality.

As we essentially rebuilt the frontend from scratch, we looked at what was essential to keep from the Vue version of the frontend and figure out how to best implement it in React.

## Instructions for Running Final Sprint
We have the all of our work running on [this site](http://goldengophers.sociallycompute.io/). Below are instructions for setting up and running a local version of our React frontend:
1. basically links to create react app or something

## Reflection
### Team Roles
* Michael: Development with focus in graphs and API calls
* Max: Documentation and additional work in API calls
* Paul: Documentation and initial server setup
* Simon: Development all-around, team organization, and API calls

### Our Success
We feel, overall, that our project has met our initial goals and provided a stable frontend for displaying information received from Augur's backend. We believe the frontend is quite a bit quicker and more reliable than what is currently in place. It's now a single-page application, and accessing repositories using a URL is now easier and more reliable. 

We utilized the following resources throughout the course of the 
 project:
>  - [Create React App](https://create-react-app.dev/)
>  - [React Bootstrap](https://react-bootstrap.github.io/)
>  - [React Chartkick](https://chartkick.com/react)
>  - [Augur API Documentation](https://oss-augur.readthedocs.io/en/dev/rest-api/api.html)

#### API Streamlining
When developing the graphs, we looked at the old vue frontend, and looked at what API calls were being made. Many of them, it seemed, were queries that failed, so we ended up removing them. Those that we didn't remove we included [here](https://github.com/malkrc/augur/blob/gophers-frontend/react/Insomnia_2020-12-17.json) in this file using the app [Insomnia](https://insomnia.rest/) to visualize and streamline the process. You can simply open the Insomnia app and import our data to see all of the calls that we made, changing or adding environment variables to access different repos if you choose to.

## Where to Go From Here
We wanted to focus specifically on changing frontend frameworks (from Vue to React) and clean up the API calls already in place. Because of this, we felt it was beyond the scope of our project to implement every single feature that is currently available to Augur users. This also leaves room for your team to explore React and create things like the insights page and comparison functionality between repos.