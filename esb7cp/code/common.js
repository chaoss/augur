    let dropdown2 = document.getElementById('repoId');
    dropdown2.length = 0;

    let defaultOption2 = document.createElement('option');
    defaultOption2.text = 'Choose Repo ID';

    dropdown2.add(defaultOption2);
    dropdown2.selectedIndex = 0; 
    
    let dropdown = document.getElementById('groupId');
    dropdown.length = 0;

    let defaultOption = document.createElement('option');
    defaultOption.text = 'Choose Repo Group ID';

    dropdown.add(defaultOption);
    dropdown.selectedIndex = 0;

function firstDropdown()
{
    const url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups';

    fetch(url)  
      .then(  
        function(response) {  
          if (response.status !== 200) {  
            console.warn('Error ' + 
              response.status + 'occured');  
            return;  
          }

          // Examine the text in the response  
          response.json().then(function(data) {  
            let option;

            for (let i = 0; i < data.length; i++) {
              option = document.createElement('option');
              option.text = data[i].repo_group_id;

              dropdown.add(option);
            }    
          });  
        }  
      )  
      .catch(function(err) {  
        console.error('Fetch Error -', err);  
      });
}

function getNavBar()
{
    var x = document.getElementById("navbar");
    if(x.className == "topbar")
        {
            x.className += " newClass";
        }
    else
        {
            x.className = "topbar";
        }
}
function displayNavBar(x)
{
    document.getElementById("navbar").innerHTML = "<a id='home' href = 'http://augur.osshealth.io/'>Home</a><a id='data1' href = 'contributers.html'>Contributers</a><a id='data2' href = 'issues.html'>Issues</a><a id='data3' href = 'commits.html'>Commits</a> <a href='javascript:void(0);' class='click' onclick='getNavBar()'> <i class='fa fa-bars'></i> </a>";
    if (x == 0)
    {
        document.getElementById("home").className = "activeButton";
    }
    if (x == 1)
    {
        document.getElementById("data1").className = "activeButton";
    }
    if (x == 2)
    {
        document.getElementById("data2").className = "activeButton";
    }
    if (x == 3)
    {
        document.getElementById("data3").className = "activeButton";
    }
}

function secondDropdown()
{

    dropdown2.length = 1;

    const url2 = 'http://augur.osshealth.io:5000/api/unstable/repos';
    
    document.getElementById("first").text = 
    
    fetch(url2)  
      .then(  
        function(response) 
        {  
          if (response.status !== 200) 
          {  
            console.warn('Error ' + 
              response.status + 'occured');  
            return;  
          }
           //if (dropdown.select) {
          // Examine the text in the response  
          response.json().then(function(data) {  
            let option;

            for (let i = 0; i < data.length; i++) 
            {
//                console.log(document.getElementById('groupId').value);
                if (document.getElementById('groupId').value == data[i].repo_group_id)
                {
                    option = document.createElement('option');
                    option.text = data[i].repo_id;
                    dropdown2.add(option);
                }
            }    
          });  
        }
       // }
      )  
      .catch(function(err) {  
        console.error('Fetch Error -', err);  
      });
}