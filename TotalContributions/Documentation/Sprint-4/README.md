# Sprint 4

### Design Document Link
-[Design Document](https://github.com/computationalmystic/sengfs19-group3/blob/master/Sprint-1/Design-Document/Description.md)

### FinalSprintProject link

-[Link to Angular code for our website](https://github.com/computationalmystic/sengfs19-group3/tree/master/Sprint-3)


### Website's Function
* User can apply filter, pageing(10, 25, 50 100), and sorting with each columns.
* Repo page! Users can check the table of the commits for each repos!
* Repo group page! Users can check the table of the message and table of contributor for each repo group!
* Table of message and table of contributor and switch using button in the top-left!
* [Message Table Test Link](http://129.114.104.142:4250/messages/20)
* [Contributor Table Test Link](http://129.114.104.142:4250/contributors/20)
* [Info Page Table Test Link](http://129.114.104.142:4250/info/24/21623)
* [Sample API Endpoint Link for messages-by-contributor](http://129.114.104.142:5000/api/unstable/repo-groups/20/messages-by-contributor)
* [Sample API Endpoint Link for contributors-by-company](http://129.114.104.142:5000/api/unstable/repo-groups/20/contributors-by-company)



### Deployment Instructions
* Deploy augur using the instructions provided by the augur read the docs website.
* To deploy our project, the only other dependency we had to install was the angular-cli tool through npm package manager to deploy our website(This requires having node.js and the npm package manager). This is assuming you have all the dependencies required for augur installed already <blockquote>npm install @angular/cli -g</blockquote> and then go to the directory of our FinalSprintProject directory with our angular-based website. Then, we run the command <blockquote>ng serve --host=0.0.0.0 --port=4250</blockquote> this will deploy the website to be able to be reached from any host on the internet through port 4250. Then go to our home page on our website [Group 3 Website Homepage]()


### Modified Code 

1. We added a metric function for messages-by-contributor to contributors.py

> 

    @annotate(tag='messages-by-contributor')
    def messages_new(self, repo_group_id, repo_id=None):
        """
        Returns the number of messages made by a contributor
        :param repo_group_id: The repository's repo_group_id
        :param repo_id: The repository's repo_id, defaults to None
        """

        messages_new_SQL = ''

        if repo_id:
            messages_new_SQL = s.sql.text("""
                SELECT
                    cntrb_id, COUNT(*) AS messages FROM message
                    GROUP BY cntrb_id
                    ORDER BY messages desc;
            """)

            results = pd.read_sql(messages_new_SQL, self.database, params={'repo_id': repo_id})

            return results

            else:
                messages_new_SQL = s.sql.text("""
                    SELECT
                        cntrb_id, COUNT(*) as messages FROM message
                        GROUP BY cntrb_id
                        ORDER BY messages desc;
                """)

                results = pd.read_sql(messages_new_SQL, self.database, params={'repo_group_id': repo_group_id})

                return results 

2. Then we added the metric route for messages-by-contributor to routes.py to be able to reach the API endpoint we created

>   
    
    server.addRepoGroupMetric(metrics.top_messages, 'messages-by-contributor')

    server.addRepoMetric(metrics.top_messages, 'messages-by-contributor')
    
3. Then we created test functions for metric function messages-by-contributor in test_contributors_functions.py
 
 >
 
    def test_messages(metrics):
      assert metrics.messages_by_contributor(20, repo_id=21000)
      assert metrics.messages_by_contributor(20)
 
 4. Then we created test functions for the metric route for messages-by-contributor in test_contributors_routes.py
 
 >
 
    def test_messages_by_contributor(metrics):
      response = requests.get('http://localhost:5000/api/unstable/repo-groups/21/messages-by-contributor')
      data = response.json()
      assert response.status_code == 200
      assert len(data) >= 1
    
5. Then we created another metric function for contributors-by-company in contributors.py

>
      
      @annotate(tag='contributors-by-company')
      def contributors_by_company(self, repo_group_id, repo_id=None):
          """
          Returns the number of contributors categorized by each company.
          """
          if repo_id:
              numOfContribsByCompany = s.sql.text("""
                      SELECT cntrb_company, COUNT(*) AS counter FROM contributors
                      GROUP BY cntrb_company
                      ORDER BY counter desc;
                      """)
              results = pd.read_sql(numOfContribsByCompany, self.database, params={"repo_id": repo_id})
              return results
          else:
              numOfContribsByCompany = s.sql.text("""
                  SELECT cntrb_company, COUNT(*) as counter from contributors
                  GROUP BY cntrb_company
                  ORDER BY counter desc;
                  """)
              results = pd.read_sql(numOfContribsByCompany, self.database, params={"repo_group_id": repo_group_id})
              return results

6. Then we created a metric route for that metric function in routes.py

>

    server.addRepoMetric(metrics.contributors_by_company, 'contributors-by-company')
    """
    @apiDescription Returns a list of the number of contributors by company
    @apiParam {string} repo_group_id Repository Group ID
    @apiParam {string} repo_id Repository ID
    @apiSuccessExample {json} Success-Response:
                [
                    {
                        "cntrb_company": "Microsoft"
                        "total_commits": 14
    """
    
7. Then with the help of Sean, we fixed my SQL query for the contributors-by-company metric function in contributors.py

>

    numOfContribsByCompany_SQL = s.sql.text("""
                SELECT cntrb_company, count(*) AS counter FROM 
                (
                SELECT DISTINCT 
                    cntrb_company, repo.repo_id, contributors.cntrb_id,
                    COUNT ( * ) AS counter 
                FROM
                    contributors,
                    repo,
                    issues 
                WHERE
                    repo.repo_id = issues.repo_id 
                AND issues.cntrb_id = contributors.cntrb_id
                AND repo.repo_id = :repo_id
                GROUP BY
                    cntrb_company, repo.repo_id, contributors.cntrb_id
                UNION
                SELECT
                    cntrb_company, repo.repo_id, contributors.cntrb_id, 
                    COUNT ( * ) AS counter 
                FROM
                    contributors,
                    repo,
                    commits 
                WHERE
                    repo.repo_id = commits.repo_id 
                    AND ( commits.cmt_author_email = contributors.cntrb_canonical OR commits.cmt_committer_email = contributors.cntrb_canonical ) 
                    AND repo.repo_id = :repo_id
                GROUP BY
                    cntrb_company, repo.repo_id, contributors.cntrb_id) L
                GROUP BY L.cntrb_company
                ORDER BY counter DESC; 
                """)
                
                #fixed a problem with double quotes here
                results = pd.read_sql(numOfContribsByCompany_SQL, self.database, params={'repo_id': repo_id})
                
                # modified the else statement as well
       numOfContribsByCompany_SQL = s.sql.text("""
            SELECT cntrb_company, count(*) AS counter FROM 
                (
                SELECT DISTINCT 
                    cntrb_company, repo.repo_id, contributors.cntrb_id,
                    COUNT ( * ) AS counter 
                FROM
                    contributors,
                    repo,
                    issues 
                WHERE
                    repo.repo_id = issues.repo_id 
                AND issues.cntrb_id = contributors.cntrb_id
                AND repo.repo_group_id = :repo_group_id
                GROUP BY
                    cntrb_company, repo.repo_id, contributors.cntrb_id
                UNION
                SELECT
                    cntrb_company, repo.repo_id, contributors.cntrb_id, 
                    COUNT ( * ) AS counter 
                FROM
                    contributors,
                    repo,
                    commits 
                WHERE
                    repo.repo_id = commits.repo_id 
                    AND ( commits.cmt_author_email = contributors.cntrb_canonical OR commits.cmt_committer_email = contributors.cntrb_canonical ) 
                    AND repo.repo_group_id = :repo_group_id
                GROUP BY
                    cntrb_company, repo.repo_id, contributors.cntrb_id) L
                GROUP BY L.cntrb_company
                ORDER BY counter DESC;
            """)   
            
 8. Fixed the metric routes for the contributors-by-company metric function in routes.py
 
 >    
    
      server.addRepoMetric(metrics.contributors_by_company,'contributors-by-company')
      server.addRepoGroupMetric(metrics.contributors_by_company,'contributors-by-company')
 
 9. Fixed two lines in the SQL query for getting rid of null values
 
 >  
 
      #fixed in the repo_id if statement
      WHERE cntrb_company IS NOT NULL
      fixed in the else statement for repo_group_id
      WHERE cntrb_company IS NOT NULL
 
 10. Created test functions for the metric function contributors-by-company in test_contributors_functions.py
 
 > 
 
      def test_contributors_by_companys(metrics):

        #repo_group_id
        assert metrics.contributors_by_company(20).iloc[0]['counter'] > 0

        #repo_id
        assert metrics.contributors_by_company(20, repo_id=25432).iloc[0]['counter'] > 0
    
 11. Created test functions for the metric route for metric function contributors-by-company in test_contributors_routes.py
 
 >
 
     def test_contributors_by_company_group(metrics):
      response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/contributors-by-company')
      data = response.json()
      assert response.status_code == 200
      assert len(data) >= 1


    def test_contributors_by_company_repo(metrics):
        response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/repos/25432/contributors-by-company')
        data = response.json()
        assert response.status_code == 200
        assert len(data) >= 1
        
11. Then we created the web GUI for displaying our endpoints using Angular framework

* [Link to angular changes part 1](https://github.com/computationalmystic/sengfs19-group3/commit/f81da6cc12133f5d3a4a6742d97646d09f758ca9)

* [Link to angular changes part 2](https://github.com/computationalmystic/sengfs19-group3/commit/7bc8b896d1fd4ef52f6702b0a35f4c4dc5184a90)

12. Fixed the repo and repo_group metric function for messages-by-contributor test function in test_contributors-functions.py

>

        assert metrics.messages_by_contributor(20, repo_id=21000).iloc[0]['messages'] > 0
        assert metrics.messages_by_contributor(20).iloc[0]['messages'] > 0




### Testing Metric Functions and Metric Routes
1. After creating the endpoints, we created pytest functions to ensure the endpoints wouldn't fail.
2. Create pytest functions for metric functions
> 

    def test_contributors_by_companys(metrics):
    
         #repo_group_id
         assert metrics.contributors_by_company(20).iloc[0]['counter'] > 0

         #repo_id
         assert metrics.contributors_by_company(20, repo_id=25432).iloc[0]['counter'] > 0

    def test_messages(metrics):
        # repo id
        assert metrics.messages_by_contributor(20, repo_id=21000).iloc[0]['messages'] > 0

        #repo group
        assert metrics.messages_by_contributor(20).iloc[0]['messages'] > 0

3. Create pytest functions for metric routes
>       

        def test_contributors_by_company_group(metrics):
            response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/contributors-by-company')
            data = response.json()
            assert response.status_code == 200
            assert len(data) >= 1
            
        def test_messages_by_contributor_by_group(metrics):
            response = requests.get('http://localhost:5000/api/unstable/repo-groups/21/messages-by-contributor')
            data = response.json()
            assert response.status_code == 200
            assert len(data) >= 1
            
        def test_contributors_by_company_repo(metrics):
            response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/repos/25432/contributors-by-company')
            data = response.json()
            assert response.status_code == 200
            assert len(data) >= 1
            
        def test_messages_by_contributor_by_repo(metrics):
            response = requests.get('http://localhost:5000/api/unstable/repo-groups/21/repos/21222/messages-by-contributor')
            data = response.json()
            assert response.status_code == 200
            assert len(data) >= 1
            
 4. Test the metric functions and metric routes using pytest
 >
 
        pytest -vs test_contributor_functions.py
        
        pytest -vs test_contributor_routes.py
  
 ### Testing Web Application
 
 **API information:**
 
1. Contributors   by   company:   it   shows   how   many   contributors   come   from   a specific company.
2. Message   by   contributor:   it   shows   how   many   messages   provide   by   each contributor
3. Repo group: show all repo group in database
4. Repo: show all repo in database 
5. Commits: show how many commits is posted by specific user.

**Function:**

1. User can select any repo group to see the table of contributor and table of message (if there is data from database, it will be in the table.) User can test group ID:20, (http://129.114.104.142:4250/contributors/20). There a button which can switch between message and contributor table on the top left.
2. User can select any repo pages to see the table of commit. User can testgroup id: 24 and repo id: 21623 (http://129.114.104.142:4250/info/24/21623)
3. User can  sort every  column,  just click  the  header  of  the  column  (such  assorting   commits   in   repo   page,   we   will   know   which   people   doing   mostcommits)
4. User can change how many items show in each page in the bottom of the table. Also, change to go to next page and preview page.
5. User can search data from table, user needs to type in the filter bar abovethe table. (test data in repo, such as 21623.)

**System integration:**

**How we call the API:**

1. Use the httpclient in an API server JavaScript file to call API from server

**Code example:**

>

    Public getGroups():Observable<any>{
        console.log("called getGroups");
        return
    this.http.get('http://augur.osshealth.io:5000/api/unstable/repo-groups')
    }
    
2. Import the JavaScript file to other component (such as repo, info, message ,repo group, or contributors)
3. Use getter function to get the data from JavaScript file 
4. Import mat table from Angular model and put all the data from API to the mat table data source.

**Code example:**

>  

        getter() {
        this.apiService.getGroups().subscribe(data=>{
            this.dataSource = newMatTableDataSource(data);
            console.log(this.dataSource);
            this.dataSource.paginator = this.paginator;
            this.dataSource.sort = this.sort;    
        
        },(error:any)=>{
            this.erro = error;
            console.error("Error:",error);    
        
        });
               
        }

5. Use applyFilter function to support searching.

>

    applyFilter(filterValue:string){
        this.dataSource.filter = filterValue.trim().toLowerCase();  
    }
    
6. Check data source get the data or not

**Example code:**

>
    
    <ng-container*ngIf="!dataSource">        
            <h4>Loading repository group information...</h4>    
        </ng-container>

7. Use form field to create a filter bar

>

    <divclass = "search-div">
            <mat-form-fieldclass="center" floatLabel="never">
                <input matInput(keyup)="applyFilter($event.target.value)"
                placeholder="Filter" >        
                    <button mat-button matSuffix mat-icon-button aria-label = "Clear"
                *ngIf="filterValue"(click)= "onSearchClear()">          
                    </button>      
                    </mat-form-field>
            </div>
            
8. call the data from mat table data source to show in the table

>

    <mat-table[dataSource]="dataSource"matSort>              
            <ng-container matColumnDef="cntrb_id">                
                <mat-header-cell *matHeaderCellDef mat-sort-header> ID </mat-header-cell>                
                    <mat-cell *matCellDef="let message"> 
            {{message.cntrb_id}} </mat-cell>              
                </ng-container>
            <ng-container matColumnDef="messages">
                    <mat-header-cell *matHeaderCellDef mat-sort-header> Message </mat-header-cell>
                    <mat-cell *matCellDef="let message"> {{message.messages}} </mat-cell>
                </ng-container>
                    <mat-header-row *matHeaderRowDef="displayedColumns"></mat-header-row>
                    <mat-row *matRowDef="let row; columns: displayedColumns;"></mat-row> 
                    
                </mat-table>
                
9. apply paginator

**Example code:**

>

    <mat-paginator [pageSizeOptions]="[10,   25,   50,100]" showFirstLastButtons></mat-paginator>
    
10. router link between contributor table and message table

**Example code**

>

    <a routerLink = "/contributors/{{this.urlGroupId}}"><button class="Contributor" style="color:gray;margin-left: 2.5%;"> Contributor Table</button></a>
    <divclass = "search-div">
    
11. router link to table of commit

**Example code:**

>

    <a routerLink ="/info/{{repo.repo_group_id}}/{{repo.repo_id}}">
        {{repo.repo_name}} </a>  </mat-cell>
        
12. router link table of contributor

**Example code:**

>

    <a routerLink ="/contributors/{{repog.repo_group_id}}">
        {{repog.repo_group_id}}</a>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
