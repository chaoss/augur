
// document.getElementById("item1").value;

// <select id= "groupId" name="repo group"></select>
// <select id= "repoId" name="repo stuff"></select>

function cardView(){

    let repoId = document.getElementById("repoId").value ; 
    let groupId = document.getElementById("groupId").value ; 
    const container = document.getElementById('accordion');

    const url2 = 'http://augur.osshealth.io:5000/api/unstable/repos';

    fetch(url2)  
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
        
            for (let result = 0; result < data.length; result++) {
                //Example Data 
                // repo_id	:	22293
                // repo_name	:	commons-el
                // description	:	null
                // url	:	github.com/apache/commons-el.git
                // repo_status	:	Complete
                // commits_all_time	:	null
                // issues_all_time	:	null
                // rg_name	:	Apache (wg-value)
                // repo_group_id	:	24
                // base64_url	:	Z2l0aHViLmNvbS9hcGFjaGUvY29tbW9ucy1lbC5naXQ=
                
                if(data[result].repo_id == repoId){

                console.log(data[result])
                const card = document.createElement('div');
                card.classList = 'card-body';
            
                const content = `
                <div class="card">
                <div class="card-header" id="heading-${result}">
                    <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapse-${result}" aria-expanded="true" aria-controls="collapse-${result}">
                            </button>
                    </h5>
                </div>

                <div id="collapse-${result}" class="collapse show" aria-labelledby="heading-${result}" data-parent="#accordion">
                    <div class="card-body">

                    <h5>${data[result].repo_name}</h5>
                    <p>${data[result].repo_id}</p>
                    <p>${data[result].repo_group_id}</p>
                    ...
                    </div>
                </div>
                </div>
                `;

                // Append newyly created card element to the container
                container.innerHTML += content;
            }
        }  
        }  
    )  
    .catch(function(err) {  
        console.error('Fetch Error -', err);  
    }); 
    } )

}