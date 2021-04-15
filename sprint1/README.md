# Progress Report

### What I Did
- Set up server
- Created new fork of Augur 
- Set up Augur on server
  - LINK: <http://ec2-3-84-10-103.compute-1.amazonaws.com>
  - LINK: <http://ec2-3-84-10-103.compute-1.amazonaws.com:5000/api/unstable>  
[![Augur Status Screenshot](/sprint1/img/AugurScreenshot.PNG)](<http://ec2-3-84-10-103.compute-1.amazonaws.com:5000/api/unstable>)
- Completed Use Cases and Requirements Analysis
  - Use Case: <https://github.com/xzhang1011/augur/blob/xzzm2Sprint1/sprint1/UseCase.md>
  - Requirements: <https://github.com/xzhang1011/augur/blob/xzzm2Sprint1/sprint1/Final%20Project%20Requirements.xlsx>

### Obstacles & Reflection
- Errors running make install because didn't install wheel package (pip install wheel), python.h (sudo apt-get install python3-dev), tensorflow (pip install –upgrade pip)
- Wasn't able to finish installing frontend dependencies using make install because stalled for 30+ minutes after warning
![Augur Frontend Installation Stuck](/sprint1/img/AugurFrontendIssue.PNG)

### Goals
- Install Augur's frontend
- Figure out jupyter notebooks? in order to do some frontend fixes
