var button_raw_html = '<li><a class="" type="application/pdf" href="{.ANZEIGEN_URL.}?custom_recreate"><i class="icon icon-link-icon icon-redo"></i>Neueinstellen</a></li>'; 

console.log("Ebay Kleinanzeigen Improver --> anzeigen-overview.js");

window.onload = windowLoaded();

function windowLoaded() {
	setTimeout(function() {
	    addRenewButtons();
	},500);		
}

function addRenewButtons() {
  var anzeigen_bars = document.getElementsByClassName("linklist");
  var curr_index_ = 0;
  while(curr_index_ < anzeigen_bars.length) {
    var anzeigen_bar = anzeigen_bars[curr_index_];
    var normal_url = anzeigen_bar.parentElement.parentElement.parentElement.getElementsByTagName("h2")[0].getElementsByTagName("a")[0].href;
    anzeigen_bar.innerHTML += button_raw_html.replace("{.ANZEIGEN_URL.}", normal_url);
	curr_index_++;
  }
}