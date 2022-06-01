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

