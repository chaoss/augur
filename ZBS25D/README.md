# AugurInformaticsApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.3.4.

### Link to running project: http://129.114.104.224/

### Augur is focused on prototyping open source software metrics

Functionally, Augur is a prototyped implementation of the Linux Foundation's CHAOSS Project on open source software metrics. 
Technically, Augur is a Flask web application, Python library and REST server that presents metrics on open source software development 
project health and sustainability.

This Augur information site shows different types of data on the progression and development on the Augur application. On the home page
of the site, all of the repository groups that help develop Augur are displayed. Selecting a repo group and a repo, will give the user the ability to select contributors to see information about each developer. The user can also see the number of commits per day of the selected repo, represented as a bar graph to show the number of commits for each of the recorded dates. Overall, this is a visual representation of the development of the Augur application.

This UI design was created using the Angular framework, which allows a developer to create very dynamic web applications in a minimal amount of code. It improves on the basic HTML/JS style of building by providing built in tools, and giving acccess to tools that other developers have created for the framework. One such tool we could take advantage of in this angular project is ng2-charts, which is built off the charts.js api. This allows a developer to combine angular dynamic data binding, with a powerful graph drawing tool. This allows for creating dynamic, clean looking graphs with a very minimal amount of work.

## Steps to Navigate Project

- Select an Augur repository group
- Select a repository within that group
- Select a type of info about that repository from the selector at the top of the page. The visualization will then appear below

## Running Angular Project

To run code on your personal local machine, you must have the lastest version of `Node JS` installed. 

Then, run `npm install -g @angular/cli` to download the Angular CLI  

Once installed, enter the project folder. Make sure to run `npm install` to include all the node modules and necessary dependencies 

## Development Server 

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. This will allow you to run the current project in a test environment. The app will automatically reload if you change any of the source files.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

## Notes

The professor recommended in our sprint three grade comments that we include the name and email of contributors instead of just the user ID, but the Augur endpoint we were provided with did not contain that information. Since we are front end focused, we were told we would not have to go above and beyond to obtain that information. 


