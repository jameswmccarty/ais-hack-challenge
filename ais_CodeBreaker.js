// to copy/paste into the dev console
// https://hack.ainfosec.com/
// Code Breaker

let solved_pass = ['*','*','*','*','*','*','*']
let found_vals = []
let all_vals = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

for (let i = 0; i < all_vals.length; i++) {
	let p2 = Promise.resolve((CodeBreaker_submit(all_vals[i].repeat(7))))
	await sleep(10)
	p2.then((value) => { if (value != 0) { found_vals.push(all_vals[i]) } } )
}

await sleep(4000)
console.log(found_vals)

for (let i = 0; i < found_vals.length; i++) {
	for (let j = 0; j < 7; j++) {
		let str = "-------".split('');
		str[j] = found_vals[i];
		str = str.join('');
		let p3 = Promise.resolve((CodeBreaker_submit(str)))
		await sleep(10)
		p3.then((value) => { if (value != 0) { solved_pass[j] = found_vals[i] } } )
	}
}
await sleep(4000)
CodeBreaker_submit(solved_pass.join(''))
console.log(solved_pass.join(''))
