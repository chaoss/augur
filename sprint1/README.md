# Progress Report

### What I Did
- Set up server
- Created new fork of Augur 
- Set up Augur on server
  - LINK: <http://ec2-3-84-10-103.compute-1.amazonaws.com>
  - LINK: <http://ec2-3-84-10-103.compute-1.amazonaws.com:5000/api/unstable/repo>  
[![Augur API Status Screenshot](/sprint1/img/AugurAPIEndpt.PNG)]
[![Augur Status Screenshot](/sprint1/img/AugurScreenshot.PNG)](<http://ec2-3-84-10-103.compute-1.amazonaws.com:5000/api/unstable>)
- Completed Use Cases and Requirements Analysis
  - Use Case Doc: <https://docs.google.com/document/d/1kpX-QgWyduh-6M5s0f4VkoWcEuLB4odX_kPyrCN8fq4/edit?usp=sharing>
  - Requirements Sheet: <https://docs.google.com/spreadsheets/d/1Pdw9Y00sb5DneLfcz_oBSfiNO0EL_f8qgskaYr8olHA/edit?usp=sharing>

### Obstacles & Reflection
- Errors running make install because didn't install wheel package (pip install wheel), python.h (sudo apt-get install python3-dev), tensorflow (pip install –upgrade pip)
- Wasn't able to finish installing frontend dependencies using make install because stalled for 30+ minutes after warning
![Augur Frontend Installation Stuck](/sprint1/img/AugurFrontendIssue.PNG)

### Goals
- Install Augur's frontend + frontend dependencies
- Figure out jupyter notebooks? in order to do some frontend fixes
- Design frontend fixes plan
