function showAlert(){
    alert("JavaScript Alert Working!");
}
function changeText(){
    document.getElementById("heading").innerHTML="Text Changed!";
}
function calc(){
    var a=parseFloat(document.getElementById("n1").value);
    var b=parseFloat(document.getElementById("n2").value);

    if(isNaN(a)||isNaN(b)){
        document.getElementById("ans").innerHTML="Enter numbers";
        return;
    }

    document.getElementById("ans").innerHTML="Result: "+(a+b);
}
function validate(){
    var name=document.getElementById("name").value;
    var email=document.getElementById("email").value;
    var pass=document.getElementById("pass").value;

    if(name==""||email==""||pass==""){
        document.getElementById("msg").innerHTML="All fields required!";
        return false;
    }

    if(pass.length<6){
        document.getElementById("msg").innerHTML="Password must be 6+ characters";
        return false;
    }

    alert("Form Submitted Successfully!");
    return true;
}