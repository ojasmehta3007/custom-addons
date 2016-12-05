function myFunction() {

    var inpObj = document.getElementById("phone");
    if (inpObj.checkValidity() == false) {
        document.getElementById("phone_msg").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("phone_msg").innerHTML = "Ok";
    }
//    var phoneno = /^\d{10}$/;
//    var phone = document.getElementById('phone').value;
//    alert("Phone no is ",phone);
//    if (val.match(phoneno))) {
//        document.getElementById("phone_msg").innerHTML = "Ok";
//    } else {
//        document.getElementById("phone_msg").innerHTML =  "Enter 10 digit Phone Number";
//        document.getElementById("phone").focus()
//        return false
//    }

//    if (isNumeric(phone)) //check only numbers. Same code for FaxNo.
//            alert("Correct");
//            document.getElementById("phone_msg").innerHTML = "Ok";
//        else {
//            alert("invalid");
//            document.getElementById("phone_msg").innerHTML =  "Enter 10 digit Phone Number";
//            document.getElementById("phone").focus()
//            return false;
//        }

    var pass = document.getElementById("pass").value;
    var cpass = document.getElementById("cpass").value;
    console.log("password >...........",pass,typeof pass)
    if(pass == cpass)
    {
        document.getElementById("cpass_msg").innerHTML =  "Matched";
    }
    else
    {
        document.getElementById("cpass_msg").innerHTML =  "Not Matched";
        document.getElementById("cpass").focus()
        return false;
    }

}
