<?php
if(isset($_POST['upload'])){
    $target_dir = "uploads/";
    $target_file = $target_dir . 
basename($_FILES["fileToUpload"]["name"]);
    $uploadOk = 1;
    $imageFileType = 
strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

    if(isset($_FILES["fileToUpload"])){
        $uploadOk = 1;
    }

    if ($_FILES["fileToUpload"]["size"] > 500000) {
        echo "Sorry, your file is too large.";
        $uploadOk = 0;
    }

    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    } else {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], 
$target_file)) {
            echo "The file ". basename( $_FILES["fileToUpload"]["name"]). 
" has been uploaded to /uploads/";
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }
}
?>

