function changeColor(className, status) {
	var elements = document.getElementsByClassName(className);

	for (var i = 0; i < elements.length; i++) {
        if (status == 'new') {
            elements[i].style.color = 'rgb(170, 170, 170)';
        }
        else {
            if (i == 1) elements[i].style.color = 'rgb(158, 255, 169)';
            else elements[i].style.color = 'rgb(97, 255, 116)';
        }
	}
}
