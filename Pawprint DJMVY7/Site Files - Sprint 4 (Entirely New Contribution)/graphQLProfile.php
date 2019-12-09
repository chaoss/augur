<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Augur: GraphQL Profile</title>
        <meta charset="utf-8">
        <link href="https://fonts.googleapis.com/css?family=Lora|Encode+Sans+Condensed" rel="stylesheet">
       <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" type="text/css" href="stylesheet.css">

        <!-- jQuery library -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

        <!-- Latest compiled JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
        <script src="https://www.chartjs.org/dist/2.8.0/Chart.min.js"></script>
        <script src="graphQLGroup.js"></script>
    </head>

    <body id="graphQLProfileBody" onload="getRepoGroupInfo()">      
        
        <?php
            $graphUser = empty($_COOKIE['graph']) ? '' : $_COOKIE['graph'];
            if (!$graphUser) {
                header('Location: logIn.php');
                exit;
            }
        ?>
        
        <div class="navbar">
            <a href="index.php">Home</a>
            <a href="about.php">About</a>
            <a href="contact.php">Contact</a>
            <?php
            $graphUser = empty($_COOKIE['graph']) ? '' : $_COOKIE['graph'];
            $zephyrUser = empty($_COOKIE['zephyr']) ? '' : $_COOKIE['zephyr'];
            if (!$graphUser && !$zephyrUser) {
              echo '<a href="graphQLProfile.php">Profile</a>'; 
              echo '<a>Settings</a>';
            echo '<div class="dropdown">';
              echo '<button class="dropbtn"><img src="logOutNavbar.jpg"></button>';
              echo '<div class="dropdown-content"><a href="logIn.php">Login</a></div>'; 
              echo '</div>';
            }
            else if ($graphUser) {
                echo '<a class="active" href="graphQLProfile.php">Profile</a>';
                echo '<a>Settings</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($zephyrUser) {
                echo '<a href="zephyrProfile.php">Profile</a>';
                echo '<a>Settings</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
           ?>
       </div>
        
        <h1 id="pageTitle">Welcome GraphQL Repo Group!</h1>
        
        <script>
//            functions in javascript
//            routing
            
            import { HomeComponent } from './home/home.component';
            import { AboutComponent } from './about/about.component';
            import { PrivacyComponent } from './privacy/privacy.component';
            import { TermsComponent } from './terms/terms.component';
            
            const routes: Routes = [
              { path: 'home', component: HomeComponent },
              { path: 'about', component: AboutComponent },
              { path: 'contact', component: ContactComponent },
              { path: 'profile', component: ProfileComponent },
              { path: '', redirectTo: '/home', pathMatch: 'full' }
            ];
        </script>
        
        <div id = "mainWrapper">
            <div id = "innerWrapper">
                <div id="chartWrapper">
                    <div class="row">
                        <div class="col-sm-9" id="sectionBody"></div>
                    </div>
                    <div class="row">
                        <div class="col-sm-9" id="sectionBody2"></div>
                    </div>
                    <div class="row">
                        <div class="col-sm-9" id="sectionBody2"></div>
                    </div>
                </div>
                <div id="secondaryWrapper">
                   <div id="otherFunctionProfileWrapper">
                     <h3 id="viewGraphRepoLine">View Repos In GraphQL!</h3>   
                       <p id="graphQLDropdown"><select id="graphDrop" name="GraphQL-Repos"><option>View Repos ↓</option></select></p>
                   </div>
                   <div id="profileLogoWrapper"><img src="graphLogo.png" alt="GraphQL Logo" class="albumCover"></div>
                </div>
            </div>
        </div>    
    </body>
</html>