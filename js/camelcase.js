String.prototype.toCamelCase2 = function() {
	var re = /\b\w|(?<=\p{Ll})\p{Lu}/; 
	var words = this.split(' ');
	var camelCasedWord = '';
	for (i in words) {
		console.log(words[i]);
		console.log(words[i].replace(re,function up(x) { return x.toUpperCase(); } ));
		camelCasedWord += words[i][0].replace(re,function up(x) { return x.toUpperCase(); } ) + ' ';
		console.log(camelCasedWord);
	}
	return camelCasedWord;
}

var s = "some text"

console.log(s.toCamelCase2());


