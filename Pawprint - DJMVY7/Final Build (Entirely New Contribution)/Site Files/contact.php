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
    
    <body id="contactBody">    
        <div class="navbar">
            <a href="index.php">Home</a>
            <a href="about.php">About</a>
            <a href="contact.php" class="active">Contact</a>
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
        
        <h1 id="pageTitle">Augur - Contact</h1> 
        
        <!-- Main Wrapper -->
         <div id = "bandMainWrapper"> 
            <!-- Inner Wrapper -->
            <div id="innerWrapper">
                <!-- Greeting Wrapper -->
                <div id="greetWrapper"><p id="greetLine">Ways To Contact Us:</p></div>
                <!-- Dom Wrapper -->
                <div id="liamWrapper">
                    <!-- Liam Picture Wrapper -->    
                    <div id="liamPicWrapper"><img src="liveChat.jpg" alt="Dominic" id="liamBioPic"></div>
                    <!-- Liam Text Wrapper -->
                    <div id="liamBioText">
                        <p id="introLine">Go To Our Live Chat For Support!</p>
                    </div>
                </div>
                <!-- Derek Wrapper -->
                <div id="noelWrapper">
                    <!-- Noel Picture Wrapper -->
                    <div id="noelPicWrapper"><img src="facebookLogo.jpg" alt="Derek" id="noelBioPic"></div>
                    <!-- Noel Text Wrapper -->
                    <div id="noelBioText">
                        <p id="introLine">Find us on Facebook @Augur!</p>
                    </div>
                </div>
                <!-- Martian Wrapper -->
                <div id="gemWrapper">
                    <!-- Gem Picture Wrapper -->
                    <div id="gemPicWrapper"><img src="twitterLogo.png" alt="Martian" id="gemBioPic"></div>
                    <!-- Gem Text Wrapper -->
                    <div id="gemBioText">
                        <p id="introLine">Find us on Twitter @Augur!</p>
                    </div>
                </div>
                <!-- Jess Wrapper -->
                <div id="andyWrapper">
                    <!-- Andy Picture Wrapper -->
                    <div id="andyPicWrapper"><img src="phoneLogo.png" alt="Jessica" id="andyBioPic"></div>
                    <!-- Andy Text Wrapper -->
                    <div id="andyBioText">
                        <p id="introLine">Call us at 573-867-5309!</p>
                    </div>
                </div>
            </div>
        </div>
    </body>  
</html>