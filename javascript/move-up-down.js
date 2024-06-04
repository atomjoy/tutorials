// Move up or down element in array
function moveUp(index, array) {
	move(array, index, -1)
}

function moveDown(index, array) {
	move(array, index, 1)
}

function move(array, index, delta) {
	let newIndex = index + delta
	if (newIndex < 0 || newIndex == array.length) return
	let indexes = [index, newIndex].sort((a, b) => a - b)
	array.splice(indexes[0], 2, array[indexes[1]], array[indexes[0]])
}

export { move as default, moveUp, moveDown }
