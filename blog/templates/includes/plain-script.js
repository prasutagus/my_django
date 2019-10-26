<script>
// find images
let myNodeList = document.querySelectorAll("img");
// add bootstrap "img-fluid" class to each image to make it responsive
for (var i = 0; i < myNodeList.length; i++) {
	myNodeList[i].classList.add("img-fluid")
}
</script>
