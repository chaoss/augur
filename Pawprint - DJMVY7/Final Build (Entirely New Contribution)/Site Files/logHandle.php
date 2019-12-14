<?php  
    $userName = $_POST['userName'] ? $_POST['userName'] : null;
    $passWord = $_POST['passWord'] ? $_POST['passWord'] : null;
            
    if ($userName == 'graph' && $passWord == 'pass') {
        setcookie('graph', $userName);
        header('Location: index.php');
        exit;
    }
    else if ($userName == 'zephyr' && $passWord == 'pass') {
        setcookie('zephyr', $userName);
        header('Location: index.php');
        exit;
    }
    else if ($userName == 'mhs' && $passWord == 'pass') {
        setcookie('mhs', $userName);
        header('Location: index.php');
        exit;
    }
    else if ($userName == 'netflix' && $passWord == 'pass') {
        setcookie('netflix', $userName);
        header('Location: index.php');
        exit;
    } 
    else if ($userName == 'rails' && $passWord == 'pass') {
        setcookie('rails', $userName);
        header('Location: index.php');
        exit;
    } 
    else if ($userName == 'comcast' && $passWord == 'pass') {
        setcookie('comcast', $userName);
        header('Location: index.php');
        exit;
    } 
    else if ($userName == 'chaoss' && $passWord == 'pass') {
        setcookie('chaoss', $userName);
        header('Location: index.php');
        exit;
    } 
    else if ($userName == 'apache' && $passWord == 'pass') {
        setcookie('apache', $userName);
        header('Location: index.php');
        exit;
    } 
    else {
        require('logIn.php');
        $wrongInfo = "Sorry! The username or password you have entered is incorrect. Please try again.";
        echo "<script type='text/javascript'>alert('$wrongInfo');</script>";
        exit;
    }
?>