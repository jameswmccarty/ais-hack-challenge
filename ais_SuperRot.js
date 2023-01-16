// to copy/paste into the dev console
// https://hack.ainfosec.com/
// Super Rot (retired puzzle)

var englishWords = []
function push_to_words(text) {
	var list = text.split('\n')
	for (var i=0; i<list.length; i++) {
		englishWords.push(list[i]);
	}
}

// find a good word list if this link is dead
fetch('https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt', {
	method: 'GET'})
.then(response => response.text())
.then(text => push_to_words(text))

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

function rotChar(a,i) {
	lowers = 'abcdefghijklmnopqrstuvwxyz';
	uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	if (lowers.includes(a)) {
		return lowers[(lowers.indexOf(a)+i)%26]
	}
	if (uppers.includes(a)) {
		return uppers[(uppers.indexOf(a)+i)%26]
	}
	return a
}

function rotStr(a_str,i) {
	let trial = ''
	for (let k=0; k<a_str.length; k++) {
		trial += rotChar(a_str[k],i);
	}
	return trial
}

function score_string(a_str) {
	var score = 0;
	a_str = a_str.split(" ")
	for (let i=0; i<a_str.length; i++) {
		if(englishWords.indexOf(a_str[i]) > 0) { score += 1 }
	}
	return score
}

function solve_a_puzz() {

	var puzz=SuperRot_getEncryptedMessage();
		console.log(puzz)
		var best_score = 0
		var best_solution = ''
		for (let j=1; j<26; j++) {
			var trial = rotStr(puzz,j)
			var this_score = score_string(trial)
			if (this_score > best_score) {
				best_score = this_score
				best_solution = trial
			}
		}
		console.log(best_solution)
		let p4 = Promise.resolve((SuperRot_submit(best_solution)))
	sleep(2000)
}

//perform this call once previous solution submitted
solve_a_puzz()
