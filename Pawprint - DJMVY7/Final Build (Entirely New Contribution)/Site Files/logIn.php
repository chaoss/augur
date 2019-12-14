<!DOCTYPE html>
<html lang="en">
    <head>       
      <title>Augur: Login</title> 
        <meta charset="utf-8">
          <link href="https://fonts.googleapis.com/css?family=Lora|Encode+Sans+Condensed" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="stylesheet.css">
                    <script src="djmvy7FinalJS.js"></script> 
                        <script src="https://code.jquery.com/jquery-3.4.0.min.js" integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg=" crossorigin="anonymous"></script>
                        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js" integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU=" crossorigin="anonymous"></script>

        <!-- jQuery library -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

        <!-- Latest compiled JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
        <script src="https://www.chartjs.org/dist/2.8.0/Chart.min.js"></script>
        <script src="loginGraph.js"></script>
    </head>
    <body id="logInBody" onload="getRepoGroupInfo()"> 
        <div class="navbar">
            <a href="index.php">Home</a>
            <a href="about.php">About</a>
            <a href="contact.php">Contact</a>
            <?php
            $graphUser = empty($_COOKIE['graph']) ? '' : $_COOKIE['graph'];
            $zephyrUser = empty($_COOKIE['zephyr']) ? '' : $_COOKIE['zephyr'];
            $mhsUser = empty($_COOKIE['mhs']) ? '' : $_COOKIE['mhs'];
            $netflixUser = empty($_COOKIE['netflix']) ? '' : $_COOKIE['netflix'];
            $railsUser = empty($_COOKIE['rails']) ? '' : $_COOKIE['rails'];
            $comcastUser = empty($_COOKIE['comcast']) ? '' : $_COOKIE['comcast'];
            $chaossUser = empty($_COOKIE['chaoss']) ? '' : $_COOKIE['chaoss'];
            $apacheUser = empty($_COOKIE['apache']) ? '' : $_COOKIE['apache'];
            if (!$graphUser && !$zephyrUser && !$mhsUser && !$netflixUser && !$railsUser && !$comcastUser && !$chaossUser && !$apacheUser) {
              echo '<a href="graphQLProfile.php">Profile</a>'; 
              echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
              echo '<button class="dropbtn"><img src="logOutNavbar.jpg"></button>';
              echo '<div class="dropdown-content"><a href="logIn.php">Login</a></div>'; 
              echo '</div>';
            }
            else if ($graphUser) {
                echo '<a href="graphQLProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($zephyrUser) {
                echo '<a href="zephyrProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
             else if ($mhsUser) {
                echo '<a href="mhsProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($netflixUser) {
                echo '<a href="netflixProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($railsUser) {
                echo '<a href="railsProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($comcastUser) {
                echo '<a href="comcastProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($chaossUser) {
                echo '<a href="chaossProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($apacheUser) {
                echo '<a href="apacheProfile.php">Profile</a>';
                echo '<a href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
           ?>
       </div>
        
        <h1 id="pageTitle">Augur - Login Page</h1> 
        
        <!-- Main Wrapper -->
        <div id = "mainWrapper"> 
            <!-- Inner Wrapper -->
            <div id="innerWrapper">
                <!-- Text Wrapper -->
                <div id="textWrapper">
                <h3 id="welcomeLine">Please Enter Your Username &amp; Password Below:</h3>
                <form action="logHandle.php" method="POST">
                    <label for="userName" class="wikiEntry">Username:</label>
                    <input class="nameInput" type="text" id="userName" name="userName"><br>
                    <label for="passWord" class="wikiEntry">Password:</label>
                    <input id="passInput" type="password" id="passWord" name="passWord"><br>
                    <button type="submit" id="logButton" class="wikiEntry">Log-In</button>
                </form>    
                <h3 id="submitInfo">While you are logged in, you can access your info and view your stats.</h3>
                <h4>Logging in is only available for Repo Group Owners!</h4>
<!--                <img src="noelHype.gif" alt="Liam Logo Gif" id="loginGif">-->
                    <div id= "loginGif"> <div class="row">
                <nav class="col-sm-3" id="myScrollspy">
                    <ul class="nav nav-pills nav-stacked" id="sectionList">
                    </ul>
                </nav>
                <div class="col-sm-9" id="sectionBody">
            </div>
        </div>
        <div id="graph">
            <canvas id="canvas"></canvas>
        </div></div>
                </div>
                <div id="imagesWrapper">
                   <div id="logInDemoWrapper"><img src="logInDemo.jpg" alt="Successful Log-In">
                   <p id="clickNotify">This is what the logo in the navbar will look like when you ARE Logged-In!</p>
                   </div>
                   <div id="logOutDemoWrapper"><img src="logOutDemo.jpg" alt="Unsuccessful Log-In">
                   <p id="clickNotify">This is what the logo in the navbar will look like when you are NOT Logged-In!</p>
                   </div>
                </div>
            </div>
        </div>
    </body>  
</html>