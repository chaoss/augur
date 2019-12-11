//CREATES DIV ELEMENTS FOR EACH REPO NAME in group 10 AND DISPLAYS THE NAMES
const app = document.getElementById('root');

//create a variable called container & give it a class "container"
const container = document.createElement('div');
container.setAttribute = ('class', 'container');
app.appendChild(container);

//calls html page & changes container element
var request = new XMLHttpRequest();
request.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/10/committers-locations', true);

//function to parse data
request.onload = function() {

    //parse
    var data = JSON.parse(this.response);
    var count = 0;

    //if you have a valid request
    if(request.status >= 200 && request.status < 400) {
        //for every repo
        data.forEach(repo => {
            //log the repo_name
            console.log(repo.cntrb_id);
            
            //create div elements
            const card = document.createElement('div');
            card.setAttribute('class', 'card');
            
            const h1 = document.createElement('h1');
            h1.textContent = repo.cntrb_id;
            
            container.appendChild(card);
            //put repo name in card
            card.appendChild(h1);
            count++;
        });
    }
}

request.send()




//CREATES DIV ELEMENTS FOR EACH REPO in group 20 NAME AND DISPLAYS THE NAMES
const app2 = document.getElementById('root2');

//create a variable called container & give it a class "container"
const container2 = document.createElement('div');
container2.setAttribute = ('class', 'container');
app2.appendChild(container2);

//calls html page & changes container element
var request2 = new XMLHttpRequest();
request2.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/20/committers-locations', true);

//function to parse data
request2.onload = function() {

    //parse
    var data = JSON.parse(this.response);
    var count = 0;

    //if you have a valid request
    if(request2.status >= 200 && request2.status < 400) {
        //for every repo
        data.forEach(repo => {
            //log the repo_name
            console.log(repo.cntrb_id);
            
            //create div elements
            const card2 = document.createElement('div');
            card2.setAttribute('class', 'card');
            
            const h1 = document.createElement('h1');
            h1.textContent = repo.cntrb_id;
            
            container2.appendChild(card2);
            //put repo name in card
            card2.appendChild(h1);
            count++;
        });
    }
}

request2.send()
