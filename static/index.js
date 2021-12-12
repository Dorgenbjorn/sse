var targetContainer = document.getElementById('result-div');
var eventSource = new EventSource('/stream')

eventSource.addEventListener('update', function(e) {
	console.log(e);
	targetContainer.innerHTML = e.data;
}, false);
