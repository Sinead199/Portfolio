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

  <link href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

  <!-- Custom styles for this template -->
  <link href="css/custom.css" rel="stylesheet">

  <!-- Bootstrap core JavaScript -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

</head>

<body>

  <!-- Navigation -->
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark bg-dark fixed-top">
    <div class="container">
      <img class="navbar-logo" href="index.html" src="img/logov1.png"></img>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="index.html">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownPortfolio" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Courses
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownPortfolio">
              <a class="dropdown-item" href="info.html">Yoga and Massage</a>
              <a class="dropdown-item" href="pricing.html">Pricing and Booking</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="contact.html">Contact</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownPortfolio" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Login
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownPortfolio">
              <a class="dropdown-item" href="login/login.php">Login</a>
              <a class="dropdown-item" href="login/register.php">Register</a>
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
    <h1 class="mt-5 mb-3">Booking
      <small>Request an appointment</small>
    </h1>

    <ol class="breadcrumb">
      <li class="breadcrumb-item">
        <a href="index.html">Home</a>
      </li>
      <li class="breadcrumb-item active">Booking</li>
    </ol>

    <div class="scallop-up"></div><!-- Divider --> 

    <div class="row">
      <div class="col-lg-12">
        <h1 class="my-4">Request booking</h1>
        <br>

        <form action="requestbooking.php" method="post">
            <p>
                <label for="FNAME">First name:</label>
                <input type="text" name="FNAME" id="FNAME" class="form-control">
                <span class="help-block"></span>
            </p>

            <p>
                <label for="SNAME">Surname:</label>
                <input type="text" name="SNAME" id="SNAME" class="form-control">
                <span class="help-block"></span>
            </p>

            <p>
                <label for="EMAIL">Email:</label>
                <input type="email" name="EMAIL" id="EMAIL" class="form-control">
                <span class="help-block"></span>
            </p>
            
            <p>
                <label for="PHONE_NUM">Phone number:</label>
                <input type="number" name="PHONE_NUM" id="PHONE_NUM" class="form-control">
                <span class="help-block"></span>
            </p>
            
          
              <!-- Button HTML (to Trigger Modal) -->
              <input type ="submit" class="btn btn-primary" data-toggle="modal" id="submit" name="submit" value="Submit">
              <!-- <a href="#myModal" class="trigger-btn" data-toggle="modal">Click to Open Confirm Modal</a> -->
              <br>
        </form>
      </div>
    </div>

    <!-- Accept HTML -->
    <div id="myModal" class="modal fade">
          <div class="modal-dialog modal-confirm">
            <div class="modal-content">
              <div class="modal-header">
                <!-- <div class="icon-box">
                  <i class="material-icons">&#xE876;</i>
                </div>				 -->
                <h4 class="modal-title">Awesome!</h4>	
              </div>
              <div class="modal-body">
                <p class="text-center">Your booking has been confirmed. Check your email for updates.</p>
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary btn-block" data-dismiss="modal">OK</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Reject HTML -->
    <div id="emailAlert" class="modal fade">
          <div class="modal-dialog modal-confirm">
            <div class="modal-content">
              <div class="modal-header">
                <!-- <div class="icon-box">
                  <i class="material-icons">&#xE876;</i>
                </div>				 -->
                <h4 class="modal-title">Field empty</h4>	
              </div>
              <div class="modal-body">
                <p class="text-center">You must enter values for all fields. Please re-enter.</p>
              </div>
              <div class="modal-footer">
                <button class="btn btn-primary btn-block" data-dismiss="modal">OK</button>
              </div>
            </div>
          </div>
        </div>

    <?php

    //Connect to database
    include 'connect/config.php';

    // Check if the user has submitted data into the form
    if (isset ($_POST ['submit'])){
        $FNAME = $_POST ['FNAME'];
        $SNAME = $_POST['SNAME'];
        $EMAIL = $_POST['EMAIL'];
        $PHONE_NUM = $_POST ['PHONE_NUM'];
        
        //Check if all fields have been entered
        if ($FNAME && $SNAME && $EMAIL && $PHONE_NUM){
        
            // Check if that mechanic exists
            mysqli_query ($link, "INSERT INTO APP_REQUEST (FNAME, SNAME, EMAIL, PHONE_NUM) VALUES ('$FNAME', '$SNAME', '$EMAIL', '$PHONE_NUM')");
            
            // Update the firstname field in the Mechanic table
            if (mysqli_affected_rows($link)>0){
              echo "<script type='text/javascript'>
              $(document).ready(function(){
              $('#myModal').modal('show');
              });
              </script>";
                // echo "Your appointment request has been sent.";
                //Select * from booking to display table
            } else{
                echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
            }
        }
        else {
          echo "<script type='text/javascript'>
          $(document).ready(function(){
          $('#emailAlert').modal('show');
          });
          </script>";   
                }
    }

    //close connection
    mysqli_close($link);
    ?>

      <div class="scallop-down"></div><!-- Divider --> 

    </div>
    <!-- /.container -->

    <br>
  <!-- Footer -->
  <footer class="py-5 bg-dark">
    <div class="container">
      <p class="m-0 text-center text-white">Copyright &copy; Baby Óga 2020</p>
    </div>
    <!-- /.container -->
  </footer>

  
</body>
</html>