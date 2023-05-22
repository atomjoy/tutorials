const color = '#' + Math.random().toString(16).substring(2, 6)

function randomColor() {
	const letters = '0123456789ABCDEF'
	let color = '#'

	for (let i = 0; i < 6; i++) {
		color += letters[Math.floor(Math.random() * 16)]
	}

	return color
}

function randomColorHsl() {
	return `hsl(${Math.random() * 360}, 100%, 70%)`
}
