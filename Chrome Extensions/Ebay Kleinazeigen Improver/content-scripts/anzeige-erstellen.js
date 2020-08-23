console.log("[EKS] Seite --> Anzeige erstellen");
custom_show_loading();

var custom_button_html = '<button style="background-color: #6eff00;" id="pstad-submit-custom" class="button custom-submit-delete-old" type="submit"><span>Anzeige aufgeben &amp; Alte Anzeige Löschen</span></button>';
var auto_insert = false;

window.addEventListener("load", windowLoaded(), false);

async function windowLoaded() {
	setTimeout(async function() {
	    await checkURLParams();
		custom_hide_loading();
	},500);		
}

async function loadAllData(overgive_id) {
  id = overgive_id;
  title = localStorage.getItem(id + "_title");
  price = localStorage.getItem(id + "_price");
  description = localStorage.getItem(id + "_desc");
  return;
}

async function checkURLParams() {
	if(url_vars["auto_insert"] != null && url_vars["auto_insert"] != "" && url_vars["auto_insert"] != 1) {
        console.log("Automatically Inserting Infos...");
    	auto_insert = true;
		id = url_vars["auto_insert"];
        await loadAllData(id);
        await insertData();
		await addCustomSubmitButton();
    }
	return;
}

async function addCustomSubmitButton() {
	if(auto_insert == true) {
	    var default_submit_button = document.getElementById("pstad-submit");
       	default_submit_button.parentElement.innerHTML = custom_button_html + default_submit_button.parentElement.innerHTML;
	    document.getElementById("pstad-submit-custom").addEventListener('click',function() {
            console.log("Should delete: " + id); 
        });		
	}
	return;
}

async function insertData() {
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
  return;
}

function setToFestpreis()  { document.getElementById("priceType1").click(); }

function setToVB() { document.getElementById("priceType2").click(); }

function setToVerschenken() { document.getElementById("priceType3").click(); }