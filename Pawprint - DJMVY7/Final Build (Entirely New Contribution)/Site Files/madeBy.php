<!DOCTYPE html>
<html lang="en">
    <head>       
      <title>Augur: Made By</title> 
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
    </head>
    
    <body id="madeByBody" onload="getRepoGroupInfo()">    
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
              echo '<a class="active" href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
              echo '<button class="dropbtn"><img src="logOutNavbar.jpg"></button>';
              echo '<div class="dropdown-content"><a href="logIn.php">Login</a></div>'; 
              echo '</div>';
            }
            else if ($graphUser) {
                echo '<a href="graphQLProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($zephyrUser) {
                echo '<a href="zephyrProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
             else if ($mhsUser) {
                echo '<a href="mhsProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($netflixUser) {
                echo '<a href="netflixProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($railsUser) {
                echo '<a href="railsProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($comcastUser) {
                echo '<a href="comcastProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($chaossUser) {
                echo '<a href="chaossProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
            else if ($apacheUser) {
                echo '<a href="apacheProfile.php">Profile</a>';
                echo '<a class="active href="madeBy.php">Made By</a>';
            echo '<div class="dropdown">';
                echo '<button class="dropbtn"><img src="logInNavbar.jpg"></button>';
                echo '<div class="dropdown-content"><a href="logOut.php">Logout</a></div>';
                echo '</div>';
            }
           ?>
       </div>
        
        <h1 id="bhnPageTitle">Augur - Made By</h1> 
        
         <!-- Main Wrapper -->
         <div id = "bandMainWrapper"> 
            <!-- Inner Wrapper -->
            <div id="innerWrapper">
                <!-- Greeting Wrapper -->
                <div id="greetWrapper"><p id="greetLine">This Site Was Made By:</p></div>
                <!-- Dom Wrapper -->
                <div id="liamWrapper">
                    <!-- Liam Picture Wrapper -->    
                    <div id="liamPicWrapper"><img src="dom.jpg" alt="Dominic" id="liamBioPic"></div>
                    <!-- Liam Text Wrapper -->
                    <div id="liamBioText">
                        <p id="introLine">Dominic Mantro</p>
                    </div>
                </div>
                <!-- Derek Wrapper -->
                <div id="noelWrapper">
                    <!-- Noel Picture Wrapper -->
                    <div id="noelPicWrapper"><img src="derek.jpg" alt="Derek" id="noelBioPic"></div>
                    <!-- Noel Text Wrapper -->
                    <div id="noelBioText">
                        <p id="introLine">Derek Rechtien</p>
                    </div>
                </div>
                <!-- Martian Wrapper -->
                <div id="gemWrapper">
                    <!-- Gem Picture Wrapper -->
                    <div id="gemPicWrapper"><img src="martian.jpg" alt="Martian" id="gemBioPic"></div>
                    <!-- Gem Text Wrapper -->
                    <div id="gemBioText">
                        <p id="introLine">Martian Lapadatescu</p>
                    </div>
                </div>
                <!-- Jess Wrapper -->
                <div id="andyWrapper">
                    <!-- Andy Picture Wrapper -->
                    <div id="andyPicWrapper"><img src="jessica.jpg" alt="Jessica" id="andyBioPic"></div>
                    <!-- Andy Text Wrapper -->
                    <div id="andyBioText">
                        <p id="introLine">Jessica Dean</p>
                    </div>
                </div>
            </div>
        </div>
    </body>  
</html>