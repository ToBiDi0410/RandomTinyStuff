console.log("[EKS] Haupt-Engine geladen!");
importScriptFromURL("https://unpkg.com/jspdf@latest/dist/jspdf.min.js");

var title;
var price;
var description;
var id;
var url_vars = getUrlVars();


function forceDownload(url, fileName){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = "blob";
    xhr.onload = function(){
        var urlCreator = window.URL || window.webkitURL;
        var imageUrl = urlCreator.createObjectURL(this.response);
        var tag = document.createElement('a');
        tag.href = imageUrl;
        tag.download = fileName;
        document.body.appendChild(tag);
        tag.click();
        document.body.removeChild(tag);
    }
    xhr.send();
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getUrlVars() {
  var vars = {};
  var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
      vars[key] = value;
  });
  return vars;
}

function deleteAnzeige(id) {
	fetch("https://www.ebay-kleinanzeigen.de/m-anzeigen-loeschen.json?ids=" + id, {
		"headers": {
			"accept": "*/*",
			"accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,nl;q=0.6",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
		},
		"referrer": "https://www.ebay-kleinanzeigen.de/m-meine-anzeigen.html",
		"referrerPolicy": "no-referrer-when-downgrade",
		"body": null,
		"method": "POST",
		"mode": "cors",
		"credentials": "include"
	});
}

function custom_show_loading() {
	var loading_div = document.createElement("div"); loading_div.classList.add("loading"); loading_div.id = "custom-loading";
	var ring_div = document.createElement("div"); ring_div.classList.add("uil-ring-css"); ring_div.style = 'transform:scale(0.79);';
	var empty_div = document.createElement("div");
	ring_div.appendChild(empty_div);
	loading_div.appendChild(ring_div);
	document.body.appendChild(loading_div);
}

function custom_hide_loading() {
	var loading_div = document.getElementById("custom-loading");
	loading_div.remove();
}
function importScriptFromURL(source) {
	var script_elem = document.createElement("script");
	script_elem.src = source;
	document.body.appendChild(script_elem);
}