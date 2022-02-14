function changeColor(className, isOn) {
	const elements = document.getElementsByClassName(className);

    if (isOn) {
        elements[0].style.color = 'rgb(170, 170, 170)';
        elements[1].style.color = 'rgb(170, 170, 170)';
        elements[2].style.color = 'rgb(170, 170, 170)';
    } else {
        elements[0].style.color = 'rgb(97, 255, 116)';
        elements[1].style.color = 'rgb(158, 255, 169)';
        elements[2].style.color = 'rgb(97, 255, 116)';
    }

}
