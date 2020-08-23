console.log("[EKS] Seite --> Anzeigen Übersicht");
custom_show_loading();

window.addEventListener("load", windowLoaded(), false);

async function windowLoaded() {
	setTimeout(async function() {
	    await addRenewButtons();
		custom_hide_loading();
	},500);		
}

async function addRenewButtons() {
  return new Promise(resolve => {
  
  var ads = getAllAdsFromUser();
  var curr_index_ = 0;
  while(curr_index_ < ads.length) { 
    var adurl = ads[curr_index_].getElementsByClassName("manageaditem-image")[0].getElementsByTagName("a")[0].href;
    var footer = ads[curr_index_].getElementsByTagName("footer")[0];
	var new_section_element = document.createElement("section"); new_section_element.classList.add("manageaditem-actions"); new_section_element.classList.add("custom-overview-section");
	var section = footer.insertBefore(new_section_element, footer.firstChild);
	var new_list_element = document.createElement("ul"); new_list_element.classList.add("linklist"); new_list_element.classList.add("custom-overview-actionlist");
	var list = section.appendChild(new_list_element);
	list.appendChild(createRenewListEntry(adurl));
	curr_index_++;
  }
  resolve("done");
  
  });
}

function createRenewListEntry(adurl) {
	var new_li_element = document.createElement("li");
	var new_li_a_element = document.createElement("a");
	var new_li_a_i_element = document.createElement("i"); new_li_a_i_element.classList.add("icon"); new_li_a_i_element.classList.add("icon-link-icon"); new_li_a_i_element.classList.add("icon-redo");
	var new_li_a_span_element = document.createElement("span"); new_li_a_span_element.innerHTML = "Neueinstellen";
	var a = new_li_element.appendChild(new_li_a_element);
	a.href = adurl + "?custom_recreate";
	var i = a.appendChild(new_li_a_i_element);
	var span = a.appendChild(new_li_a_span_element);
	return new_li_element;
}

function getAllAdsFromUser() {
	return document.getElementById("my-manageads-adlist").getElementsByClassName("cardbox");
}