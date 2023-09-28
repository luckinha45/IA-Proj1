function search() {
	let de = document.getElementById('slct_de').value;
	let para = document.getElementById('slct_para').value;
	eel.busca(de, para);
}


eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}