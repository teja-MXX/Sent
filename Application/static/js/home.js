
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
			document.location.reload()	
			}
})

// IMAGE UPLOAD CODE
imageUploadButton = document.getElementById('imageUploadButton')
hiddenImageInput = document.getElementById('hiddenImageInput')
imageUploadButton.addEventListener('click', function(){
	hiddenImageInput.click()
})


// IMAGE VIEW CODE
userPhotos = document.querySelectorAll('.userPhotos')
for(let i=0 ; i<userPhotos.length; i++){
	console.log(i)
	var imageFileNameSplit = userPhotos[i].src.split("/").slice(-1)
	var locationn = "'/imageShow/" + imageFileNameSplit +"'"
	userPhotos[i].setAttribute("onclick", `location.href=${locationn}`)
}



