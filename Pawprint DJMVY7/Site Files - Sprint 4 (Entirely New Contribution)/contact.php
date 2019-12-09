<!DOCTYPE html>
<html lang="en">
    <head>       
      <title>Augur: Under Construction</title> 
        <meta charset="utf-8">
          <link href="https://fonts.googleapis.com/css?family=Lora|Encode+Sans+Condensed" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="stylesheet.css">
                    <script src="djmvy7FinalJS.js"></script> 
                        <script src="https://code.jquery.com/jquery-3.4.0.min.js" integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg=" crossorigin="anonymous"></script>
                        <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.min.js" integrity="sha256-VazP97ZCwtekAsvgPBSUwPFKdrwD3unUfSGVYrahUqU=" crossorigin="anonymous"></script>

        <!-- jQuery library -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

        <!-- Latest compiled JavaScript -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://www.chartjs.org/dist/2.8.0/Chart.min.js"></script>
        <script src="home.js"></script>
    </head>
    
    <body id="aboutBody" onload="getRepoGroupInfo()">    
        <div class="navbar">
            <a href="index.php">Home</a>
            <a href="about.php">About</a>
            <a href="contact.php" class="active">Contact</a>
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
                echo '<a href="graphQLProfile.php">Profile</a>';
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
        
        <h1 id="pageTitle">Augur - Contact (Sprint 4)</h1> 
        
         <!-- Main Wrapper -->
        <div id = "mainWrapper"> 
            <!-- Inner Wrapper -->
            <div id="constructWrapper">
                <p><img src="constructPic.jpg"></p>
            </div>
        </div>
    </body>  
</html>