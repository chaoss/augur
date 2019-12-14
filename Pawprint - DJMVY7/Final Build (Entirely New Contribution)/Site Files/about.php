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
    
    <body id="aboutBody">    
        <div class="navbar">
            <a href="index.php">Home</a>
            <a href="about.php" class="active">About</a>
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
        
        <h1 id="pageTitle">Augur - About Us</h1> 
        
       <!-- Main Wrapper -->
        <div id = "mainWrapper"> 
            <!-- Inner Wrapper -->
            <div id="innerWrapper">
                <!-- Text Wrapper -->
                <div id="textWrapper">
                <h3 id="welcomeLine">We Are Augur And We Hope That You Enjoy Your Time On Our Site!</h3>
                <h4>A Part Of The CHAOSS Community</h4>
                <p class="bonusInterview">More Information:</p>
                <p class="wikiEntry" id="interviewIntro">This site works as a login service for heads of the repo groups in our system. Below are some of our groups.</p>
                       
                <p class="wikiEntry" id="closingParagraph">Netflix - Netflix, Inc. is an American media-services provider and production company headquartered in Los Gatos, California, founded in 1997 by Reed Hastings and Marc Randolph in Scotts Valley, California. The company's primary business is its subscription-based streaming service which offers online streaming of a library of films and television programs, including those produced in-house. As of April 2019, Netflix had over 148 million paid subscriptions worldwide, including 60 million in the United States, and over 154 million subscriptions total including free trials.</p>
                    
                <p class="wikiEntry" id="closingParagraph">Comcast - Comcast Corporation (formerly registered as Comcast Holdings) is an American telecommunications conglomerate headquartered in Philadelphia, Pennsylvania. It is the second-largest broadcasting and cable television company in the world by revenue and the largest pay-TV company, the largest cable TV company and largest home Internet service provider in the United States, and the nation's third-largest home telephone service provider.</p>
                    
                <p class="wikiEntry" id="closingParagraph">MHS - Game Based Learning for Next Generation Science Learning. Mission HydroSci (MHS) is a game-based virtual learning environment that brings innovative game design to middle school science education. Teachers use MHS because it is highly engaging for their students, builds and integrates knowledge about water systems with competencies in scientific argumentation, and fosters an interest in science and science practices.</p>
                
                <p class="wikiEntry" id="closingParagraph">GraphQL - GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data. GraphQL was developed internally by Facebook in 2012 before being publicly released in 2015. On 7 November 2018, the GraphQL project was moved from Facebook to the newly-established GraphQL Foundation, hosted by the non-profit Linux Foundation.</p>
                </div>
                 
                <!-- Images Wrapper -->
                <div id="imagesWrapper">
                   <!-- Video Wrapper -->
                   <div id="albumVideoWrapper"><iframe width="500" height="282" src="https://www.youtube.com/embed/SHyGwKSz5B0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="albumCover"></iframe></div>
                   <!-- Album Cover Wrapper -->
                   <div id="albumWrapper"><img src="augurLogo2.png" alt="Augur Logo" class="albumCover"></div>
                </div>
           </div>
        </div>
    </body>  
</html>