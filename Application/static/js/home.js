// var socket = io();

// socket.on('connect', function() {
// 	console.log(socket.id)
// 	socket.emit('event', { data : 'I\'m Connected', id: socket.id });
// })

hiddenInput = document.getElementById('imgupload')
uploadButton = document.getElementById('uploadBtn')
innerUpload = document.getElementById('innerUpload')
uploadButton.addEventListener('click', function(){
			hiddenInput.click()
		})


// DP CHANGE CODE

hiddenImageInput = document.getElementById('hiddenDPInput')
dpChangeIcon = document.getElementById('dpChangeIcon')

dpChangeIcon.addEventListener('click', function(){
			hiddenImageInput.click()
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
