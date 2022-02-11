function seller_validate_form() {
    alert('asdfgfdssdf');

    let seller_phone = document.forms["sellerSignForm"]["sellerInputNumber"].value;
    let seller_mail = document.forms["sellerSignForm"]["email"].value;
    let seller_pass1 = document.forms["sellerSignForm"]["password_first"].value;
    let seller_pass2 = document.forms["sellerSignForm"]["password_conf"].value;
    let mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var phoneno = /^\d{10}$/;
    console.log(seller_phone)

    // mobile no validation
    if (seller_phone == "") {
        document.getElementById("label1").style.color = "#ff0000";
        document.getElementById("n1").style.borderColor = "#ff0000";
        document.getElementById("label1").innerHTML = 'Mobile no must be filled out';
        return false;
    } else if (seller_phone.match(phoneno)) {
        document.getElementById("label1").innerHTML = '';
        document.getElementById("n1").style.borderColor = "black";
    } else {
        document.getElementById("label1").style.color = "#ff0000";
        document.getElementById("n1").style.borderColor = "#ff0000";
        document.getElementById("label1").innerHTML = 'Enter a valid mobile no';
        return false;
    }

    // //  email validation
    if (seller_mail == "") {
        document.getElementById("label2").style.color = "#ff0000";
        document.getElementById("Email1").style.borderColor = "#ff0000";
        document.getElementById("label2").innerHTML = 'Email must be filled out';
        return false;
    } else if (seller_mail.match(mailformat)) {
        document.getElementById("label2").innerHTML = '';
        document.getElementById("Email1").style.borderColor = "black";
    } else {
        document.getElementById("label2").style.color = "#ff0000";
        document.getElementById("Email1").style.borderColor = "#ff0000";
        document.getElementById("label2").innerHTML = 'Enetr a valid Email  ';
    }

    //password validation
    if (seller_pass1 == "") {
        document.getElementById("label3").style.color = "#ff0000";
        document.getElementById("pass1").style.borderColor = "#ff0000";
        document.getElementById("label3").innerHTML = 'Password must filled out';
        return false;
    } else if (seller_pass1.length < 6) {
        document.getElementById("label3").style.color = "#ff0000";
        document.getElementById("label3").innerHTML = 'Password must be 6 charachters';
        return false;
    } else {
        document.getElementById("label3").innerHTML = '';
        document.getElementById("pass1").style.borderColor = "black";
    }

    //confirm password validation
    if (seller_pass2 != seller_pass1) {
        document.getElementById("label4").style.color = "#ff0000";
        document.getElementById("pass2").style.borderColor = "#ff0000";
        document.getElementById("label4").innerHTML = 'Password must be same';
        return false;
    } else {
        document.getElementById("label4").innerHTML = '';
        document.getElementById("pass2").style.borderColor = "black";
    }
}

//return in place holder----
// document.getElementsByName("username")[0].placeholder = 'Username must be filled out';