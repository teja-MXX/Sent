/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

// EDIT BUTTON
editButton = document.getElementById('editImage')
editButton.addEventListener('click', function(){
  
})

// DELETE PHOTO
deleteButton = document.getElementById('deleteButton')
deleteButton.addEventListener('click', function(){
  var confirmation = prompt("Type DELETE to delete the photo")
  if(confirmation == 'DELETE'){
    URL = document.URL.split("/")[4] + "/delete"
    fetch(URL)  
  }
  window.location.href='/'
})

// LIKES UPDATED
likeButton = document.getElementById('likeDiv')
likeButton.addEventListener('click', function(){
  URL = document.URL.split("/")[4] + "/updateLikes"
  fetch(URL)
  window.location.reload()
  window.location.reload()
  window.location.reload()
})


// GOING TO PROFILE OF THE USERS WHO LIKED THE PHOTO
likedUser = document.querySelector('.fUser')
var userName = likedUser.innerText
var locationn = "'/profile/" + userName +"'"
likedUser.setAttribute('onclick', `location.href=${locationn}`)
