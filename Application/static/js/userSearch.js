
// USER SEARCH

searchBox = document.getElementById('searchBox')
searchBox.addEventListener("keypress", ale)
searchValue = ""

function ale(e){
	searchValue = searchBox.value
	
	if(e.keyCode === 13) {
		searchBox.value = ""

  	}
	else{
		chatListDiv = document.getElementById('chatLIST')
		chatListDiv.innerHTML = ""
		var obj;
		fetch('/chat/'+searchValue + e.key)
  			.then(res => res.json())
  			.then(data => obj = data)
  			.then(function(){ 
  				for(let i=0; i<Object.keys(obj).length; i++){
  					searchResultsDiv = document.createElement('div')
  					searchResultsDiv.classList.toggle('searchResults')

  					pElement = document.createElement('p')
  					pElement.innerText = Object.values(obj)[i]['FirstName'] + " " + Object.values(obj)[i]['LastName']
  					if(i === 0){
  						pElement.classList.toggle('firstResult')
  					}
  					searchResultsDiv.appendChild(pElement)
  					chatListDiv.append(searchResultsDiv)

  					// Chat Select on clicking on Search Result
  					searchResultss = document.querySelector(".searchResults")
					UserFullName = document.getElementById('UserFullName')
					searchResultss.addEventListener('click', function(){
						UserFullName.innerText = searchResultss.firstChild.innerText
						searchBox.value = ""
						chatListDiv.innerHTML = ""
						msgInputDiv = document.getElementById('msgInputDiv')
						msgInputDiv.style.opacity = 1
						chatAreaIcon = document.getElementById('chatAreaIcon')
						chatAreaIcon.remove()
						chatAreaHeading = document.getElementById('chatAreaHeading')
						chatAreaHeading.remove()
					})
  				}
  			})
	}
}

// SOCK INITIALIZATION
var socket = io();
socket.on('connect', function(){
	console.log(socket.id)
	socket.emit('socketidFromJsPython', {"sockID" : socket.id})
})



// CHAT SENT
msgInput = document.getElementById('msgInput')
msgInput.addEventListener('keydown', function(e){
	
	if(e.key == "Enter"){
		from = document.getElementById('profile').firstElementChild.innerText
		to = document.getElementById('UserFullName').innerText
		data = {"from" : from, 
				"to" : to, 
				"msg" : this.value,
				"sockId" : socket.id}
		socket.emit('msgFromJsPython', data)
		this.value = ""
	}
})


socket.on('msgFromPythonJs', function(data){
	chatAreaDiv = document.getElementById('chatArea')
	p = document.createElement('p')
	p.classList.toggle('msgs')
	chatUserName = document.createElement('span')
	chatUserName.classList.toggle('chatUserName')
	if(data.sockId != socket.id){
		p.classList.toggle('receivedMsg')
		chatUserName.innerText = data['from'] + " :    " + data['msg']	
	}
	else{
		chatUserName.innerText = "You" + " :    " + data['msg']
	}

	time = document.createElement('sub')
	time.classList.toggle('time')
	time.innerText = "     " + data['time']
	p.appendChild(chatUserName)
	p.appendChild(time)
	
	// msgInput.remove()
	msgInputDiv = document.getElementById('msgInputDiv')
	chatAreaDiv.insertBefore(p, msgInputDiv)
	chatAreaDiv.scrollBy(0, chatAreaDiv.scrollHeight)


})