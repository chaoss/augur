<!DOCTYPE html>
<html lang="en">
    <head>       
      <title>Augur: Home</title> 
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
    
    <body id="indexBody" onload="getRepoGroupInfo()">    
        <div class="navbar">
            <a class="active" href="index.php">Home</a>
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
        
        <h1 id="pageTitle">Augur - Home</h1> 
        
        <!-- Main Wrapper -->
        <div id = "mainWrapper"> 
            <!-- Inner Wrapper -->
            <div id="innerWrapper">
                <!-- Text Wrapper -->
                <div id="indexTextWrapper">
                <h3 id="welcomeLine">Welcome To Augur! If You Are A Repo Group Owner, Feel Free To Login.</h3>
                <p class="wikiEntry" id="openingParagraphIndex">Augur is a Python library and web service of Open Source Software Health and Sustainability metrics and data collection. Augur can be directly accessed at http://augur.osshealth.io/.</p>
                <div id="indexChartWrapper">
                    <div class="row">
                        <nav class="col-sm-3" id="myScrollspy">
                            <ul class="nav nav-pills nav-stacked" id="sectionList">
                            </ul>
                        </nav>
                        <div class="col-sm-9" id="sectionBody"></div>
                    </div>
                    <canvas id="canvas"></canvas>
                </div>
                </div> 
                <div id="secondaryWrapper">
                   <div id="otherFunctionWrapper"><iframe width="500" height="282" src="https://www.youtube.com/embed/bqoTwf5Pds0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="albumCover"></iframe></div>
                   <div id="logoWrapper"><a href="logIn.php"><img src="augurLogo.png" alt="Augur Logo" class="albumCover"></a>
                   <p id="clickNotify">Click the logo to be taken to the login page!</p>
                   </div>
                </div>
            </div>
        </div>
    </body>  
</html>