requestIcon = document.querySelectorAll('.requestIcon')
var a
for(a=0; a<requestIcon.length; a++){
	requestIcon[a].addEventListener('click', function(){
		to = this.parentElement.parentElement.parentElement.getAttribute('onclick').split("/")[2].slice(0,-2)
		from = document.getElementById('profile').innerText
		//getAttribut('onclick')
		alert(to)
		URL = 'addFriend/'+from+'/'+to
		fetch(URL)
	})
}

// UPDATE REQUEST
requestButtons = document.querySelectorAll('div.requestButtons button')
var r
for(r=0; r<requestButtons.length; r++){
	requestButtons[r].addEventListener('click', function(){
		from = this.parentElement.parentElement.querySelector('.requestFrom').innerText
		to = document.getElementById('profile').querySelector('b').innerText
		response = this.innerText
		URL = "friendRequest/"+from+"/"+to+"/"+response
		fetch(URL)
		window.location.reload()
		window.location.reload()
		window.location.reload()
		window.location.reload()
		window.location.reload()
	})
	
}