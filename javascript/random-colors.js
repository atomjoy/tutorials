function randomColor() {
	var letters = '0123456789ABCDEF'
	var color = '#'
	for (var i = 0; i < 6; i++) {
		color += letters[Math.floor(Math.random() * 16)]
	}
	return color
}

function randomColorHex() {
	return '#' + Math.random().toString(16).substring(2, 6)
}

function randomColorHsl() {
	return `hsl(${Math.random() * 360}, 100%, 70%)`
}

const changeRootColor = () => {
	let color = randomColor()
	document.documentElement.style.setProperty('--root-color', color)
	return color
}

export { randomColor as default, randomColorHex, randomColorHsl, changeRootColor }
