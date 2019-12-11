# AugurInformaticsApp

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.3.4.

## Sprint 3 Design Descriptions

This Front-End design was created based off the wireframes drafted in the previous sprint. For sprint three, we created multiple different designs individually to model how the UI could look when created using different technologies. This UI design was created using the Angular framework, which allows a developer to create very dynamic web applications in a minimal amount of code. It improves on the basic HTML/JS style of building by providing built in tools, and giving acccess to tools that other developers have created for the framework. One such tool we could take advantage of in this angular project is ng2-charts, which is built off the charts.js api. This allows a developer to combine angular dynamic data binding, with a powerful graph drawing tool. This allows for creating dynamic, clean looking graphs with a very minimal amount of work.
  
Once a user enters the page, they will be presented with all the repository groups that are stored in the augur system. Clicking on a repository group will navigate the user to a new page, which is a detail page for the selected repository group. On that page, there is a list of all the repositories contained within that group. In the future, there could be a graphical representation of the commits as a bar graph on the top of the page, to show which repositories contribute to the most commits in that group. The repositories are displayed in a card gallery layout, and clicking on the desired repository will navigate you to a detail page about that repository.
  
Once on this detailed info page about the selected repository, the user will be presented with a page that has a UI selector object on
it. This selector allows the user to select which type of data about the selected repository they would like to view. For example, the
user can click on the "contributors" selector, and all the contributors in that repository will be displayed on the screen. Selecting
another type of info will change the page layout to display that new piece of data. Other information included may be presented as a graphical representation of data, such as line graphs to show total pull requests over time. Information can also be shown in bar graph form, such as showing top committers, and showing their number of commits as a bar so they can be compared with the other committers.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build. **TO BUILD OUR ANGULAR PROJECT: "ng build --base-href '/(path-to-project-if-in-directory/directories)/' --prod** "

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
