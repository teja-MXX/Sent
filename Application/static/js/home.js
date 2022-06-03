// var socket = io();

// socket.on('connect', function() {
// 	console.log(socket.id)
// 	socket.emit('event', { data : 'I\'m Connected', id: socket.id });
// })


// DP DISPLAY CODE
imgElement = document.getElementById('profilePicture')
userName = document.getElementById('profile').firstElementChild.innerText
imgElement.src = "/static/profiles/" + userName +"/"  +userName +".jpg"
console.log("Haha "+imgElement.src)

// DP CHANGE CODE

hiddenDPInput = document.getElementById('hiddenDPInput')
dpChangeIcon = document.getElementById('dpChangeIcon')

dpChangeIcon.addEventListener('click', function(){
			hiddenDPInput.click()
		})


// DP REMOVE CODE
dpRemoveIcon = document.getElementById('dpRemove')
dpRemoveIcon.addEventListener('click', function(){
	let respo = prompt('Type YES to remove DP')
	if(respo == "YES")
		{
			fetch('dpRemove')
			}
})

// IMAGE UPLOAD CODE
imageUploadButton = document.getElementById('imageUploadButton')
hiddenImageInput = document.getElementById('hiddenImageInput')
imageUploadButton.addEventListener('click', function(){
	hiddenImageInput.click()
})


