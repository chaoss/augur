//first dropdown
//let dropdown = document.getElementById('groupId');
//dropdown.length = 0;
//
//let defaultOption = document.createElement('option');
//defaultOption.text = 'Choose Repo Group ID';
//
//dropdown.add(defaultOption);
//dropdown.selectedIndex = 0;
//
//const url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups';
//
//fetch(url)  
//  .then(  
//    function(response) {  
//      if (response.status !== 200) {  
//        console.warn('Error ' + 
//          response.status + 'occured');  
//        return;  
//      }
//
//      // Examine the text in the response  
//      response.json().then(function(data) {  
//        let option;
//    
//    	for (let i = 0; i < data.length; i++) {
//          option = document.createElement('option');
//      	  option.text = data[i].repo_group_id;
//      	 
//      	  dropdown.add(option);
//    	}    
//      });  
//    }  
//  )  
//  .catch(function(err) {  
//    console.error('Fetch Error -', err);  
//  });