
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

// MULTIPLE PAGES FOR IMAGES . NAVIGATING TO PAGES
rightPageButton = document.getElementById('rightPage')
rightPageButton.addEventListener('click', function(){
	urlSplit = document.URL.split("/")
	if(urlSplit[3] == ''){
		page = '2'
	}
	else{
		page = parseInt(document.URL.split("/")[3]) + 1	
	}
	window.location = '/pageChange/'+page
	})

leftPageButton = document.getElementById('leftPage')
leftPageButton.addEventListener('click', function(){
	if(document.URL.split("/")[3] == '2'){
		page = parseInt(document.URL.split("/")[3]) - 1
	}
	else if(document.URL.split("/")[3] != ''){
		page = parseInt(document.URL.split("/")[3]) - 1
	}
	window.location = '/pageChange/'+page
	
})

//IMAGE VIEW CODE
userrPhotos = document.querySelectorAll('.userPhotos')
for(let i=0 ; i<userrPhotos.length; i++){
	var imageFileNameSplit = userrPhotos[i].src.split("/").slice(-1)
	var locationn = "'/imageShow/" + imageFileNameSplit +"'"
	userrPhotos[i].setAttribute("onclick", `location.href=${locationn}`)
}


