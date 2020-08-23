console.log("[EKS] Seite --> Nachrichten");
custom_show_loading();

window.addEventListener("load", windowLoaded(), false);

async function windowLoaded() {
	addDownloadPDFButton();
	custom_hide_loading();
}

function addDownloadPDFButton() {
	var button_box = document.getElementsByClassName("replybox-submit-field align-right")[0];
	var new_button = createNewButtonBoxButton("Als PDF Speichern");
	new_button.id = "custom-pdf-download";
	
	var inserted_button = button_box.appendChild(new_button);
	inserted_button.addEventListener("click", saveAsPDF);
}

function createNewButtonBoxButton(button_text) {
	var box_button = document.createElement("button"); box_button.classList.add("button"); box_button.classList.add("button");
	var button_span = document.createElement("span"); button_span.classList.add("btn-lable"); button_span.classList.add("small"); button_span.innerHTML = button_text;
	var button_i = document.createElement("i"); button_i.classList.add("icon-play");
	
	box_button.appendChild(button_span);
	box_button.appendChild(button_i);
	return box_button;
}

function saveAsPDF() {
	var doc = new jsPDF();
    var source = $('#msgbox-conversation-list').first();
    var specialElementHandlers = {
        '#bypassme': function(element, renderer) {
            return true;
        }
    };
	
	doc.fromHTML(source,0.5,0.5, 
	{
		'elementHandlers': specialElementHandlers
	});
	
	var data_url = doc.output('dataurl');
	downloadURI(data_url,"messages.pdf");
}

function downloadURI(uri, name) {
  var link = document.createElement("a");
  link.download = name;
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  delete link;
}