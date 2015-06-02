String.prototype.toCamelCase = function() {
	words = this.split(' ')
	var upperCased = '';
	for (var i = 0; i < words.length; i++) {
		for (var y = 0; y < words[i].length; y++) {
			if (y == 0) {
				upperCased += words[i][y].toUpperCase();
			}
			else {
				upperCased += words[i][y];
			}
		}
		upperCased += ' ';	
	}	
	return upperCased;
}


var s = "i'm a test"




console.log(s.toCamelCase())





