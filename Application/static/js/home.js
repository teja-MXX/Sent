// var socket = io();

// socket.on('connect', function() {
// 	console.log(socket.id)
// 	socket.emit('event', { data : 'I\'m Connected', id: socket.id });
// })

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
