searchBox = document.getElementById('searchBox')
searchBox.addEventListener("keypress", ale)
searchValue = ""

function ale(e){
	searchValue = searchBox.value
	
	if(e.keyCode === 13) {
		searchBox.value = ""
		var obj;
		fetch('/chat/'+searchValue)
  			.then(res => res.json())
  			.then(data => obj = data)
  			.then(function(){ 


  				chatListDiv = document.getElementById('chatList')
  				for(let i=0; i<Object.keys(obj).length; i++){

  					console.log(Object.values(obj)[i]['FirstName'])
  					searchResultsDiv = document.createElement('div')
  					searchResultsDiv.classList.toggle('searchResults')

  					pElement = document.createElement('p')
  					console.log(Object.keys(obj)[i]['FirstName'])
  					pElement.innerText = Object.values(obj)[i]['FirstName'] + " " + Object.values(obj)[i]['LastName']
  					if(i === 0){
  						pElement.classList.toggle('firstResult')
  					}
  					searchResultsDiv.appendChild(pElement)
  					chatListDiv.append(searchResultsDiv)
  				}

  				

  			})
  	}
	else{
		searchBox.innerHTML = ""
	}
}