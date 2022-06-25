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

// ENABLING INPUT COMMENT DIV
commentDiv = document.querySelectorAll("#commentDiv , .replyButton")
var j;
for(j=0; j<commentDiv.length; j++){
  commentDiv[j].addEventListener('click', function(){
  photoCommentDiv = document.getElementById('photoCommentsDiv')
  photoCommentDiv.style.height = '52vh'
  commentInputDiv = document.getElementById('commentInputDiv')
  commentInputDiv.style.visibility = 'visible' 
})  
}

// ADDING Comment PLACEHOLDER TO commentInput when clicked on Comment Button
commentButton = document.getElementById('commentDiv')
commentButton.addEventListener('click', function(){
  if(commentInput.placeholder[0] == "R"){
    commentInput.placeholder = "Comment " + commentInput.placeholder.slice(6)
  }
  else if(commentInput.placeholder[0] != "C"){
    commentInput.placeholder = "Comment as " + commentInput.placeholder
  }
})

// ADDING REPLY PLACEHOLDER TO commentInput when clicked on Reply Button
replyButton = document.querySelectorAll('.replyButton')
var r;
for(r=0; r<replyButton.length; r++){
  replyButton[r].addEventListener('click', function(){
    commentId = this.parentElement.previousElementSibling.id
    URL = document.URL.split("/")[4] + "/reply/" + commentId +"/"
    commentInput = document.getElementById('commentInput')
    if(commentInput.placeholder[0] == "C"){
      commentInput.placeholder = "Reply " + commentInput.placeholder.slice(8)  
    }   
    else if(commentInput.placeholder[0] != "R"){
      commentInput.placeholder = "Reply as " + commentInput.placeholder
    }
  })
}

// SENDING COMMENT/REPLY TO SERVER
commentInput = document.getElementById('commentInput')
commentInput.addEventListener('keypress', function(e){
  if(e.key == "Enter"){
    
    if(commentInput.placeholder[0] == "R"){
      uname = commentInput.placeholder.slice(9)
      
    }
    else{
      uname = commentInput.placeholder.slice(11)
      URL = document.URL.split("/")[4] + "/comment/"
    }

    comment = uname + " : " + this.value
    URL = URL + comment
    fetch(URL)
    window.location.reload()
    window.location.reload()
    window.location.reload()
    window.location.reload()
    window.location.reload()
  }
})

// DISABLING COMMENT INPUT DIV
deleteInput = document.getElementById('deleteInputIcon')
deleteInput.addEventListener('click', function(){
  commentInputDiv = document.getElementById('commentInputDiv')
  commentInputDiv.style.visibility = 'hidden'
  window.location.reload()
})