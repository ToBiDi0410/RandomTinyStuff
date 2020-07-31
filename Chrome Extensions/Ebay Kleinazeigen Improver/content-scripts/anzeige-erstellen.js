var custom_button_html = '<button style="background-color: #6eff00;" id="pstad-submit-custom" class="button custom-submit-delete-old" type="submit"><span>Anzeige aufgeben &amp; Alte Anzeige Löschen</span></button>';
var auto_insert = false;

console.log("Ebay Kleinanzeigen Improver --> anzeige-create.js");

window.onload = windowLoaded();

function windowLoaded() {
	setTimeout(function() {
	    checkURLParams();
		addCustomSubmitButton();
	},500);		
}

function loadAllData(overgive_id) {
  id = overgive_id;
  title = localStorage.getItem(id + "_title");
  price = localStorage.getItem(id + "_price");
  description = localStorage.getItem(id + "_desc");
}

function checkURLParams() {
	if(url_vars["auto_insert"] != null && url_vars["auto_insert"] != "" && url_vars["auto_insert"] != 1) {
        console.log("Automatically Inserting Infos...");
    	auto_insert = true;
		id = url_vars["auto_insert"];
        loadAllData(id);
        insertData();
    }
}

function addCustomSubmitButton() {
	if(auto_insert == true) {
	    var default_submit_button = document.getElementById("pstad-submit");
       	default_submit_button.parentElement.innerHTML = custom_button_html + default_submit_button.parentElement.innerHTML;
	    document.getElementById("pstad-submit-custom").addEventListener('click',function() {
            console.log("Should delete: " + id); 
        });		
	}
}

function insertData() {
  document.getElementById("postad-title").value = title;
  document.getElementById("pstad-descrptn").value = description;
  if(isNaN(price)) {
    if(price.includes("VB")) {
      setToVB();
    }
    if(price.replace("VB","") != "" || price.replace("VB","") != null) {
      if(!isNaN(price.replace("VB",""))) {
        document.getElementById("pstad-price").value = price.replace("VB","");
      }
    }
  } else {
    setToFestpreis();
    document.getElementById("pstad-price").value = price;
  }
}

function setToFestpreis()  { document.getElementById("priceType1").click(); }

function setToVB() { document.getElementById("priceType2").click(); }

function setToVerschenken() { document.getElementById("priceType3").click(); }