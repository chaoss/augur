Deployment Test Process
============

Since Augur is a data centric system, software testing is not sufficient for ensuring the integrity of current and future implementations. We also test data collection against real repository lists for each release. 

1. New developers will work on forks in their own repositories, generally. For for active contributors, we may create branches for everyone. 

2. Commit and push your work no less frequently than the end of each day. 

3. There are 3 main environments: 
        - development ('dev branch')
        - testing ('deploy-test' branch)
        - production ('master' branch)

4. Only maintainers can push to any of these branches (by merging pull requests.)  We will do this quickly when things are ready.
