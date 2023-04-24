function validate() {
    var field1 = document.getElementById("f1");
    var field2 = document.getElementById("f2");
    var field3 = document.getElementById("f3");
    var field4 = document.getElementById("f4");
    var field5 = document.getElementById("f5");
    var field6 = document.getElementById("f6");

    if (field1.value == "" || field2.value == "" || field3.value == "" || field4.value == "" || field5.value == "" || field6.value == "") {
        alert("Please enter all the values");
        //return false;
    }
    else {
        //true;
        window.location.href = "/predict.html";
    }
}

function redirectToForm1() {
    window.location.href = "form1.html";
}

function redirectToForm2() {
    window.location.href = "auth.html";
}

const predictBtn = document.getElementById('btn_predict');
const researchersBtn = document.getElementById('btn_predict1');
const naiveUsersBtn = document.getElementById('btn_predict2');

predictBtn.addEventListener('click', () => {
    researchersBtn.style.display = 'inline';
    naiveUsersBtn.style.display = 'inline';
    predictBtn.style.display = 'none'
});

const firebaseConfig = {
    apiKey: "AIzaSyDlP32poHuwa9xpGeSibDh3CvlwRQRD9ZM",
    authDomain: "contactform-b1ceb.firebaseapp.com",
    databaseURL: "https://contactform-b1ceb-default-rtdb.firebaseio.com",
    projectId: "contactform-b1ceb",
    storageBucket: "contactform-b1ceb.appspot.com",
    messagingSenderId: "329378688876",
    appId: "1:329378688876:web:415cd238f92abc5c210d49"
};

// initialize firebase
firebase.initializeApp(firebaseConfig);

// reference your database
var contactFormDB = firebase.database().ref("contactForm");

document.getElementById("contactForm").addEventListener("submit", submitForm);

function submitForm(e) {
    e.preventDefault();

    var name = getElementVal("name");
    var emailid = getElementVal("emailid");
    var msgContent = getElementVal("msgContent");

    // console.log(name, emailid, msgContent);
    saveMessages(name, emailid, msgContent);

    //   enable alert
    document.querySelector(".alert").style.display = "block";

    //   remove the alert
    setTimeout(() => {
        document.querySelector(".alert").style.display = "none";
    }, 3000);

    //   reset the form
    document.getElementById("contactForm").reset();
}

const saveMessages = (name, emailid, msgContent) => {
    var newContactForm = contactFormDB.push();

    newContactForm.set({
        name: name,
        emailid: emailid,
        msgContent: msgContent,
    });
};

const getElementVal = (id) => {
    return document.getElementById(id).value;
};

function validate_contact() {
    var field1 = document.getElementById("name");
    var field2 = document.getElementById("emailid");
    var field3 = document.getElementById("msgContent");

    if (field1.value == "" || field2.value == "" || field3.value == "") {
        alert("Please enter all the values");
        return false;
    }
    else{
        alert("Your Message was sent!")
    }
}

// var slider = document.getElementById("f2");
// var output = document.getElementById("value");

// output.innerHTML = slider.value;

// slider.output = function(){
//     output.innerHTML = this.value;
// }

// slider.addEventListener("input", function(){
//     var x = slider.value;
//     var color = 'linear-gradient(90deg, brown' + x+ '%, white' + x + '%)'
//     slider.style.background = color;
// })

