var title;
var price;
var description;
var id;
var url_vars = getUrlVars();

//AUTOMATICS
if(url_vars["auto_insert"] != null && url_vars["auto_insert"] != "" && url_vars["auto_insert"] != 1) {
  setTimeout(async function() {
    console.log("Automatically Inserting Infos...");
    loadAllData(url_vars["auto_insert"]);
    insertData();
  },1000);
}

if(window.location.href.includes("custom_save") || window.location.href.includes("custom_renew")) {
  console.log("Automatically Saving Infos and/or Renewing Anzeige...");
  setTimeout(async function() {
     await storeAllData();
     if(window.location.href.includes("custom_renew")) {
      window.location.href = "https://www.ebay-kleinanzeigen.de/p-anzeige-aufgeben-schritt2.html" + "?auto_insert=" + id;
     } else {
      window.location.href = window.location.href.replace("custom_save","");
     }
  },1000);
}



//SITE MANIPULATION

if(window.location.href.includes("m-meine-anzeigen.html")) {
  setTimeout(async function() {
    addRenewButtons();
  },1000);
}

function addRenewButtons() {
  var anzeigen_bars = document.getElementsByClassName("linklist");
  var curr_index_ = 0;
  while(curr_index_ < anzeigen_bars.length) {
    var anzeigen_bar = anzeigen_bars[curr_index_];
    var normal_url = anzeigen_bar.parentElement.parentElement.parentElement.getElementsByTagName("h2")[0].getElementsByTagName("a")[0].href;
    anzeigen_bar.innerHTML += '<li><a class="" type="application/pdf" href="' + normal_url + '?custom_save&custom_renew"><i class="icon icon-link-icon icon-redo"></i>Neueinstellen</a></li>'; 
    curr_index_++;
  }
}

//DATA SAVING

async function storeAllData() {
  storeInfos();
  await downloadImages();
}

function storeInfos() {
title = document.getElementById("viewad-title").innerHTML;
price = document.getElementById("viewad-price").innerHTML;
description = document.getElementById("viewad-description-text").innerHTML;
if(document.getElementsByClassName("align-right").length > 1) {
  id = document.getElementsByClassName("align-right")[1].innerHTML;
} else {
  id = document.getElementsByClassName("align-right")[0].innerHTML;
}

title = title.replace("                    ", "").replace(/(\r\n|\n|\r)/gm, "");
price = price.replace("€", "").replace("                        ","").replace(" ","").replace(/(\r\n|\n|\r)/gm, "");
description = description.replace("                        ", "").replace(/(\r\n|\n|\r)/gm, "");
description = description.split("<br>").join("\n");
id = id.replace("Anzeigennr.: ","");

localStorage.setItem(id + "_title", title);
localStorage.setItem(id + "_price", price);
localStorage.setItem(id + "_desc", description);

console.log("Updated Text Data!");
}

async function downloadImages() {
  //document.getElementsByClassName("galleryimage-element")[0].getElementsByTagName("img")[0];
  var images = document.getElementsByClassName("galleryimage-element");
  var curr_index = 0;
  while(curr_index < images.length-1) {
    var imgObj = images[curr_index].getElementsByTagName("img")[0];
    //forceDownload(imgObj.src,(images.length - 1 - curr_index) + "_" + id + ".jpg");
    forceDownload(imgObj.src,id + "_" + (curr_index + 1) + ".jpg");
    curr_index++;
    await sleep(100);
  }
}

//DATA LOADING
function loadAllData(id) {
  title = localStorage.getItem(id + "_title");
  price = localStorage.getItem(id + "_price");
  description = localStorage.getItem(id + "_desc");
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