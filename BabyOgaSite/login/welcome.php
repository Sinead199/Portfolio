<?php
// Initialize the session
session_start();
 
// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login/login.php");
    exit;
}
?>
 
 <!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Baby Óga - Yoga and Massage</title>

  <!-- Bootstrap core CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

  <!-- Custom styles for this template -->
  <link href="../css/custom.css" rel="stylesheet">

</head>

<body>

   <!-- Navigation -->
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <img class="navbar-logo" href="index.html" src="../img/logov1.png"></img>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="../index.html">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownPortfolio" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Courses
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownPortfolio">
              <a class="dropdown-item" href="../info.html">Yoga and Massage</a>
              <a class="dropdown-item" href="../pricing.html">Pricing and Booking</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="../contact.html">Contact</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownPortfolio" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Login
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownPortfolio">
              <a class="dropdown-item" href="login.php">Login</a>
              <a class="dropdown-item" href="register.php">Register</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
    <br>
    <!-- Page Heading/Breadcrumbs -->
    <h1 class="mt-5 mb-3">Welcome
      <small>Options</small>
    </h1>

    <ol class="breadcrumb">
      <li class="breadcrumb-item">
        <a href="index.html">Home</a>
      </li>
      <li class="breadcrumb-item active">Welcome</li>
    </ol>

    <div class="scallop-up"></div><!-- Divider -->

    <div class="row">
    <div class="col-lg-12">
      <div class="page-header">
          <h1 class="my-4">Hi, <b><?php echo htmlspecialchars($_SESSION["username"]); ?></b>.<br>Thank you for registering!</h1> 
      </div>
    </div>
    </div> 

    <div class="scallop-down"></div><!-- Divider -->

    <div class="scallop-up"></div><!-- Divider -->

    <div class="row">
      <div class="col-lg-12">
        <h1 class="my-4">Choose what you'd like to do next.</h1>
        <br>

        <div class="btn-group btn-group-justified">
          <a href="../requestbooking.php" class="btn btn-primary">Request a Booking</a>
          <a href="reset.php" class="btn btn-primary">Change Your Password</a>
          <a href="#logOut" class="btn btn-primary" data-toggle="modal">Sign Out of Your Account</a>
        </div>
      </div>
    </div>

    <!-- Logout Modal HTML -->
    <div id="logOut" class="modal fade">
          <div class="modal-dialog modal-confirm">
            <div class="modal-content">
              <div class="modal-header">
                <!-- <div class="icon-box">
                  <i class="material-icons">&#xE876;</i>
                </div>				 -->
                <h4 class="modal-title">Bye!</h4>	
              </div>
              <div class="modal-body">
                <p class="text-center">You have been succesfully logged out!</p>
              </div>
              <div class="modal-footer">
                <a class="btn btn-primary btn-block" href="logout.php">OK</a>
              </div>
            </div>
          </div>
        </div>

    <div class="scallop-down"></div><!-- Divider --> 

    
  </div>
   <!-- /.container -->

  <!-- Footer -->
  <footer class="py-5 bg-dark">
    <div class="container">
      <p class="m-0 text-center text-white">Copyright &copy; Baby Óga 2020</p>
    </div>
    <!-- /.container -->
  </footer>

  <!-- Bootstrap core JavaScript -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

</body>
</html>