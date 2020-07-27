var title;
var price;
var description;
var id;
var url_vars = getUrlVars();

console.log("Ebay Kleinanzeigen Improver --> main.js");


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