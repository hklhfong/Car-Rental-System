// This function is used for the message button
// Begin
function openMenu() {
						document.getElementById("menu").style.width = "150px";
					}

function closeMenu() {
						document.getElementById("menu").style.width = "0";
					}
//End

// This function is used for the first dropdown list
// Begin
function dropdownOne() {
    document.getElementById("dropdown-list").classList.toggle("show");
}
//End

// This function is used for the second dropdown list
// Begin
function dropdownTwo() {
    document.getElementById("dropdown-list-two").classList.toggle("show");
}
//End

// This function is used for the third dropdown list
// Begin
function dropdownThree() {
    document.getElementById("dropdown-list-three").classList.toggle("show");
}
//End

// This function is used for the fourth dropdown list
// Begin
function dropdownFour() {
    document.getElementById("dropdown-list-four").classList.toggle("show");
}
//End

// This function is used for the fifth dropdown list
// Begin
function dropdownFive() {
    document.getElementById("dropdown-list-five").classList.toggle("show");
}
//End

// This function is used for close the dropdown list when user click outside
// Begin
window.onclick = function(event) {
  if (!event.target.matches('.dropdown-button')) {

    var dropdownList = document.getElementsByClassName("dropdown-list-content");
    var i;
    for (i = 0; i < dropdownList.length; i++) {
      var dropdown_open = dropdownList[i];
      if (dropdown_open.classList.contains('show')) {
        dropdown_open.classList.remove('show');
      }
    }
  }
}
//End

