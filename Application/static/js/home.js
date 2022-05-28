var socket = io();

socket.on('connect', function() {
	console.log(socket.id)
	socket.emit('event', { data : 'I\'m Connected', id: socket.id });
})